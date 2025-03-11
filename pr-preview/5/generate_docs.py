#!/usr/bin/env python3
"""
Documentation Generator for Prompt Decorators

This script generates API documentation for the Prompt Decorators package.
It creates Markdown files for each module, class, and function in the package.
"""

import argparse
import importlib
import inspect
import json
import os
import pkgutil
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Type, Union

# Add the parent directory to the path so we can import prompt_decorators
sys.path.insert(0, str(Path(__file__).parent.parent))

import prompt_decorators
from prompt_decorators.core.base import DecoratorBase
from prompt_decorators.core.dynamic_decorator import DynamicDecorator
from prompt_decorators.core.registry import get_categories, get_decorator, get_registry

# Directory where API documentation will be generated
API_DOCS_DIR = Path(__file__).parent / "api"
API_MODULES_DIR = API_DOCS_DIR / "modules"
API_DECORATORS_DIR = API_DOCS_DIR / "decorators"
DECORATOR_DOCS_DIR = Path(__file__).parent / "decorators"
REGISTRY_DIR = Path(__file__).parent.parent / "registry"


def ensure_directory(directory: Path) -> None:
    """Ensure the directory exists."""
    directory.mkdir(parents=True, exist_ok=True)


def sanitize_docstring(docstring: str) -> str:
    """Clean up problematic references in docstrings.

    This function replaces references to external modules like pydantic_core with
    plain text to avoid cross-reference warnings.

    Args:
        docstring: The original docstring

    Returns:
        Sanitized docstring with problematic references fixed
    """
    # Replace references to external modules that cause cross-reference warnings
    replacements = {
        "[`ValidationError`][pydantic_core.ValidationError]": "`ValidationError`",
        "[`PydanticSerializationError`][pydantic_core.PydanticSerializationError]": "`PydanticSerializationError`",
        "pydantic_core.ValidationError": "ValidationError",
        "pydantic_core.PydanticSerializationError": "PydanticSerializationError",
    }

    for search, replace in replacements.items():
        docstring = docstring.replace(search, replace)

    return docstring


