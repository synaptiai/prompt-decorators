"""Registry for prompt decorators.

This module maintains a global registry of all available decorators and provides
functions for registering and retrieving them.
"""

from typing import Dict, List, Optional, Set, Type

from prompt_decorators.core.base import DecoratorBase

# Global registry of decorators
_DECORATOR_REGISTRY: Dict[str, Type[DecoratorBase]] = {}
_DECORATOR_CATEGORIES: Dict[str, Set[str]] = {}


class DecoratorRegistry:
    """Registry class for managing prompt decorators.

    This class provides an object-oriented interface to the decorator registry,
    allowing for easier management and access to registered decorators.
    """

    def __init__(self) -> None:
        """Initialize the decorator registry."""
        # Use the global registry
        self._registry = _DECORATOR_REGISTRY
        self._categories = _DECORATOR_CATEGORIES

    @property
    def decorators(self) -> Dict[str, Type[DecoratorBase]]:
        """Get all registered decorators.

        Args:
            self: The instance of the class

        Returns:
            Dictionary mapping decorator names to decorator classes
        """
        return self._registry.copy()

    @property
    def categories(self) -> Dict[str, Set[str]]:
        """Get all decorator categories.

        Args:
            self: The instance of the class

        Returns:
            Dictionary mapping category names to sets of decorator names
        """
        return {k: v.copy() for k, v in self._categories.items()}

    def register(
        self, decorator_class: Type[DecoratorBase], category: str = "unknown"
    ) -> None:
        """Register a decorator class.

        Args:
            decorator_class: The decorator class to register
            category: The category to register the decorator under

        Returns:
            None
        """
        name = decorator_class.__name__
        self._registry[name] = decorator_class

        # Register the category
        if category not in self._categories:
            self._categories[category] = set()
        self._categories[category].add(name)

    def get_decorator(self, name: str) -> Optional[Type[DecoratorBase]]:
        """Get a decorator class by name.

        Args:
            name: The name of the decorator to get

        Returns:
            The decorator class, or None if not found
        """
        return self._registry.get(name)

    def get_by_category(self, category: str) -> List[Type[DecoratorBase]]:
        """Get all decorators in a category.

        Args:
            category: The category to get decorators for

        Returns:
            List of decorator classes in the category
        """
        if category not in self._categories:
            return []
        return [self._registry[name] for name in self._categories[category]]

    def clear(self) -> None:
        """Clear the registry."""
        self._registry.clear()
        self._categories.clear()


def register_decorator(
    decorator_class: Type[DecoratorBase], category: str = "unknown"
) -> None:
    """Register a decorator class in the global registry.

    This function registers a decorator class in the global registry,
    making it available for use in the system.

    Args:
        decorator_class: The decorator class to register
        category: The category to register the decorator under

    Returns:
        None
    """
    # Get the global registry
    registry = DecoratorRegistry()
    registry.register(decorator_class, category)


def get_decorator(name: str) -> Optional[Type[DecoratorBase]]:
    """Get a decorator class by name from the global registry.

    Args:
        name: The name of the decorator to get

    Returns:
        The decorator class, or None if not found
    """
    registry = DecoratorRegistry()
    return registry.get_decorator(name)


def get_registry() -> Dict[str, Type[DecoratorBase]]:
    """Get the global decorator registry.

    Returns:
        Dictionary mapping decorator names to decorator classes
    """
    registry = DecoratorRegistry()
    return registry.decorators


def get_categories() -> Dict[str, Set[str]]:
    """Get all decorator categories from the global registry.

    Returns:
        Dictionary mapping category names to sets of decorator names
    """
    registry = DecoratorRegistry()
    return registry.categories


def get_decorators_by_category(category: str) -> List[Type[DecoratorBase]]:
    """Get all decorators in a category from the global registry.

    Args:
        category: The category to get decorators for

    Returns:
        List of decorator classes in the category
    """
    registry = DecoratorRegistry()
    return registry.get_by_category(category)


def clear_registry() -> None:
    """Clear the global decorator registry."""
    registry = DecoratorRegistry()
    registry.clear()
