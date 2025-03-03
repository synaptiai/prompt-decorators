"""
Implementation of the ELI5 decorator.

This module provides the ELI5 decorator class for use in prompt engineering.

Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class ELI5(BaseDecorator):
    """
    Adapts the response to explain a concept as if to a 5-year-old child.
    This decorator simplifies complex topics using basic vocabulary,
    concrete examples, and relatable analogies to make information
    accessible to non-experts or those new to a subject.

    Attributes:
        strictness: Whether to strictly maintain a child-appropriate level of simplicity or allow slightly more complexity when necessary
    """

    decorator_name = "eli5"
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
        strictness: bool = False,
    ) -> None:
        """
        Initialize the ELI5 decorator.

        Args:
            strictness: Whether to strictly maintain a child-appropriate level of
                simplicity or allow slightly more complexity when necessary

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._strictness = strictness

        # Validate parameters
        # Validate parameters
        if self._strictness is not None:
            if not isinstance(self._strictness, bool):
                raise ValidationError(
                    "The parameter 'strictness' must be a boolean type value."
                )

    @property
    def strictness(self) -> bool:
        """
        Get the strictness parameter value.

        Args:
            self: The decorator instance

        Returns:
            The strictness parameter value
        """
        return self._strictness

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "eli5",
            "parameters": {
                "strictness": self.strictness,
            },
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.strictness is not None:
            params.append(f"strictness={self.strictness}")

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
            "description": """Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.""",
            "category": "general",
            "version": cls.version,
        }
