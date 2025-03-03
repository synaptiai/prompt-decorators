"""
Implementation of the Debate decorator.

This module provides the Debate decorator class for use in prompt engineering.

Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.
"""

from typing import Any, Dict

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Debate(BaseDecorator):
    """
    Structures the response as a debate between multiple perspectives on a
    topic. This decorator encourages balanced representation of different
    viewpoints and helps explore complex issues from various angles.

    Attributes:
        perspectives: Number of different perspectives to include in the debate
        balanced: Whether to ensure equal representation and strength of arguments for each perspective
    """

    decorator_name = "debate"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        perspectives: Any = 2,
        balanced: bool = True,
    ) -> None:
        """
        Initialize the Debate decorator.

        Args:
            perspectives: Number of different perspectives to include in the debate
            balanced: Whether to ensure equal representation and strength of
                arguments for each perspective

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._perspectives = perspectives
        self._balanced = balanced

        # Validate parameters
        if self._perspectives is not None:
            if not isinstance(self._perspectives, (int, float)) or isinstance(
                self._perspectives, bool
            ):
                raise ValidationError(
                    "The parameter 'perspectives' must be a numeric value."
                )

        if self._balanced is not None:
            if not isinstance(self._balanced, bool):
                raise ValidationError(
                    "The parameter 'balanced' must be a boolean value."
                )

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
    def balanced(self) -> bool:
        """
        Get the balanced parameter value.

        Args:
            self: The decorator instance

        Returns:
            The balanced parameter value
        """
        return self._balanced

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "debate",
            "perspectives": self.perspectives,
            "balanced": self.balanced,
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
        if self.balanced is not None:
            params.append(f"balanced={self.balanced}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