def generate_module_doc(module_name: str, module: Any) -> str:
    """Generate documentation for a module.

    Args:
        module_name: The fully-qualified name of the module
        module: The imported module object

    Returns:
        Markdown documentation for the module
    """
    # Create short name for display
    short_name = module_name.split(".")[-1]
    doc = f"# {short_name}\n\n"

    # Try to extract the module docstring
    if module.__doc__:
        # Clean up the docstring (remove indentation and extra whitespace)
        docstring = inspect.cleandoc(module.__doc__)
        # Sanitize problematic references
        docstring = sanitize_docstring(docstring)
        doc += f"{docstring}\n\n"
    else:
        doc += f"Module documentation for {module_name}.\n\n"

    # Check for __all__ to determine the public API
    public_api = getattr(module, "__all__", None)

    if public_api:
        doc += "## Public API\n\n"
        doc += "This module exports the following components:\n\n"

        for name in public_api:
            try:
                obj = getattr(module, name)
                obj_doc = obj.__doc__ if obj.__doc__ else "No description available"
                obj_doc = sanitize_docstring(obj_doc).split(".")[0]

                if inspect.isclass(obj):
                    doc += f"- `{name}`: Class - {obj_doc}\n"
                elif inspect.isfunction(obj):
                    doc += f"- `{name}`: Function - {obj_doc}\n"
                else:
                    doc += f"- `{name}`: {type(obj).__name__} - {obj_doc}\n"
            except AttributeError:
                doc += f"- `{name}`: Not found in module\n"

        doc += "\n"

    # Get all classes, functions, and variables in the module
    classes = []
    functions = []
    variables = []

    for name, obj in inspect.getmembers(module):
        # Skip private members
        if name.startswith("_") and name != "__all__":
            continue

        # For classes and functions, check if they're defined in this module or imported
        if inspect.isclass(obj) or inspect.isfunction(obj):
            obj_module = getattr(obj, "__module__", None)

            # Include if defined in this module or explicitly listed in __all__
            if obj_module == module.__name__ or (public_api and name in public_api):
                if inspect.isclass(obj):
                    classes.append((name, obj, obj_module))
                else:
                    functions.append((name, obj, obj_module))
        # For variables, include if not callable and not a module
        elif (
            not callable(obj) and not inspect.ismodule(obj) and not name.startswith("_")
        ):
            variables.append((name, obj))

    # Document module variables (constants, etc.)
    if variables:
        doc += "## Module Variables\n\n"
        for name, value in sorted(variables):
            doc += f"### `{name}`\n\n"
            doc += f"Type: `{type(value).__name__}`\n\n"
            try:
                doc += f"Value: `{repr(value)}`\n\n"
            except Exception:
                doc += "Value: `<unable to represent>`\n\n"

    # Document classes
    if classes:
        doc += "## Classes\n\n"
        for name, cls, cls_module in sorted(classes):
            doc += f"### `{name}`\n\n"

            # Indicate if the class is imported
            if cls_module != module.__name__:
                doc += f"*Imported from `{cls_module}`*\n\n"

            if cls.__doc__:
                doc += f"{inspect.cleandoc(cls.__doc__)}\n\n"
            else:
                doc += f"No documentation available for class `{name}`.\n\n"

            # Document base classes if any
            if cls.__bases__ and cls.__bases__ != (object,):
                doc += "**Bases:** "
                bases = []
                for base in cls.__bases__:
                    if base.__name__ != "object":
                        base_module = base.__module__
                        bases.append(f"`{base_module}.{base.__name__}`")
                doc += ", ".join(bases) + "\n\n"

            # Document class attributes
            class_attrs = []
            for attr_name, attr_value in cls.__dict__.items():
                if (
                    not attr_name.startswith("_")
                    and not inspect.isfunction(attr_value)
                    and not inspect.ismethod(attr_value)
                ):
                    class_attrs.append((attr_name, attr_value))

            if class_attrs:
                doc += "#### Attributes\n\n"
                for attr_name, attr_value in sorted(class_attrs):
                    doc += f"- `{attr_name}`: `{type(attr_value).__name__}`"
                    try:
                        doc += f" = `{repr(attr_value)}`"
                    except Exception:
                        # Some objects can't be repr'd safely
                        pass
                    doc += "\n"
                doc += "\n"

            # Document methods
            methods = []
            for method_name, method in inspect.getmembers(cls, inspect.isfunction):
                if not method_name.startswith("_") or method_name == "__init__":
                    methods.append((method_name, method))

            if methods:
                doc += "#### Methods\n\n"
                for method_name, method in sorted(methods):
                    doc += f"##### `{method_name}`\n\n"
                    if method.__doc__:
                        clean_doc = inspect.cleandoc(method.__doc__)
                        clean_doc = sanitize_docstring(clean_doc)
                        doc += f"{clean_doc}\n\n"

                    # Document method signature
                    try:
                        sig = inspect.signature(method)
                        doc += f"**Signature:** `{method_name}{sig}`\n\n"
                    except (ValueError, TypeError):
                        pass

                    # Document parameters
                    if sig.parameters:
                        doc += "**Parameters:**\n\n"
                        for param_name, param in sig.parameters.items():
                            if param_name == "self" or param_name == "cls":
                                continue
                            doc += f"- `{param_name}`: "
                            if param.annotation != inspect.Parameter.empty:
                                doc += f"`{param.annotation.__name__ if hasattr(param.annotation, '__name__') else str(param.annotation)}` "
                            if param.default != inspect.Parameter.empty:
                                doc += f"(default: `{param.default}`)"
                            doc += "\n"
                        doc += "\n"

                    # Document return type if available
                    if (
                        sig.return_annotation != inspect.Signature.empty
                        and sig.return_annotation != None
                    ):
                        doc += f"**Returns:** `{sig.return_annotation.__name__ if hasattr(sig.return_annotation, '__name__') else str(sig.return_annotation)}`\n\n"

    # Document functions
    if functions:
        doc += "## Functions\n\n"
        for name, func, func_module in sorted(functions):
            doc += f"### `{name}`\n\n"

            # Indicate if the function is imported
            if func_module != module.__name__:
                doc += f"*Imported from `{func_module}`*\n\n"

            if func.__doc__:
                clean_doc = inspect.cleandoc(func.__doc__)
                clean_doc = sanitize_docstring(clean_doc)
                doc += f"{clean_doc}\n\n"
            else:
                doc += f"No documentation available for function `{name}`.\n\n"

            # Document function signature
            try:
                sig = inspect.signature(func)
                doc += f"**Signature:** `{name}{sig}`\n\n"
            except (ValueError, TypeError):
                pass

            # Document parameters
            if sig.parameters:
                doc += "**Parameters:**\n\n"
                for param_name, param in sig.parameters.items():
                    doc += f"- `{param_name}`: "
                    if param.annotation != inspect.Parameter.empty:
                        doc += f"`{param.annotation.__name__ if hasattr(param.annotation, '__name__') else str(param.annotation)}` "
                    if param.default != inspect.Parameter.empty:
                        doc += f"(default: `{param.default}`)"
                    doc += "\n"
                doc += "\n"

            # Document return type if available
            if (
                sig.return_annotation != inspect.Signature.empty
                and sig.return_annotation != None
            ):
                doc += f"**Returns:** `{sig.return_annotation.__name__ if hasattr(sig.return_annotation, '__name__') else str(sig.return_annotation)}`\n\n"

    # If no public API was found, add a note
    if not public_api and not classes and not functions and not variables:
        doc += "This module does not contain any public classes, functions, or variables.\n"

    return doc


