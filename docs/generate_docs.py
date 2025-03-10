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


def generate_module_doc(module_name: str, module: Any) -> str:
    """Generate documentation for a module."""
    doc = f"# {module_name}\n\n"

    if module.__doc__:
        doc += f"{module.__doc__.strip()}\n\n"
    else:
        doc += f"Module documentation for {module_name}.\n\n"

    # Get all classes and functions in the module
    classes = []
    functions = []

    for name, obj in inspect.getmembers(module):
        if name.startswith("_"):
            continue

        if inspect.isclass(obj) and obj.__module__ == module.__name__:
            classes.append((name, obj))
        elif inspect.isfunction(obj) and obj.__module__ == module.__name__:
            functions.append((name, obj))

    # Document classes
    if classes:
        doc += "## Classes\n\n"
        for name, cls in classes:
            doc += f"### {name}\n\n"
            if cls.__doc__:
                doc += f"{cls.__doc__.strip()}\n\n"
            else:
                doc += f"Class documentation for {name}.\n\n"

            # Document methods
            methods = []
            for method_name, method in inspect.getmembers(cls, inspect.isfunction):
                if not method_name.startswith("_") or method_name == "__init__":
                    methods.append((method_name, method))

            if methods:
                doc += "#### Methods\n\n"
                for method_name, method in methods:
                    doc += f"##### `{method_name}`\n\n"
                    if method.__doc__:
                        doc += f"{method.__doc__.strip()}\n\n"
                    else:
                        doc += f"Method documentation for {method_name}.\n\n"

    # Document functions
    if functions:
        doc += "## Functions\n\n"
        for name, func in functions:
            doc += f"### {name}\n\n"
            if func.__doc__:
                doc += f"{func.__doc__.strip()}\n\n"
            else:
                doc += f"Function documentation for {name}.\n\n"

            # Document parameters
            sig = inspect.signature(func)
            if sig.parameters:
                doc += "#### Parameters\n\n"
                for param_name, param in sig.parameters.items():
                    if param_name == "self":
                        continue
                    doc += f"- `{param_name}`: "
                    if param.annotation != inspect.Parameter.empty:
                        doc += f"{param.annotation.__name__ if hasattr(param.annotation, '__name__') else str(param.annotation)} "
                    if param.default != inspect.Parameter.empty:
                        doc += f"(default: {param.default})"
                    doc += "\n"
                doc += "\n"

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
        doc += f"{decorator_class.__doc__.strip()}\n\n"
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

    # Special case for TechDebtControl
    if decorator_name == "TechDebtControl":
        tech_debt_path = os.path.join(
            REGISTRY_DIR, "extensions", "implementation-focused", "techdebtcontrol.json"
        )
        print(f"Checking special case path: {tech_debt_path}")
        print(f"Path exists: {os.path.exists(tech_debt_path)}")
        if os.path.exists(tech_debt_path):
            print(f"Found exact match for TechDebtControl: {tech_debt_path}")
            return tech_debt_path

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

    print(f"Looking for patterns: {pattern_variants}")

    # Search through all registry folders
    for root, _, files in os.walk(REGISTRY_DIR):
        for file in files:
            print(f"Checking file: {file}")
            if file.lower() in pattern_variants:
                print(f"Found exact match: {os.path.join(root, file)}")
                return os.path.join(root, file)

            # Check if it's a JSON file with the decorator name in it
            if file.endswith(".json"):
                try:
                    file_path = os.path.join(root, file)
                    print(f"Checking content of: {file_path}")
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
    print(f"Generating doc from registry for: {name}")
    description = registry_data.get("description", "No description available.")
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
        print(f"Found {len(parameters)} parameters for {name}")
        doc += "## Parameters\n\n"
        doc += "| Parameter | Type | Description | Default |\n"
        doc += "|-----------|------|-------------|--------|\n"

        for param in parameters:
            param_name = param.get("name", "")
            param_type = param.get("type", "")
            param_desc = param.get("description", "")
            param_default = param.get("default", "")
            required = param.get("required", False)

            if required and param_default == "":
                param_default = "Required"

            doc += (
                f"| `{param_name}` | {param_type} | {param_desc} | {param_default} |\n"
            )

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

            doc += f"### {model_name}\n\n"
            if instruction:
                doc += f"**Instruction:** {instruction}\n\n"
            if notes:
                doc += f"**Notes:** {notes}\n\n"

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

    # Add transformation template information if requested by users
    transform_template = registry_data.get("transformationTemplate", {})
    if transform_template and "advanced" in registry_data.get(
        "documentation_options", []
    ):
        doc += "## Implementation Details\n\n"

        instruction = transform_template.get("instruction", "")
        placement = transform_template.get("placement", "")
        composition = transform_template.get("compositionBehavior", "")

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
                        doc += f"  - When set to `{value}`: {effect}\n"

                format_str = mapping.get("format", "")
                if format_str:
                    doc += f"  - Format: {format_str}\n"

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
    ensure_directory(API_DOCS_DIR)
    ensure_directory(API_MODULES_DIR)

    # Generate index file
    index_content = """# API Reference

This section contains the API reference for the Prompt Decorators package.

## Modules

"""

    # Get all modules in the prompt_decorators package
    modules = []
    for _, name, is_pkg in pkgutil.iter_modules(
        prompt_decorators.__path__, prompt_decorators.__name__ + "."
    ):
        if not name.endswith("__pycache__"):
            modules.append(name)

    # Add core modules to index
    for module_name in sorted(modules):
        rel_name = module_name.replace("prompt_decorators.", "")
        index_content += f"- [{rel_name}](modules/{module_name}.md)\n"

    # Write index file
    with open(API_DOCS_DIR / "index.md", "w") as f:
        f.write(index_content)

    # Generate documentation for each module
    for module_name in modules:
        try:
            module = importlib.import_module(module_name)

            # Generate and write module documentation
            doc_content = generate_module_doc(module_name, module)
            with open(API_MODULES_DIR / f"{module_name}.md", "w") as f:
                f.write(doc_content)

        except ImportError as e:
            print(f"Error importing {module_name}: {e}")


