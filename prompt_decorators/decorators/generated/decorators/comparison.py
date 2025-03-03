"""Implementation of the Comparison decorator.

This module provides the Comparison decorator class for use in prompt engineering.

Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import ComparisonFormatEnum


class Comparison(BaseDecorator):
    """Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.

    Attributes:
        aspects: Specific aspects or dimensions to compare. (List[Any])
        format: The presentation format for the comparison. (Literal["table", "prose", "bullets"])
        highlight: Whether to explicitly emphasize key differences. (bool)
    """

    name = "comparison"  # Class-level name for serialization
    decorator_name = "comparison"
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
        aspects: List[Any] = None,
        format: Literal["table", "prose", "bullets"] = "table",
        highlight: bool = True,
    ) -> None:
        """Initialize the Comparison decorator.

        Args:
            aspects: Specific aspects or dimensions to compare
            format: The presentation format for the comparison
            highlight: Whether to explicitly emphasize key differences

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._aspects = aspects
        self._format = format
        self._highlight = highlight

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._aspects = aspects
        self._format = format
        self._highlight = highlight

        # Validate parameters
        if self._aspects is not None:
            if not isinstance(self._aspects, list):
                raise ValidationError(
                    "The parameter 'aspects' must be an array type value."
                )
        if self._format is not None:
            if not isinstance(self._format, str):
                raise ValidationError(
                    "The parameter 'format' must be a string type value."
                )
            if self._format not in ["table", "prose", "bullets"]:
                raise ValidationError(
                    f"The parameter 'format' must be one of the allowed enum values: ['table', 'prose', 'bullets']. Got {self._format}"
                )
        if self._highlight is not None:
            if not isinstance(self._highlight, bool):
                raise ValidationError(
                    "The parameter 'highlight' must be a boolean type value."
                )

    @property
    def aspects(self) -> List[Any]:
        """Get the aspects parameter value.

        Args:
            self: The decorator instance

        Returns:
            The aspects parameter value
        """
        return self._aspects

    @property
    def format(self) -> Literal["table", "prose", "bullets"]:
        """Get the format parameter value.

        Args:
            self: The decorator instance

        Returns:
            The format parameter value
        """
        return self._format

    @property
    def highlight(self) -> bool:
        """Get the highlight parameter value.

        Args:
            self: The decorator instance

        Returns:
            The highlight parameter value
        """
        return self._highlight

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "comparison",
            "parameters": {
                "aspects": self.aspects,
                "format": self.format,
                "highlight": self.highlight,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Args:
            self: The decorator instance

        Returns:
            String representation of the decorator
        """
        params = []
        if self.aspects is not None:
            params.append(f"aspects={self.aspects}")
        if self.format is not None:
            params.append(f"format={self.format}")
        if self.highlight is not None:
            params.append(f"highlight={self.highlight}")

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
            "description": """Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.""",
            "category": "general",
            "version": cls.version,
        }
