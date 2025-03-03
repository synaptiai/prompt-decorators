"""
Implementation of the Balanced decorator.

This module provides the Balanced decorator class for use in prompt engineering.

Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Balanced(BaseDecorator):
    """
    Ensures equal representation of different perspectives or viewpoints
    on a topic. This decorator promotes fairness and comprehensiveness by
    giving proportional attention to multiple sides of an issue, avoiding
    bias toward any particular position.

    Attributes:
        perspectives: Number of different perspectives to include
        structure: How to structure the different perspectives
        equal: Whether to strictly enforce equal word count for each perspective
    """

    decorator_name = "balanced"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        perspectives: Any = 2,
        structure: Literal["alternating", "sequential", "comparative"] = "sequential",
        equal: bool = True,
    ) -> None:
        """
        Initialize the Balanced decorator.

        Args:
            perspectives: Number of different perspectives to include
            structure: How to structure the different perspectives
            equal: Whether to strictly enforce equal word count for each
                perspective

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._perspectives = perspectives
        self._structure = structure
        self._equal = equal

        # Validate parameters
        if self._perspectives is not None:
            if not isinstance(self._perspectives, (int, float)) or isinstance(
                self._perspectives, bool
            ):
                raise ValidationError(
                    "The parameter 'perspectives' must be a numeric value."
                )

        if self._structure is not None:
            valid_values = ["alternating", "sequential", "comparative"]
            if self._structure not in valid_values:
                raise ValidationError(
                    "The parameter 'structure' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._equal is not None:
            if not isinstance(self._equal, bool):
                raise ValidationError("The parameter 'equal' must be a boolean value.")

    @property
    def perspectives(self) -> Any:
        """
        Get the perspectives parameter value.

        Args:
            self: The decorator instance

        Returns:
            The perspectives parameter value
        """
        return self._perspectives

    @property
    def structure(self) -> Literal["alternating", "sequential", "comparative"]:
        """
        Get the structure parameter value.

        Args:
            self: The decorator instance

        Returns:
            The structure parameter value
        """
        return self._structure

    @property
    def equal(self) -> bool:
        """
        Get the equal parameter value.

        Args:
            self: The decorator instance

        Returns:
            The equal parameter value
        """
        return self._equal

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "balanced",
            "perspectives": self.perspectives,
            "structure": self.structure,
            "equal": self.equal,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.perspectives is not None:
            params.append(f"perspectives={self.perspectives}")
        if self.structure is not None:
            params.append(f"structure={self.structure}")
        if self.equal is not None:
            params.append(f"equal={self.equal}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
