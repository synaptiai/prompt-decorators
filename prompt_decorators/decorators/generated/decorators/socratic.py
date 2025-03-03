"""
Implementation of the Socratic decorator.

This module provides the Socratic decorator class for use in prompt engineering.

Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


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
        # Validate parameters
        if self._iterations is not None:
            if not isinstance(self._iterations, (int, float)):
                raise ValidationError("The parameter 'iterations' must be a numeric type value.")
            if self._iterations < 1:
                raise ValidationError("The parameter 'iterations' must be greater than or equal to 1.")
            if self._iterations > 5:
                raise ValidationError("The parameter 'iterations' must be less than or equal to 5.")

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
            "parameters": {
                "iterations": self.iterations,
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
            "description": """Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.""",
            "category": "general",
            "version": cls.version,
        }