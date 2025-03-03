"""
Implementation of the Override decorator.

This module provides the Override decorator class for use in prompt engineering.

A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Override(BaseDecorator):
    """
    A meta-decorator that overrides the default parameters or behaviors of
    other decorators. This enables customization of standard decorators
    without modifying their definitions, allowing for reuse of established
    patterns with specific adjustments.

    Attributes:
        decorator: The specific decorator whose behavior to override
        parameters: JSON string specifying the parameters to override (e.g., '{"depth": "comprehensive", "focus": "methodology"}')
        behavior: Optional custom behavior modification instructions that override the standard decorator interpretation
    """

    decorator_name = "override"
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
        decorator: str,
        parameters: str = None,
        behavior: str = None,
    ) -> None:
        """
        Initialize the Override decorator.

        Args:
            decorator: The specific decorator whose behavior to override
            parameters: JSON string specifying the parameters to override (e.g.,
                '{"depth": "comprehensive", "focus": "methodology"}')
            behavior: Optional custom behavior modification instructions that
                override the standard decorator interpretation

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._decorator = decorator
        self._parameters = parameters
        self._behavior = behavior

        # Validate parameters
        # Validate parameters
        if self._decorator is not None:
            if not isinstance(self._decorator, str):
                raise ValidationError(
                    "The parameter 'decorator' must be a string type value."
                )
        if self._parameters is not None:
            if not isinstance(self._parameters, str):
                raise ValidationError(
                    "The parameter 'parameters' must be a string type value."
                )
        if self._behavior is not None:
            if not isinstance(self._behavior, str):
                raise ValidationError(
                    "The parameter 'behavior' must be a string type value."
                )

    @property
    def decorator(self) -> str:
        """
        Get the decorator parameter value.

        Args:
            self: The decorator instance

        Returns:
            The decorator parameter value
        """
        return self._decorator

    @property
    def params(self) -> str:
        """
        Get the parameters parameter value.

        Args:
            self: The decorator instance

        Returns:
            The parameters parameter value
        """
        return self._parameters

    @property
    def behavior(self) -> str:
        """
        Get the behavior parameter value.

        Args:
            self: The decorator instance

        Returns:
            The behavior parameter value
        """
        return self._behavior

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "override",
            "parameters": {
                "decorator": self.decorator,
                "parameters": self.params,
                "behavior": self.behavior,
            },
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.decorator is not None:
            params.append(f"decorator={self.decorator}")
        if self.params is not None:
            params.append(f"parameters={self.params}")
        if self.behavior is not None:
            params.append(f"behavior={self.behavior}")

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
            "description": """A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.""",
            "category": "general",
            "version": cls.version,
        }
