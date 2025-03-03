"""
Implementation of the Creative decorator.

This module provides the Creative decorator class for use in prompt engineering.

Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.
"""

from typing import Any, Dict, List, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Creative(BaseDecorator):
    """
    Enhances responses with imaginative, novel, and original content. This
    decorator encourages divergent thinking, metaphorical language, and
    unusual connections to generate engaging and non-obvious outputs.

    Attributes:
        level: The degree of creative thinking to apply
        elements: Specific creative elements to incorporate (e.g., metaphor, wordplay, narrative)
        constraints: Optional creative constraints to work within
    """

    decorator_name = "creative"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        level: Literal["moderate", "high", "unconventional"] = "high",
        elements: List[Any] = None,
        constraints: List[Any] = None,
    ) -> None:
        """
        Initialize the Creative decorator.

        Args:
            level: The degree of creative thinking to apply
            elements: Specific creative elements to incorporate (e.g., metaphor,
                wordplay, narrative)
            constraints: Optional creative constraints to work within

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._level = level
        self._elements = elements
        self._constraints = constraints

        # Validate parameters
        if self._level is not None:
            valid_values = ["moderate", "high", "unconventional"]
            if self._level not in valid_values:
                raise ValidationError(
                    "The parameter 'level' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._elements is not None:
            if not isinstance(self._elements, (list, tuple)):
                raise ValidationError("The parameter 'elements' must be an array.")

        if self._constraints is not None:
            if not isinstance(self._constraints, (list, tuple)):
                raise ValidationError("The parameter 'constraints' must be an array.")

    @property
    def level(self) -> Literal["moderate", "high", "unconventional"]:
        """
        Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

    @property
    def elements(self) -> List[Any]:
        """
        Get the elements parameter value.

        Args:
            self: The decorator instance

        Returns:
            The elements parameter value
        """
        return self._elements

    @property
    def constraints(self) -> List[Any]:
        """
        Get the constraints parameter value.

        Args:
            self: The decorator instance

        Returns:
            The constraints parameter value
        """
        return self._constraints

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "creative",
            "level": self.level,
            "elements": self.elements,
            "constraints": self.constraints,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.level is not None:
            params.append(f"level={self.level}")
        if self.elements is not None:
            params.append(f"elements={self.elements}")
        if self.constraints is not None:
            params.append(f"constraints={self.constraints}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
