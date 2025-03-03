"""
Implementation of the Steelman decorator.

This module provides the Steelman decorator class for use in prompt engineering.

Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.
"""

from typing import Any, Dict

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Steelman(BaseDecorator):
    """
    Presents the strongest possible version of an argument or position,
    even those the AI might not agree with. This decorator opposes
    strawman fallacies by ensuring each viewpoint is represented in its
    most compelling and charitable form.

    Attributes:
        sides: Number of different viewpoints to steel-man
        critique: Whether to include critique after presenting the steel-manned arguments
        separation: Whether to clearly separate the steel-manned presentations from any analysis
    """

    decorator_name = "steelman"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        sides: Any = 2,
        critique: bool = False,
        separation: bool = True,
    ) -> None:
        """
        Initialize the Steelman decorator.

        Args:
            sides: Number of different viewpoints to steel-man
            critique: Whether to include critique after presenting the steel-
                manned arguments
            separation: Whether to clearly separate the steel-manned presentations
                from any analysis

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._sides = sides
        self._critique = critique
        self._separation = separation

        # Validate parameters
        if self._sides is not None:
            if not isinstance(self._sides, (int, float)) or isinstance(
                self._sides, bool
            ):
                raise ValidationError("The parameter 'sides' must be a numeric value.")

        if self._critique is not None:
            if not isinstance(self._critique, bool):
                raise ValidationError(
                    "The parameter 'critique' must be a boolean value."
                )

        if self._separation is not None:
            if not isinstance(self._separation, bool):
                raise ValidationError(
                    "The parameter 'separation' must be a boolean value."
                )

    @property
    def sides(self) -> Any:
        """
        Get the sides parameter value.

        Args:
            self: The decorator instance

        Returns:
            The sides parameter value
        """
        return self._sides

    @property
    def critique(self) -> bool:
        """
        Get the critique parameter value.

        Args:
            self: The decorator instance

        Returns:
            The critique parameter value
        """
        return self._critique

    @property
    def separation(self) -> bool:
        """
        Get the separation parameter value.

        Args:
            self: The decorator instance

        Returns:
            The separation parameter value
        """
        return self._separation

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "steelman",
            "sides": self.sides,
            "critique": self.critique,
            "separation": self.separation,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.sides is not None:
            params.append(f"sides={self.sides}")
        if self.critique is not None:
            params.append(f"critique={self.critique}")
        if self.separation is not None:
            params.append(f"separation={self.separation}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
