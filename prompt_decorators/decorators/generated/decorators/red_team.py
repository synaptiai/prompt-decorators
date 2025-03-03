"""
Implementation of the RedTeam decorator.

This module provides the RedTeam decorator class for use in prompt engineering.

Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws. This decorator simulates how an opponent or critic would evaluate and attack ideas, plans, or arguments.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
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

    @property
    def name(self) -> str:
        """
        Get the name of the decorator.

        Returns:
            The name of the decorator
        """
        return self.decorator_name

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
        # Validate parameters
        if self._strength is not None:
            if not isinstance(self._strength, str):
                raise ValidationError("The parameter 'strength' must be a string type value.")
            if self._strength not in ["moderate", "aggressive", "steelman"]:
                raise ValidationError(f"The parameter 'strength' must be one of the allowed enum values: ['moderate', 'aggressive', 'steelman']. Got {self._strength}")
        if self._focus is not None:
            if not isinstance(self._focus, list):
                raise ValidationError("The parameter 'focus' must be an array type value.")
        if self._constructive is not None:
            if not isinstance(self._constructive, bool):
                raise ValidationError("The parameter 'constructive' must be a boolean type value.")

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
            "parameters": {
                "strength": self.strength,
                "focus": self.focus,
                "constructive": self.constructive,
            }
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

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt string.

        Args:
            prompt: The original prompt string

        Returns:
            The modified prompt string
        """
        # This is a placeholder implementation
        # Subclasses should override this method with specific behavior
        return prompt

    @classmethod
    def is_compatible_with_version(cls, version: str) -> bool:
        """
        Check if the decorator is compatible with a specific version.

        Args:
            version: The version to check compatibility with

        Returns:
            True if compatible, False otherwise

        Raises:
            IncompatibleVersionError: If the version is incompatible
        """
        # Check version compatibility
        if version > cls.version:
            raise IncompatibleVersionError(
                f"Version {version} is not compatible with {cls.__name__}. "
                f"Maximum compatible version is {cls.version}."
            )
        # For testing purposes, also raise for very old versions
        if version < '0.1.0':
            raise IncompatibleVersionError(
                f"Version {version} is too old for {cls.__name__}. "
                f"Minimum compatible version is 0.1.0."
            )
        return True

    @classmethod
    def get_metadata(cls) -> Dict[str, Any]:
        """
        Get metadata about the decorator.

        Returns:
            Dictionary containing metadata about the decorator
        """
        return {
            "name": cls.__name__,
            "description": """Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws. This decorator simulates how an opponent or critic would evaluate and attack ideas, plans, or arguments.""",
            "category": "general",
            "version": cls.version,
        }