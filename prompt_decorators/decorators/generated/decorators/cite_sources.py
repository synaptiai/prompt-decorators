"""
Implementation of the CiteSources decorator.

This module provides the CiteSources decorator class for use in prompt engineering.

Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
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
        if self._style is not None:
            valid_values = ["inline", "footnote", "endnote"]
            if self._style not in valid_values:
                raise ValidationError("The parameter 'style' must be one of the following values: " + ", ".join(valid_values))

        if self._format is not None:
            valid_values = ["APA", "MLA", "Chicago", "Harvard", "IEEE"]
            if self._format not in valid_values:
                raise ValidationError("The parameter 'format' must be one of the following values: " + ", ".join(valid_values))

        if self._comprehensive is not None:
            if not isinstance(self._comprehensive, bool):
                raise ValidationError("The parameter 'comprehensive' must be a boolean value.")


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
            "style": self.style,
            "format": self.format,
            "comprehensive": self.comprehensive,
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