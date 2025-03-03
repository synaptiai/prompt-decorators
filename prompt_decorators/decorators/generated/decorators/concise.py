"""
Implementation of the Concise decorator.

This module provides the Concise decorator class for use in prompt engineering.

Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Concise(BaseDecorator):
    """
    Optimizes the response for brevity and directness, eliminating
    unnecessary details and verbose language. This decorator is ideal for
    obtaining quick answers, executive summaries, or essential information
    when time or space is limited.

    Attributes:
        maxWords: Maximum word count for the entire response
        bulletPoints: Whether to use bullet points for maximum brevity
        level: The degree of conciseness to apply
    """

    decorator_name = "concise"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        maxWords: Any = None,
        bulletPoints: bool = False,
        level: Literal["moderate", "high", "extreme"] = "moderate",
    ) -> None:
        """
        Initialize the Concise decorator.

        Args:
            maxWords: Maximum word count for the entire response
            bulletPoints: Whether to use bullet points for maximum brevity
            level: The degree of conciseness to apply

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._maxWords = maxWords
        self._bulletPoints = bulletPoints
        self._level = level

        # Validate parameters
        if self._maxWords is not None:
            if not isinstance(self._maxWords, (int, float)) or isinstance(
                self._maxWords, bool
            ):
                raise ValidationError(
                    "The parameter 'maxWords' must be a numeric value."
                )

        if self._bulletPoints is not None:
            if not isinstance(self._bulletPoints, bool):
                raise ValidationError(
                    "The parameter 'bulletPoints' must be a boolean value."
                )

        if self._level is not None:
            valid_values = ["moderate", "high", "extreme"]
            if self._level not in valid_values:
                raise ValidationError(
                    "The parameter 'level' must be one of the following values: "
                    + ", ".join(valid_values)
                )

    @property
    def maxWords(self) -> Any:
        """
        Get the maxWords parameter value.

        Args:
            self: The decorator instance

        Returns:
            The maxWords parameter value
        """
        return self._maxWords

    @property
    def bulletPoints(self) -> bool:
        """
        Get the bulletPoints parameter value.

        Args:
            self: The decorator instance

        Returns:
            The bulletPoints parameter value
        """
        return self._bulletPoints

    @property
    def level(self) -> Literal["moderate", "high", "extreme"]:
        """
        Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "concise",
            "maxWords": self.maxWords,
            "bulletPoints": self.bulletPoints,
            "level": self.level,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.maxWords is not None:
            params.append(f"maxWords={self.maxWords}")
        if self.bulletPoints is not None:
            params.append(f"bulletPoints={self.bulletPoints}")
        if self.level is not None:
            params.append(f"level={self.level}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