def generate_decorator_doc(name: str, decorator_class: Type[DecoratorBase]) -> str:
    """Generate documentation for a decorator using both class attributes and registry metadata.

    Args:
        name: The name of the decorator
        decorator_class: The decorator class

    Returns:
        Markdown documentation for the decorator
    """
    # Start with basic information from the class
    doc = f"# {name} Decorator\n\n"

    # Try to find registry metadata
    registry_file = find_decorator_registry_file(name)

    print(f"For decorator {name}, found registry file: {registry_file}")

    if registry_file and os.path.exists(registry_file):
        # Use registry metadata if available
        print(f"Using registry file for {name}: {registry_file}")
        with open(registry_file, "r") as f:
            try:
                registry_data = json.load(f)
                print(f"Successfully loaded registry data for {name}")
                return generate_doc_from_registry(registry_data, registry_file)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON in registry file for {name}: {str(e)}")

    # Fallback to basic documentation from the class
    if decorator_class.__doc__:
        clean_doc = inspect.cleandoc(decorator_class.__doc__)
        clean_doc = sanitize_docstring(clean_doc)
        doc += f"{clean_doc}\n\n"
    elif hasattr(decorator_class, "description"):
        doc += f"{decorator_class.description}\n\n"
    else:
        doc += f"Documentation for the {name} decorator.\n\n"

    category = getattr(decorator_class, "category", "Unknown")
    doc += f"**Category**: {category}\n\n"

    if hasattr(decorator_class, "parameters") and decorator_class.parameters:
        doc += "## Parameters\n\n"
        doc += "| Parameter | Type | Description | Default |\n"
        doc += "|-----------|------|-------------|--------|\n"

        for param in decorator_class.parameters:
            param_name = param.name
            param_type = param.type
            param_desc = param.description
            param_default = param.default

            doc += (
                f"| `{param_name}` | {param_type} | {param_desc} | {param_default} |\n"
            )

        doc += "\n"

    doc += "\nThis documentation is automatically generated from class attributes. For more detailed information, please refer to the registry definition.\n"

    return doc


def find_decorator_registry_file(decorator_name: str) -> Optional[str]:
    """Find the registry file for a decorator.

    Args:
        decorator_name: The name of the decorator

    Returns:
        The path to the registry file, or None if not found
    """
    print(f"Finding registry file for: {decorator_name}")

    # Helper to convert CamelCase to kebab-case
    def camel_to_kebab(s):
        # Add hyphen before uppercase letters and convert to lowercase
        return "".join(
            ["-" + c.lower() if c.isupper() else c.lower() for c in s]
        ).lstrip("-")

    # Search patterns to try
    pattern_variants = [
        f"{decorator_name.lower()}.json",  # all lowercase
        f"{decorator_name.lower().replace('_', '-')}.json",  # snake to kebab
        f"{camel_to_kebab(decorator_name)}.json",  # CamelCase to kebab-case
    ]

    # Search through all registry folders
    for root, _, files in os.walk(REGISTRY_DIR):
        for file in files:
            if file.lower() in pattern_variants:
                return os.path.join(root, file)

            # Check if it's a JSON file with the decorator name in it
            if file.endswith(".json"):
                try:
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as f:
                        data = json.load(f)
                        if (
                            "decoratorName" in data
                            and data["decoratorName"] == decorator_name
                        ):
                            print(f"Found by decoratorName: {file_path}")
                            return file_path
                except (
                    json.JSONDecodeError,
                    UnicodeDecodeError,
                    FileNotFoundError,
                ) as e:
                    print(f"Error reading file {file}: {str(e)}")

    print(f"No registry file found for: {decorator_name}")
    return None


