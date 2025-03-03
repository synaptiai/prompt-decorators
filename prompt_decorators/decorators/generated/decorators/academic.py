"""
Implementation of the Academic decorator.

This module provides the Academic decorator class for use in prompt engineering.

Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    AcademicStyleEnum,
    AcademicCitationstyleEnum,
)


class Academic(BaseDecorator):
    """
    Adapts the response to follow scholarly writing conventions
    appropriate for academic publications. This decorator generates
    responses with formal language, structured argumentation, and proper
    citations following established academic citation styles.

    Attributes:
        style: The academic discipline style to follow
        citationStyle: The citation format to use for references
    """

    decorator_name = "academic"
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
        style: Literal["humanities", "scientific", "legal"] = "scientific",
        citationStyle: Literal["APA", "MLA", "Chicago", "Harvard", "IEEE"] = "APA",
    ) -> None:
        """
        Initialize the Academic decorator.

        Args:
            style: The academic discipline style to follow
            citationStyle: The citation format to use for references

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._style = style
        self._citationStyle = citationStyle

        # Validate parameters
        # Validate parameters
        if self._style is not None:
            if not isinstance(self._style, str):
                raise ValidationError("The parameter 'style' must be a string type value.")
            if self._style not in ["humanities", "scientific", "legal"]:
                raise ValidationError(f"The parameter 'style' must be one of the allowed enum values: ['humanities', 'scientific', 'legal']. Got {self._style}")
        if self._citationStyle is not None:
            if not isinstance(self._citationStyle, str):
                raise ValidationError("The parameter 'citationStyle' must be a string type value.")
            if self._citationStyle not in ["APA", "MLA", "Chicago", "Harvard", "IEEE"]:
                raise ValidationError(f"The parameter 'citationStyle' must be one of the allowed enum values: ['APA', 'MLA', 'Chicago', 'Harvard', 'IEEE']. Got {self._citationStyle}")

    @property
    def style(self) -> Literal["humanities", "scientific", "legal"]:
        """
        Get the style parameter value.

        Args:
            self: The decorator instance

        Returns:
            The style parameter value
        """
        return self._style

    @property
    def citationStyle(self) -> Literal["APA", "MLA", "Chicago", "Harvard", "IEEE"]:
        """
        Get the citationStyle parameter value.

        Args:
            self: The decorator instance

        Returns:
            The citationStyle parameter value
        """
        return self._citationStyle

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "academic",
            "parameters": {
                "style": self.style,
                "citationStyle": self.citationStyle,
            }
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.style is not None:
            params.append(f"style={self.style}")
        if self.citationStyle is not None:
            params.append(f"citationStyle={self.citationStyle}")

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
            "description": """Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.""",
            "category": "general",
            "version": cls.version,
        }