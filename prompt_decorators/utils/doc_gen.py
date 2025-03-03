"""Documentation Generator Module.

This module provides utilities for generating API documentation from code and registry metadata.
"""
import importlib
import inspect
import json
import logging
import os
import pkgutil
import re
from pathlib import Path
from typing import Any, Dict, Optional, get_type_hints

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class DocGenerator:
    """Generator for API documentation from code and registry metadata.

    This class provides utilities for extracting docstrings, type annotations,
    and other metadata from Python code, and generating documentation in various formats.
    """

    def __init__(
        self,
        package_path: Optional[str] = None,
        registry_path: Optional[str] = None,
        output_dir: Optional[str] = None,
    ):
        """Initialize the documentation generator.

        Args:
            package_path: Path to the Python package to document
            registry_path: Path to the registry directory containing decorator definitions
            output_dir: Directory where documentation should be written
        """
        self.package_path = package_path
        self.registry_path = registry_path
        self.output_dir = output_dir or "docs/api"

        # Store extracted documentation
        self.modules_doc: Dict[str, Dict[str, Any]] = {}
        self.classes_doc: Dict[str, Dict[str, Any]] = {}
        self.functions_doc: Dict[str, Dict[str, Any]] = {}

        # Registry data
        self.registry_data: Dict[str, Dict[str, Any]] = {}

    def extract_package_docs(self, package_name: str) -> Dict[str, Any]:
        """Extract documentation from a Python package.

        Args:
            package_name: Name of the package to document

        Returns:
            Dictionary containing documentation for all modules, classes, and functions
        """
        logger.info(f"Extracting documentation from package: {package_name}")

        try:
            # Import the package
            package = importlib.import_module(package_name)

            # Extract documentation from the package
            package_doc = self._extract_module_doc(package)
            self.modules_doc[package_name] = package_doc

            # Walk through all modules in the package
            for _, modname, ispkg in pkgutil.iter_modules(
                package.__path__, package.__name__ + "."
            ):
                try:
                    # Import the module
                    module = importlib.import_module(modname)

                    # Extract documentation from the module
                    module_doc = self._extract_module_doc(module)
                    self.modules_doc[modname] = module_doc

                    # Extract documentation from classes and functions
                    self._extract_members_doc(module)

                    # Recursively extract docs from subpackages
                    if ispkg:
                        self.extract_package_docs(modname)

                except Exception as e:
                    logger.warning(f"Error extracting docs from module {modname}: {e}")

            # Store the extracted documentation in self.code_docs
            self.code_docs = {
                "modules": self.modules_doc,
                "classes": self.classes_doc,
                "functions": self.functions_doc,
            }

            return self.code_docs

        except Exception as e:
            logger.error(f"Error extracting docs from package {package_name}: {e}")
            return {}

    def _extract_module_doc(self, module) -> Dict[str, Any]:
        """Extract documentation from a module.

        Args:
            module: The module to extract documentation from

        Returns:
            Dictionary containing module documentation
        """
        # Get module docstring
        docstring = inspect.getdoc(module) or ""

        # Get module info
        module_path = getattr(module, "__file__", "")
        module_name = module.__name__

        return {
            "name": module_name,
            "path": module_path,
            "docstring": docstring,
            "members": {},
        }

    def _extract_members_doc(self, module) -> None:
        """Extract documentation from module members (classes and functions).

        Args:
            module: The module to extract documentation from

        Returns:
            None
        """
        module_name = module.__name__

        # Get all members
        for name, obj in inspect.getmembers(module):
            # Skip private members
            if name.startswith("_"):
                continue

            # Check if the member is defined in this module
            if hasattr(obj, "__module__") and obj.__module__ != module_name:
                continue

            try:
                # Extract class documentation
                if inspect.isclass(obj):
                    class_doc = self._extract_class_doc(obj)
                    self.classes_doc[f"{module_name}.{name}"] = class_doc
                    self.modules_doc[module_name]["members"][name] = {
                        "type": "class",
                        "ref": f"{module_name}.{name}",
                    }

                # Extract function documentation
                elif inspect.isfunction(obj):
                    func_doc = self._extract_function_doc(obj)
                    self.functions_doc[f"{module_name}.{name}"] = func_doc
                    self.modules_doc[module_name]["members"][name] = {
                        "type": "function",
                        "ref": f"{module_name}.{name}",
                    }
            except Exception as e:
                logger.warning(f"Error extracting docs from {module_name}.{name}: {e}")

    def _extract_class_doc(self, cls) -> Dict[str, Any]:
        """Extract documentation from a class.

        Args:
            cls: The class to extract documentation from

        Returns:
            Dictionary containing class documentation
        """
        # Get class docstring
        docstring = inspect.getdoc(cls) or ""

        # Get class info
        class_name = cls.__name__
        module_name = cls.__module__
        bases = [base.__name__ for base in cls.__bases__ if base.__name__ != "object"]

        # Get class members
        methods = {}
        class_properties = {}

        # Extract method and property documentation
        for name, obj in inspect.getmembers(cls):
            try:
                # Skip inherited and private members
                if name.startswith("_") and name != "__init__":
                    continue

                # Extract method documentation
                if inspect.isfunction(obj) or inspect.ismethod(obj):
                    methods[name] = self._extract_function_doc(obj)

                # Extract property documentation
                elif isinstance(obj, property):
                    class_properties[name] = {
                        "name": name,
                        "docstring": inspect.getdoc(obj) or "",
                    }
            except Exception as e:
                logger.warning(f"Error extracting docs from {class_name}.{name}: {e}")

        # Get type annotations
        try:
            annotations = get_type_hints(cls)
        except Exception:
            annotations = {}

        return {
            "name": class_name,
            "module": module_name,
            "docstring": docstring,
            "bases": bases,
            "methods": methods,
            "properties": class_properties,
            "annotations": {name: str(type_) for name, type_ in annotations.items()},
        }

    def _extract_function_doc(self, func) -> Dict[str, Any]:
        """Extract documentation from a function or method.

        Args:
            func: The function to extract documentation from

        Returns:
            Dictionary containing function documentation
        """
        # Get function docstring
        docstring = inspect.getdoc(func) or ""

        # Get function info
        func_name = func.__name__
        module_name = func.__module__

        # Get parameter info
        params = {}
        signature = inspect.signature(func)

        for name, param in signature.parameters.items():
            # Skip self parameter for methods
            if name == "self":
                continue

            param_info = {
                "name": name,
                "default": None if param.default is param.empty else str(param.default),
                "optional": param.default is not param.empty,
                "kind": str(param.kind),
            }

            # Add to params
            params[name] = param_info

        # Get return type
        return_annotation = signature.return_annotation
        return_type = (
            None if return_annotation is signature.empty else str(return_annotation)
        )

        # Get parameter types from docstring
        param_types = self._extract_param_types_from_docstring(docstring)

        # Get return type from docstring
        docstring_return_type = self._extract_return_type_from_docstring(docstring)
        if docstring_return_type and not return_type:
            return_type = docstring_return_type

        # Update parameter types from docstring
        for name, param_info in params.items():
            if name in param_types:
                param_info["type"] = param_types[name]

        # Try to get type annotations
        try:
            annotations = get_type_hints(func)

            # Update parameter types from annotations
            for name, type_hint in annotations.items():
                if name in params:
                    params[name]["type"] = str(type_hint)
                elif name == "return":
                    return_type = str(type_hint)
        except Exception:
            pass

        return {
            "name": func_name,
            "module": module_name,
            "docstring": docstring,
            "parameters": params,
            "return_type": return_type,
        }

    def _extract_param_types_from_docstring(self, docstring: str) -> Dict[str, str]:
        """Extract parameter types from a docstring.

        Args:
            docstring: The docstring to extract types from

        Returns:
            Dictionary mapping parameter names to types
        """
        param_types = {}

        # Check if docstring is None or empty
        if not docstring:
            return param_types

        # Split docstring into sections
        sections = {}
        current_section = None
        section_content = []

        for line in docstring.split("\n"):
            # Check for section headers
            section_match = re.match(
                r"^\s*(Args|Returns|Raises|Yields|Examples|Note|Notes|Warning|Attributes):\s*$",
                line,
            )
            if section_match:
                # Save the previous section
                if current_section:
                    sections[current_section] = section_content

                # Start a new section
                current_section = section_match.group(1)
                section_content = []
            elif current_section and line.strip():
                # Add content to current section
                section_content.append(line)

        # Save the last section
        if current_section and section_content:
            sections[current_section] = section_content

        # Process Args section for parameter types
        if "Args" in sections:
            for line in sections["Args"]:
                # Match patterns like "param_name: Description" or "param_name (type): Description"
                param_match = re.match(
                    r"^\s*([a-zA-Z0-9_]+)(\s*\(([^)]+)\))?:\s*(.+)$", line
                )
                if param_match:
                    param_name = param_match.group(1).strip()
                    param_type = (
                        param_match.group(3).strip() if param_match.group(3) else None
                    )

                    if param_type:
                        param_types[param_name] = param_type

        return param_types

    def _extract_return_type_from_docstring(self, docstring: str) -> Optional[str]:
        """Extract return type from a docstring.

        Args:
            docstring: The docstring to extract the return type from

        Returns:
            Return type as a string, or None if not found
        """
        # Check if docstring is None or empty
        if not docstring:
            return None

        # Split docstring into sections
        sections = {}
        current_section = None
        section_content = []

        for line in docstring.split("\n"):
            # Check for section headers
            section_match = re.match(
                r"^\s*(Args|Returns|Raises|Yields|Examples|Note|Notes|Warning|Attributes):\s*$",
                line,
            )
            if section_match:
                # Save the previous section
                if current_section:
                    sections[current_section] = section_content

                # Start a new section
                current_section = section_match.group(1)
                section_content = []
            elif current_section and line.strip():
                # Add content to current section
                section_content.append(line)

        # Save the last section
        if current_section and section_content:
            sections[current_section] = section_content

        # Process Returns section for return type
        if "Returns" in sections:
            for line in sections["Returns"]:
                # Match patterns like "type: Description"
                return_match = re.match(r"^\s*([^:]+):\s*(.+)$", line)
                if return_match:
                    return_type = return_match.group(1).strip()
                    return return_type

        return None

    def load_registry_data(self) -> Dict[str, Dict[str, Any]]:
        """Load decorator definitions from the registry.

        Args:
            self: The DocGenerator instance

        Returns:
            Dictionary mapping decorator names to their definitions
        """
        if not self.registry_path:
            logger.warning("Registry path not specified")
            return {}

        registry_path = Path(self.registry_path)
        if not registry_path.exists() or not registry_path.is_dir():
            logger.warning(f"Registry path not found: {registry_path}")
            return {}

        logger.info(f"Loading registry data from: {registry_path}")

        registry_data = {}

        # Scan for JSON files
        for json_file in registry_path.glob("**/*.json"):
            try:
                with open(json_file, "r") as f:
                    data = json.load(f)

                # Check if this is a decorator definition
                if "decoratorName" in data:
                    decorator_name = data["decoratorName"]
                    registry_data[decorator_name] = data
                    logger.debug(f"Loaded decorator definition: {decorator_name}")
            except Exception as e:
                logger.warning(f"Error loading {json_file}: {e}")

        self.registry_data = registry_data
        return registry_data

    def merge_code_and_registry_docs(self) -> Dict[str, Dict[str, Any]]:
        """Merge documentation extracted from code with registry data.

        Args:
            self: The DocGenerator instance

        Returns:
            Dictionary mapping decorator names to their merged documentation"""
        # Initialize with empty dictionaries to ensure keys always exist
        merged_docs = {
            "modules": {},
            "classes": {},
            "functions": {},
            "decorators": {},
        }

        # Create self.code_docs if it doesn't exist
        if not hasattr(self, "code_docs"):
            self.code_docs = {
                "modules": self.modules_doc,
                "classes": self.classes_doc,
                "functions": self.functions_doc,
            }

        if not self.code_docs or not self.code_docs.get("classes"):
            logger.warning("Code documentation not available")
            # Still return the structure with empty dictionaries
            return merged_docs

        # Copy code documentation
        merged_docs["modules"] = self.code_docs["modules"].copy()
        merged_docs["classes"] = self.code_docs["classes"].copy()
        merged_docs["functions"] = self.code_docs["functions"].copy()

        # Match registry data with code documentation
        for decorator_name, registry_def in self.registry_data.items():
            # Try to find the corresponding class
            found_class = False
            for class_path, class_doc in self.code_docs["classes"].items():
                # Check if class name matches decorator name (case-insensitive)
                if class_doc["name"].lower() == decorator_name.lower():
                    # Merge the data
                    merged_docs["decorators"][decorator_name] = {
                        "code_docs": class_doc,
                        "registry_def": registry_def,
                    }
                    found_class = True
                    break

                # Also check if the class is in the decorators module and matches the decorator name
                if (
                    class_doc["module"].startswith("prompt_decorators.decorators")
                    and class_doc["name"].lower() == decorator_name.lower()
                ):
                    merged_docs["decorators"][decorator_name] = {
                        "code_docs": class_doc,
                        "registry_def": registry_def,
                    }
                    found_class = True
                    break

            # If no matching class was found, just use registry data
            if not found_class:
                logger.debug(
                    f"No code documentation found for decorator: {decorator_name}"
                )
                merged_docs["decorators"][decorator_name] = {
                    "code_docs": None,
                    "registry_def": registry_def,
                }

        return merged_docs

    def generate_markdown_docs(self, output_dir: Optional[str] = None) -> None:
        """Generate markdown documentation files.

        Args:
            output_dir: Optional output directory path

        Returns:
            None"""
        # Use provided output_dir or default
        output_dir = output_dir or self.output_dir
        os.makedirs(output_dir, exist_ok=True)

        logger.info(f"Generating Markdown documentation in: {output_dir}")

        # Merge code and registry documentation
        merged_docs = self.merge_code_and_registry_docs()

        # Generate index file
        self._generate_index_markdown(merged_docs, output_dir)

        # Generate module documentation
        os.makedirs(f"{output_dir}/modules", exist_ok=True)
        for module_path, module_doc in merged_docs["modules"].items():
            self._generate_module_markdown(
                module_path, module_doc, merged_docs, output_dir
            )

        # Generate decorator documentation
        os.makedirs(f"{output_dir}/decorators", exist_ok=True)
        for decorator_name, decorator_doc in merged_docs["decorators"].items():
            self._generate_decorator_markdown(decorator_name, decorator_doc, output_dir)

    def _generate_index_markdown(self, docs: Dict[str, Any], output_dir: str) -> None:
        """Generate the index markdown file.

        Args:
            docs: Dictionary of documentation data
            output_dir: Output directory path

        Returns:
            None"""
        logger.info(f"Generating index markdown in {output_dir}")
        index_content = "# Prompt Decorators API Documentation\n\n"

        # Add modules section
        index_content += "## Modules\n\n"
        if "modules" in docs and docs["modules"]:
            for module_path, _module_doc in docs["modules"].items():
                # Skip internal modules
                if "._" in module_path:
                    continue

                module_path.split(".")[-1]
                index_content += f"- [{module_path}](modules/{module_path}.md)\n"
        else:
            index_content += "No modules documented.\n"

        # Add decorators section
        index_content += "\n## Decorators\n\n"
        if "decorators" in docs and docs["decorators"]:
            for decorator_name, _decorator_doc in docs["decorators"].items():
                index_content += (
                    f"- [{decorator_name}](decorators/{decorator_name}.md)\n"
                )
        else:
            index_content += "No decorators documented.\n"

        # Write the index file
        with open(f"{output_dir}/index.md", "w") as f:
            f.write(index_content)

    def _generate_module_markdown(
        self,
        module_path: str,
        module_doc: Dict[str, Any],
        docs: Dict[str, Any],
        output_dir: str,
    ) -> None:
        """Generate markdown documentation for a module.

        Args:
            module_path: Path to the module
            module_doc: Module documentation data
            docs: Dictionary of all documentation data
            output_dir: Output directory path

        Returns:
            None"""
        logger.info(f"Generating markdown for module: {module_path}")

        # Skip internal modules
        if "._" in module_path:
            return

        module_content = f"# Module `{module_path}`\n\n"

        # Add docstring
        if module_doc["docstring"]:
            module_content += f"{module_doc['docstring']}\n\n"

        # Add classes section
        classes = []
        for name, member in module_doc["members"].items():
            if member["type"] == "class":
                classes.append((name, member["ref"]))

        if classes:
            module_content += "## Classes\n\n"
            for name, ref in classes:
                class_doc = docs["classes"].get(ref, {})
                summary = self._get_summary(class_doc.get("docstring", ""))
                module_content += f"- [`{name}`](#class-{name.lower()}): {summary}\n"

            module_content += "\n"

            # Add detailed class documentation
            for name, ref in classes:
                class_doc = docs["classes"].get(ref, {})
                module_content += self._format_class_markdown(name, class_doc)

        # Add functions section
        functions = []
        for name, member in module_doc["members"].items():
            if member["type"] == "function":
                functions.append((name, member["ref"]))

        if functions:
            module_content += "## Functions\n\n"
            for name, ref in functions:
                func_doc = docs["functions"].get(ref, {})
                summary = self._get_summary(func_doc.get("docstring", ""))
                module_content += f"- [`{name}`](#function-{name.lower()}): {summary}\n"

            module_content += "\n"

            # Add detailed function documentation
            for name, ref in functions:
                func_doc = docs["functions"].get(ref, {})
                module_content += self._format_function_markdown(name, func_doc)

        # Write the module file
        with open(f"{output_dir}/modules/{module_path}.md", "w") as f:
            f.write(module_content)

    def _generate_decorator_markdown(
        self, decorator_name: str, decorator_doc: Dict[str, Any], output_dir: str
    ) -> None:
        """Generate markdown documentation for a decorator.

        Args:
            decorator_name: Name of the decorator
            decorator_doc: Decorator documentation data
            output_dir: Output directory path

        Returns:
            None"""
        logger.info(f"Generating markdown for decorator: {decorator_name}")

        registry_def = decorator_doc["registry_def"]
        code_docs = decorator_doc.get("code_docs")

        decorator_content = f"# Decorator `{decorator_name}`\n\n"

        # Add a note if this is a placeholder
        if not code_docs:
            decorator_content += "> **Note:** This documentation is currently being updated. Some details may be incomplete.\n\n"

        # Add version
        if "version" in registry_def:
            decorator_content += f"**Version:** {registry_def['version']}\n\n"

        # Add description
        if "description" in registry_def:
            decorator_content += f"{registry_def['description']}\n\n"
        elif code_docs and code_docs.get("docstring"):
            decorator_content += f"{code_docs['docstring']}\n\n"
        else:
            decorator_content += "No description available.\n\n"

        # Add category
        if "category" in registry_def:
            decorator_content += f"**Category:** {registry_def['category']}\n\n"

        # Add parameters section
        if "parameters" in registry_def:
            decorator_content += "## Parameters\n\n"

            for param in registry_def["parameters"]:
                param_name = param.get("name", "")
                param_type = param.get("type", "")
                param_desc = param.get("description", "")
                param_default = param.get("default", "")
                param_required = param.get("required", False)

                decorator_content += f"### `{param_name}`\n\n"
                decorator_content += f"**Type:** {param_type}  \n"
                decorator_content += (
                    f"**Required:** {'Yes' if param_required else 'No'}  \n"
                )

                if param_default:
                    decorator_content += f"**Default:** `{param_default}`  \n"

                if param_desc:
                    decorator_content += f"\n{param_desc}\n\n"

                # Add enum values if applicable
                if param_type == "enum" and "enum" in param:
                    decorator_content += "**Allowed values:**\n\n"
                    for enum_val in param["enum"]:
                        decorator_content += f"- `{enum_val}`\n"
                    decorator_content += "\n"

        # Add examples section
        if "examples" in registry_def and registry_def["examples"]:
            decorator_content += "## Examples\n\n"

            for i, example in enumerate(registry_def["examples"], 1):
                example_desc = example.get("description", f"Example {i}")
                example_usage = example.get("usage", "")
                example_result = example.get("result", "")

                decorator_content += f"### {example_desc}\n\n"

                if example_usage:
                    decorator_content += "```\n"
                    decorator_content += f"{example_usage}\n"
                    decorator_content += "```\n\n"

                if example_result:
                    decorator_content += "Result:\n\n"
                    decorator_content += f"{example_result}\n\n"

        # Add compatibility section
        if "compatibility" in registry_def:
            compat = registry_def["compatibility"]
            decorator_content += "## Compatibility\n\n"

            if "requires" in compat and compat["requires"]:
                decorator_content += "**Requires:**\n\n"
                for req in compat["requires"]:
                    decorator_content += f"- `{req}`\n"
                decorator_content += "\n"

            if "conflicts" in compat and compat["conflicts"]:
                decorator_content += "**Conflicts with:**\n\n"
                for conflict in compat["conflicts"]:
                    decorator_content += f"- `{conflict}`\n"
                decorator_content += "\n"

            if "models" in compat and compat["models"]:
                decorator_content += "**Supported models:**\n\n"
                for model in compat["models"]:
                    decorator_content += f"- `{model}`\n"
                decorator_content += "\n"

        # Add implementation details if code documentation is available
        if code_docs:
            decorator_content += "## Implementation\n\n"

            # Add class inheritance
            if code_docs.get("bases"):
                bases = ", ".join(code_docs["bases"])
                decorator_content += f"Inherits from: `{bases}`\n\n"

            # Add methods
            methods = code_docs.get("methods", {})
            if methods:
                decorator_content += "### Methods\n\n"

                for method_name, method_doc in methods.items():
                    decorator_content += f"#### `{method_name}`\n\n"

                    # Add method signature
                    params = method_doc.get("parameters", {})
                    param_str = ", ".join(
                        [
                            f"{name}{'=' + default if default and default != 'None' else ''}"
                            for name, param in params.items()
                            for default in [param.get("default")]
                        ]
                    )

                    return_type = method_doc.get("return_type", "")
                    if return_type:
                        decorator_content += f"**Signature:** `{method_name}({param_str}) -> {return_type}`\n\n"
                    else:
                        decorator_content += (
                            f"**Signature:** `{method_name}({param_str})`\n\n"
                        )

                    # Add method docstring
                    if method_doc.get("docstring"):
                        decorator_content += f"{method_doc['docstring']}\n\n"
        else:
            # Add a placeholder for implementation details
            decorator_content += "## Implementation\n\n"
            decorator_content += (
                "Implementation details will be available in a future update.\n\n"
            )

        # Create the decorators directory if it doesn't exist
        os.makedirs(f"{output_dir}/decorators", exist_ok=True)

        # Write the decorator file
        with open(f"{output_dir}/decorators/{decorator_name}.md", "w") as f:
            f.write(decorator_content)

    def _format_class_markdown(self, class_name: str, class_doc: Dict[str, Any]) -> str:
        """Format a class for Markdown documentation.

        Args:
            class_name: The class name
            class_doc: The class documentation

        Returns:
            Formatted Markdown string
        """
        content = f"### Class `{class_name}`\n\n"

        # Add docstring
        if class_doc.get("docstring"):
            content += f"{class_doc['docstring']}\n\n"

        # Add inheritance
        if class_doc.get("bases"):
            bases = ", ".join(class_doc["bases"])
            content += f"**Inherits from:** `{bases}`\n\n"

        # Add methods
        methods = class_doc.get("methods", {})
        if methods:
            content += "#### Methods\n\n"

            for method_name, method_doc in methods.items():
                # Add method signature
                params = method_doc.get("parameters", {})
                param_str = ", ".join(
                    [
                        f"{name}{'=' + default if default and default != 'None' else ''}"
                        for name, param in params.items()
                        for default in [param.get("default")]
                    ]
                )

                return_type = method_doc.get("return_type", "")
                if return_type:
                    content += f"- `{method_name}({param_str}) -> {return_type}`\n"
                else:
                    content += f"- `{method_name}({param_str})`\n"

        # Add properties
        properties = class_doc.get("properties", {})
        if properties:
            content += "#### Properties\n\n"

            for prop_name, prop_doc in properties.items():
                content += f"- `{prop_name}`: {self._get_summary(prop_doc.get('docstring', ''))}\n"

        return content + "\n"

    def _format_function_markdown(
        self, func_name: str, func_doc: Dict[str, Any]
    ) -> str:
        """Format a function for Markdown documentation.

        Args:
            func_name: The function name
            func_doc: The function documentation

        Returns:
            Formatted Markdown string
        """
        content = f"### Function `{func_name}`\n\n"

        # Add function signature
        params = func_doc.get("parameters", {})
        param_str = ", ".join(
            [
                f"{name}{'=' + default if default and default != 'None' else ''}"
                for name, param in params.items()
                for default in [param.get("default")]
            ]
        )

        return_type = func_doc.get("return_type", "")
        if return_type:
            content += f"**Signature:** `{func_name}({param_str}) -> {return_type}`\n\n"
        else:
            content += f"**Signature:** `{func_name}({param_str})`\n\n"

        # Add docstring
        if func_doc.get("docstring"):
            content += f"{func_doc['docstring']}\n\n"

        return content

    def _get_summary(self, docstring: str) -> str:
        """Get a summary from a docstring.

        Args:
            docstring: The docstring to get a summary from

        Returns:
            The first line of the docstring
        """
        if not docstring:
            return ""

        lines = docstring.strip().split("\n")
        return lines[0].strip()

    def generate_html_docs(self, output_dir: Optional[str] = None) -> None:
        """Generate HTML documentation files.

        Args:
            output_dir: Optional output directory path

        Returns:
            None"""
        # Use provided output_dir or default
        output_dir = output_dir or f"{self.output_dir}/html"
        os.makedirs(output_dir, exist_ok=True)

        logger.info(f"Converting Markdown to HTML in: {output_dir}")

        # First generate Markdown
        markdown_dir = f"{self.output_dir}/markdown"
        self.generate_markdown_docs(markdown_dir)

        # Convert Markdown to HTML
        # For now, this is a placeholder
        logger.warning("HTML generation not yet implemented")

        # Copy the index file
        with open(f"{markdown_dir}/index.md", "r") as f:
            content = f.read()

        with open(f"{output_dir}/index.html", "w") as f:
            f.write(f"<html><body><pre>{content}</pre></body></html>")

    def generate_cli(self) -> None:
        """Create a command-line interface script for documentation generation."""
        script_path = Path(self.output_dir).parent / "generate_docs.py"

        script_content = '''#!/usr/bin/env python
"""
Documentation Generator CLI

This script provides a command-line interface for generating API documentation.
"""
import argparse
import logging
import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from prompt_decorators.utils.doc_gen import DocGenerator

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    """Run the documentation generator CLI."""
    parser = argparse.ArgumentParser(description="Generate API documentation")
    parser.add_argument(
        "--package", "-p",
        default="prompt_decorators",
        help="Name of the package to document"
    )
    parser.add_argument(
        "--registry", "-r",
        default="registry",
        help="Path to the registry directory"
    )
    parser.add_argument(
        "--output", "-o",
        default="docs/api",
        help="Directory where documentation should be written"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["markdown", "html", "both"],
        default="markdown",
        help="Output format for documentation"
    )

    args = parser.parse_args()

    # Create the documentation generator
    generator = DocGenerator(
        package_path=args.package,
        registry_path=args.registry,
        output_dir=args.output
    )

    # Extract documentation
    generator.extract_package_docs(args.package)

    # Load registry data
    generator.load_registry_data()

    # Generate documentation
    if args.format == "markdown" or args.format == "both":
        generator.generate_markdown_docs()

    if args.format == "html" or args.format == "both":
        generator.generate_html_docs()

    logger.info("Documentation generation complete")


if __name__ == "__main__":
    main()
'''
        # Write the script
        with open(script_path, "w") as f:
            f.write(script_content)

        # Make the script executable
        os.chmod(script_path, 0o755)

        logger.info(f"Created documentation generator CLI script: {script_path}")


# Convenience function to get a documentation generator
def get_doc_generator(
    package_path: Optional[str] = None,
    registry_path: Optional[str] = None,
    output_dir: Optional[str] = None,
) -> DocGenerator:
    """Get a documentation generator.

    Args:
        package_path: Path to the Python package to document
        registry_path: Path to the registry directory containing decorator definitions
        output_dir: Directory where documentation should be written

    Returns:
        A documentation generator instance
    """
    return DocGenerator(
        package_path=package_path, registry_path=registry_path, output_dir=output_dir
    )
