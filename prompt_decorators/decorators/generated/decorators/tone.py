"""Implementation of the Tone decorator.

This module provides the Tone decorator class for use in prompt engineering.

Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import ToneStyleEnum


class Tone(BaseDecorator):
    """Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.

    Attributes:
        style: The desired tone and style for the response. (Literal["formal", "casual", "friendly", "technical", "humorous"])
    """

    name = "tone"  # Class-level name for serialization
    decorator_name = "tone"
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
        style: Literal["formal", "casual", "friendly", "technical", "humorous"],
    ) -> None:
        """Initialize the Tone decorator.

        Args:
            style: The desired tone and style for the response

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._style = style

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._style = style

        # Validate parameters
        if self._style is not None:
            if not isinstance(self._style, str):
                raise ValidationError(
                    "The parameter 'style' must be a string type value."
                )
            if self._style not in [
                "formal",
                "casual",
                "friendly",
                "technical",
                "humorous",
            ]:
                raise ValidationError(
                    f"The parameter 'style' must be one of the allowed enum values: ['formal', 'casual', 'friendly', 'technical', 'humorous']. Got {self._style}"
                )

    @property
    def style(self) -> Literal["formal", "casual", "friendly", "technical", "humorous"]:
        """Get the style parameter value.

        Args:
            self: The decorator instance

        Returns:
            The style parameter value
        """
        return self._style

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "tone",
            "parameters": {
                "style": self.style,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.style is not None:
            params.append(f"style={self.style}")

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
            "description": """Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.""",
            "category": "general",
            "version": cls.version,
        }
