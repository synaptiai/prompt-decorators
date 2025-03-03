#!/usr/bin/env python
"""DocGenerator Enhancement Script.

This script enhances the DocGenerator class to improve documentation generation.
It adds additional functionality to ensure that all modules and decorators are
properly documented.

Example:
    Run the script to enhance the DocGenerator:

    $ python scripts/enhance_doc_generator.py

Returns:
    None: This script doesn't return anything but modifies the DocGenerator class.
"""

import logging
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))


def enhance_doc_generator() -> bool:
    """Enhance the DocGenerator class to improve documentation generation.

    Returns:
        bool: True if the enhancement succeeds, False otherwise
    """
    logger.info("Enhancing DocGenerator class...")

    # Path to the DocGenerator class
    doc_gen_path = project_root / "prompt_decorators" / "utils" / "doc_gen.py"

    if not doc_gen_path.exists():
        logger.error(f"DocGenerator file not found at {doc_gen_path}")
        return False

    # Read the current file
    with open(doc_gen_path, "r") as f:
        content = f.read()

    # Make enhancements to the DocGenerator class
    enhanced_content = enhance_docstring_extraction(content)
    enhanced_content = enhance_registry_documentation(enhanced_content)
    enhanced_content = enhance_markdown_generation(enhanced_content)
    enhanced_content = add_link_validation(enhanced_content)

    # Write the enhanced file
    with open(doc_gen_path, "w") as f:
        f.write(enhanced_content)

    logger.info("DocGenerator class enhanced successfully")
    return True


def enhance_docstring_extraction(content: str) -> str:
    """Enhance the docstring extraction functionality.

    Args:
        content: The current content of the DocGenerator class

    Returns:
        str: The enhanced content
    """
    logger.info("Enhancing docstring extraction...")

    # Improve the _extract_function_doc method to handle more docstring formats
    extract_function_pattern = (
        r"def _extract_function_doc\(self, func\).*?return \{.*?\}"
    )
    extract_function_replacement = """def _extract_function_doc(self, func) -> Dict[str, Any]:
        \"\"\"
        Extract documentation from a function or method.

        Args:
            func: The function to extract documentation from

        Returns:
            Dictionary containing function documentation
        \"\"\"
        # Get function docstring
        docstring = inspect.getdoc(func) or ""

        # Get function info
        func_name = func.__name__
        module_name = func.__module__

        # Get parameter info
        signature = inspect.signature(func)
        parameters = {}

        for name, param in signature.parameters.items():
            # Skip self and cls parameters for methods
            if name in ("self", "cls") and name == list(signature.parameters.keys())[0]:
                continue

            parameters[name] = {
                "name": name,
                "default": str(param.default) if param.default is not inspect.Parameter.empty else None,
                "kind": str(param.kind),
                "required": param.default is inspect.Parameter.empty and param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD,
            }

        # Get return annotation
        return_annotation = signature.return_annotation
        return_type = str(return_annotation) if return_annotation is not inspect.Signature.empty else None

        # Parse docstring to extract parameter descriptions, return description, and examples
        param_descriptions = {}
        return_description = ""
        raises = {}
        examples = []

        # Extract sections from Google-style docstring
        sections = self._parse_google_docstring(docstring)

        # Extract parameter descriptions
        if "Args" in sections:
            param_pattern = r"(\w+):\s*(.*?)(?=\n\s*\w+:|$)"
            for match in re.finditer(param_pattern, sections["Args"], re.DOTALL):
                param_name, param_desc = match.groups()
                param_descriptions[param_name] = param_desc.strip()

        # Extract return description
        if "Returns" in sections:
            return_description = sections["Returns"].strip()

        # Extract exceptions
        if "Raises" in sections:
            raises_pattern = r"(\w+):\s*(.*?)(?=\n\s*\w+:|$)"
            for match in re.finditer(raises_pattern, sections["Raises"], re.DOTALL):
                exception_name, exception_desc = match.groups()
                raises[exception_name] = exception_desc.strip()

        # Extract examples
        if "Example" in sections or "Examples" in sections:
            example_section = sections.get("Example", sections.get("Examples", ""))
            examples = [example_section.strip()]

        # Get type annotations
        try:
            annotations = get_type_hints(func)
        except Exception:
            annotations = {}

        return {
            "name": func_name,
            "module": module_name,
            "docstring": docstring,
            "parameters": parameters,
            "param_descriptions": param_descriptions,
            "return_type": return_type,
            "return_description": return_description,
            "raises": raises,
            "examples": examples,
            "annotations": {name: str(type_) for name, type_ in annotations.items()},
        }"""

    # Add a method to parse Google-style docstrings
    parse_docstring_method = """
    def _parse_google_docstring(self, docstring: str) -> Dict[str, str]:
        \"\"\"
        Parse a Google-style docstring into sections.

        Args:
            docstring: The docstring to parse

        Returns:
            Dictionary mapping section names to section content
        \"\"\"
        if not docstring:
            return {}

        # Split the docstring into sections
        sections = {}
        current_section = "Summary"
        current_content = []

        # Add the summary section (everything before the first section header)
        lines = docstring.split("\\n")
        for i, line in enumerate(lines):
            # Check if this line is a section header
            match = re.match(r"^\s*(\w+):\s*$", line)
            if match:
                # Store the current section
                sections[current_section] = "\\n".join(current_content).strip()
                # Start a new section
                current_section = match.group(1)
                current_content = []
            else:
                current_content.append(line)

        # Add the last section
        if current_content:
            sections[current_section] = "\\n".join(current_content).strip()

        return sections
    """

    # Replace the _extract_function_doc method
    content = re.sub(
        extract_function_pattern, extract_function_replacement, content, flags=re.DOTALL
    )

    # Add the _parse_google_docstring method before the last method
    last_method_pattern = (
        r"(def [^(]+\([^)]*\).*?return.*?\n)(\s*if __name__ == \"__main__\")"
    )
    content = re.sub(
        last_method_pattern,
        r"\1" + parse_docstring_method + r"\n\2",
        content,
        flags=re.DOTALL,
    )

    return content