def generate_decorator_docs() -> None:
    """Generate documentation for all decorators."""
    print("Generating decorator documentation...")
    ensure_directory(API_DECORATORS_DIR)

    registry = get_registry()
    dynamic_registry = DynamicDecorator._registry

    print(f"Registry from get_registry() has {len(registry)} decorators")
    print(f"Dynamic registry has {len(dynamic_registry)} decorators")

    # Check specifically for TechDebtControl
    print(f"TechDebtControl in registry: {'TechDebtControl' in registry}")
    print(
        f"TechDebtControl in dynamic registry: {'TechDebtControl' in dynamic_registry}"
    )

    # Use dynamic registry if standard registry is empty
    if not registry and dynamic_registry:
        print("Using dynamic registry instead")
        registry = dynamic_registry

    print(f"Found {len(registry)} decorators in registry")
    decorators = list(registry.keys())

    # Debug: Print first 5 decorators
    print(
        f"First 5 decorators: {decorators[:5] if len(decorators) >= 5 else decorators}"
    )

    # Dictionary to organize decorators by category
    decorators_by_category = {}

    # Generate documentation for each decorator
    for name in registry:
        try:
            decorator_class = registry[name]

            # Debug: Print info for TechDebtControl
            if name == "TechDebtControl":
                print(
                    f"Generating documentation for TechDebtControl: {decorator_class}"
                )
                print(f"Type: {type(decorator_class)}")

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

            print(f"Generated documentation for {name}")
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

                        print(
                            f"Found additional decorator in registry file: {decorator_name}"
                        )

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
                        print(
                            f"Generated documentation for {decorator_name} from registry file"
                        )
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

        # Generate index file with links to all decorators, organized by category
        index_content = """# Decorator API Reference

This section provides API reference for all available decorators in the Prompt Decorators package.

## Decorators by Category

"""
        # Sort categories
        sorted_categories = sorted(decorators_by_category.keys())

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


def main() -> None:
    """Main function to generate documentation."""
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

    # Generate decorator documentation
    generate_decorator_docs()

    # Directly generate documentation for TechDebtControl
    print("Directly generating documentation for TechDebtControl...")
    tech_debt_path = os.path.join(
        REGISTRY_DIR, "extensions", "implementation-focused", "techdebtcontrol.json"
    )
    if os.path.exists(tech_debt_path):
        print(f"Found TechDebtControl registry file: {tech_debt_path}")
        with open(tech_debt_path, "r") as f:
            try:
                registry_data = json.load(f)
                print(f"Successfully loaded TechDebtControl registry data")
                doc_content = generate_doc_from_registry(registry_data, tech_debt_path)
                # Define the output directory for API decorators
                api_decorators_dir = os.path.join("api", "decorators")
                output_file = os.path.join(api_decorators_dir, "TechDebtControl.md")
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                with open(output_file, "w") as doc_file:
                    doc_file.write(doc_content)
                print(
                    f"Generated documentation for TechDebtControl directly from registry file"
                )
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON in TechDebtControl registry file: {str(e)}")
    else:
        print(f"TechDebtControl registry file not found at {tech_debt_path}")

    print("Documentation generation complete!")


if __name__ == "__main__":
    main()
