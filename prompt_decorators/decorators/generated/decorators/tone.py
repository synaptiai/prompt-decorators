"""
Implementation of the Tone decorator.

This module provides the Tone decorator class for use in prompt engineering.

Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    ToneStyleEnum,
)


class Tone(BaseDecorator):
    """
    Adjusts the writing style and tone of the AI's response. This
    decorator helps ensure that responses are appropriately styled for
    different audiences and contexts, from formal technical documentation
    to casual explanations.

    Attributes:
        style: The desired tone and style for the response
    """

    decorator_name = "tone"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        style: Literal["formal", "casual", "friendly", "technical", "humorous"],
    ) -> None:
        """
        Initialize the Tone decorator.

        Args:
            style: The desired tone and style for the response

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._style = style

        # Validate parameters
        if self._style is None:
            raise ValidationError("The parameter 'style' is required for Tone decorator.")

        if self._style is not None:
            valid_values = ["formal", "casual", "friendly", "technical", "humorous"]
            if self._style not in valid_values:
                raise ValidationError("The parameter 'style' must be one of the following values: " + ", ".join(valid_values))


    @property
    def style(self) -> Literal["formal", "casual", "friendly", "technical", "humorous"]:
        """
        Get the style parameter value.

        Args:
            self: The decorator instance

        Returns:
            The style parameter value
        """
        return self._style

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "tone",
            "style": self.style,
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

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"