"""
Implementation of the OutputFormat decorator.

This module provides the OutputFormat decorator class for use in prompt engineering.

Specifies the format of the AI's response. This decorator ensures the output follows a specific format, making it easier to parse, display, or process the response in a consistent way.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    OutputFormatFormatEnum,
)


class OutputFormat(BaseDecorator):
    """
    Specifies the format of the AI's response. This decorator ensures the
    output follows a specific format, making it easier to parse, display,
    or process the response in a consistent way.

    Attributes:
        format: The format to use for the response
    """

    decorator_name = "output_format"
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
        format: Literal["json", "markdown", "yaml", "xml", "plaintext"],
    ) -> None:
        """
        Initialize the OutputFormat decorator.

        Args:
            format: The format to use for the response

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._format = format

        # Validate parameters
        # Validate parameters
        if self._format is not None:
            if not isinstance(self._format, str):
                raise ValidationError("The parameter 'format' must be a string type value.")
            if self._format not in ["json", "markdown", "yaml", "xml", "plaintext"]:
                raise ValidationError(f"The parameter 'format' must be one of the allowed enum values: ['json', 'markdown', 'yaml', 'xml', 'plaintext']. Got {self._format}")

    @property
    def format(self) -> Literal["json", "markdown", "yaml", "xml", "plaintext"]:
        """
        Get the format parameter value.

        Args:
            self: The decorator instance

        Returns:
            The format parameter value
        """
        return self._format

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "output_format",
            "parameters": {
                "format": self.format,
            }
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.format is not None:
            params.append(f"format={self.format}")

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
            "description": """Specifies the format of the AI's response. This decorator ensures the output follows a specific format, making it easier to parse, display, or process the response in a consistent way.""",
            "category": "general",
            "version": cls.version,
        }