def generate_doc_from_registry(
    registry_data: Dict[str, Any], registry_file: Optional[str] = None
) -> str:
    """Generate comprehensive documentation from registry metadata.

    Args:
        registry_data: The registry data for the decorator
        registry_file: The path to the registry file (optional)

    Returns:
        Markdown documentation for the decorator
    """
    name = registry_data.get("decoratorName", "Unknown")
    description = registry_data.get("description", "No description available.")
    # Sanitize description to remove problematic references
    description = sanitize_docstring(description)

    category = "Unknown"  # Default category
    parameters = registry_data.get("parameters", [])

    # Try to determine category from file path if available
    if registry_file:
        # Extract category from path, e.g., /registry/core/tone/audience.json -> "Tone"
        # or /registry/extensions/developer_education/learningpath.json -> "Developer Education"
        path_parts = registry_file.split(os.sep)
        if "core" in path_parts and len(path_parts) > path_parts.index("core") + 1:
            core_index = path_parts.index("core")
            category = path_parts[core_index + 1].replace("_", " ").title()
        elif (
            "extensions" in path_parts
            and len(path_parts) > path_parts.index("extensions") + 1
        ):
            extensions_index = path_parts.index("extensions")
            category = path_parts[extensions_index + 1].replace("_", " ").title()
        elif "simplified_decorators" in path_parts:
            category = "Simplified"

    # Try to determine category from parameters as a fallback
    if category == "Unknown":
        for param in parameters:
            if param.get("name") == "category":
                category = param.get("default", "Unknown")

    # Start with basic information
    doc = f"# {name} Decorator\n\n"
    doc += f"{description}\n\n"
    doc += f"**Category**: {category}\n\n"

    # Add parameters section if parameters exist
    if parameters:
        doc += "## Parameters\n\n"
        doc += "| Parameter | Type | Description | Default |\n"
        doc += "|-----------|------|-------------|--------|\n"

        for param in parameters:
            param_name = param.get("name", "")
            param_type = param.get("type", "")
            param_desc = param.get("description", "")
            # Sanitize parameter descriptions
            param_desc = sanitize_docstring(param_desc)
            param_default = param.get("default", "")
            required = param.get("required", False)

            if required and param_default == "":
                param_default = "Required"

            doc += f"| `{param_name}` | `{param_type}` | {param_desc} | `{param_default}` |\n"

        doc += "\n"

    # Add enum values for enum parameters
    for param in parameters:
        if param.get("type") == "enum" and "enum" in param:
            enum_values = param.get("enum", [])
            if enum_values:
                param_name = param.get("name", "")
                doc += f"## {param_name.title()} Options\n\n"

                # Check if we have detailed descriptions in transformationTemplate
                value_descriptions = {}
                transform_template = registry_data.get("transformationTemplate", {})
                param_mapping = transform_template.get("parameterMapping", {}).get(
                    param_name, {}
                )
                value_map = param_mapping.get("valueMap", {})

                for value in enum_values:
                    description = value_map.get(value, f"Option: {value}")
                    # Sanitize enum value descriptions
                    description = sanitize_docstring(description)
                    doc += f"- `{value}`: {description}\n"

                doc += "\n"

    # Add examples section if examples exist
    examples = registry_data.get("examples", [])
    if examples:
        doc += "## Examples\n\n"

        for i, example in enumerate(examples):
            title = example.get("description", f"Example {i+1}")
            usage = example.get("usage", "")
            result = example.get("result", "")
            # Sanitize example descriptions
            title = sanitize_docstring(title)
            result = sanitize_docstring(result)

            doc += f"### {title}\n\n"

            if usage:
                doc += "```\n" + usage + "\n```\n\n"

            if result:
                doc += f"{result}\n\n"

    # Add model-specific implementations if available
    impl_guidance = registry_data.get("implementationGuidance", {})
    model_specific = impl_guidance.get("modelSpecificImplementations", {})

    if model_specific:
        doc += "## Model-Specific Implementations\n\n"

        for model_name, implementation in model_specific.items():
            instruction = implementation.get("instruction", "")
            notes = implementation.get("notes", "")
            # Sanitize model-specific implementation fields
            instruction = sanitize_docstring(instruction)
            notes = sanitize_docstring(notes)

            doc += f"### {model_name}\n\n"
            if instruction:
                doc += f"**Instruction:** {instruction}\n\n"
            if notes:
                doc += f"**Notes:** {notes}\n\n"

        doc += "\n"

    # Add implementation guidance if available
    if impl_guidance:
        examples = impl_guidance.get("examples", [])
        if examples and not "modelSpecificImplementations" in doc:
            doc += "## Implementation Guidance\n\n"

            for i, example in enumerate(examples):
                context = example.get("context", f"Context {i+1}")
                original = example.get("originalPrompt", "")
                transformed = example.get("transformedPrompt", "")
                notes = example.get("notes", "")
                # Sanitize implementation guidance fields
                context = sanitize_docstring(context)
                notes = sanitize_docstring(notes)

                doc += f"### {context}\n\n"

                if original:
                    doc += "**Original Prompt:**\n```\n" + original + "\n```\n\n"

                if transformed:
                    doc += "**Transformed Prompt:**\n```\n" + transformed + "\n```\n\n"

                if notes:
                    doc += f"**Notes:** {notes}\n\n"

    # Add transformation template information
    transform_template = registry_data.get("transformationTemplate", {})
    if transform_template:
        doc += "## Transformation Details\n\n"

        instruction = transform_template.get("instruction", "")
        placement = transform_template.get("placement", "")
        composition = transform_template.get("compositionBehavior", "")
        # Sanitize transformation template fields
        instruction = sanitize_docstring(instruction)

        if instruction:
            doc += f"**Base Instruction:** {instruction}\n\n"

        if placement:
            doc += f"**Placement:** {placement}\n\n"

        if composition:
            doc += f"**Composition Behavior:** {composition}\n\n"

        param_mapping = transform_template.get("parameterMapping", {})
        if param_mapping:
            doc += "**Parameter Effects:**\n\n"

            for param_name, mapping in param_mapping.items():
                doc += f"- `{param_name}`:\n"

                value_map = mapping.get("valueMap", {})
                if value_map:
                    for value, effect in value_map.items():
                        # Sanitize parameter effect descriptions
                        effect = sanitize_docstring(effect)
                        doc += f"  - When set to `{value}`: {effect}\n"

                format_str = mapping.get("format", "")
                if format_str:
                    doc += f"  - Format: {format_str}\n"

                doc += "\n"

    # Add compatibility section
    compatibility = registry_data.get("compatibility", {})
    if compatibility:
        doc += "## Compatibility\n\n"

        requires = compatibility.get("requires", [])
        conflicts = compatibility.get("conflicts", [])
        models = compatibility.get("models", [])
        min_version = compatibility.get("minStandardVersion", "")
        max_version = compatibility.get("maxStandardVersion", "")

        if requires:
            doc += f"- **Requires**: {', '.join(requires)}\n"
        else:
            doc += "- **Requires**: None\n"

        if conflicts:
            doc += f"- **Conflicts**: {', '.join(conflicts)}\n"
        else:
            doc += "- **Conflicts**: None\n"

        if models:
            doc += f"- **Compatible Models**: {', '.join(models)}\n"

        if min_version and max_version:
            doc += f"- **Standard Version**: {min_version} - {max_version}\n"
        elif min_version:
            doc += f"- **Minimum Standard Version**: {min_version}\n"

        doc += "\n"

    # Add related decorators section from implementation guidance
    compat_notes = impl_guidance.get("compatibilityNotes", [])

    if compat_notes:
        doc += "## Related Decorators\n\n"

        for note in compat_notes:
            decorator = note.get("decorator", "")
            relationship = note.get("relationship", "")
            notes = note.get("notes", "")
            # Sanitize compatibility notes
            notes = sanitize_docstring(notes)

            if decorator and notes:
                relation_text = ""
                if relationship == "enhances":
                    relation_text = "Enhances"
                elif relationship == "conflicts":
                    relation_text = "Conflicts with"
                elif relationship == "requires":
                    relation_text = "Requires"
                else:
                    relation_text = "Related to"

                doc += f"- **{decorator}**: {relation_text} {name} {notes}\n"

        doc += "\n"

    return doc


