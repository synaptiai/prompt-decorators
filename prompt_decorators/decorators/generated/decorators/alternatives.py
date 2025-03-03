"""
Implementation of the Alternatives decorator.

This module provides the Alternatives decorator class for use in prompt engineering.

Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Alternatives(BaseDecorator):
    """
    Presents multiple distinct options, approaches, or solutions to a
    question or problem. This decorator encourages exploring different
    paths or perspectives rather than providing a single definitive
    answer.

    Attributes:
        count: Number of alternative options or approaches to generate
        diversity: How different or varied the alternatives should be from each other
        comparison: Whether to include a comparative analysis of the alternatives
    """

    decorator_name = "alternatives"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        count: Any = 3,
        diversity: Literal["low", "medium", "high"] = "medium",
        comparison: bool = False,
    ) -> None:
        """
        Initialize the Alternatives decorator.

        Args:
            count: Number of alternative options or approaches to generate
            diversity: How different or varied the alternatives should be from each
                other
            comparison: Whether to include a comparative analysis of the
                alternatives

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._count = count
        self._diversity = diversity
        self._comparison = comparison

        # Validate parameters
        if self._count is not None:
            if not isinstance(self._count, (int, float)) or isinstance(
                self._count, bool
            ):
                raise ValidationError("The parameter 'count' must be a numeric value.")

        if self._diversity is not None:
            valid_values = ["low", "medium", "high"]
            if self._diversity not in valid_values:
                raise ValidationError(
                    "The parameter 'diversity' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._comparison is not None:
            if not isinstance(self._comparison, bool):
                raise ValidationError(
                    "The parameter 'comparison' must be a boolean value."
                )

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
    def diversity(self) -> Literal["low", "medium", "high"]:
        """
        Get the diversity parameter value.

        Args:
            self: The decorator instance

        Returns:
            The diversity parameter value
        """
        return self._diversity

    @property
    def comparison(self) -> bool:
        """
        Get the comparison parameter value.

        Args:
            self: The decorator instance

        Returns:
            The comparison parameter value
        """
        return self._comparison

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "alternatives",
            "count": self.count,
            "diversity": self.diversity,
            "comparison": self.comparison,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.count is not None:
            params.append(f"count={self.count}")
        if self.diversity is not None:
            params.append(f"diversity={self.diversity}")
        if self.comparison is not None:
            params.append(f"comparison={self.comparison}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
