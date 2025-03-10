"""Parser module for extracting decorators from prompts.

This module provides functionality to parse and extract decorator annotations
from prompt text using the +++ syntax.
"""

import re
from typing import Any, Dict, List, Optional, Tuple

from prompt_decorators.core.base import DecoratorBase
from prompt_decorators.core.registry import DecoratorRegistry


class DecoratorParser:
    """Parser for extracting decorator annotations from prompts.

    This class handles the parsing of decorator annotations in the format:
    +++DecoratorName(param1=value1, param2=value2)
    """

    # Regex pattern for matching decorator annotations
    DECORATOR_PATTERN = r"\+\+\+([A-Za-z0-9_]+)(?:\(([^)]*)\))?"

    def __init__(self, registry: Optional[DecoratorRegistry] = None):
        """Initialize the decorator parser.

        Args:
            registry: Optional decorator registry to use for creating decorators. If not provided, the global registry will be used.
        """
        from prompt_decorators.core.registry import get_registry

        self.registry = registry or get_registry()

    def extract_decorators(self, prompt: str) -> Tuple[List[DecoratorBase], str]:
        """Extract decorator annotations from a prompt.

        This method extracts all decorator annotations from the prompt text,
        creates decorator instances for each annotation, and returns both the
        list of decorators and the cleaned prompt text.

        Args:
            prompt: The prompt text to parse

        Returns:
            A tuple containing:
                - A list of decorator instances
                - The prompt text with decorator annotations removed
        """
        # Find all decorator annotations
        matches = re.finditer(self.DECORATOR_PATTERN, prompt, re.MULTILINE)
        decorators = []
        cleaned_prompt = prompt

        # Process each match
        for match in matches:
            # Extract decorator name and parameters
            decorator_name = match.group(1)
            params_str = match.group(2) or ""

            # Parse parameters
            params = self._parse_parameters(params_str)

            # Create decorator instance
            try:
                decorator = self._create_decorator(decorator_name, **params)
                decorators.append(decorator)
            except Exception as e:
                # Log error but continue processing
                import logging

                logging.getLogger(__name__).warning(
                    f"Failed to create decorator {decorator_name}: {e}"
                )

            # Remove the decorator annotation from the prompt
            cleaned_prompt = cleaned_prompt.replace(match.group(0), "", 1)

        # Clean up any leading/trailing whitespace
        cleaned_prompt = cleaned_prompt.strip()

        return decorators, cleaned_prompt

    def _create_decorator(self, decorator_name: str, **params: Any) -> DecoratorBase:
        """Create a decorator instance by name.

        Args:
            decorator_name: Name of the decorator to create
            **params: Parameters to pass to the decorator constructor

        Returns:
            A decorator instance

        Raises:
            ValueError: If the decorator is not found in the registry
        """
        # Get the decorator class from the registry
        if isinstance(self.registry, DecoratorRegistry):
            decorator_class = self.registry.get_decorator(decorator_name)
        else:
            decorator_class = self.registry.get(decorator_name)

        if not decorator_class:
            raise ValueError(f"Decorator not found: {decorator_name}")

        # Create and return the decorator instance
        return decorator_class(**params)

    def _parse_parameters(self, params_str: str) -> Dict[str, Any]:
        """Parse parameter string into a dictionary.

        This method parses a parameter string in the format:
        param1=value1, param2=value2

        Args:
            params_str: Parameter string to parse

        Returns:
            Dictionary of parameter names and values
        """
        if not params_str:
            return {}

        # Regular expression for matching parameters
        # This handles quoted strings, numbers, booleans, and nested structures
        param_pattern = r'([a-zA-Z0-9_]+)=(?:"([^"]*)"|(True|False|[0-9]+(?:\.[0-9]+)?|[a-zA-Z0-9_]+))'

        # Find all parameter matches
        matches = re.finditer(param_pattern, params_str)
        params = {}

        for match in matches:
            name = match.group(1)
            # Use the quoted value if available, otherwise use the unquoted value
            value = match.group(2) if match.group(2) is not None else match.group(3)

            # Convert value to appropriate type
            if value == "True":
                value = True
            elif value == "False":
                value = False
            elif value is not None and re.match(r"^[0-9]+$", value):
                value = int(value)
            elif value is not None and re.match(r"^[0-9]+\.[0-9]+$", value):
                value = float(value)

            params[name] = value

        return params
