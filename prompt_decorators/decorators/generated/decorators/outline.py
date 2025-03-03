"""
Implementation of the Outline decorator.

This module provides the Outline decorator class for use in prompt engineering.

Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
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
        if self._depth is not None:
            if not isinstance(self._depth, (int, float)) or isinstance(self._depth, bool):
                raise ValidationError("The parameter 'depth' must be a numeric value.")

        if self._style is not None:
            valid_values = ["numeric", "bullet", "roman", "alpha", "mixed"]
            if self._style not in valid_values:
                raise ValidationError("The parameter 'style' must be one of the following values: " + ", ".join(valid_values))

        if self._detailed is not None:
            if not isinstance(self._detailed, bool):
                raise ValidationError("The parameter 'detailed' must be a boolean value.")


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
            "depth": self.depth,
            "style": self.style,
            "detailed": self.detailed,
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