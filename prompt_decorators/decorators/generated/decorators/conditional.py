"""Implementation of the Conditional decorator.

This module provides the Conditional decorator class for use in prompt engineering.

A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Conditional(BaseDecorator):
    """A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.

    Attributes:
        if_param: The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}'). (str)
        then: The decorator to apply if the condition is true (can be a specific decorator with parameters). (str)
        else_param: The decorator to apply if the condition is false (can be a specific decorator with parameters). (str)
    """

    name = "conditional"  # Class-level name for serialization
    decorator_name = "conditional"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please evaluate the topic and adapt your response formatting based on"
        "the conditional logic specified.",
        "parameterMapping": {
            "if_param": {
                "format": "First, determine if the topic or question can be classified as '{value}'.",
            },
            "then": {
                "format": "If the condition is true (the topic IS {if_param}), then apply the following approach: {value}.",
            },
            "else_param": {
                "format": "If the condition is false (the topic is NOT {if_param}), then apply the following approach instead: {value}.",
            },
        },
        "placement": "prepend",
        "compositionBehavior": "override",
    }

    @property
    def name(self) -> str:
        """Get the name of the decorator.

        Args:
            self: The decorator instance


        Returns:
            The name of the decorator

        """
        return self.decorator_name

    def __init__(
        self,
        if_param: str,
        then: str,
        else_param: str = None,
    ) -> None:
        """Initialize the Conditional decorator.

        Args:
            if_param: The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}')
            then: The decorator to apply if the condition is true (can be a specific decorator with parameters)
            else_param: The decorator to apply if the condition is false (can be a specific decorator with parameters)


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._if_param = if_param
        self._then = then
        self._else_param = else_param

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._if_param = if_param
        self._then = then
        self._else_param = else_param

        # Validate parameters
        if self._if_param is not None:
            if not isinstance(self._if_param, str):
                raise ValidationError(
                    "The parameter 'if_param' must be a string type value."
                )
        if self._then is not None:
            if not isinstance(self._then, str):
                raise ValidationError(
                    "The parameter 'then' must be a string type value."
                )
        if self._else_param is not None:
            if not isinstance(self._else_param, str):
                raise ValidationError(
                    "The parameter 'else_param' must be a string type value."
                )

    @property
    def if_param(self) -> str:
        """Get the if_param parameter value.

        Args:
            self: The decorator instance

        Returns:
            The if_param parameter value
        """
        return self._if_param

    @property
    def then(self) -> str:
        """Get the then parameter value.

        Args:
            self: The decorator instance

        Returns:
            The then parameter value
        """
        return self._then

    @property
    def else_param(self) -> str:
        """Get the else_param parameter value.

        Args:
            self: The decorator instance

        Returns:
            The else_param parameter value
        """
        return self._else_param

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "conditional",
            "parameters": {
                "if_param": self.if_param,
                "then": self.then,
                "else_param": self.else_param,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Args:
            self: The decorator instance

        Returns:
            String representation of the decorator
        """
        params = []
        if self.if_param is not None:
            params.append(f"if_param={self.if_param}")
        if self.then is not None:
            params.append(f"then={self.then}")
        if self.else_param is not None:
            params.append(f"else_param={self.else_param}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"

    def apply(self, prompt: str) -> str:
        """Apply the decorator to a prompt string.

        Args:
            prompt: The prompt to apply the decorator to


        Returns:
            The modified prompt

        """
        # Subclasses should override this method with specific behavior
        return prompt

    @classmethod
    def is_compatible_with_version(cls, version: str) -> bool:
        """Check if the decorator is compatible with a specific version.

        Args:
            version: The version to check compatibility with.


        Returns:
            True if compatible, False otherwise.


        Raises:
            IncompatibleVersionError: If the version is incompatible.

        """
        # Check version compatibility
        if version > cls.version:
            raise IncompatibleVersionError(
                f"Version {version} is not compatible with {cls.__name__}. "
                f"Maximum compatible version is {cls.version}."
            )
        # For testing purposes, also raise for very old versions
        if version < "0.1.0":
            raise IncompatibleVersionError(
                f"Version {version} is too old for {cls.__name__}. "
                f"Minimum compatible version is 0.1.0."
            )
        return True

    @classmethod
    def get_metadata(cls) -> Dict[str, Any]:
        """Get metadata about the decorator.

        Returns:
            Dictionary containing metadata about the decorator


        Args:
            cls: The decorator class

        """
        return {
            "name": cls.__name__,
            "description": """A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.""",
            "category": "general",
            "version": cls.version,
        }

    def apply_to_prompt(self, prompt: str) -> str:
        """Apply the decorator to a prompt.

        This method transforms the prompt using the transformation template.

        Args:
            prompt: The prompt to decorate

        Returns:
            The decorated prompt

        """
        # Use the apply_to_prompt implementation from BaseDecorator
        return super().apply_to_prompt(prompt)
