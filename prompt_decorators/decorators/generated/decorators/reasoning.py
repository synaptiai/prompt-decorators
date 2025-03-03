"""
Implementation of the Reasoning decorator.

This module provides the Reasoning decorator class for use in prompt engineering.

Modifies the AI's response to provide explicit reasoning paths before reaching conclusions. This decorator encourages the model to show its thought process, making responses more transparent and trustworthy.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    ReasoningDepthEnum,
)


class Reasoning(BaseDecorator):
    """
    Modifies the AI's response to provide explicit reasoning paths before
    reaching conclusions. This decorator encourages the model to show its
    thought process, making responses more transparent and trustworthy.

    Attributes:
        depth: The level of detail in the reasoning process
    """

    decorator_name = "reasoning"
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
        depth: Literal["basic", "moderate", "comprehensive"] = "moderate",
    ) -> None:
        """
        Initialize the Reasoning decorator.

        Args:
            depth: The level of detail in the reasoning process

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
            if not isinstance(self._depth, str):
                raise ValidationError("The parameter 'depth' must be a string type value.")
            if self._depth not in ["basic", "moderate", "comprehensive"]:
                raise ValidationError(f"The parameter 'depth' must be one of the allowed enum values: ['basic', 'moderate', 'comprehensive']. Got {self._depth}")

    @property
    def depth(self) -> Literal["basic", "moderate", "comprehensive"]:
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
            "name": "reasoning",
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
            "description": """Modifies the AI's response to provide explicit reasoning paths before reaching conclusions. This decorator encourages the model to show its thought process, making responses more transparent and trustworthy.""",
            "category": "general",
            "version": cls.version,
        }