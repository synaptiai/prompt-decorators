"""
Implementation of the FirstPrinciples decorator.

This module provides the FirstPrinciples decorator class for use in prompt engineering.

Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class FirstPrinciples(BaseDecorator):
    """
    Structures the response by breaking down complex topics into their
    fundamental truths or axioms, then building up from there. This
    decorator promotes a deeper understanding by examining the most basic
    elements of a concept before constructing more complex ideas.

    Attributes:
        depth: Level of detail in breaking down to fundamental principles
    """

    decorator_name = "first_principles"
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
        depth: Any = 3,
    ) -> None:
        """
        Initialize the FirstPrinciples decorator.

        Args:
            depth: Level of detail in breaking down to fundamental principles

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._depth = depth

        # Validate parameters
        # Validate parameters
        if self._depth is not None:
            if not isinstance(self._depth, (int, float)):
                raise ValidationError("The parameter 'depth' must be a numeric type value.")
            if self._depth < 1:
                raise ValidationError("The parameter 'depth' must be greater than or equal to 1.")
            if self._depth > 5:
                raise ValidationError("The parameter 'depth' must be less than or equal to 5.")

    @property
    def depth(self) -> Any:
        """
        Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "first_principles",
            "parameters": {
                "depth": self.depth,
            }
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.depth is not None:
            params.append(f"depth={self.depth}")

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
        if version < '0.1.0':
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
            "description": """Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas.""",
            "category": "general",
            "version": cls.version,
        }