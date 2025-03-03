"""
Implementation of the DecoratorName decorator.

This module provides the DecoratorName decorator class for use in prompt engineering.

A detailed description of what the decorator does, its purpose, and how it modifies AI behavior.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class DecoratorName(BaseDecorator):
    """
    A detailed description of what the decorator does, its purpose, and
    how it modifies AI behavior.

    Attributes:
        parameterName: Description of what this parameter does
    """

    decorator_name = "decorator_name"
    version = "1.0.0"  # Initial version

    @property
    def name(self) -> str:
        """
        Get the name of the decorator.

        Returns:
            The name of the decorator
        """
        return self.decorator_name

    def __init__(
        self,
        parameterName: Any = "defaultValue",
    ) -> None:
        """
        Initialize the DecoratorName decorator.

        Args:
            parameterName: Description of what this parameter does

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._parameterName = parameterName

        # Validate parameters
        # Validate parameters
        if self._parameterName is not None:
            if self._parameterName not in ["option1", "option2", "option3"]:
                raise ValidationError(
                    f"The parameter 'parameterName' must be one of the allowed enum values: ['option1', 'option2', 'option3']. Got {self._parameterName}"
                )

    @property
    def parameterName(self) -> Any:
        """
        Get the parameterName parameter value.

        Args:
            self: The decorator instance

        Returns:
            The parameterName parameter value
        """
        return self._parameterName

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "decorator_name",
            "parameters": {
                "parameterName": self.parameterName,
            },
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.parameterName is not None:
            params.append(f"parameterName={self.parameterName}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt string.

        Args:
            prompt: The original prompt string

        Returns:
            The modified prompt string
        """
        # This is a placeholder implementation
        # Subclasses should override this method with specific behavior
        return prompt

    @classmethod
    def is_compatible_with_version(cls, version: str) -> bool:
        """
        Check if the decorator is compatible with a specific version.

        Args:
            version: The version to check compatibility with

        Returns:
            True if compatible, False otherwise

        Raises:
            IncompatibleVersionError: If the version is incompatible
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
        """
        Get metadata about the decorator.

        Returns:
            Dictionary containing metadata about the decorator
        """
        return {
            "name": cls.__name__,
            "description": """A detailed description of what the decorator does, its purpose, and how it modifies AI behavior.""",
            "category": "general",
            "version": cls.version,
        }
