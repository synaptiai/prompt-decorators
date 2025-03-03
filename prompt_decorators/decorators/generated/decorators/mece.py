"""
Implementation of the MECE decorator.

This module provides the MECE decorator class for use in prompt engineering.

Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    MECEFrameworkEnum,
)


class MECE(BaseDecorator):
    """
    Structures the response using the Mutually Exclusive, Collectively
    Exhaustive framework - a principle where categories have no overlaps
    and cover all possibilities. This decorator ensures comprehensive
    analysis with clear categorization for decision-making and problem-
    solving.

    Attributes:
        dimensions: Number of top-level MECE dimensions to use for categorization
        depth: Maximum level of hierarchical breakdown within each dimension
        framework: Optional predefined MECE framework to apply
    """

    decorator_name = "mece"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        dimensions: Any = 3,
        depth: Any = 2,
        framework: Literal["issue tree", "value chain", "business segments", "stakeholders", "custom"] = "custom",
    ) -> None:
        """
        Initialize the MECE decorator.

        Args:
            dimensions: Number of top-level MECE dimensions to use for
                categorization
            depth: Maximum level of hierarchical breakdown within each
                dimension
            framework: Optional predefined MECE framework to apply

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._dimensions = dimensions
        self._depth = depth
        self._framework = framework

        # Validate parameters
        if self._dimensions is not None:
            if not isinstance(self._dimensions, (int, float)) or isinstance(self._dimensions, bool):
                raise ValidationError("The parameter 'dimensions' must be a numeric value.")

        if self._depth is not None:
            if not isinstance(self._depth, (int, float)) or isinstance(self._depth, bool):
                raise ValidationError("The parameter 'depth' must be a numeric value.")

        if self._framework is not None:
            valid_values = ["issue tree", "value chain", "business segments", "stakeholders", "custom"]
            if self._framework not in valid_values:
                raise ValidationError("The parameter 'framework' must be one of the following values: " + ", ".join(valid_values))


    @property
    def dimensions(self) -> Any:
        """
        Get the dimensions parameter value.

        Args:
            self: The decorator instance

        Returns:
            The dimensions parameter value
        """
        return self._dimensions

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
    def framework(self) -> Literal["issue tree", "value chain", "business segments", "stakeholders", "custom"]:
        """
        Get the framework parameter value.

        Args:
            self: The decorator instance

        Returns:
            The framework parameter value
        """
        return self._framework

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "mece",
            "dimensions": self.dimensions,
            "depth": self.depth,
            "framework": self.framework,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.dimensions is not None:
            params.append(f"dimensions={self.dimensions}")
        if self.depth is not None:
            params.append(f"depth={self.depth}")
        if self.framework is not None:
            params.append(f"framework={self.framework}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"