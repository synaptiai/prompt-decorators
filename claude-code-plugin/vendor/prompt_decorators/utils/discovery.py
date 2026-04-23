"""Decorator discovery and registration utilities.

This module provides utilities for discovering and registering prompt decorators.
"""

import importlib
import importlib.util
import inspect
import json
import os
import sys
from typing import Dict, List, Optional, Set, Type, Union

from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.utils.json_loader import load_json_file


class DecoratorRegistry:
    """Registry for prompt decorators.

    This class provides methods for registering and discovering decorators at runtime.
    """

    _instance = None

    def __new__(cls):
        """Create a singleton instance of the registry.

        Returns:
            The singleton registry instance
        """
        if cls._instance is None:
            cls._instance = super(DecoratorRegistry, cls).__new__(cls)
            cls._instance._decorators = {}
            cls._instance._decorator_instances = {}
            cls._instance._categories = {}
        return cls._instance

    def __init__(self):
        """Initialize the registry.

        This is a no-op for the singleton pattern.

        Args:
            self: The DecoratorRegistry instance

        Returns:
            None
        """
        pass

    def clear(self):
        """Clear all registered decorators.

        This is primarily used for testing.

        Args:
            self: The DecoratorRegistry instance

        Returns:
            None
        """
        self._decorators = {}
        self._decorator_instances = {}
        self._categories = {}

    def register_decorator(self, decorator_class: Type[BaseDecorator]) -> None:
        """Register a decorator class.

        Args:
            decorator_class: The decorator class to register

        Returns:
            None
        """
        name = decorator_class.name
        self._decorators[name] = decorator_class

        # Register category
        category = getattr(decorator_class, "category", "unknown")
        if category not in self._categories:
            self._categories[category] = set()
        self._categories[category].add(name)

    def register_decorator_instance(self, decorator: BaseDecorator) -> None:
        """Register a decorator instance.

        Args:
            decorator: The decorator instance to register

        Returns:
            None
        """
        name = decorator.name
        self._decorator_instances[name] = decorator

    def get_decorator(self, name: str) -> Optional[Type[BaseDecorator]]:
        """Get a decorator class by name.

        Args:
            name: The name of the decorator to retrieve

        Returns:
            The decorator class if found, None otherwise
        """
        return self._decorators.get(name)

    def get_decorator_instance(self, name: str) -> Optional[BaseDecorator]:
        """Get a decorator instance by name.

        Args:
            name: The name of the decorator instance to retrieve

        Returns:
            The decorator instance if found, None otherwise
        """
        return self._decorator_instances.get(name)

    def get_all_decorators(self) -> Dict[str, Type[BaseDecorator]]:
        """Get all registered decorator classes.

        Args:
            self: The DecoratorRegistry instance

        Returns:
            Dictionary mapping decorator names to decorator classes
        """
        return self._decorators.copy()

    def get_all_decorator_instances(self) -> Dict[str, BaseDecorator]:
        """Get all registered decorator instances.

        Args:
            self: The DecoratorRegistry instance

        Returns:
            Dictionary mapping decorator names to decorator instances
        """
        return self._decorator_instances.copy()

    def find_decorators_by_category(
        self, category: str
    ) -> Dict[str, Type[BaseDecorator]]:
        """Find all decorators in a specific category.

        Args:
            category: The category to search for

        Returns:
            Dictionary mapping decorator names to decorator classes
        """
        if category not in self._categories:
            return {}

        return {
            name: self._decorators[name]
            for name in self._categories[category]
            if name in self._decorators
        }

    def get_categories(self) -> Set[str]:
        """Get all registered decorator categories.

        Args:
            self: The DecoratorRegistry instance

        Returns:
            Set of category names
        """
        return set(self._categories.keys())

    def register_all_from_directory(self, directory: str) -> int:
        """Register all decorators from Python files in a directory.

        Args:
            directory: The directory to scan for decorator modules

        Returns:
            Number of decorators registered

        Note:
            This method will import all Python files in the directory and
            register any classes that inherit from BaseDecorator.
        """
        count = 0
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py") and not file.startswith("__"):
                    file_path = os.path.join(root, file)
                    module_name = os.path.splitext(file)[0]

                    # Import the module
                    spec = importlib.util.spec_from_file_location(
                        module_name, file_path
                    )
                    if spec and spec.loader:
                        module = importlib.util.module_from_spec(spec)
                        sys.modules[module_name] = module
                        spec.loader.exec_module(module)

                        # Find and register decorator classes
                        for _, obj in inspect.getmembers(module):
                            if (
                                inspect.isclass(obj)
                                and issubclass(obj, BaseDecorator)
                                and obj != BaseDecorator
                            ):
                                self.register_decorator(obj)
                                count += 1

        return count

    def register_from_json_string(
        self, json_string: str
    ) -> Optional[Type[BaseDecorator]]:
        """Register a decorator from a JSON string.

        Args:
            json_string: JSON string defining a decorator

        Returns:
            The registered decorator class if successful, None otherwise

        Raises:
            ValueError: If the JSON is invalid or missing required fields
        """
        try:
            data = json.loads(json_string)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")

        # Validate required fields
        if "name" not in data:
            raise ValueError("Missing required field 'name'")
        if "description" not in data:
            raise ValueError("Missing required field 'description'")

        # Create a dynamic decorator class
        from prompt_decorators.utils.factory import create_decorator_class

        decorator_class = create_decorator_class(data)
        self.register_decorator(decorator_class)
        return decorator_class

    def register_from_json_file(self, file_path: str) -> Optional[Type[BaseDecorator]]:
        """Register a decorator from a JSON file.

        Args:
            file_path: Path to the JSON file

        Returns:
            The registered decorator class if successful, None otherwise

        Raises:
            ValueError: If the file cannot be read or contains invalid JSON
        """
        try:
            data = load_json_file(file_path)
            json_string = json.dumps(data)
            return self.register_from_json_string(json_string)
        except Exception as e:
            raise ValueError(f"Error loading decorator from {file_path}: {e}")

    def register_all_from_json_directory(self, directory: str) -> int:
        """Register all decorators from JSON files in a directory.

        Args:
            directory: The directory to scan for JSON files

        Returns:
            Number of decorators registered

        Note:
            This method will attempt to register a decorator from each JSON file
            in the specified directory.
        """
        count = 0
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".json"):
                    file_path = os.path.join(root, file)
                    try:
                        if self.register_from_json_file(file_path):
                            count += 1
                    except ValueError as e:
                        # Log the error but continue processing other files
                        print(f"Error registering decorator from {file_path}: {e}")

        return count

    def create_decorator(self, name: str, **parameters) -> Optional[BaseDecorator]:
        """Create a decorator instance by name with the specified parameters.

        Args:
            name: The name of the decorator class to instantiate
            **parameters: Parameters to pass to the decorator constructor

        Returns:
            The created decorator instance if successful, None otherwise

        Raises:
            ValueError: If the decorator class is not found
            TypeError: If the parameters are invalid for the decorator
        """
        decorator_class = self.get_decorator(name)
        if not decorator_class:
            raise ValueError(f"Decorator class not found: {name}")

        try:
            decorator = decorator_class(**parameters)
            return decorator
        except Exception as e:
            raise TypeError(f"Error creating decorator {name}: {e}")


def get_registry() -> DecoratorRegistry:
    """Get the global decorator registry.

    Returns:
        The global decorator registry instance
    """
    return DecoratorRegistry()
