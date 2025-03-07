#!/usr/bin/env python3
"""YAML to JSON Schema Converter for Prompt Decorators.

This script converts decorator definitions from a simplified YAML format to
complete JSON schema files following the registry-entry.schema.json format.
It uses the Claude 3.7 Sonnet model to intelligently expand the simplified
definitions into compliant schema files.

Example usage:
    # Basic usage
    $ python scripts/yaml_to_schema_converter.py --input registry/simplified_decorators/example.yml --output registry/core

    # With custom options
    $ python scripts/yaml_to_schema_converter.py --input registry/simplified_decorators/example.yml --output registry/core --batch-size 5 --validate --verbose

    # Dry run mode
    $ python scripts/yaml_to_schema_converter.py --input registry/simplified_decorators/example.yml --dry-run

Returns:
    int: 0 for success, non-zero for errors
"""

import argparse
import json
import logging
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union

import anthropic
import jsonschema
import yaml
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger("yaml_to_schema")


class SchemaConverter:
    """Converts YAML decorator definitions to JSON schema files using Claude API."""

    def __init__(
        self,
        api_key: str,
        schema_path: str = "schemas/registry-entry.schema.json",
        cache_dir: str = ".cache/schema_converter",
        batch_size: int = 3,
        max_workers: int = 2,
        rate_limit_delay: float = 1.0,
        verbose: bool = False,
    ):
        """Initialize the converter.

        Args:
            api_key: Anthropic API key
            schema_path: Path to the registry-entry.schema.json file
            cache_dir: Directory to store cache files
            batch_size: Number of decorators to process in a batch
            max_workers: Maximum number of concurrent workers
            rate_limit_delay: Delay between API calls to respect rate limits
            verbose: Whether to enable verbose logging
        """
        # Initialize Anthropic client with the latest SDK format
        self.client = anthropic.Anthropic(api_key=api_key)
        self.schema_path = schema_path
        self.cache_dir = Path(cache_dir)
        self.batch_size = batch_size
        self.max_workers = max_workers
        self.rate_limit_delay = rate_limit_delay
        self.verbose = verbose

        # Set up logging
        if verbose:
            logger.setLevel(logging.DEBUG)

        # Load the schema
        self.schema = self._load_schema()

        # Create cache directory if it doesn't exist
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Load cache
        self.cache = self._load_cache()

    def _load_schema(self) -> Dict[str, Any]:
        """Load the registry-entry.schema.json file.

        Returns:
            Dict[str, Any]: The loaded schema

        Raises:
            FileNotFoundError: If the schema file doesn't exist
            json.JSONDecodeError: If the schema file is invalid JSON
        """
        try:
            with open(self.schema_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Schema file not found: {self.schema_path}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in schema file: {e}")
            raise

    def _load_cache(self) -> Dict[str, Dict[str, Any]]:
        """Load the cache from disk.

        Returns:
            Dict[str, Dict[str, Any]]: The loaded cache
        """
        cache_file = self.cache_dir / "cache.json"
        if cache_file.exists():
            try:
                with open(cache_file, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load cache: {e}")
                return {}
        return {}

    def _save_cache(self) -> None:
        """Save the cache to disk."""
        cache_file = self.cache_dir / "cache.json"
        try:
            with open(cache_file, "w") as f:
                json.dump(self.cache, f, indent=2)
        except IOError as e:
            logger.warning(f"Failed to save cache: {e}")

    def _get_cache_key(self, decorator: Dict[str, Any]) -> str:
        """Generate a cache key for a decorator.

        Args:
            decorator: The decorator definition

        Returns:
            str: The cache key
        """
        # Use the name and a hash of the content as the cache key
        import hashlib

        content_hash = hashlib.md5(
            json.dumps(decorator, sort_keys=True).encode()
        ).hexdigest()
        return f"{decorator['name']}_{content_hash}"

    def load_yaml(self, yaml_path: str) -> Dict[str, Any]:
        """Load a YAML file containing decorator definitions.

        Args:
            yaml_path: Path to the YAML file

        Returns:
            Dict[str, Any]: The loaded YAML content

        Raises:
            FileNotFoundError: If the YAML file doesn't exist
            yaml.YAMLError: If the YAML file is invalid
        """
        try:
            with open(yaml_path, "r") as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            logger.error(f"YAML file not found: {yaml_path}")
            raise
        except yaml.YAMLError as e:
            logger.error(f"Invalid YAML: {e}")
            raise

    def validate_schema(self, schema: Dict[str, Any]) -> bool:
        """Validate a schema against the registry-entry.schema.json schema.

        Args:
            schema: The schema to validate

        Returns:
            bool: Whether the schema is valid
        """
        try:
            jsonschema.validate(instance=schema, schema=self.schema)
            return True
        except jsonschema.exceptions.ValidationError as e:
            logger.error(f"Schema validation failed: {e}")
            return False

    def generate_schema(
        self, decorator: Dict[str, Any], author: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate a JSON schema for a decorator using Claude API.

        Args:
            decorator: The decorator definition from the YAML file
            author: The author information from the YAML file

        Returns:
            Dict[str, Any]: The generated schema

        Raises:
            anthropic.APIError: If the API call fails
            json.JSONDecodeError: If the API response is invalid JSON
        """
        # Check cache first
        cache_key = self._get_cache_key(decorator)
        if cache_key in self.cache:
            logger.debug(f"Using cached schema for {decorator['name']}")
            return self.cache[cache_key]

        # Prepare the prompt for Claude
        prompt = self._create_claude_prompt(decorator, author)

        # Set up retry parameters
        max_retries = 3
        base_delay = 2.0

        # Try API call with retries
        for attempt in range(max_retries):
            try:
                # Call the Claude API with the latest SDK format
                logger.debug(
                    f"Calling Claude API for {decorator['name']} (Attempt {attempt + 1}/{max_retries})"
                )
                response = self.client.messages.create(
                    model="claude-3-7-sonnet-20250219",  # Using Sonnet for a balance of quality and cost
                    max_tokens=4000,
                    temperature=0.2,
                    system="""You are an expert in converting simplified prompt decorator definitions to complete JSON schema files.
Your task is to expand a simplified decorator definition into a complete, compliant schema file following the registry-entry.schema.json format.
You should intelligently fill in missing fields based on the provided information and your understanding of the decorator's purpose.
Your response should be ONLY the valid JSON schema with no additional text or explanation.
Always validate your output against the provided schema before responding to ensure it is fully compliant.""",
                    messages=[{"role": "user", "content": prompt}],
                )

                # Extract the JSON from the response
                content = response.content[0].text

                # Try to parse the JSON
                try:
                    schema = json.loads(content)
                except json.JSONDecodeError as e:
                    # Try to extract JSON from the response if it contains additional text
                    import re

                    json_match = re.search(
                        r"```(?:json)?\n(.*?)\n```", content, re.DOTALL
                    )
                    if json_match:
                        try:
                            schema = json.loads(json_match.group(1))
                        except json.JSONDecodeError:
                            logger.error(
                                f"Failed to parse JSON from Claude response for {decorator['name']}"
                            )
                            raise e
                    else:
                        logger.error(
                            f"Failed to parse JSON from Claude response for {decorator['name']}"
                        )
                        raise e

                # Validate the schema
                if not self.validate_schema(schema):
                    logger.warning(
                        f"Generated schema for {decorator['name']} is invalid"
                    )
                    # Try to fix common issues
                    schema = self._fix_common_issues(schema)
                    if not self.validate_schema(schema):
                        logger.error(f"Failed to fix schema for {decorator['name']}")
                        raise ValueError(
                            f"Generated schema for {decorator['name']} is invalid"
                        )

                # Cache the result
                self.cache[cache_key] = schema
                self._save_cache()

                return schema

            except anthropic.APIError as e:
                if "overloaded" in str(e).lower() and attempt < max_retries - 1:
                    # Exponential backoff for overloaded errors
                    wait_time = base_delay * (2**attempt)
                    logger.warning(
                        f"API is overloaded. Retrying in {wait_time} seconds..."
                    )
                    time.sleep(wait_time)
                else:
                    logger.error(f"Claude API error: {e}")
                    raise
            except Exception as e:
                logger.error(f"Error generating schema for {decorator['name']}: {e}")
                if attempt < max_retries - 1:
                    logger.info(f"Retrying in {base_delay} seconds...")
                    time.sleep(base_delay)
                else:
                    raise

    def _create_claude_prompt(
        self, decorator: Dict[str, Any], author: Dict[str, Any]
    ) -> str:
        """Create a prompt for Claude to generate a schema.

        Args:
            decorator: The decorator definition from the YAML file
            author: The author information from the YAML file

        Returns:
            str: The prompt for Claude
        """
        # Load the schema for reference
        schema_json = json.dumps(self.schema, indent=2)

        # Create the prompt
        prompt = f"""
I need you to convert a simplified prompt decorator definition to a complete JSON schema file following the registry-entry.schema.json format.

Here is the registry-entry.schema.json format that your output MUST conform to:
```json
{schema_json}
```

Here is the simplified decorator definition:
```yaml
name: {decorator['name']}
category: {decorator['category']}
description: {decorator['description']}
"""

        # Add parameters if they exist
        if "parameters" in decorator and decorator["parameters"]:
            prompt += "parameters:\n"
            for param in decorator["parameters"]:
                prompt += f"  - name: {param['name']}\n"
                prompt += f"    type: {param['type']}\n"
                prompt += f"    description: {param['description']}\n"
                if "values" in param:
                    values_str = ", ".join([f'"{v}"' for v in param["values"]])
                    prompt += f"    values: [{values_str}]\n"
                if "default" in param:
                    prompt += f"    default: {param['default']}\n"
                if "required" in param:
                    prompt += f"    required: {param['required']}\n"

        # Add example if it exists
        if "example" in decorator:
            prompt += f"example: |\n  {decorator['example']}\n"

        # Add conflicts_with if it exists
        if "conflicts_with" in decorator:
            conflicts_str = ", ".join([f'"{c}"' for c in decorator["conflicts_with"]])
            prompt += f"conflicts_with: [{conflicts_str}]\n"

        # Add requires if it exists
        if "requires" in decorator:
            requires_str = ", ".join([f'"{r}"' for r in decorator["requires"]])
            prompt += f"requires: [{requires_str}]\n"

        # Add notes if they exist
        if "notes" in decorator:
            prompt += f"notes: {decorator['notes']}\n"

        prompt += "```\n\n"

        # Add author information
        prompt += f"""
Author information:
```yaml
name: {author['name']}
"""
        if "email" in author:
            prompt += f"email: {author['email']}\n"
        if "url" in author:
            prompt += f"url: {author['url']}\n"
        prompt += "```\n\n"

        # Add instructions
        prompt += """
Please convert this simplified definition into a complete JSON schema file following the registry-entry.schema.json format. The output should:

1. Use "decoratorName" instead of "name" for the decorator name
2. Set "version" to "1.0.0"
3. Include the author information
4. Properly convert the parameters
5. Add appropriate transformationTemplate, implementationGuidance, examples, and compatibility sections
6. Ensure the schema is valid according to the registry-entry.schema.json format

IMPORTANT: Your response must be ONLY the valid JSON schema with no additional text or explanation. The JSON must be valid and must conform to the schema provided above. Do not include markdown code blocks or any other formatting - just the raw JSON object.
"""

        return prompt

    def _fix_common_issues(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        """Fix common issues in generated schemas.

        Args:
            schema: The schema to fix

        Returns:
            Dict[str, Any]: The fixed schema
        """
        # Ensure required fields are present
        required_fields = ["decoratorName", "version", "description", "parameters"]
        for field in required_fields:
            if field not in schema:
                if field == "decoratorName" and "name" in schema:
                    schema["decoratorName"] = schema.pop("name")
                elif field == "version":
                    schema["version"] = "1.0.0"
                elif field == "parameters":
                    schema["parameters"] = []

        # Ensure parameters have required fields
        if "parameters" in schema:
            for i, param in enumerate(schema["parameters"]):
                required_param_fields = ["name", "type", "description"]
                for field in required_param_fields:
                    if field not in param:
                        logger.warning(f"Parameter {i} missing required field: {field}")
                        if field == "type":
                            param["type"] = "string"
                        elif field == "description":
                            param[
                                "description"
                            ] = f"Parameter {param.get('name', f'#{i}')}"

        # Fix enum parameters
        if "parameters" in schema:
            for param in schema["parameters"]:
                if param.get("type") == "enum":
                    # Change type to string and add enum values
                    param["type"] = "string"
                    if "values" in param and "enum" not in param:
                        param["enum"] = param.pop("values")
                    elif "enum" not in param:
                        logger.warning(
                            f"Enum parameter {param.get('name')} missing enum values"
                        )
                        param["enum"] = ["default"]

        return schema

    def process_yaml(
        self,
        yaml_path: str,
        output_dir: str,
        dry_run: bool = False,
        force: bool = False,
        parallel: bool = False,
    ) -> Tuple[int, int, int]:
        """Process a YAML file and generate JSON schema files.

        Args:
            yaml_path: Path to the YAML file
            output_dir: Directory to save the generated schema files
            dry_run: Whether to perform a dry run without saving files
            force: Whether to overwrite existing files
            parallel: Whether to process decorators in parallel

        Returns:
            Tuple[int, int, int]: (total, success, error) counts
        """
        # Load the YAML file
        yaml_data = self.load_yaml(yaml_path)

        # Extract author information
        author = yaml_data.get("author", {"name": "Unknown"})

        # Get the list of decorators
        decorators = yaml_data.get("decorators", [])

        if not decorators:
            logger.warning(f"No decorators found in {yaml_path}")
            return 0, 0, 0

        # Create the output directory if it doesn't exist
        if not dry_run:
            os.makedirs(output_dir, exist_ok=True)

        # Process decorators
        total = len(decorators)
        success = 0
        error = 0

        if parallel and self.max_workers > 1:
            # Process decorators in parallel
            results = self._process_parallel(
                decorators, author, output_dir, dry_run, force
            )
            success = sum(1 for r in results if r)
            error = total - success
        else:
            # Process decorators in batches
            for i in range(0, total, self.batch_size):
                batch = decorators[i : i + self.batch_size]
                batch_results = self._process_batch(
                    batch, author, output_dir, dry_run, force
                )
                success += sum(1 for r in batch_results if r)
                error += sum(1 for r in batch_results if not r)

        return total, success, error

    def _process_batch(
        self,
        decorators: List[Dict[str, Any]],
        author: Dict[str, Any],
        output_dir: str,
        dry_run: bool,
        force: bool,
    ) -> List[bool]:
        """Process a batch of decorators.

        Args:
            decorators: List of decorator definitions
            author: Author information
            output_dir: Directory to save the generated schema files
            dry_run: Whether to perform a dry run without saving files
            force: Whether to overwrite existing files

        Returns:
            List[bool]: List of success/failure results
        """
        results = []

        for decorator in tqdm(
            decorators, desc="Processing batch", disable=not self.verbose
        ):
            result = self._process_decorator(
                decorator, author, output_dir, dry_run, force
            )
            results.append(result)

            # Add delay to respect rate limits
            time.sleep(self.rate_limit_delay)

        return results

    def _process_parallel(
        self,
        decorators: List[Dict[str, Any]],
        author: Dict[str, Any],
        output_dir: str,
        dry_run: bool,
        force: bool,
    ) -> List[bool]:
        """Process decorators in parallel.

        Args:
            decorators: List of decorator definitions
            author: Author information
            output_dir: Directory to save the generated schema files
            dry_run: Whether to perform a dry run without saving files
            force: Whether to overwrite existing files

        Returns:
            List[bool]: List of success/failure results
        """
        results = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []

            for decorator in decorators:
                future = executor.submit(
                    self._process_decorator,
                    decorator,
                    author,
                    output_dir,
                    dry_run,
                    force,
                )
                futures.append(future)

                # Add delay to respect rate limits
                time.sleep(self.rate_limit_delay / self.max_workers)

            # Show progress
            for future in tqdm(
                futures, desc="Processing decorators", disable=not self.verbose
            ):
                results.append(future.result())

        return results

    def _process_decorator(
        self,
        decorator: Dict[str, Any],
        author: Dict[str, Any],
        output_dir: str,
        dry_run: bool,
        force: bool,
    ) -> bool:
        """Process a single decorator.

        Args:
            decorator: The decorator to process
            author: The author information
            output_dir: The output directory
            dry_run: Whether to perform a dry run
            force: Whether to force regeneration

        Returns:
            bool: Whether the processing was successful
        """
        name = decorator["name"]
        category = decorator.get("category", "uncategorized").lower()

        # Sanitize category name by replacing spaces with underscores
        sanitized_category = category.replace(" ", "_")

        # Create category directory if it doesn't exist
        category_dir = os.path.join(output_dir, sanitized_category)
        if not dry_run:
            os.makedirs(category_dir, exist_ok=True)

        # Generate output file path
        output_file = os.path.join(category_dir, f"{name.lower()}.json")

        # Check if file already exists
        if os.path.exists(output_file) and not force and not dry_run:
            logger.info(f"Skipping {name} (file already exists)")
            return True

        try:
            # Generate schema
            schema = self.generate_schema(decorator, author)

            if dry_run:
                logger.info(f"Dry run: Would save schema for {name} to {output_file}")
                return True

            # Save schema to file
            with open(output_file, "w") as f:
                json.dump(schema, f, indent=2)

            logger.info(f"Successfully generated schema for {name}")
            return True

        except Exception as e:
            logger.error(f"Failed to process {name}: {e}")
            return False

    def show_diff(self, old_schema: Dict[str, Any], new_schema: Dict[str, Any]) -> None:
        """Show differences between old and new schemas.

        Args:
            old_schema: The old schema
            new_schema: The new schema
        """
        try:
            import difflib
            import pprint

            old_str = pprint.pformat(old_schema, width=88)
            new_str = pprint.pformat(new_schema, width=88)

            diff = difflib.unified_diff(
                old_str.splitlines(),
                new_str.splitlines(),
                fromfile="old",
                tofile="new",
                lineterm="",
            )

            for line in diff:
                if line.startswith("+"):
                    print(f"\033[92m{line}\033[0m")  # Green
                elif line.startswith("-"):
                    print(f"\033[91m{line}\033[0m")  # Red
                elif line.startswith("@@"):
                    print(f"\033[94m{line}\033[0m")  # Blue
                else:
                    print(line)

        except ImportError:
            logger.warning("difflib or pprint not available, skipping diff")
            return


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        argparse.Namespace: The parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Convert YAML decorator definitions to JSON schema files"
    )

    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to the input YAML file",
    )

    parser.add_argument(
        "--output",
        "-o",
        default="registry/core",
        help="Directory to save the generated schema files (default: registry/core)",
    )

    parser.add_argument(
        "--api-key",
        "-k",
        help="Anthropic API key (default: from ANTHROPIC_API_KEY environment variable)",
    )

    parser.add_argument(
        "--schema",
        "-s",
        default="schemas/registry-entry.schema.json",
        help="Path to the registry-entry.schema.json file (default: schemas/registry-entry.schema.json)",
    )

    parser.add_argument(
        "--cache-dir",
        "-c",
        default=".cache/schema_converter",
        help="Directory to store cache files (default: .cache/schema_converter)",
    )

    parser.add_argument(
        "--batch-size",
        "-b",
        type=int,
        default=3,
        help="Number of decorators to process in a batch (default: 3)",
    )

    parser.add_argument(
        "--max-workers",
        "-w",
        type=int,
        default=2,
        help="Maximum number of concurrent workers (default: 2)",
    )

    parser.add_argument(
        "--rate-limit",
        "-r",
        type=float,
        default=1.0,
        help="Delay between API calls to respect rate limits (default: 1.0)",
    )

    parser.add_argument(
        "--parallel",
        "-p",
        action="store_true",
        help="Process decorators in parallel",
    )

    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Overwrite existing files",
    )

    parser.add_argument(
        "--dry-run",
        "-d",
        action="store_true",
        help="Perform a dry run without saving files",
    )

    parser.add_argument(
        "--validate",
        "-v",
        action="store_true",
        help="Validate generated schemas",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    return parser.parse_args()


def main() -> int:
    """Main entry point.

    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """
    args = parse_args()

    # Get API key from environment variable if not provided
    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        logger.error(
            "Anthropic API key not provided. Use --api-key or set ANTHROPIC_API_KEY environment variable."
        )
        return 1

    try:
        # Create converter
        converter = SchemaConverter(
            api_key=api_key,
            schema_path=args.schema,
            cache_dir=args.cache_dir,
            batch_size=args.batch_size,
            max_workers=args.max_workers,
            rate_limit_delay=args.rate_limit,
            verbose=args.verbose,
        )

        # Process YAML file
        total, success, error = converter.process_yaml(
            yaml_path=args.input,
            output_dir=args.output,
            dry_run=args.dry_run,
            force=args.force,
            parallel=args.parallel,
        )

        # Print summary
        logger.info(
            f"Summary: {total} decorators processed, {success} succeeded, {error} failed"
        )

        # Return appropriate exit code
        return 0 if error == 0 else 1

    except Exception as e:
        logger.error(f"Error: {e}")
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
