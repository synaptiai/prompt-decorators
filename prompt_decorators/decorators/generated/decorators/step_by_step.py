"""
Implementation of the StepByStep decorator.

This module provides the StepByStep decorator class for use in prompt engineering.

Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.
"""

from typing import Any, Dict

from prompt_decorators.core.base import BaseDecorator, ValidationError


class StepByStep(BaseDecorator):
    """
    Structures the AI's response as a sequence of clearly labeled steps.
    This decorator helps break down complex processes, explanations, or
    solutions into manageable, sequential parts for better understanding.

    Attributes:
        numbered: Whether to number the steps or use bullet points
    """

    decorator_name = "step_by_step"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        numbered: bool = True,
    ) -> None:
        """
        Initialize the StepByStep decorator.

        Args:
            numbered: Whether to number the steps or use bullet points

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._numbered = numbered

        # Validate parameters
        if self._numbered is not None:
            if not isinstance(self._numbered, bool):
                raise ValidationError(
                    "The parameter 'numbered' must be a boolean value."
                )

    @property
    def numbered(self) -> bool:
        """
        Get the numbered parameter value.

        Args:
            self: The decorator instance

        Returns:
            The numbered parameter value
        """
        return self._numbered

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "step_by_step",
            "numbered": self.numbered,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.numbered is not None:
            params.append(f"numbered={self.numbered}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