def enhance_registry_documentation(content: str) -> str:
    """Enhance the registry documentation functionality.

    Args:
        content: The current content of the DocGenerator class

    Returns:
        str: The enhanced content
    """
    logger.info("Enhancing registry documentation...")

    # Improve the load_registry_data method to handle more registry formats
    load_registry_pattern = (
        r"def load_registry_data\(self\).*?return self\.registry_data"
    )
    load_registry_replacement = """def load_registry_data(self) -> Dict[str, Dict[str, Any]]:
        \"\"\"
        Load decorator definitions from the registry.

        Returns:
            Dictionary containing registry data
        \"\"\"
        logger.info(f"Loading registry data from {self.registry_path}")

        try:
            # Get all JSON files in the registry
            registry_path = Path(self.registry_path)
            json_files = []
            for pattern in ["*/*/decorator.json", "*/*/*.json"]:
                json_files.extend(registry_path.glob(pattern))

            if not json_files:
                logger.warning(f"No JSON files found in {self.registry_path}")
                return self.registry_data

            logger.info(f"Found {len(json_files)} JSON files in the registry")

            # Load each file
            for json_file in json_files:
                try:
                    # Extract decorator name from path
                    parts = json_file.parts
                    if len(parts) >= 3:
                        decorator_name = parts[2]  # registry/category/decorator_name/...

                        # Load the JSON file
                        with open(json_file) as f:
                            data = json.load(f)

                        # Store the registry data
                        self.registry_data[decorator_name] = {
                            "name": decorator_name,
                            "path": str(json_file),
                            "data": data,
                            "category": parts[1] if len(parts) >= 2 else "unknown",
                        }
                except Exception as e:
                    logger.warning(f"Error loading registry file {json_file}: {e}")

            return self.registry_data

        except Exception as e:
            logger.error(f"Error loading registry data: {e}")
            return self.registry_data"""

    # Replace the load_registry_data method
    content = re.sub(
        load_registry_pattern, load_registry_replacement, content, flags=re.DOTALL
    )

    return content


