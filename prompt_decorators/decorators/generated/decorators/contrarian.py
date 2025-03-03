"""
Implementation of the Contrarian decorator.

This module provides the Contrarian decorator class for use in prompt engineering.

Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    ContrarianApproachEnum,
)


class Contrarian(BaseDecorator):
    """
    Generates responses that deliberately challenge conventional wisdom or
    mainstream perspectives. This decorator encourages critical thinking
    by presenting counterarguments, alternative interpretations, or
    challenging established positions on a topic.

    Attributes:
        approach: The specific contrarian approach to take
        maintain: Whether to maintain contrarian stance throughout (true) or provide balanced view at the end (false)
        focus: Optional specific aspect of the topic to focus contrarian analysis on
    """

    decorator_name = "contrarian"
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
        approach: Literal["outsider", "skeptic", "devils-advocate"] = "devils-advocate",
        maintain: bool = False,
        focus: str = None,
    ) -> None:
        """
        Initialize the Contrarian decorator.

        Args:
            approach: The specific contrarian approach to take
            maintain: Whether to maintain contrarian stance throughout (true) or
                provide balanced view at the end (false)
            focus: Optional specific aspect of the topic to focus contrarian
                analysis on

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._approach = approach
        self._maintain = maintain
        self._focus = focus

        # Validate parameters
        # Validate parameters
        if self._approach is not None:
            if not isinstance(self._approach, str):
                raise ValidationError(
                    "The parameter 'approach' must be a string type value."
                )
            if self._approach not in ["outsider", "skeptic", "devils-advocate"]:
                raise ValidationError(
                    f"The parameter 'approach' must be one of the allowed enum values: ['outsider', 'skeptic', 'devils-advocate']. Got {self._approach}"
                )
        if self._maintain is not None:
            if not isinstance(self._maintain, bool):
                raise ValidationError(
                    "The parameter 'maintain' must be a boolean type value."
                )
        if self._focus is not None:
            if not isinstance(self._focus, str):
                raise ValidationError(
                    "The parameter 'focus' must be a string type value."
                )

    @property
    def approach(self) -> Literal["outsider", "skeptic", "devils-advocate"]:
        """
        Get the approach parameter value.

        Args:
            self: The decorator instance

        Returns:
            The approach parameter value
        """
        return self._approach

    @property
    def maintain(self) -> bool:
        """
        Get the maintain parameter value.

        Args:
            self: The decorator instance

        Returns:
            The maintain parameter value
        """
        return self._maintain

    @property
    def focus(self) -> str:
        """
        Get the focus parameter value.

        Args:
            self: The decorator instance

        Returns:
            The focus parameter value
        """
        return self._focus

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "contrarian",
            "parameters": {
                "approach": self.approach,
                "maintain": self.maintain,
                "focus": self.focus,
            },
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.approach is not None:
            params.append(f"approach={self.approach}")
        if self.maintain is not None:
            params.append(f"maintain={self.maintain}")
        if self.focus is not None:
            params.append(f"focus={self.focus}")

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
            "description": """Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.""",
            "category": "general",
            "version": cls.version,
        }
