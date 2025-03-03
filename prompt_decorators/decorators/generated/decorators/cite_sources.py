"""
Implementation of the CiteSources decorator.

This module provides the CiteSources decorator class for use in prompt engineering.

Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    CiteSourcesStyleEnum,
    CiteSourcesFormatEnum,
)


class CiteSources(BaseDecorator):
    """
    Structures the response to include citations for claims and
    information. This decorator enhances credibility by providing
    references to source material, enabling fact verification and further
    exploration of topics.

    Attributes:
        style: The placement and format of citations within the response
        format: The citation format to use
        comprehensive: Whether to cite every claim (true) or only major claims (false)
    """

    decorator_name = "cite_sources"
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
        style: Literal["inline", "footnote", "endnote"] = "inline",
        format: Literal["APA", "MLA", "Chicago", "Harvard", "IEEE"] = "APA",
        comprehensive: bool = False,
    ) -> None:
        """
        Initialize the CiteSources decorator.

        Args:
            style: The placement and format of citations within the response
            format: The citation format to use
            comprehensive: Whether to cite every claim (true) or only major claims
                (false)

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._style = style
        self._format = format
        self._comprehensive = comprehensive

        # Validate parameters
        # Validate parameters
        if self._style is not None:
            if not isinstance(self._style, str):
                raise ValidationError("The parameter 'style' must be a string type value.")
            if self._style not in ["inline", "footnote", "endnote"]:
                raise ValidationError(f"The parameter 'style' must be one of the allowed enum values: ['inline', 'footnote', 'endnote']. Got {self._style}")
        if self._format is not None:
            if not isinstance(self._format, str):
                raise ValidationError("The parameter 'format' must be a string type value.")
            if self._format not in ["APA", "MLA", "Chicago", "Harvard", "IEEE"]:
                raise ValidationError(f"The parameter 'format' must be one of the allowed enum values: ['APA', 'MLA', 'Chicago', 'Harvard', 'IEEE']. Got {self._format}")
        if self._comprehensive is not None:
            if not isinstance(self._comprehensive, bool):
                raise ValidationError("The parameter 'comprehensive' must be a boolean type value.")

    @property
    def style(self) -> Literal["inline", "footnote", "endnote"]:
        """
        Get the style parameter value.

        Args:
            self: The decorator instance

        Returns:
            The style parameter value
        """
        return self._style

    @property
    def format(self) -> Literal["APA", "MLA", "Chicago", "Harvard", "IEEE"]:
        """
        Get the format parameter value.

        Args:
            self: The decorator instance

        Returns:
            The format parameter value
        """
        return self._format

    @property
    def comprehensive(self) -> bool:
        """
        Get the comprehensive parameter value.

        Args:
            self: The decorator instance

        Returns:
            The comprehensive parameter value
        """
        return self._comprehensive

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "cite_sources",
            "parameters": {
                "style": self.style,
                "format": self.format,
                "comprehensive": self.comprehensive,
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
        if self.format is not None:
            params.append(f"format={self.format}")
        if self.comprehensive is not None:
            params.append(f"comprehensive={self.comprehensive}")

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
            "description": """Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.""",
            "category": "general",
            "version": cls.version,
        }