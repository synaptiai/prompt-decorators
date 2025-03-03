"""Registry Scanner Module.

This module scans the registry directory and parses decorator JSON files.
"""

import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Type alias for decorator data
DecoratorData = Dict[str, Any]


class RegistryScanner:
    """Scanner for decorator registry files."""

    def __init__(self, registry_path: Union[str, Path]):
        """
        Initialize the registry scanner.

        Args:
            registry_path: Path to the decorator registry directory
        """
        self.registry_path = Path(registry_path)
        if not self.registry_path.exists() or not self.registry_path.is_dir():
            raise ValueError(
                f"Registry path '{registry_path}' is not a valid directory"
            )

        # Categories discovered in the registry
        self.categories: Set[str] = set()

        # Store parsed decorators by category
        self.decorators_by_category: Dict[str, List[DecoratorData]] = {}

        # Store all decorators
        self.all_decorators: List[DecoratorData] = []

    def scan(self) -> List[DecoratorData]:
        """
        Scan the registry directory for decorator JSON files.

        Args:
            self: The RegistryScanner instance.

        Returns:
            List of parsed decorator data dictionaries
        """
        logger.info(f"Scanning registry at {self.registry_path}")

        # Find all JSON files recursively
        decorator_files = self._find_all_json_files()
        logger.info(f"Found {len(decorator_files)} JSON files in the registry")

        # Parse each JSON file
        self.all_decorators = []
        self.decorators_by_category = {}

        for file_path in decorator_files:
            try:
                decorator_data = self._parse_json_file(file_path)
                if decorator_data:
                    # Determine category from file path
                    category = self._get_category_from_path(file_path)
                    self.categories.add(category)

                    # Store by category
                    if category not in self.decorators_by_category:
                        self.decorators_by_category[category] = []
                    self.decorators_by_category[category].append(decorator_data)

                    # Add to all decorators list
                    self.all_decorators.append(decorator_data)
            except Exception as e:
                logger.error(f"Error parsing {file_path}: {e}")

        logger.info(f"Successfully parsed {len(self.all_decorators)} decorators")
        logger.info(f"Found categories: {', '.join(sorted(self.categories))}")

        return self.all_decorators

    def get_decorators_by_category(self, category: str) -> List[DecoratorData]:
        """
        Get decorators for a specific category.

        Args:
            category: Category name

        Returns:
            List of decorator data for the category
        """
        return self.decorators_by_category.get(category, [])

    def _find_all_json_files(self) -> List[Path]:
        """
        Find all JSON files in the registry directory recursively.

        Args:
            self: The RegistryScanner instance.

        Returns:
            List of paths to JSON files
        """
        json_files = []
        for root, _, files in os.walk(self.registry_path):
            for file in files:
                if file.endswith(".json") and not file.startswith("."):
                    # Skip the template file
                    if file == "decorator-template.json":
                        logger.info(
                            f"Skipping template file: {os.path.join(root, file)}"
                        )
                        continue

                    file_path = Path(root) / file

                    # Skip files in __pycache__, .git, etc.
                    if any(part.startswith(".") for part in file_path.parts):
                        continue

                    json_files.append(file_path)

        return json_files

    def _parse_json_file(self, file_path: Path) -> Optional[DecoratorData]:
        """
        Parse a JSON file and validate its structure as a decorator.

        Args:
            file_path: Path to the JSON file

        Returns:
            Parsed decorator data, or None if invalid
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Basic validation
            if not self._is_valid_decorator(data, file_path):
                return None

            # Add file path information
            data["_source_file"] = str(file_path.relative_to(self.registry_path))

            return data
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {file_path}: {e}")
            return None
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return None

    def _is_valid_decorator(self, data: Dict[str, Any], file_path: Path) -> bool:
        """
        Check if the JSON data represents a valid decorator definition.

        Args:
            data: Parsed JSON data
            file_path: Path to the source file (for error reporting)

        Returns:
            True if valid, False otherwise
        """
        # Check required fields
        required_fields = ["decoratorName", "version", "description"]
        for field in required_fields:
            if field not in data:
                logger.warning(f"Missing required field '{field}' in {file_path}")
                return False

        # Verify parameters field
        if "parameters" in data and not isinstance(data["parameters"], list):
            logger.warning(f"'parameters' must be a list in {file_path}")
            return False

        # Validate parameters
        if "parameters" in data:
            for i, param in enumerate(data["parameters"]):
                if "name" not in param:
                    logger.warning(f"Parameter {i} missing 'name' in {file_path}")
                    return False
                if "type" not in param:
                    logger.warning(
                        f"Parameter '{param.get('name', f'at index {i}')}' missing 'type' in {file_path}"
                    )
                    return False

        return True

    def _get_category_from_path(self, file_path: Path) -> str:
        """
        Determine the decorator category from its file path.

        Args:
            file_path: Path to the decorator file

        Returns:
            Category name
        """
        rel_path = file_path.relative_to(self.registry_path)
        parts = rel_path.parts

        # Skip the file name
        if len(parts) > 1:
            # The category is typically the first directory under the registry root
            return parts[0]

        # Default category if no directory structure
        return "unknown"


def scan_registry(registry_path: Union[str, Path]) -> List[DecoratorData]:
    """
    Scan the registry at the given path and return all decorator definitions.

    Args:
        registry_path: Path to the decorator registry

    Returns:
        List of decorator definitions
    """
    scanner = RegistryScanner(registry_path)
    return scanner.scan()


if __name__ == "__main__":
    # Simple test when run directly
    import sys

    if len(sys.argv) > 1:
        registry_dir = sys.argv[1]
    else:
        # Default to registry directory relative to this file
        script_dir = Path(__file__).parent.parent.parent
        registry_dir = script_dir / "registry"

    print(f"Scanning registry at: {registry_dir}")

    try:
        scanner = RegistryScanner(registry_dir)
        decorators = scanner.scan()

        print(f"\nFound {len(decorators)} decorators:")
        for category, category_decorators in scanner.decorators_by_category.items():
            decorator_names = [d["decoratorName"] for d in category_decorators]
            print(
                f"  {category} ({len(category_decorators)}): {', '.join(decorator_names)}"
            )

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
