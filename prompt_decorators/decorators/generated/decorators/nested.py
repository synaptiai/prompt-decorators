"""
Implementation of the Nested decorator.

This module provides the Nested decorator class for use in prompt engineering.

Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    NestedStyleEnum,
)


class Nested(BaseDecorator):
    """
    Organizes information in a deeply hierarchical structure with multiple
    levels of nesting. This decorator is ideal for complex topics with
    many subcategories, helping to maintain clarity through consistent
    organization patterns.

    Attributes:
        depth: Maximum nesting level of the hierarchy
        style: Visual style for hierarchical levels
        collapsible: Whether to suggest the hierarchy could be rendered as collapsible sections (for UI implementations)
    """

    decorator_name = "nested"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        depth: Any = 3,
        style: Literal["bullet", "numbered", "mixed"] = "mixed",
        collapsible: bool = False,
    ) -> None:
        """
        Initialize the Nested decorator.

        Args:
            depth: Maximum nesting level of the hierarchy
            style: Visual style for hierarchical levels
            collapsible: Whether to suggest the hierarchy could be rendered as
                collapsible sections (for UI implementations)

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._depth = depth
        self._style = style
        self._collapsible = collapsible

        # Validate parameters
        if self._depth is not None:
            if not isinstance(self._depth, (int, float)) or isinstance(self._depth, bool):
                raise ValidationError("The parameter 'depth' must be a numeric value.")

        if self._style is not None:
            valid_values = ["bullet", "numbered", "mixed"]
            if self._style not in valid_values:
                raise ValidationError("The parameter 'style' must be one of the following values: " + ", ".join(valid_values))

        if self._collapsible is not None:
            if not isinstance(self._collapsible, bool):
                raise ValidationError("The parameter 'collapsible' must be a boolean value.")


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
    def style(self) -> Literal["bullet", "numbered", "mixed"]:
        """
        Get the style parameter value.

        Args:
            self: The decorator instance

        Returns:
            The style parameter value
        """
        return self._style

    @property
    def collapsible(self) -> bool:
        """
        Get the collapsible parameter value.

        Args:
            self: The decorator instance

        Returns:
            The collapsible parameter value
        """
        return self._collapsible

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "nested",
            "depth": self.depth,
            "style": self.style,
            "collapsible": self.collapsible,
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
        if self.collapsible is not None:
            params.append(f"collapsible={self.collapsible}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"