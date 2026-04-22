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
    """Factory for creating decorator instances from JSON definitions.

    This class provides utilities for creating decorator instances from JSON definitions,
    either by using existing decorator classes or by dynamically generating new ones.
    """

    def __init__(self, registry: Optional[DecoratorRegistry] = None):
        """Initialize the decorator factory.

        Args:
            registry: The decorator registry to use (optional)
        """
        self.registry = registry or DecoratorRegistry()
        self.json_loader = JSONLoader()

    def create_from_json_string(self, json_string: str) -> Optional[BaseDecorator]:
        """Create a decorator instance from a JSON string.

        Args:
            json_string: JSON string containing the decorator definition

        Returns:
            The created decorator instance, or None if creation failed
        """
        try:
            # Parse the JSON
            decorator_data = self.json_loader.load_from_string(json_string)

            # Create the decorator
            return self.create_from_dict(decorator_data)
        except Exception as e:
            logger.error(f"Error creating decorator from JSON string: {e}")
            return None

    def create_from_file(self, file_path: str) -> Optional[BaseDecorator]:
        """Create a decorator instance from a JSON file.

        Args:
            file_path: Path to the JSON file containing the decorator definition

        Returns:
            The created decorator instance, or None if creation failed
        """
        try:
            # Load the JSON from file
            decorator_data = self.json_loader.load_from_file(file_path)

            # Create the decorator
            return self.create_from_dict(decorator_data)
        except Exception as e:
            logger.error(f"Error creating decorator from file {file_path}: {e}")
            return None

    def create_from_dict(
        self, decorator_data: Dict[str, Any]
    ) -> Optional[BaseDecorator]:
        """Create a decorator instance from a dictionary.

        Args:
            decorator_data: Dictionary containing the decorator definition

        Returns:
            The created decorator instance, or None if creation failed
        """
        try:
            # Get the decorator name
            decorator_name = decorator_data.get("name")
            if not decorator_name:
                logger.error("Decorator definition missing 'name' field")
                return None

            # Try to find an existing decorator class
            decorator_class = self.find_decorator_class(decorator_name)

            # If not found, create a dynamic class
            if not decorator_class:
                decorator_class = self.create_dynamic_class(decorator_data)
                self.registry.register_decorator(decorator_class)

            # Extract parameters from the definition
            parameters = self.extract_parameters(decorator_data)

            # Create an instance of the decorator
            decorator = decorator_class(**parameters)

            # Register the instance
            self.registry.register_decorator_instance(decorator)

            return decorator
        except Exception as e:
            logger.error(f"Error creating decorator from dict: {e}")
            return None

    def find_decorator_class(
        self, decorator_name: str
    ) -> Optional[Type[BaseDecorator]]:
        """Find a decorator class by name.

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
        """Create a dynamic decorator class from a dictionary definition.

        Args:
            decorator_data: Dictionary containing the decorator definition

        Returns:
            A new decorator class
        """
        # Get basic decorator information
        decorator_name = decorator_data.get("name", "CustomDecorator")
        description = decorator_data.get("description", "")
        category = decorator_data.get("category", "custom")
        parameters = decorator_data.get("parameters", [])

        # Create a dictionary of class attributes
        attrs = {
            "name": decorator_name,
            "description": description,
            "category": category,
            "parameters": parameters,
        }

        # Define the apply method
        def apply(self, prompt: str) -> str:
            """Apply the decorator to a prompt.

            Args:
                prompt: The prompt to decorate

            Returns:
                The decorated prompt
            """
            # Get the template
            template = decorator_data.get("template", "{prompt}")

            # Format the template with the prompt and parameters
            try:
                # Create a dictionary of parameter values
                param_values = {}
                for param in parameters:
                    param_name = param.get("name")
                    if hasattr(self, param_name):
                        param_values[param_name] = getattr(self, param_name)

                # Add the prompt
                param_values["prompt"] = prompt

                # Format the template
                return template.format(**param_values)
            except Exception as e:
                logger.error(f"Error applying decorator {decorator_name}: {e}")
                return prompt

        # Add the apply method to the class attributes
        attrs["apply"] = apply

        # Create the class
        return type(decorator_name, (BaseDecorator,), attrs)

    def extract_parameters(self, decorator_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract parameter values from a decorator definition.

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
        """Create decorator instances from all JSON files in a directory.

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
