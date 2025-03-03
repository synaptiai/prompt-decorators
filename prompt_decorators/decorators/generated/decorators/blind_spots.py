"""
Implementation of the BlindSpots decorator.

This module provides the BlindSpots decorator class for use in prompt engineering.

Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.
"""

from typing import Any, Dict, List, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class BlindSpots(BaseDecorator):
    """
    Identifies potential cognitive blind spots, unstated assumptions, and
    overlooked perspectives in the response. This decorator helps mitigate
    bias by explicitly acknowledging the limitations of one's thinking and
    analysis.

    Attributes:
        categories: Specific categories of blind spots to check for (e.g., cultural, temporal, confirmation bias)
        depth: How thoroughly to analyze for blind spots
        position: Where to place the blind spots analysis
    """

    decorator_name = "blind_spots"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        categories: List[Any] = None,
        depth: Literal["basic", "thorough", "comprehensive"] = "thorough",
        position: Literal["after", "before", "integrated"] = "after",
    ) -> None:
        """
        Initialize the BlindSpots decorator.

        Args:
            categories: Specific categories of blind spots to check for (e.g.,
                cultural, temporal, confirmation bias)
            depth: How thoroughly to analyze for blind spots
            position: Where to place the blind spots analysis

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._categories = categories
        self._depth = depth
        self._position = position

        # Validate parameters
        if self._categories is not None:
            if not isinstance(self._categories, (list, tuple)):
                raise ValidationError("The parameter 'categories' must be an array.")

        if self._depth is not None:
            valid_values = ["basic", "thorough", "comprehensive"]
            if self._depth not in valid_values:
                raise ValidationError(
                    "The parameter 'depth' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._position is not None:
            valid_values = ["after", "before", "integrated"]
            if self._position not in valid_values:
                raise ValidationError(
                    "The parameter 'position' must be one of the following values: "
                    + ", ".join(valid_values)
                )

    @property
    def categories(self) -> List[Any]:
        """
        Get the categories parameter value.

        Args:
            self: The decorator instance

        Returns:
            The categories parameter value
        """
        return self._categories

    @property
    def depth(self) -> Literal["basic", "thorough", "comprehensive"]:
        """
        Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    @property
    def position(self) -> Literal["after", "before", "integrated"]:
        """
        Get the position parameter value.

        Args:
            self: The decorator instance

        Returns:
            The position parameter value
        """
        return self._position

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "blind_spots",
            "categories": self.categories,
            "depth": self.depth,
            "position": self.position,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.categories is not None:
            params.append(f"categories={self.categories}")
        if self.depth is not None:
            params.append(f"depth={self.depth}")
        if self.position is not None:
            params.append(f"position={self.position}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
