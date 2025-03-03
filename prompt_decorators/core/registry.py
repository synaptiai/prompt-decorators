"""Registry for prompt decorators.

This module maintains a global registry of all available decorators and provides
functions for registering and retrieving them.
"""

from typing import Dict, List, Optional, Set, Type

from prompt_decorators.core.base import BaseDecorator

# Global registry of decorators
_DECORATOR_REGISTRY: Dict[str, Type[BaseDecorator]] = {}
_DECORATOR_CATEGORIES: Dict[str, Set[str]] = {}


def register_decorator(
    decorator_class: Type[BaseDecorator], category: str = "unknown"
) -> None:
    """Register a decorator class in the global registry.

    Args:
        decorator_class: The decorator class to register
        category: Optional category for organizing decorators
    """
    name = decorator_class.name
    _DECORATOR_REGISTRY[name] = decorator_class

    # Register in category
    if category not in _DECORATOR_CATEGORIES:
        _DECORATOR_CATEGORIES[category] = set()

    _DECORATOR_CATEGORIES[category].add(name)


def get_decorator(name: str) -> Optional[Type[BaseDecorator]]:
    """Get a decorator class by name.

    Args:
        name: Name of the decorator

    Returns:
        The decorator class if found, None otherwise
    """
    return _DECORATOR_REGISTRY.get(name)


def get_registry() -> Dict[str, Type[BaseDecorator]]:
    """Get the complete decorator registry.

    Returns:
        Dictionary mapping decorator names to decorator classes
    """
    return _DECORATOR_REGISTRY.copy()


def get_categories() -> Dict[str, Set[str]]:
    """Get all decorator categories and their members.

    Returns:
        Dictionary mapping category names to sets of decorator names
    """
    return {k: v.copy() for k, v in _DECORATOR_CATEGORIES.items()}


def get_decorators_by_category(category: str) -> List[Type[BaseDecorator]]:
    """Get all decorators in a specific category.

    Args:
        category: The category name

    Returns:
        List of decorator classes in the specified category
    """
    if category not in _DECORATOR_CATEGORIES:
        return []

    return [_DECORATOR_REGISTRY[name] for name in _DECORATOR_CATEGORIES[category]]


def clear_registry() -> None:
    """Clear the decorator registry.

    This is primarily used for testing.
    """
    _DECORATOR_REGISTRY.clear()
    _DECORATOR_CATEGORIES.clear()
