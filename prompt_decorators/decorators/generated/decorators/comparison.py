"""
Implementation of the Comparison decorator.

This module provides the Comparison decorator class for use in prompt engineering.

Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    ComparisonFormatEnum,
)


class Comparison(BaseDecorator):
    """
    Structures the response as a direct comparison between multiple items,
    concepts, or approaches. This decorator is ideal for highlighting
    similarities and differences across specific dimensions or criteria.

    Attributes:
        aspects: Specific aspects or dimensions to compare
        format: The presentation format for the comparison
        highlight: Whether to explicitly emphasize key differences
    """

    decorator_name = "comparison"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        aspects: List[Any] = None,
        format: Literal["table", "prose", "bullets"] = "table",
        highlight: bool = True,
    ) -> None:
        """
        Initialize the Comparison decorator.

        Args:
            aspects: Specific aspects or dimensions to compare
            format: The presentation format for the comparison
            highlight: Whether to explicitly emphasize key differences

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._aspects = aspects
        self._format = format
        self._highlight = highlight

        # Validate parameters
        if self._aspects is not None:
            if not isinstance(self._aspects, (list, tuple)):
                raise ValidationError("The parameter 'aspects' must be an array.")

        if self._format is not None:
            valid_values = ["table", "prose", "bullets"]
            if self._format not in valid_values:
                raise ValidationError("The parameter 'format' must be one of the following values: " + ", ".join(valid_values))

        if self._highlight is not None:
            if not isinstance(self._highlight, bool):
                raise ValidationError("The parameter 'highlight' must be a boolean value.")


    @property
    def aspects(self) -> List[Any]:
        """
        Get the aspects parameter value.

        Args:
            self: The decorator instance

        Returns:
            The aspects parameter value
        """
        return self._aspects

    @property
    def format(self) -> Literal["table", "prose", "bullets"]:
        """
        Get the format parameter value.

        Args:
            self: The decorator instance

        Returns:
            The format parameter value
        """
        return self._format

    @property
    def highlight(self) -> bool:
        """
        Get the highlight parameter value.

        Args:
            self: The decorator instance

        Returns:
            The highlight parameter value
        """
        return self._highlight

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "comparison",
            "aspects": self.aspects,
            "format": self.format,
            "highlight": self.highlight,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.aspects is not None:
            params.append(f"aspects={self.aspects}")
        if self.format is not None:
            params.append(f"format={self.format}")
        if self.highlight is not None:
            params.append(f"highlight={self.highlight}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"