def enhance_markdown_generation(content: str) -> str:
    """Enhance the markdown generation functionality.

    Args:
        content: The current content of the DocGenerator class

    Returns:
        str: The enhanced content
    """
    logger.info("Enhancing markdown generation...")

    # Improve the generate_markdown_docs method to create better documentation
    generate_markdown_pattern = r"def generate_markdown_docs\(self\).*?logger\.info\(\"Markdown documentation generated\"\)"
    generate_markdown_replacement = """def generate_markdown_docs(self) -> None:
        \"\"\"
        Generate markdown documentation for the package.
        \"\"\"
        logger.info(f"Generating markdown documentation in {self.output_dir}")

        try:
            # Create the output directory if it doesn't exist
            os.makedirs(self.output_dir, exist_ok=True)

            # Create subdirectories
            modules_dir = os.path.join(self.output_dir, "modules")
            os.makedirs(modules_dir, exist_ok=True)

            classes_dir = os.path.join(self.output_dir, "classes")
            os.makedirs(classes_dir, exist_ok=True)

            decorators_dir = os.path.join(self.output_dir, "decorators")
            os.makedirs(decorators_dir, exist_ok=True)

            # Generate module documentation
            for module_name, module_doc in self.modules_doc.items():
                try:
                    # Create the module documentation file
                    module_file = os.path.join(modules_dir, f"{module_name}.md")
                    with open(module_file, "w") as f:
                        # Write the module header
                        f.write(f"# {module_name}\\n\\n")

                        # Write the module docstring
                        if module_doc["docstring"]:
                            f.write(f"{module_doc['docstring']}\\n\\n")

                        # Write the module members
                        if module_doc["members"]:
                            f.write("## Members\\n\\n")

                            # Write classes
                            classes = [name for name, info in module_doc["members"].items() if info["type"] == "class"]
                            if classes:
                                f.write("### Classes\\n\\n")
                                for class_name in classes:
                                    class_ref = module_doc["members"][class_name]["ref"]
                                    class_doc = self.classes_doc.get(class_ref, {})
                                    class_summary = class_doc.get("docstring", "").split("\\n")[0] if class_doc.get("docstring") else ""
                                    f.write(f"- [{class_name}](../classes/{class_ref}.md): {class_summary}\\n")
                                f.write("\\n")

                            # Write functions
                            functions = [name for name, info in module_doc["members"].items() if info["type"] == "function"]
                            if functions:
                                f.write("### Functions\\n\\n")
                                for func_name in functions:
                                    func_ref = module_doc["members"][func_name]["ref"]
                                    func_doc = self.functions_doc.get(func_ref, {})
                                    func_summary = func_doc.get("docstring", "").split("\\n")[0] if func_doc.get("docstring") else ""
                                    f.write(f"- `{func_name}`: {func_summary}\\n")
                                f.write("\\n")
                except Exception as e:
                    logger.warning(f"Error generating documentation for module {module_name}: {e}")

            # Generate class documentation
            for class_name, class_doc in self.classes_doc.items():
                try:
                    # Create the class documentation file
                    class_file = os.path.join(classes_dir, f"{class_name}.md")
                    with open(class_file, "w") as f:
                        # Write the class header
                        f.write(f"# {class_doc['name']}\\n\\n")

                        # Write the class docstring
                        if class_doc["docstring"]:
                            f.write(f"{class_doc['docstring']}\\n\\n")

                        # Write the class inheritance
                        if class_doc["bases"]:
                            f.write(f"**Inherits from:** {', '.join(class_doc['bases'])}\\n\\n")

                        # Write the class properties
                        if class_doc["properties"]:
                            f.write("## Properties\\n\\n")
                            for prop_name, prop_info in class_doc["properties"].items():
                                f.write(f"### {prop_name}\\n\\n")
                                if prop_info["docstring"]:
                                    f.write(f"{prop_info['docstring']}\\n\\n")

                        # Write the class methods
                        if class_doc["methods"]:
                            f.write("## Methods\\n\\n")
                            for method_name, method_info in class_doc["methods"].items():
                                f.write(f"### {method_name}\\n\\n")

                                # Write the method signature
                                params = []
                                for param_name, param_info in method_info.get("parameters", {}).items():
                                    if param_info.get("default"):
                                        params.append(f"{param_name}={param_info['default']}")
                                    else:
                                        params.append(param_name)

                                return_type = method_info.get("return_type", "")
                                if return_type:
                                    f.write(f"```python\\ndef {method_name}({', '.join(params)}) -> {return_type}:\\n```\\n\\n")
                                else:
                                    f.write(f"```python\\ndef {method_name}({', '.join(params)}):\\n```\\n\\n")

                                # Write the method docstring
                                if method_info["docstring"]:
                                    f.write(f"{method_info['docstring']}\\n\\n")

                                # Write the method parameters
                                if method_info.get("param_descriptions"):
                                    f.write("**Parameters:**\\n\\n")
                                    for param_name, param_desc in method_info["param_descriptions"].items():
                                        f.write(f"- `{param_name}`: {param_desc}\\n")
                                    f.write("\\n")

                                # Write the method return value
                                if method_info.get("return_description"):
                                    f.write("**Returns:**\\n\\n")
                                    f.write(f"{method_info['return_description']}\\n\\n")

                                # Write the method exceptions
                                if method_info.get("raises"):
                                    f.write("**Raises:**\\n\\n")
                                    for exception_name, exception_desc in method_info["raises"].items():
                                        f.write(f"- `{exception_name}`: {exception_desc}\\n")
                                    f.write("\\n")

                                # Write the method examples
                                if method_info.get("examples"):
                                    f.write("**Examples:**\\n\\n")
                                    for example in method_info["examples"]:
                                        f.write(f"```python\\n{example}\\n```\\n\\n")
                except Exception as e:
                    logger.warning(f"Error generating documentation for class {class_name}: {e}")

            # Generate decorator documentation from registry
            for decorator_name, decorator_info in self.registry_data.items():
                try:
                    # Create the decorator documentation file
                    decorator_file = os.path.join(decorators_dir, f"{decorator_name}.md")
                    with open(decorator_file, "w") as f:
                        # Write the decorator header
                        f.write(f"# {decorator_name} Decorator\\n\\n")

                        # Write the decorator category
                        category = decorator_info.get("category", "unknown")
                        f.write(f"**Category:** {category}\\n\\n")

                        # Write the decorator description
                        data = decorator_info.get("data", {})
                        description = data.get("description", "")
                        if description:
                            f.write(f"{description}\\n\\n")

                        # Write the decorator parameters
                        parameters = data.get("parameters", {})
                        if parameters:
                            f.write("## Parameters\\n\\n")
                            for param_name, param_info in parameters.items():
                                f.write(f"### {param_name}\\n\\n")

                                # Parameter description
                                param_desc = param_info.get("description", "")
                                if param_desc:
                                    f.write(f"{param_desc}\\n\\n")

                                # Parameter type
                                param_type = param_info.get("type", "")
                                if param_type:
                                    f.write(f"**Type:** `{param_type}`\\n\\n")

                                # Parameter default value
                                param_default = param_info.get("default", "")
                                if param_default:
                                    f.write(f"**Default:** `{param_default}`\\n\\n")

                                # Parameter required
                                param_required = param_info.get("required", False)
                                f.write(f"**Required:** {'Yes' if param_required else 'No'}\\n\\n")

                        # Write the decorator examples
                        examples = data.get("examples", [])
                        if examples:
                            f.write("## Examples\\n\\n")
                            for i, example in enumerate(examples):
                                f.write(f"### Example {i+1}\\n\\n")

                                # Example description
                                example_desc = example.get("description", "")
                                if example_desc:
                                    f.write(f"{example_desc}\\n\\n")

                                # Example code
                                example_code = example.get("code", "")
                                if example_code:
                                    f.write(f"```python\\n{example_code}\\n```\\n\\n")

                                # Example result
                                example_result = example.get("result", "")
                                if example_result:
                                    f.write(f"**Result:**\\n\\n```\\n{example_result}\\n```\\n\\n")

                        # Write the decorator compatibility
                        compatibility = data.get("compatibility", {})
                        if compatibility:
                            f.write("## Compatibility\\n\\n")

                            # Compatible with
                            compatible_with = compatibility.get("compatible_with", [])
                            if compatible_with:
                                f.write("### Compatible With\\n\\n")
                                for compat in compatible_with:
                                    f.write(f"- {compat}\\n")
                                f.write("\\n")

                            # Incompatible with
                            incompatible_with = compatibility.get("incompatible_with", [])
                            if incompatible_with:
                                f.write("### Incompatible With\\n\\n")
                                for incompat in incompatible_with:
                                    f.write(f"- {incompat}\\n")
                                f.write("\\n")
                except Exception as e:
                    logger.warning(f"Error generating documentation for decorator {decorator_name}: {e}")

            logger.info("Markdown documentation generated")
        except Exception as e:
            logger.error(f"Error generating markdown documentation: {e}")"""

    # Replace the generate_markdown_docs method
    content = re.sub(
        generate_markdown_pattern,
        generate_markdown_replacement,
        content,
        flags=re.DOTALL,
    )

    return content