def find_registry_files() -> List[Path]:
    """Find all registry files in the registry directory.

    Returns:
        List of paths to registry files
    """
    print(f"Searching for all registry files in {REGISTRY_DIR}")
    registry_files = list(Path(REGISTRY_DIR).glob("**/*.json"))

    # Filter out any non-registry files (like schema.json)
    filtered_files = []
    for file in registry_files:
        file_name = file.name.lower()
        if "schema" in file_name or "template" in file_name or "readme" in file_name:
            continue
        filtered_files.append(file)

    print(f"Found {len(filtered_files)} registry files")
    return filtered_files


def generate_api_docs() -> None:
    """Generate API documentation for all modules in the prompt_decorators package."""
    print("Generating API documentation...")
    ensure_directory(API_DOCS_DIR)
    ensure_directory(API_MODULES_DIR)

    # Dictionary to organize modules by category
    modules_by_category = {
        "Core Modules": [],
        "Schema Modules": [],
        "Utility Modules": [],
        "Integration Modules": [],
        "Other Modules": [],
    }

    # Helper function to recursively discover modules
    def discover_modules(package_name, package_path):
        discovered = []
        for _, name, is_pkg in pkgutil.iter_modules([package_path], package_name + "."):
            if name.endswith("__pycache__"):
                continue

            discovered.append(name)

            # If this is a package, recurse into it
            if is_pkg:
                pkg_path = os.path.join(package_path, name.split(".")[-1])
                discovered.extend(discover_modules(name, pkg_path))

        return discovered

    # Get all modules in the prompt_decorators package recursively
    modules = discover_modules(
        prompt_decorators.__name__, os.path.dirname(prompt_decorators.__file__)
    )

    # Categorize modules
    for name in modules:
        if ".core." in name or name.endswith(".core"):
            modules_by_category["Core Modules"].append(name)
        elif ".schemas." in name or name.endswith(".schemas"):
            modules_by_category["Schema Modules"].append(name)
        elif ".utils." in name or name.endswith(".utils"):
            modules_by_category["Utility Modules"].append(name)
        elif ".integrations." in name or name.endswith(".integrations"):
            modules_by_category["Integration Modules"].append(name)
        else:
            modules_by_category["Other Modules"].append(name)

    # Generate index file with improved formatting and module descriptions
    index_content = """# API Reference

This section contains the API reference for the Prompt Decorators package. It provides detailed documentation for all modules, classes, functions, and properties in the package.

"""

    # Get module descriptions to enrich the index
    module_descriptions = {}
    for module_name in modules:
        try:
            module = importlib.import_module(module_name)
            if module.__doc__:
                first_line = sanitize_docstring(
                    module.__doc__.strip().split("\n")[0].strip()
                )
                module_descriptions[module_name] = first_line
        except ImportError as e:
            print(f"  Warning: Could not import {module_name} for description: {e}")
            module_descriptions[module_name] = "Module documentation"

    # Add modules organized by category
    for category, category_modules in modules_by_category.items():
        if not category_modules:
            continue  # Skip empty categories

        # Add heading with ID attribute for the category (kebab case for the ID)
        anchor_id = category.lower().replace(" ", "-")
        index_content += f"## {category} {{#{anchor_id}}}\n\n"

        for module_name in sorted(category_modules):
            # Use the full module name as the path for the link
            doc_path = f"{module_name}.md"

            # Add module description if available
            description = module_descriptions.get(module_name, "")
            if description:
                index_content += f"- [{module_name}]({doc_path}): {description}\n"
            else:
                index_content += f"- [{module_name}]({doc_path})\n"

        index_content += "\n"

    # Write index file
    with open(API_MODULES_DIR / "index.md", "w") as f:
        f.write(index_content)

    # Generate documentation for each module
    for module_name in modules:
        try:
            print(f"Generating documentation for {module_name}...")
            # Create module object
            try:
                module = importlib.import_module(module_name)

                # Generate and write module documentation
                doc_content = generate_module_doc(module_name, module)
                module_filename = f"{module_name}.md"
                with open(API_MODULES_DIR / module_filename, "w") as f:
                    f.write(doc_content)
                print(f"  Documentation for {module_name} generated successfully")
            except ImportError as e:
                print(f"  Error importing {module_name}: {e}")
                # Create a minimal placeholder documentation
                short_name = module_name.split(".")[-1]
                doc_content = f"# {short_name}\n\n"
                doc_content += f"Module documentation for {module_name}.\n\n"
                doc_content += "This module could not be imported for documentation generation. Please check for any import errors.\n"
                module_filename = f"{module_name}.md"
                with open(API_MODULES_DIR / module_filename, "w") as f:
                    f.write(doc_content)
        except Exception as e:
            print(f"  Error generating documentation for {module_name}: {e}")
            # Create an error documentation
            short_name = module_name.split(".")[-1]
            doc_content = f"# {short_name}\n\n"
            doc_content += f"Module documentation for {module_name}.\n\n"
            doc_content += (
                f"An error occurred while generating documentation: {str(e)}\n"
            )
            module_filename = f"{module_name}.md"
            with open(API_MODULES_DIR / module_filename, "w") as f:
                f.write(doc_content)

    print(f"API documentation generated for {len(modules)} modules")


