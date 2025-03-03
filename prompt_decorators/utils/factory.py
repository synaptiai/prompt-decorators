"""Decorator Factory Module.

This module provides utilities for creating decorator instances from JSON definitions.
"""

import logging
from typing import Any, Dict, List, Optional, Type

from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.utils.discovery import DecoratorRegistry
from prompt_decorators.utils.json_loader import JSONLoader

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class DecoratorFactory:
    """
    Factory for creating decorator instances from JSON definitions.

    This class provides utilities for creating decorator instances from JSON definitions,
    either by using existing decorator classes or by dynamically generating new ones.
    """

    def __init__(self, registry: Optional[DecoratorRegistry] = None):
        """
        Initialize the decorator factory.

        Args:
            registry: The decorator registry to use (optional)
        """
        self.registry = registry or DecoratorRegistry()
        self.json_loader = JSONLoader()

    def create_from_json_string(self, json_string: str) -> Optional[BaseDecorator]:
        """
        Create a decorator instance from a JSON string.

        Args:
            json_string: The JSON string containing the decorator definition

        Returns:
            The decorator instance, or None if creation failed

        Raises:
            ValueError: If the JSON is invalid or doesn't define a valid decorator
        """
        try:
            # Load the JSON
            decorator_data = self.json_loader.load_from_string(json_string)

            # Create the decorator
            return self.create_from_dict(decorator_data)
        except Exception as e:
            logger.error(f"Error creating decorator from JSON string: {e}")
            return None

    def create_from_file(self, file_path: str) -> Optional[BaseDecorator]:
        """
        Create a decorator instance from a JSON file.

        Args:
            file_path: Path to the JSON file

        Returns:
            The decorator instance, or None if creation failed

        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the JSON is invalid or doesn't define a valid decorator
        """
        try:
            # Load the JSON
            decorator_data = self.json_loader.load_from_file(file_path)

            # Create the decorator
            return self.create_from_dict(decorator_data)
        except Exception as e:
            logger.error(f"Error creating decorator from file {file_path}: {e}")
            return None

    def create_from_dict(
        self, decorator_data: Dict[str, Any]
    ) -> Optional[BaseDecorator]:
        """
        Create a decorator instance from a dictionary.

        Args:
            decorator_data: The decorator definition as a dictionary

        Returns:
            The decorator instance, or None if creation failed

        Raises:
            ValueError: If the dictionary doesn't define a valid decorator
        """
        try:
            # Get the decorator name and version
            decorator_name = decorator_data.get("decoratorName")
            if not decorator_name:
                raise ValueError("Decorator name is required")

            # Try to find an existing decorator class
            decorator_class = self.find_decorator_class(decorator_name)

            # If no matching class is found, create a dynamic class
            if not decorator_class:
                decorator_class = self.create_dynamic_class(decorator_data)

            # Create the decorator parameters
            parameters = self.extract_parameters(decorator_data)

            # Create the decorator instance
            return decorator_class(**parameters)
        except Exception as e:
            logger.error(f"Error creating decorator from dictionary: {e}")
            return None

    def find_decorator_class(
        self, decorator_name: str
    ) -> Optional[Type[BaseDecorator]]:
        """
        Find a decorator class by name.

        Args:
            decorator_name: The name of the decorator

        Returns:
            The decorator class, or None if not found
        """
        # Try to find in registry
        return self.registry.get_decorator(decorator_name)

    def create_dynamic_class(
        self, decorator_data: Dict[str, Any]
    ) -> Type[BaseDecorator]:
        """
        Create a dynamic decorator class from a definition.

        Args:
            decorator_data: The decorator definition as a dictionary

        Returns:
            The dynamically created decorator class

        Raises:
            ValueError: If the dictionary doesn't define a valid decorator
        """
        decorator_name = decorator_data.get("decoratorName")
        if not decorator_name:
            raise ValueError("Decorator name is required")

        version = decorator_data.get("version", "1.0.0")
        description = decorator_data.get("description", "")
        category = decorator_data.get("category", "uncategorized")
        parameters = decorator_data.get("parameters", [])

        # Create parameter getters for each parameter
        param_properties = {}
        for param in parameters:
            param_name = param.get("name")
            if not param_name:
                continue

            # Create a property for each parameter
            param_properties[param_name] = property(
                lambda self, name=param_name: self.get_parameter(name)
            )

        # Create the apply method
        def apply(self, prompt: str) -> str:
            """

            Args:
                prompt: str description
            Returns:

                            Description of return value
                        Apply the decorator to a prompt.

            """
            # Build a detailed instruction based on the decorator definition
            instruction = f"Instructions for {self.name} decorator:\n"

            # Add description if available
            if description:
                instruction += f"{description}\n"

            # Add parameters
            for param_name, param_value in self.parameters.items():
                instruction += f"- {param_name}: {param_value}\n"

            # Combine with original prompt
            return f"{instruction}\n\n{prompt}"

        # Create the dynamic class
        attrs = {
            "name": decorator_name,
            "version": version,
            "description": description,
            "category": category,
            "apply": apply,
            "_json_definition": decorator_data,
            **param_properties,
        }

        # Create the class
        dynamic_class = type(decorator_name, (BaseDecorator,), attrs)

        # Register the class with the registry
        self.registry.register_decorator(dynamic_class)

        return dynamic_class

    def extract_parameters(self, decorator_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract parameter values from a decorator definition.

        Args:
            decorator_data: The decorator definition as a dictionary

        Returns:
            Dictionary of parameter values
        """
        param_values = {}

        # Check if parameters are in array format (new style) or direct properties (old style)
        parameters = decorator_data.get("parameters", [])
        if isinstance(parameters, list):
            # New style: parameters is an array of objects with name and default
            for param in parameters:
                param_name = param.get("name")
                if not param_name:
                    continue

                # If a specific value was provided in the data, use that
                if "value" in param:
                    param_values[param_name] = param.get("value")
                # Otherwise, use the default value if available
                elif "default" in param:
                    param_values[param_name] = param.get("default")
        elif isinstance(parameters, dict):
            # Old style: parameters is a dictionary of name -> value
            param_values = parameters.copy()

        # Check for direct parameter values
        if "parameters" in decorator_data:
            direct_params = decorator_data.get("parameters")
            if isinstance(direct_params, dict):
                param_values.update(direct_params)

        return param_values

    def create_all_from_directory(self, directory_path: str) -> List[BaseDecorator]:
        """
        Create decorator instances from all JSON files in a directory.

        Args:
            directory_path: Path to the directory containing JSON files

        Returns:
            List of decorator instances
        """
        decorators = []

        # Load all JSON files in the directory
        json_files = self.json_loader.load_from_directory(directory_path)

        # Create decorators from each file
        for json_data in json_files:
            try:
                decorator = self.create_from_dict(json_data)
                if decorator:
                    decorators.append(decorator)
            except Exception as e:
                source_file = json_data.get("_source_file", "unknown")
                logger.warning(f"Error creating decorator from {source_file}: {e}")
                continue

        return decorators
