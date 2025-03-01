"""
Decorator Discovery Module

This module provides utilities for discovering and registering decorators at runtime.
"""

import importlib
import importlib.util
import inspect
import json
import logging
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Type, TypeVar, Union, Any, cast
from types import ModuleType
import glob

from ..core.base import BaseDecorator

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Type variable for decorator classes
T = TypeVar('T', bound=BaseDecorator)


class DecoratorRegistry:
    """
    Registry for prompt decorators.
    
    This class provides methods for registering and discovering decorators at runtime.
    """
    
    _instance = None
    
    def __new__(cls):
        """Create a singleton instance of the registry."""
        if cls._instance is None:
            cls._instance = super(DecoratorRegistry, cls).__new__(cls)
            cls._instance._decorators = {}
            cls._instance._decorator_instances = {}
        return cls._instance
    
    def __init__(self):
        """Initialize the registry."""
        # Initialization is done in __new__
        pass
    
    def clear(self):
        """Clear the registry."""
        self._decorators = {}
        self._decorator_instances = {}
    
    def register_decorator(self, decorator_class: Type[BaseDecorator]) -> None:
        """
        Register a decorator class.
        
        Args:
            decorator_class: The decorator class to register
        """
        name = getattr(decorator_class, "name", decorator_class.__name__)
        self._decorators[name] = decorator_class
        logger.debug(f"Registered decorator class: {name}")
    
    def register_decorator_instance(self, decorator: BaseDecorator) -> None:
        """
        Register a decorator instance.
        
        Args:
            decorator: The decorator instance to register
        """
        name = getattr(decorator, "name", decorator.__class__.__name__)
        self._decorator_instances[name] = decorator
        logger.debug(f"Registered decorator instance: {name}")
    
    def get_decorator(self, name: str) -> Optional[Type[BaseDecorator]]:
        """
        Get a decorator class by name.
        
        Args:
            name: The name of the decorator
            
        Returns:
            The decorator class, or None if not found
        """
        return self._decorators.get(name)
    
    def get_decorator_instance(self, name: str) -> Optional[BaseDecorator]:
        """
        Get a decorator instance by name.
        
        Args:
            name: The name of the decorator
            
        Returns:
            The decorator instance, or None if not found
        """
        return self._decorator_instances.get(name)
    
    def get_all_decorators(self) -> Dict[str, Type[BaseDecorator]]:
        """
        Get all registered decorator classes.
        
        Returns:
            Dictionary mapping decorator names to classes
        """
        return self._decorators.copy()
    
    def get_all_decorator_instances(self) -> Dict[str, BaseDecorator]:
        """
        Get all registered decorator instances.
        
        Returns:
            Dictionary mapping decorator names to instances
        """
        return self._decorator_instances.copy()
    
    def find_decorators_by_category(self, category: str) -> Dict[str, Type[BaseDecorator]]:
        """
        Find decorators by category.
        
        Args:
            category: The category to search for
            
        Returns:
            Dictionary mapping decorator names to classes
        """
        return {
            name: decorator_class
            for name, decorator_class in self._decorators.items()
            if getattr(decorator_class, "category", "").lower() == category.lower()
        }
    
    def get_categories(self) -> Set[str]:
        """
        Get all decorator categories.
        
        Returns:
            Set of category names
        """
        return {
            getattr(decorator_class, "category", "uncategorized").lower()
            for decorator_class in self._decorators.values()
        }
    
    def register_all_from_directory(self, directory: str) -> int:
        """
        Register all decorators from a directory.
        
        Args:
            directory: Path to the directory containing decorator modules
            
        Returns:
            Number of decorators registered
        """
        count = 0
        directory_path = Path(directory)
        
        if not directory_path.exists() or not directory_path.is_dir():
            logger.warning(f"Directory not found: {directory}")
            return 0
        
        # Add the directory to the Python path
        sys.path.insert(0, str(directory_path.parent))
        
        try:
            # Scan for Python files
            for root, _, files in os.walk(directory_path):
                for file in files:
                    if file.endswith(".py") and not file.startswith("__"):
                        # Get the module path
                        module_path = os.path.join(root, file)
                        module_name = os.path.splitext(os.path.relpath(module_path, directory_path.parent))[0]
                        module_name = module_name.replace(os.path.sep, ".")
                        
                        try:
                            # Import the module
                            module = importlib.import_module(module_name)
                            
                            # Find decorator classes
                            for name, obj in inspect.getmembers(module):
                                if (inspect.isclass(obj) and 
                                    issubclass(obj, BaseDecorator) and 
                                    obj != BaseDecorator):
                                    self.register_decorator(obj)
                                    count += 1
                                    logger.debug(f"Registered decorator {obj.name} from {module_name}")
                        except (ImportError, AttributeError) as e:
                            logger.warning(f"Error importing {module_name}: {e}")
        finally:
            # Remove the directory from the Python path
            if str(directory_path.parent) in sys.path:
                sys.path.remove(str(directory_path.parent))
        
        return count
    
    def register_from_json_string(self, json_string: str) -> Optional[Type[BaseDecorator]]:
        """
        Register a decorator from a JSON string.
        
        Args:
            json_string: JSON string containing the decorator definition
            
        Returns:
            The registered decorator class, or None if registration failed
        """
        try:
            # Import the JSONLoader here to avoid circular imports
            from .factory import DecoratorFactory
            
            # Create a factory and register the decorator
            factory = DecoratorFactory(self)
            decorator = factory.create_from_json_string(json_string)
            
            if decorator:
                # The class is already registered by the factory
                return decorator.__class__
            
            return None
        except Exception as e:
            logger.error(f"Error registering decorator from JSON string: {e}")
            return None
    
    def register_from_json_file(self, file_path: str) -> Optional[Type[BaseDecorator]]:
        """
        Register a decorator from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            The registered decorator class, or None if registration failed
        """
        try:
            with open(file_path, 'r') as f:
                json_string = f.read()
            
            return self.register_from_json_string(json_string)
        except Exception as e:
            logger.error(f"Error registering decorator from JSON file {file_path}: {e}")
            return None
    
    def register_all_from_json_directory(self, directory: str) -> int:
        """
        Register all decorators from JSON files in a directory.
        
        Args:
            directory: Path to the directory containing JSON files
            
        Returns:
            Number of decorators registered
        """
        count = 0
        directory_path = Path(directory)
        
        if not directory_path.exists() or not directory_path.is_dir():
            logger.warning(f"Directory not found: {directory}")
            return 0
        
        # Import the JSONLoader and Factory here to avoid circular imports
        from .factory import DecoratorFactory
        
        # Create a factory
        factory = DecoratorFactory(self)
        
        # Load all decorators from the directory
        decorators = factory.create_all_from_directory(directory)
        
        # Count the number of registered decorators
        count = len(decorators)
        
        return count
    
    def create_decorator(self, name: str, **parameters) -> Optional[BaseDecorator]:
        """
        Create a decorator instance from a registered class.
        
        Args:
            name: The name of the decorator
            **parameters: Parameters for the decorator
            
        Returns:
            The decorator instance, or None if creation failed
        """
        decorator_class = self.get_decorator(name)
        if not decorator_class:
            logger.warning(f"Decorator {name} not found")
            return None
        
        try:
            return decorator_class(**parameters)
        except Exception as e:
            logger.error(f"Error creating decorator {name}: {e}")
            return None


# Create a global registry instance
registry = DecoratorRegistry()

# Convenience function to get the global registry
def get_registry() -> DecoratorRegistry:
    """
    Get the global decorator registry.
    
    Returns:
        The global decorator registry instance
    """
    return registry 