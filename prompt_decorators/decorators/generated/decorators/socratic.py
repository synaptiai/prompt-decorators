"""
Implementation of the Socratic decorator.

This module provides the Socratic decorator class for use in prompt engineering.

Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.
"""

from typing import Any, Dict

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Socratic(BaseDecorator):
    """
    Structures the response as a series of questions that guide the user
    through a problem or topic. This decorator encourages critical
    thinking through question-based exploration, helping to uncover
    assumptions and lead to deeper understanding.

    Attributes:
        iterations: Number of question-answer cycles to include
    """

    decorator_name = "socratic"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        iterations: Any = 3,
    ) -> None:
        """
        Initialize the Socratic decorator.

        Args:
            iterations: Number of question-answer cycles to include

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._iterations = iterations

        # Validate parameters
        if self._iterations is not None:
            if not isinstance(self._iterations, (int, float)) or isinstance(
                self._iterations, bool
            ):
                raise ValidationError(
                    "The parameter 'iterations' must be a numeric value."
                )

    @property
    def iterations(self) -> Any:
        """
        Get the iterations parameter value.

        Args:
            self: The decorator instance

        Returns:
            The iterations parameter value
        """
        return self._iterations

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "socratic",
            "iterations": self.iterations,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.iterations is not None:
            params.append(f"iterations={self.iterations}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
