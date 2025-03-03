"""Implementation of the Nested decorator.

This module provides the Nested decorator class for use in prompt engineering.

Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import NestedStyleEnum


class Nested(BaseDecorator):
    """Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.

    Attributes:
        depth: Maximum nesting level of the hierarchy. (Any)
        style: Visual style for hierarchical levels. (Literal["bullet", "numbered", "mixed"])
        collapsible: Whether to suggest the hierarchy could be rendered as collapsible sections (for UI implementations). (bool)
    """

    name = "nested"  # Class-level name for serialization
    decorator_name = "nested"
    version = "1.0.0"  # Initial version

    @property
    def name(self) -> str:
        """Get the name of the decorator.

        Returns:
            The name of the decorator

        """
        return self.decorator_name

    def __init__(
        self,
        depth: Any = 3,
        style: Literal["bullet", "numbered", "mixed"] = "mixed",
        collapsible: bool = False,
    ) -> None:
        """Initialize the Nested decorator.

        Args:
            depth: Maximum nesting level of the hierarchy
            style: Visual style for hierarchical levels
            collapsible: Whether to suggest the hierarchy could be rendered as collapsible sections (for UI implementations)

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._depth = depth
        self._style = style
        self._collapsible = collapsible

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._depth = depth
        self._style = style
        self._collapsible = collapsible

        # Validate parameters
        if self._depth is not None:
            if not isinstance(self._depth, (int, float)):
                raise ValidationError(
                    "The parameter 'depth' must be a numeric type value."
                )
            if self._depth < 2:
                raise ValidationError(
                    "The parameter 'depth' must be greater than or equal to 2."
                )
            if self._depth > 5:
                raise ValidationError(
                    "The parameter 'depth' must be less than or equal to 5."
                )
        if self._style is not None:
            if not isinstance(self._style, str):
                raise ValidationError(
                    "The parameter 'style' must be a string type value."
                )
            if self._style not in ["bullet", "numbered", "mixed"]:
                raise ValidationError(
                    f"The parameter 'style' must be one of the allowed enum values: ['bullet', 'numbered', 'mixed']. Got {self._style}"
                )
        if self._collapsible is not None:
            if not isinstance(self._collapsible, bool):
                raise ValidationError(
                    "The parameter 'collapsible' must be a boolean type value."
                )

    @property
    def depth(self) -> Any:
        """Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    @property
    def style(self) -> Literal["bullet", "numbered", "mixed"]:
        """Get the style parameter value.

        Args:
            self: The decorator instance

        Returns:
            The style parameter value
        """
        return self._style

    @property
    def collapsible(self) -> bool:
        """Get the collapsible parameter value.

        Args:
            self: The decorator instance

        Returns:
            The collapsible parameter value
        """
        return self._collapsible

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "nested",
            "parameters": {
                "depth": self.depth,
                "style": self.style,
                "collapsible": self.collapsible,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.depth is not None:
            params.append(f"depth={self.depth}")
        if self.style is not None:
            params.append(f"style={self.style}")
        if self.collapsible is not None:
            params.append(f"collapsible={self.collapsible}")

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

        """
        return {
            "name": cls.__name__,
            "description": """Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.""",
            "category": "general",
            "version": cls.version,
        }