def generate_decorator_docs() -> None:
    """Generate documentation for all decorators."""
    print("Generating decorator documentation...")
    ensure_directory(API_DECORATORS_DIR)

    registry = get_registry()
    dynamic_registry = DynamicDecorator._registry

    # Use dynamic registry if standard registry is empty
    if not registry and dynamic_registry:
        print("Using dynamic registry instead of standard registry")
        registry = dynamic_registry

    decorators = list(registry.keys())

    # Dictionary to organize decorators by category
    decorators_by_category = {}

    # Generate documentation for each decorator
    for name in registry:
        try:
            decorator_class = registry[name]

            # Generate documentation
            doc_content = generate_decorator_doc(name, decorator_class)

            # Extract category from the doc_content
            category_match = re.search(r"\*\*Category\*\*: (.+?)\n", doc_content)
            category = category_match.group(1) if category_match else "Uncategorized"

            # Add to the category dictionary
            if category not in decorators_by_category:
                decorators_by_category[category] = []
            decorators_by_category[category].append(name)

            # Write documentation to file
            output_file = API_DECORATORS_DIR / f"{name}.md"
            with open(output_file, "w") as f:
                f.write(doc_content)
        except Exception as e:
            print(f"Error generating documentation for {name}: {e}")
            # Create a placeholder documentation
            output_file = API_DECORATORS_DIR / f"{name}.md"
            with open(output_file, "w") as f:
                f.write(f"# {name} Decorator\n\n")
                f.write(f"Documentation for the {name} decorator.\n\n")
                f.write(
                    f"This documentation is a placeholder and will be updated in the future.\n"
                )

    # Search for additional decorators in registry files
    try:
        registry_files = find_registry_files()
        existing_decorators = {name.lower() for name in registry.keys()}

        for file_path in registry_files:
            try:
                with open(file_path, "r") as f:
                    content = json.load(f)
                    if "decoratorName" in content:
                        decorator_name = content["decoratorName"]

                        # Skip if we already have this decorator
                        if decorator_name.lower() in existing_decorators:
                            continue

                        # Generate documentation from registry data
                        doc_content = generate_doc_from_registry(
                            content, str(file_path)
                        )

                        # Extract category
                        category_match = re.search(
                            r"\*\*Category\*\*: (.+?)\n", doc_content
                        )
                        category = (
                            category_match.group(1)
                            if category_match
                            else "Uncategorized"
                        )

                        # Add to the category dictionary
                        if category not in decorators_by_category:
                            decorators_by_category[category] = []
                        decorators_by_category[category].append(decorator_name)

                        # Write to file
                        output_file = API_DECORATORS_DIR / f"{decorator_name}.md"
                        with open(output_file, "w") as doc_file:
                            doc_file.write(doc_content)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

        # Generate index file with links to all decorators, organized by category
        index_content = """# Decorator API Reference

This section provides API reference for all available decorators in the Prompt Decorators package.

## Decorators by Category

"""
        # Get the core categories we want to highlight at the top
        core_categories = ["Core", "Minimal", "Reasoning", "Structure"]
        special_categories = {
            "Core": "Core Decorators",
            "Reasoning": "Reasoning Process Decorators",
            "Structure": "Output Structure Decorators",
        }

        # Add descriptions for special categories
        category_descriptions = {
            "Core Decorators": "The essential decorators that form the foundation of the prompt decorators system.",
            "Reasoning Process Decorators": "Decorators that control or influence the reasoning process used in prompt responses.",
            "Output Structure Decorators": "Decorators that control the structure of the output generated from prompts.",
        }

        # First add the special categories
        for base_category in core_categories:
            if base_category in decorators_by_category:
                display_category = special_categories.get(base_category, base_category)
                # Add heading with ID for special categories
                kebab_id = display_category.lower().replace(" ", "-")
                index_content += f"### {display_category} {{#{kebab_id}}}\n\n"

                # Add description if available
                if display_category in category_descriptions:
                    index_content += f"{category_descriptions[display_category]}\n\n"

                # Sort decorators within category
                sorted_decorators = sorted(decorators_by_category[base_category])

                # Add links to each decorator
                for decorator in sorted_decorators:
                    index_content += f"- [{decorator}]({decorator}.md)\n"

                index_content += "\n"

        # Sort remaining categories
        sorted_categories = [
            cat
            for cat in sorted(decorators_by_category.keys())
            if cat not in core_categories
        ]

        for category in sorted_categories:
            # Add category heading
            index_content += f"### {category}\n\n"

            # Sort decorators within category
            sorted_decorators = sorted(decorators_by_category[category])

            # Add links to each decorator
            for decorator in sorted_decorators:
                index_content += f"- [{decorator}]({decorator}.md)\n"

            index_content += "\n"

        # Write index file
        with open(API_DECORATORS_DIR / "index.md", "w") as f:
            f.write(index_content)

        print("Generated decorator index file")

    except Exception as e:
        print(f"Error searching for additional decorators: {e}")
        # Create a basic index file as fallback
        index_content = """# Decorator API Reference

This section provides API reference for all available decorators in the Prompt Decorators package.

## Decorators

"""
        # Just list all decorators alphabetically
        for name in sorted(registry.keys()):
            index_content += f"- [{name}]({name}.md)\n"

        # Write basic index file
        with open(API_DECORATORS_DIR / "index.md", "w") as f:
            f.write(index_content)

    print("Decorator documentation generation complete")


