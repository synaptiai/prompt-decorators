"""
Implementation of the Bullet decorator.

This module provides the Bullet decorator class for use in prompt engineering.

Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    BulletStyleEnum,
)


class Bullet(BaseDecorator):
    """
    Formats the response as a bulleted list, making information easier to
    scan and digest. This decorator is ideal for presenting sequential
    steps, key points, or collections of related items in a clean, concise
    format.

    Attributes:
        style: The visual marker used for bullet points
        indented: Whether to allow nested, indented bullet points
        compact: Whether to keep bullet points short and concise (true) or allow longer, more detailed points (false)
    """

    decorator_name = "bullet"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        style: Literal["dash", "dot", "arrow", "star", "plus"] = "dash",
        indented: bool = True,
        compact: bool = False,
    ) -> None:
        """
        Initialize the Bullet decorator.

        Args:
            style: The visual marker used for bullet points
            indented: Whether to allow nested, indented bullet points
            compact: Whether to keep bullet points short and concise (true) or
                allow longer, more detailed points (false)

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._style = style
        self._indented = indented
        self._compact = compact

        # Validate parameters
        if self._style is not None:
            valid_values = ["dash", "dot", "arrow", "star", "plus"]
            if self._style not in valid_values:
                raise ValidationError("The parameter 'style' must be one of the following values: " + ", ".join(valid_values))

        if self._indented is not None:
            if not isinstance(self._indented, bool):
                raise ValidationError("The parameter 'indented' must be a boolean value.")

        if self._compact is not None:
            if not isinstance(self._compact, bool):
                raise ValidationError("The parameter 'compact' must be a boolean value.")


    @property
    def style(self) -> Literal["dash", "dot", "arrow", "star", "plus"]:
        """
        Get the style parameter value.

        Args:
            self: The decorator instance

        Returns:
            The style parameter value
        """
        return self._style

    @property
    def indented(self) -> bool:
        """
        Get the indented parameter value.

        Args:
            self: The decorator instance

        Returns:
            The indented parameter value
        """
        return self._indented

    @property
    def compact(self) -> bool:
        """
        Get the compact parameter value.

        Args:
            self: The decorator instance

        Returns:
            The compact parameter value
        """
        return self._compact

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "bullet",
            "style": self.style,
            "indented": self.indented,
            "compact": self.compact,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.style is not None:
            params.append(f"style={self.style}")
        if self.indented is not None:
            params.append(f"indented={self.indented}")
        if self.compact is not None:
            params.append(f"compact={self.compact}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"