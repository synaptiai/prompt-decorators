"""
Implementation of the Refine decorator.

This module provides the Refine decorator class for use in prompt engineering.

A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


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
        # Validate parameters
        if self._iterations is not None:
            if not isinstance(self._iterations, (int, float)):
                raise ValidationError("The parameter 'iterations' must be a numeric type value.")
            if self._iterations < 1:
                raise ValidationError("The parameter 'iterations' must be greater than or equal to 1.")
            if self._iterations > 3:
                raise ValidationError("The parameter 'iterations' must be less than or equal to 3.")
        if self._focus is not None:
            if not isinstance(self._focus, list):
                raise ValidationError("The parameter 'focus' must be an array type value.")
        if self._showProcess is not None:
            if not isinstance(self._showProcess, bool):
                raise ValidationError("The parameter 'showProcess' must be a boolean type value.")

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
            "parameters": {
                "iterations": self.iterations,
                "focus": self.focus,
                "showProcess": self.showProcess,
            }
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
            "description": """A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response.""",
            "category": "general",
            "version": cls.version,
        }