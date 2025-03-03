"""
Implementation of the RedTeam decorator.

This module provides the RedTeam decorator class for use in prompt engineering.

Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws. This decorator simulates how an opponent or critic would evaluate and attack ideas, plans, or arguments.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    RedTeamStrengthEnum,
)


class RedTeam(BaseDecorator):
    """
    Applies adversarial analysis to test assumptions, identify
    vulnerabilities, and strengthen proposals by actively looking for
    flaws. This decorator simulates how an opponent or critic would
    evaluate and attack ideas, plans, or arguments.

    Attributes:
        strength: How aggressive or challenging the red team analysis should be
        focus: Specific aspects to focus the red team analysis on
        constructive: Whether to include constructive suggestions for improvement after critiques
    """

    decorator_name = "red_team"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        strength: Literal["moderate", "aggressive", "steelman"] = "moderate",
        focus: List[Any] = None,
        constructive: bool = True,
    ) -> None:
        """
        Initialize the RedTeam decorator.

        Args:
            strength: How aggressive or challenging the red team analysis should
                be
            focus: Specific aspects to focus the red team analysis on
            constructive: Whether to include constructive suggestions for improvement
                after critiques

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._strength = strength
        self._focus = focus
        self._constructive = constructive

        # Validate parameters
        if self._strength is not None:
            valid_values = ["moderate", "aggressive", "steelman"]
            if self._strength not in valid_values:
                raise ValidationError("The parameter 'strength' must be one of the following values: " + ", ".join(valid_values))

        if self._focus is not None:
            if not isinstance(self._focus, (list, tuple)):
                raise ValidationError("The parameter 'focus' must be an array.")

        if self._constructive is not None:
            if not isinstance(self._constructive, bool):
                raise ValidationError("The parameter 'constructive' must be a boolean value.")


    @property
    def strength(self) -> Literal["moderate", "aggressive", "steelman"]:
        """
        Get the strength parameter value.

        Args:
            self: The decorator instance

        Returns:
            The strength parameter value
        """
        return self._strength

    @property
    def focus(self) -> List[Any]:
        """
        Get the focus parameter value.

        Args:
            self: The decorator instance

        Returns:
            The focus parameter value
        """
        return self._focus

    @property
    def constructive(self) -> bool:
        """
        Get the constructive parameter value.

        Args:
            self: The decorator instance

        Returns:
            The constructive parameter value
        """
        return self._constructive

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "red_team",
            "strength": self.strength,
            "focus": self.focus,
            "constructive": self.constructive,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.strength is not None:
            params.append(f"strength={self.strength}")
        if self.focus is not None:
            params.append(f"focus={self.focus}")
        if self.constructive is not None:
            params.append(f"constructive={self.constructive}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"