def add_link_validation(content: str) -> str:
    """Add link validation functionality to the DocGenerator class.

    Args:
        content: The current content of the DocGenerator class

    Returns:
        str: The enhanced content
    """
    logger.info("Adding link validation functionality...")

    # Add a method to validate links in the documentation
    validate_links_method = """
    def validate_links(self) -> Dict[str, List[str]]:
        \"\"\"
        Validate links in the generated documentation.

        Returns:
            Dictionary mapping files to lists of broken links
        \"\"\"
        logger.info("Validating links in documentation...")

        broken_links = {}

        try:
            # Get all markdown files in the output directory
            md_files = []
            for root, dirs, files in os.walk(self.output_dir):
                for file in files:
                    if file.endswith(".md"):
                        md_files.append(os.path.join(root, file))

            logger.info(f"Found {len(md_files)} markdown files to validate")

            # Check links in each file
            for md_file in md_files:
                try:
                    with open(md_file, "r") as f:
                        content = f.read()

                    # Find all links in the file
                    links = re.findall(r"\\[.*?\\]\\((.*?)\\)", content)

                    # Check each link
                    file_broken_links = []
                    for link in links:
                        # Skip external links
                        if link.startswith("http"):
                            continue

                        # Check if the link is valid
                        link_path = os.path.normpath(os.path.join(os.path.dirname(md_file), link))
                        if not os.path.exists(link_path):
                            file_broken_links.append(link)

                    # Store broken links for this file
                    if file_broken_links:
                        broken_links[md_file] = file_broken_links
                except Exception as e:
                    logger.warning(f"Error validating links in {md_file}: {e}")

            # Log broken links
            if broken_links:
                logger.warning(f"Found {sum(len(links) for links in broken_links.values())} broken links in {len(broken_links)} files")
                for file, links in broken_links.items():
                    logger.warning(f"Broken links in {file}: {', '.join(links)}")
            else:
                logger.info("No broken links found")

            return broken_links
        except Exception as e:
            logger.error(f"Error validating links: {e}")
            return {}
    """

    # Add the validate_links method before the last method
    last_method_pattern = (
        r"(def [^(]+\([^)]*\).*?return.*?\n)(\s*if __name__ == \"__main__\")"
    )
    content = re.sub(
        last_method_pattern,
        r"\1" + validate_links_method + r"\n\2",
        content,
        flags=re.DOTALL,
    )

    return content


def main() -> int:
    """Run the DocGenerator enhancement script.

    Returns:
        int: 0 if the enhancement succeeds, 1 otherwise
    """
    try:
        if enhance_doc_generator():
            logger.info("DocGenerator enhancement completed successfully")
            return 0
        else:
            logger.error("DocGenerator enhancement failed")
            return 1
    except Exception as e:
        logger.error(f"Error enhancing DocGenerator: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
