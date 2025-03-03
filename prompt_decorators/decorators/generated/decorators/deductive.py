"""
Implementation of the Deductive decorator.

This module provides the Deductive decorator class for use in prompt engineering.

Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.
"""

from typing import Any, Dict

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Deductive(BaseDecorator):
    """
    Structures the response using deductive reasoning, moving from general
    principles to specific conclusions. This decorator emphasizes logical
    argument development, starting with premises and working methodically
    to necessary conclusions.

    Attributes:
        premises: Number of main premises to include before deducing conclusions
        formal: Whether to use formal logical structures with explicit syllogisms
        steps: Number of logical steps to include in the deductive process
    """

    decorator_name = "deductive"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        premises: Any = 2,
        formal: bool = False,
        steps: Any = 3,
    ) -> None:
        """
        Initialize the Deductive decorator.

        Args:
            premises: Number of main premises to include before deducing
                conclusions
            formal: Whether to use formal logical structures with explicit
                syllogisms
            steps: Number of logical steps to include in the deductive process

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._premises = premises
        self._formal = formal
        self._steps = steps

        # Validate parameters
        if self._premises is not None:
            if not isinstance(self._premises, (int, float)) or isinstance(
                self._premises, bool
            ):
                raise ValidationError(
                    "The parameter 'premises' must be a numeric value."
                )

        if self._formal is not None:
            if not isinstance(self._formal, bool):
                raise ValidationError("The parameter 'formal' must be a boolean value.")

        if self._steps is not None:
            if not isinstance(self._steps, (int, float)) or isinstance(
                self._steps, bool
            ):
                raise ValidationError("The parameter 'steps' must be a numeric value.")

    @property
    def premises(self) -> Any:
        """
        Get the premises parameter value.

        Args:
            self: The decorator instance

        Returns:
            The premises parameter value
        """
        return self._premises

    @property
    def formal(self) -> bool:
        """
        Get the formal parameter value.

        Args:
            self: The decorator instance

        Returns:
            The formal parameter value
        """
        return self._formal

    @property
    def steps(self) -> Any:
        """
        Get the steps parameter value.

        Args:
            self: The decorator instance

        Returns:
            The steps parameter value
        """
        return self._steps

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "deductive",
            "premises": self.premises,
            "formal": self.formal,
            "steps": self.steps,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.premises is not None:
            params.append(f"premises={self.premises}")
        if self.formal is not None:
            params.append(f"formal={self.formal}")
        if self.steps is not None:
            params.append(f"steps={self.steps}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
