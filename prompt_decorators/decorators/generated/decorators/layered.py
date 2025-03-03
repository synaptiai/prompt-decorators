"""
Implementation of the Layered decorator.

This module provides the Layered decorator class for use in prompt engineering.

Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    LayeredLevelsEnum,
    LayeredProgressionEnum,
)


class Layered(BaseDecorator):
    """
    Presents content at multiple levels of explanation depth, allowing
    readers to engage with information at their preferred level of detail.
    This decorator structures responses with progressive disclosure, from
    high-level summaries to increasingly detailed explanations.

    Attributes:
        levels: The granularity of explanation levels to include
        count: Number of distinct explanation layers to provide
        progression: How to structure the progression between layers
    """

    decorator_name = "layered"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        levels: Literal["sentence-paragraph-full", "basic-intermediate-advanced", "summary-detail-technical"] = "summary-detail-technical",
        count: Any = 3,
        progression: Literal["separate", "nested", "incremental"] = "separate",
    ) -> None:
        """
        Initialize the Layered decorator.

        Args:
            levels: The granularity of explanation levels to include
            count: Number of distinct explanation layers to provide
            progression: How to structure the progression between layers

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._levels = levels
        self._count = count
        self._progression = progression

        # Validate parameters
        if self._levels is not None:
            valid_values = ["sentence-paragraph-full", "basic-intermediate-advanced", "summary-detail-technical"]
            if self._levels not in valid_values:
                raise ValidationError("The parameter 'levels' must be one of the following values: " + ", ".join(valid_values))

        if self._count is not None:
            if not isinstance(self._count, (int, float)) or isinstance(self._count, bool):
                raise ValidationError("The parameter 'count' must be a numeric value.")

        if self._progression is not None:
            valid_values = ["separate", "nested", "incremental"]
            if self._progression not in valid_values:
                raise ValidationError("The parameter 'progression' must be one of the following values: " + ", ".join(valid_values))


    @property
    def levels(self) -> Literal["sentence-paragraph-full", "basic-intermediate-advanced", "summary-detail-technical"]:
        """
        Get the levels parameter value.

        Args:
            self: The decorator instance

        Returns:
            The levels parameter value
        """
        return self._levels

    @property
    def count(self) -> Any:
        """
        Get the count parameter value.

        Args:
            self: The decorator instance

        Returns:
            The count parameter value
        """
        return self._count

    @property
    def progression(self) -> Literal["separate", "nested", "incremental"]:
        """
        Get the progression parameter value.

        Args:
            self: The decorator instance

        Returns:
            The progression parameter value
        """
        return self._progression

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "layered",
            "levels": self.levels,
            "count": self.count,
            "progression": self.progression,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.levels is not None:
            params.append(f"levels={self.levels}")
        if self.count is not None:
            params.append(f"count={self.count}")
        if self.progression is not None:
            params.append(f"progression={self.progression}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"