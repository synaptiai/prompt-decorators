"""
Implementation of the Refine decorator.

This module provides the Refine decorator class for use in prompt engineering.

A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response.
"""

from typing import Any, Dict, List

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Refine(BaseDecorator):
    """
    A meta-decorator that iteratively improves the output based on
    specified criteria or dimensions. This decorator simulates multiple
    drafts or revisions of content, with each iteration focusing on
    enhancing particular aspects of the response.

    Attributes:
        iterations: Number of refinement cycles to perform
        focus: Specific aspects to focus on during refinement (e.g., clarity, conciseness, evidence)
        showProcess: Whether to show the intermediate steps in the refinement process
    """

    decorator_name = "refine"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        iterations: Any = 2,
        focus: List[Any] = None,
        showProcess: bool = False,
    ) -> None:
        """
        Initialize the Refine decorator.

        Args:
            iterations: Number of refinement cycles to perform
            focus: Specific aspects to focus on during refinement (e.g.,
                clarity, conciseness, evidence)
            showProcess: Whether to show the intermediate steps in the refinement
                process

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._iterations = iterations
        self._focus = focus
        self._showProcess = showProcess

        # Validate parameters
        if self._iterations is not None:
            if not isinstance(self._iterations, (int, float)) or isinstance(
                self._iterations, bool
            ):
                raise ValidationError(
                    "The parameter 'iterations' must be a numeric value."
                )

        if self._focus is not None:
            if not isinstance(self._focus, (list, tuple)):
                raise ValidationError("The parameter 'focus' must be an array.")

        if self._showProcess is not None:
            if not isinstance(self._showProcess, bool):
                raise ValidationError(
                    "The parameter 'showProcess' must be a boolean value."
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
    def showProcess(self) -> bool:
        """
        Get the showProcess parameter value.

        Args:
            self: The decorator instance

        Returns:
            The showProcess parameter value
        """
        return self._showProcess

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "refine",
            "iterations": self.iterations,
            "focus": self.focus,
            "showProcess": self.showProcess,
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
        if self.focus is not None:
            params.append(f"focus={self.focus}")
        if self.showProcess is not None:
            params.append(f"showProcess={self.showProcess}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