def generate_api_index() -> None:
    """Generate the main API index file that links to module and decorator documentation."""
    print("Generating API index file...")

    # Create content for the API index
    api_index_content = """# API Reference

## Overview

This section contains the API reference for the Prompt Decorators package. It provides detailed documentation for all modules, classes, functions, and properties in the package.

The API is organized into the following sections:

- **[Modules](modules/index.md)**: Documentation for all Python modules in the package
  - [Core Modules](modules/index.md#core-modules): Core functionality of prompt decorators
  - [Schema Modules](modules/index.md#schema-modules): Data models and schemas
  - [Utility Modules](modules/index.md#utility-modules): Helper functions and utilities
  - [Integration Modules](modules/index.md#integration-modules): Integrations with other systems

- **[Decorators](decorators/index.md)**: Documentation for all available prompt decorators
  - [Minimal Decorators](decorators/index.md#minimal): Essential decorators for basic functionality
  - [Reasoning Process Decorators](decorators/index.md#reasoning-process-decorators): Decorators for controlling reasoning processes
  - [Output Structure Decorators](decorators/index.md#output-structure-decorators): Decorators for controlling output structure
  - [And more...](decorators/index.md)

## Usage Example

```python
from prompt_decorators import transform_prompt

# Transform a prompt using decorators
transformed_prompt = transform_prompt(
    "What are the environmental impacts of electric vehicles?",
    ["+++StepByStep(numbered=true)", "+++Reasoning(depth=comprehensive)"]
)
```

For more examples, see the [Quick Start](../quickstart.md) guide.
"""

    # Write the index file
    with open(API_DOCS_DIR / "index.md", "w") as f:
        f.write(api_index_content)

    print("API index file generated successfully")


def main() -> None:
    """Main function to generate documentation.

    This function coordinates the generation of API documentation and decorator documentation.
    It loads the decorator registry and then calls the appropriate functions to generate
    documentation for all modules and decorators.
    """
    parser = argparse.ArgumentParser(
        description="Generate documentation for prompt-decorators"
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    if args.debug:
        print("Debug mode enabled")

    # Import and load dynamic decorators
    from prompt_decorators.core.dynamic_decorator import DynamicDecorator

    DynamicDecorator.load_registry()

    # Generate API documentation
    print("Generating API documentation...")
    generate_api_docs()

    # Generate main API index
    generate_api_index()

    # Generate decorator documentation
    generate_decorator_docs()

    print("Documentation generation complete!")


if __name__ == "__main__":
    main()
