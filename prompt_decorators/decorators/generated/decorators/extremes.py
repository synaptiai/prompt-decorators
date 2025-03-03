"""
Implementation of the Extremes decorator.

This module provides the Extremes decorator class for use in prompt engineering.

Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Extremes(BaseDecorator):
    """
    Presents content at the extreme ends of a spectrum, showing both a
    radical, ambitious, or maximalist version alongside a minimal,
    conservative, or basic version. This decorator helps explore the range
    of possibilities from the simplest implementation to the most
    expansive vision.

    Attributes:
        versions: Which extreme versions to include
        dimension: The specific dimension along which to explore extremes (e.g., 'cost', 'time', 'ambition', 'complexity')
        compare: Whether to include a comparative analysis of the extreme versions
    """

    decorator_name = "extremes"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        versions: Literal["radical", "minimal", "both"] = "both",
        dimension: str = "ambition",
        compare: bool = True,
    ) -> None:
        """
        Initialize the Extremes decorator.

        Args:
            versions: Which extreme versions to include
            dimension: The specific dimension along which to explore extremes
                (e.g., 'cost', 'time', 'ambition', 'complexity')
            compare: Whether to include a comparative analysis of the extreme
                versions

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._versions = versions
        self._dimension = dimension
        self._compare = compare

        # Validate parameters
        if self._versions is not None:
            valid_values = ["radical", "minimal", "both"]
            if self._versions not in valid_values:
                raise ValidationError(
                    "The parameter 'versions' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._dimension is not None:
            if not isinstance(self._dimension, str):
                raise ValidationError(
                    "The parameter 'dimension' must be a string value."
                )

        if self._compare is not None:
            if not isinstance(self._compare, bool):
                raise ValidationError(
                    "The parameter 'compare' must be a boolean value."
                )

    @property
    def versions(self) -> Literal["radical", "minimal", "both"]:
        """
        Get the versions parameter value.

        Args:
            self: The decorator instance

        Returns:
            The versions parameter value
        """
        return self._versions

    @property
    def dimension(self) -> str:
        """
        Get the dimension parameter value.

        Args:
            self: The decorator instance

        Returns:
            The dimension parameter value
        """
        return self._dimension

    @property
    def compare(self) -> bool:
        """
        Get the compare parameter value.

        Args:
            self: The decorator instance

        Returns:
            The compare parameter value
        """
        return self._compare

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "extremes",
            "versions": self.versions,
            "dimension": self.dimension,
            "compare": self.compare,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.versions is not None:
            params.append(f"versions={self.versions}")
        if self.dimension is not None:
            params.append(f"dimension={self.dimension}")
        if self.compare is not None:
            params.append(f"compare={self.compare}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
