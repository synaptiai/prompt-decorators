#!/usr/bin/env python3
"""
Documentation Generator for Prompt Decorators

This script generates API documentation for the Prompt Decorators package.
It creates Markdown files for each module, class, and function in the package.
"""

import importlib
import inspect
import os
import pkgutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Type

# Add the parent directory to the path so we can import prompt_decorators
sys.path.insert(0, str(Path(__file__).parent.parent))

import prompt_decorators
from prompt_decorators.core.base import DecoratorBase
from prompt_decorators.core.registry import get_categories, get_decorator, get_registry

# Directory where API documentation will be generated
API_DOCS_DIR = Path(__file__).parent / "api"
API_MODULES_DIR = API_DOCS_DIR / "modules"
API_DECORATORS_DIR = API_DOCS_DIR / "decorators"
DECORATOR_DOCS_DIR = Path(__file__).parent / "decorators"


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
    """Generate documentation for a decorator."""
    doc = f"# {name} Decorator\n\n"

    if decorator_class.__doc__:
        doc += f"{decorator_class.__doc__.strip()}\n\n"
    else:
        doc += f"Documentation for the {name} decorator.\n\n"

    doc += f"**Category**: {decorator_class.category}\n\n"

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

    # Examples would need to be added manually or extracted from docstrings

    return doc


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
    """Generate documentation for all decorators in the registry."""
    ensure_directory(DECORATOR_DOCS_DIR)
    ensure_directory(API_DECORATORS_DIR)

    # Get all decorators
    registry = get_registry()
    decorators = list(registry.keys())

    # Group decorators by category
    categories_dict = get_categories()
    categories: Dict[str, List[str]] = {}

    for category, decorator_set in categories_dict.items():
        categories[category] = list(decorator_set)

    # Generate index file for decorators directory
    index_content = """# Decorator Reference

This section provides a reference for all available decorators in the Prompt Decorators package.

## Categories

"""

    for category, decorators_list in sorted(categories.items()):
        index_content += f"### {category}\n\n"
        for decorator in sorted(decorators_list):
            index_content += (
                f"- [{decorator}]({category.lower()}/{decorator.lower()}.md)\n"
            )
        index_content += "\n"

    # Write index file for decorators directory
    with open(DECORATOR_DOCS_DIR / "index.md", "w") as f:
        f.write(index_content)

    # Generate index file for API decorators directory
    api_index_content = """# Decorator API Reference

This section provides API reference for all available decorators in the Prompt Decorators package.

## Decorators

"""

    for decorator in sorted(decorators):
        api_index_content += f"- [{decorator}]({decorator}.md)\n"

    # Write index file for API decorators directory
    with open(API_DECORATORS_DIR / "index.md", "w") as f:
        f.write(api_index_content)

    # Generate documentation for each decorator in the category structure
    for category, decorators_list in categories.items():
        # Create category directory
        category_dir = DECORATOR_DOCS_DIR / category.lower()
        ensure_directory(category_dir)

        # Generate category index
        category_index = f"# {category} Decorators\n\nThis section documents decorators in the {category} category.\n\n"

        for decorator in sorted(decorators_list):
            category_index += f"- [{decorator}]({decorator.lower()}.md)\n"

        # Write category index
        with open(category_dir / "index.md", "w") as f:
            f.write(category_index)

        # Generate documentation for each decorator in the category
        for decorator in decorators_list:
            decorator_class = get_decorator(decorator)
            if decorator_class:
                # Generate documentation for the decorator category structure
                doc_content = generate_decorator_doc(decorator, decorator_class)
                with open(category_dir / f"{decorator.lower()}.md", "w") as f:
                    f.write(doc_content)

                # Generate documentation for the API decorators structure
                with open(API_DECORATORS_DIR / f"{decorator}.md", "w") as f:
                    f.write(doc_content)


def main() -> None:
    """Main function to generate all documentation."""
    print("Generating API documentation...")
    generate_api_docs()

    print("Generating decorator documentation...")
    generate_decorator_docs()

    print("Documentation generation complete!")


if __name__ == "__main__":
    main()
