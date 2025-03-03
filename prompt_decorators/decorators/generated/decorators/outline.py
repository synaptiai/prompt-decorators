"""
Implementation of the Outline decorator.

This module provides the Outline decorator class for use in prompt engineering.

Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    OutlineStyleEnum,
)


class Outline(BaseDecorator):
    """
    Structures the response as a hierarchical outline with headings and
    subheadings. This decorator organizes information in a clear, logical
    structure that highlights relationships between main topics and
    subtopics.

    Attributes:
        depth: Maximum nesting level of the outline
        style: Numbering or bullet style for the outline
        detailed: Whether to include brief explanations under each outline point
    """

    decorator_name = "outline"
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
        style: Literal["numeric", "bullet", "roman", "alpha", "mixed"] = "numeric",
        detailed: bool = False,
    ) -> None:
        """
        Initialize the Outline decorator.

        Args:
            depth: Maximum nesting level of the outline
            style: Numbering or bullet style for the outline
            detailed: Whether to include brief explanations under each outline
                point

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._depth = depth
        self._style = style
        self._detailed = detailed

        # Validate parameters
        # Validate parameters
        if self._depth is not None:
            if not isinstance(self._depth, (int, float)):
                raise ValidationError("The parameter 'depth' must be a numeric type value.")
            if self._depth < 1:
                raise ValidationError("The parameter 'depth' must be greater than or equal to 1.")
            if self._depth > 5:
                raise ValidationError("The parameter 'depth' must be less than or equal to 5.")
        if self._style is not None:
            if not isinstance(self._style, str):
                raise ValidationError("The parameter 'style' must be a string type value.")
            if self._style not in ["numeric", "bullet", "roman", "alpha", "mixed"]:
                raise ValidationError(f"The parameter 'style' must be one of the allowed enum values: ['numeric', 'bullet', 'roman', 'alpha', 'mixed']. Got {self._style}")
        if self._detailed is not None:
            if not isinstance(self._detailed, bool):
                raise ValidationError("The parameter 'detailed' must be a boolean type value.")

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

    @property
    def style(self) -> Literal["numeric", "bullet", "roman", "alpha", "mixed"]:
        """
        Get the style parameter value.

        Args:
            self: The decorator instance

        Returns:
            The style parameter value
        """
        return self._style

    @property
    def detailed(self) -> bool:
        """
        Get the detailed parameter value.

        Args:
            self: The decorator instance

        Returns:
            The detailed parameter value
        """
        return self._detailed

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "outline",
            "parameters": {
                "depth": self.depth,
                "style": self.style,
                "detailed": self.detailed,
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
        if self.style is not None:
            params.append(f"style={self.style}")
        if self.detailed is not None:
            params.append(f"detailed={self.detailed}")

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
            "description": """Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics.""",
            "category": "general",
            "version": cls.version,
        }