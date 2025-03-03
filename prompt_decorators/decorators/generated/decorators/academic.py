"""
Implementation of the Academic decorator.

This module provides the Academic decorator class for use in prompt engineering.

Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
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
        if self._style is not None:
            valid_values = ["humanities", "scientific", "legal"]
            if self._style not in valid_values:
                raise ValidationError("The parameter 'style' must be one of the following values: " + ", ".join(valid_values))

        if self._citationStyle is not None:
            valid_values = ["APA", "MLA", "Chicago", "Harvard", "IEEE"]
            if self._citationStyle not in valid_values:
                raise ValidationError("The parameter 'citationStyle' must be one of the following values: " + ", ".join(valid_values))


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
            "style": self.style,
            "citationStyle": self.citationStyle,
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