"""
Implementation of the StepByStep decorator.

This module provides the StepByStep decorator class for use in prompt engineering.

Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


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
        # Validate parameters
        if self._numbered is not None:
            if not isinstance(self._numbered, bool):
                raise ValidationError(
                    "The parameter 'numbered' must be a boolean type value."
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
            "parameters": {
                "numbered": self.numbered,
            },
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
        if version < "0.1.0":
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
            "description": """Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.""",
            "category": "general",
            "version": cls.version,
        }
