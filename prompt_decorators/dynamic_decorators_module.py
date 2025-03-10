"""Dynamic Prompt Decorators Module.

This module provides a unified interface for working with prompt decorators
without the need for code generation. It dynamically loads decorator definitions
from the registry at runtime, removing the need to generate Python classes for
each decorator.

Features:
- Dynamic loading of decorators from registry
- Prompt transformation with any decorator
- Parameter validation against schema
- Support for decorator composition
"""

from typing import Any, Callable, Dict, List, Optional, Union

from prompt_decorators.core.base import DecoratorBase, DecoratorParameter
from prompt_decorators.core.dynamic_decorator import (
    DynamicDecorator,
    extract_decorators,
    parse_decorator,
)

__all__ = [
    "DynamicDecorator",
    "DecoratorDefinition",
    "load_decorator_definitions",
    "get_available_decorators",
    "create_decorator_instance",
    "create_decorator_class",
    "apply_dynamic_decorators",
    "apply_decorator",
    "register_decorator",
    "extract_decorator_name",
    "parse_decorator_text",
    "create_decorator",
    "list_available_decorators",
    "transform_prompt",
]


class DecoratorDefinition:
    """Class representing a decorator definition."""

    def __init__(
        self,
        name: str,
        description: str,
        category: str,
        parameters: List[Dict[str, Any]],
        transform_function: str,
        version: str = "1.0.0",
    ):
        """Initialize a decorator definition.

        Args:
            name: Name of the decorator
            description: Description of the decorator
            category: Category of the decorator
            parameters: List of parameter definitions
            transform_function: JavaScript function for transforming prompts
            version: Version of the decorator
        """
        self.name = name
        self.description = description
        self.category = category
        self.parameters = parameters
        self.transform_function = transform_function
        self.version = version

    def to_dict(self) -> Dict[str, Any]:
        """Convert the definition to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "parameters": self.parameters,
            "transform_function": self.transform_function,
            "version": self.version,
        }


def load_decorator_definitions() -> None:
    """Load decorator definitions from the registry."""
    DynamicDecorator.load_registry()


def get_available_decorators() -> List[DecoratorDefinition]:
    """Get a list of all available decorators.

    Returns:
        List of decorator definitions
    """
    return DynamicDecorator.get_available_decorators()


def create_decorator_instance(name: str, **kwargs: Any) -> DynamicDecorator:
    """Create a decorator instance by name.

    Args:
        name: Name of the decorator
        **kwargs: Parameters for the decorator

    Returns:
        A decorator instance

    Raises:
        ValueError: If the decorator is not found
    """
    return DynamicDecorator(name, **kwargs)


def create_decorator_class(definition: DecoratorDefinition) -> type:
    """Create a decorator class from a definition.

    Args:
        definition: Decorator definition

    Returns:
        A decorator class
    """
    return DynamicDecorator.from_definition(definition)


def apply_dynamic_decorators(prompt: str) -> str:
    """Apply decorators to a prompt using the +++ syntax.

    Args:
        prompt: The prompt text with decorator syntax

    Returns:
        The transformed prompt
    """
    decorators, clean_prompt = extract_decorators(prompt)
    result = clean_prompt
    for decorator in decorators:
        transformed = decorator(result)
        if isinstance(transformed, str):
            result = transformed
        else:
            # This should not happen in normal usage, but handle it just in case
            result = str(transformed)
    return result


def apply_decorator(decorator_name: str, prompt: str, **kwargs: Any) -> str:
    """Apply a decorator to a prompt.

    Args:
        decorator_name: Name of the decorator
        prompt: The prompt text
        **kwargs: Parameters for the decorator

    Returns:
        The transformed prompt
    """
    decorator = create_decorator_instance(decorator_name, **kwargs)
    transformed = decorator(prompt)
    if isinstance(transformed, str):
        return transformed
    else:
        # This should not happen in normal usage, but handle it just in case
        return str(transformed)


def register_decorator(definition: DecoratorDefinition) -> None:
    """Register a decorator definition.

    Args:
        definition: Decorator definition

    Returns:
        None
    """
    # Convert DecoratorDefinition to a dictionary with the expected format
    decorator_dict = {
        "decoratorName": definition.name,
        "description": definition.description,
        "category": definition.category,
        "parameters": definition.parameters,
        "transform_function": definition.transform_function,
        "version": definition.version,
    }
    DynamicDecorator.register_decorator(decorator_dict)


def extract_decorator_name(decorator_text: str) -> str:
    """Extract the decorator name from decorator text.

    Args:
        decorator_text: Text containing a decorator definition

    Returns:
        The decorator name
    """
    return parse_decorator(decorator_text)[0]


def parse_decorator_text(decorator_text: str) -> tuple:
    """Parse decorator text into name and parameters.

    Args:
        decorator_text: Text containing a decorator definition

    Returns:
        Tuple of (name, parameters)
    """
    return parse_decorator(decorator_text)


# Functions added for backward compatibility with the demo


def create_decorator(name: str, **kwargs: Any) -> DynamicDecorator:
    """Create a decorator instance by name (alias for create_decorator_instance).

    This function is maintained for backward compatibility with demo code.

    Args:
        name: Name of the decorator
        **kwargs: Parameters for the decorator

    Returns:
        A decorator instance

    Raises:
        ValueError: If the decorator is not found
    """
    return create_decorator_instance(name, **kwargs)


def list_available_decorators() -> List[str]:
    """List all available decorator names.

    This function is maintained for backward compatibility with demo code.

    Returns:
        A list of decorator names
    """
    # Make sure decorators are loaded
    load_decorator_definitions()

    # Get all available decorators
    decorators = get_available_decorators()

    # Return just the names
    return [decorator.name for decorator in decorators]


def transform_prompt(prompt: str, decorators: List[str]) -> str:
    """Transform a prompt using a list of decorator strings.

    This function is a wrapper around the core transform_prompt function
    to ensure backward compatibility with the demo.

    Args:
        prompt: The prompt to transform
        decorators: List of decorator strings

    Returns:
        The transformed prompt
    """
    from prompt_decorators.core.dynamic_decorator import (
        transform_prompt as core_transform_prompt,
    )

    return core_transform_prompt(prompt, decorators)
