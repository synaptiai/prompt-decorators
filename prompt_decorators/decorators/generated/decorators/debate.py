"""Implementation of the Debate decorator.

This module provides the Debate decorator class for use in prompt engineering.

Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Debate(BaseDecorator):
    """Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.

    Attributes:
        perspectives: Number of different perspectives to include in the debate. (Any)
        balanced: Whether to ensure equal representation and strength of arguments for each perspective. (bool)
    """

    name = "debate"  # Class-level name for serialization
    decorator_name = "debate"
    version = "1.0.0"  # Initial version

    @property
    def name(self) -> str:
        """Get the name of the decorator.

        Returns:
            The name of the decorator

        """
        return self.decorator_name

    def __init__(
        self,
        perspectives: Any = 2,
        balanced: bool = True,
    ) -> None:
        """Initialize the Debate decorator.

        Args:
            perspectives: Number of different perspectives to include in the debate
            balanced: Whether to ensure equal representation and strength of arguments for each perspective

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._perspectives = perspectives
        self._balanced = balanced

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._perspectives = perspectives
        self._balanced = balanced

        # Validate parameters
        if self._perspectives is not None:
            if not isinstance(self._perspectives, (int, float)):
                raise ValidationError(
                    "The parameter 'perspectives' must be a numeric type value."
                )
            if self._perspectives < 2:
                raise ValidationError(
                    "The parameter 'perspectives' must be greater than or equal to 2."
                )
            if self._perspectives > 5:
                raise ValidationError(
                    "The parameter 'perspectives' must be less than or equal to 5."
                )
        if self._balanced is not None:
            if not isinstance(self._balanced, bool):
                raise ValidationError(
                    "The parameter 'balanced' must be a boolean type value."
                )

    @property
    def perspectives(self) -> Any:
        """Get the perspectives parameter value.

        Args:
            self: The decorator instance

        Returns:
            The perspectives parameter value
        """
        return self._perspectives

    @property
    def balanced(self) -> bool:
        """Get the balanced parameter value.

        Args:
            self: The decorator instance

        Returns:
            The balanced parameter value
        """
        return self._balanced

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "debate",
            "parameters": {
                "perspectives": self.perspectives,
                "balanced": self.balanced,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

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

    def apply(self, prompt: str) -> str:
        """Apply the decorator to a prompt string.

        Args:
            prompt: The prompt to apply the decorator to


        Returns:
            The modified prompt

        """
        # Subclasses should override this method with specific behavior
        return prompt

    @classmethod
    def is_compatible_with_version(cls, version: str) -> bool:
        """Check if the decorator is compatible with a specific version.

        Args:
            version: The version to check compatibility with.


        Returns:
            True if compatible, False otherwise.


        Raises:
            IncompatibleVersionError: If the version is incompatible.

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
        """Get metadata about the decorator.

        Returns:
            Dictionary containing metadata about the decorator

        """
        return {
            "name": cls.__name__,
            "description": """Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.""",
            "category": "general",
            "version": cls.version,
        }
