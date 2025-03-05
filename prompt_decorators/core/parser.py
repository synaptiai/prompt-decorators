"""
Parser module for extracting decorators from prompts.

This module provides functionality to parse and extract decorator annotations
from prompt text using the +++ syntax.
"""

import re
from typing import Any, Dict, List, Optional, Tuple

from prompt_decorators.core import BaseDecorator
from prompt_decorators.core.registry import DecoratorRegistry


class DecoratorParser:
    """
    Parser for extracting decorator annotations from prompts.

    This class handles the parsing of decorator annotations in the format:
    +++DecoratorName(param1=value1, param2=value2)
    """

    # Regex pattern for matching decorator annotations
    DECORATOR_PATTERN = r"\+\+\+([A-Za-z0-9_]+)(?:\(([^)]*)\))?"

    def __init__(self, registry: Optional[DecoratorRegistry] = None):
        """Initialize the decorator parser.

        Args:
            registry: Optional decorator registry to use for creating decorators.

        Note:
            If registry is not provided, a new registry will be created.
        """
        self.registry = registry or DecoratorRegistry()

    def extract_decorators(self, prompt: str) -> Tuple[List[BaseDecorator], str]:
        """
        Extract decorator annotations from a prompt.

        Args:
            prompt: The prompt text containing decorator annotations.

        Returns:
            A tuple containing:
            - A list of decorator instances extracted from the prompt
            - The clean prompt text with decorator annotations removed
        """
        # Find all decorator annotations in the prompt
        matches = re.finditer(self.DECORATOR_PATTERN, prompt)

        decorators = []
        clean_prompt = prompt

        for match in matches:
            # Extract decorator name and parameters
            decorator_name = match.group(1)
            params_str = match.group(2) or ""

            # Parse parameters
            params = self._parse_parameters(params_str)

            try:
                # Create decorator instance
                decorator = self._create_decorator(decorator_name, **params)
                decorators.append(decorator)
            except Exception as e:
                # Log error but continue processing
                import logging

                logging.error(f"Error creating decorator {decorator_name}: {str(e)}")
                continue

            # Remove the decorator annotation from the prompt
            clean_prompt = clean_prompt.replace(match.group(0), "", 1)

        # Clean up any extra whitespace
        clean_prompt = clean_prompt.strip()

        return decorators, clean_prompt

    def _create_decorator(self, decorator_name: str, **params: Any) -> BaseDecorator:
        """
        Create a decorator instance by name with the given parameters.

        Args:
            decorator_name: Name of the decorator to create
            **params: Parameters to pass to the decorator constructor

        Returns:
            An instance of the requested decorator

        Raises:
            ValueError: If the decorator is not found in the registry
        """
        # Get the decorator class from the registry
        decorator_class = None

        # Check which type of registry we have and call the appropriate method
        if hasattr(self.registry, "get"):
            # Using registry from core/registry.py
            decorator_class = self.registry.get(decorator_name)

            # If not found, try with lowercase name
            if decorator_class is None:
                decorator_class = self.registry.get(decorator_name.lower())

            # If still not found, try to find by class name
            if decorator_class is None:
                # Get all decorators and find one with matching class name
                all_decorators = self.registry.decorators
                for name, cls in all_decorators.items():
                    if cls.__name__ == decorator_name:
                        decorator_class = cls
                        break
        elif hasattr(self.registry, "get_decorator"):
            # Using registry from utils/discovery.py
            decorator_class = self.registry.get_decorator(decorator_name)

            # If not found, try with lowercase name
            if decorator_class is None:
                decorator_class = self.registry.get_decorator(decorator_name.lower())

            # If still not found, try to find by class name
            if decorator_class is None:
                # Get all decorators and find one with matching class name
                if hasattr(self.registry, "decorators"):
                    all_decorators = self.registry.decorators
                    for name, cls in all_decorators.items():
                        if cls.__name__ == decorator_name:
                            decorator_class = cls
                            break

        if decorator_class is None:
            raise ValueError(f"Decorator '{decorator_name}' not found in registry")

        # Create and return an instance of the decorator
        return decorator_class(**params)

    def _parse_parameters(self, params_str: str) -> Dict[str, Any]:
        """
        Parse parameter string into a dictionary.

        Args:
            params_str: String containing comma-separated key=value pairs.

        Returns:
            Dictionary of parameter names and values.
        """
        if not params_str:
            return {}

        params = {}

        # Split by commas, but respect quotes and nested structures
        param_parts = []
        current_part = ""
        in_quotes = False
        bracket_level = 0

        for char in params_str:
            if char == '"' or char == "'":
                in_quotes = not in_quotes
                current_part += char
            elif char == "," and not in_quotes and bracket_level == 0:
                param_parts.append(current_part.strip())
                current_part = ""
            else:
                if char == "(" or char == "[" or char == "{":
                    bracket_level += 1
                elif char == ")" or char == "]" or char == "}":
                    bracket_level -= 1
                current_part += char

        if current_part:
            param_parts.append(current_part.strip())

        # Process each parameter
        for part in param_parts:
            if "=" in part:
                key, value = part.split("=", 1)
                key = key.strip()
                value = value.strip()

                # Convert string values to appropriate types
                if value.lower() == "true":
                    value_converted: Any = True
                    value = value_converted
                elif value.lower() == "false":
                    value_converted = False
                    value = value_converted
                elif value.lower() == "none":
                    value_converted = None
                    value = value_converted
                elif value.isdigit():
                    value_converted = int(value)
                    value = value_converted
                elif value.replace(".", "", 1).isdigit() and value.count(".") == 1:
                    value_converted = float(value)
                    value = value_converted
                elif (value.startswith('"') and value.endswith('"')) or (
                    value.startswith("'") and value.endswith("'")
                ):
                    # Remove quotes from string values
                    value = value[1:-1]

                params[key] = value

        return params
