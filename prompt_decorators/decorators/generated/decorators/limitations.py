"""
Implementation of the Limitations decorator.

This module provides the Limitations decorator class for use in prompt engineering.

Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    LimitationsDetailEnum,
    LimitationsPositionEnum,
    LimitationsFocusEnum,
)


class Limitations(BaseDecorator):
    """
    Adds an explicit statement of limitations, caveats, or uncertainties
    related to the provided information. This decorator promotes
    intellectual honesty by acknowledging the boundaries of current
    knowledge, potential biases, or contextual constraints.

    Attributes:
        detail: The level of detail in the limitations statement
        position: Where to place the limitations statement in the response
        focus: The primary aspect to focus on in the limitations
    """

    decorator_name = "limitations"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        detail: Literal["brief", "moderate", "comprehensive"] = "moderate",
        position: Literal["beginning", "end"] = "end",
        focus: Literal["knowledge", "methodology", "context", "biases", "all"] = "all",
    ) -> None:
        """
        Initialize the Limitations decorator.

        Args:
            detail: The level of detail in the limitations statement
            position: Where to place the limitations statement in the response
            focus: The primary aspect to focus on in the limitations

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._detail = detail
        self._position = position
        self._focus = focus

        # Validate parameters
        if self._detail is not None:
            valid_values = ["brief", "moderate", "comprehensive"]
            if self._detail not in valid_values:
                raise ValidationError("The parameter 'detail' must be one of the following values: " + ", ".join(valid_values))

        if self._position is not None:
            valid_values = ["beginning", "end"]
            if self._position not in valid_values:
                raise ValidationError("The parameter 'position' must be one of the following values: " + ", ".join(valid_values))

        if self._focus is not None:
            valid_values = ["knowledge", "methodology", "context", "biases", "all"]
            if self._focus not in valid_values:
                raise ValidationError("The parameter 'focus' must be one of the following values: " + ", ".join(valid_values))


    @property
    def detail(self) -> Literal["brief", "moderate", "comprehensive"]:
        """
        Get the detail parameter value.

        Args:
            self: The decorator instance

        Returns:
            The detail parameter value
        """
        return self._detail

    @property
    def position(self) -> Literal["beginning", "end"]:
        """
        Get the position parameter value.

        Args:
            self: The decorator instance

        Returns:
            The position parameter value
        """
        return self._position

    @property
    def focus(self) -> Literal["knowledge", "methodology", "context", "biases", "all"]:
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
            "name": "limitations",
            "detail": self.detail,
            "position": self.position,
            "focus": self.focus,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.detail is not None:
            params.append(f"detail={self.detail}")
        if self.position is not None:
            params.append(f"position={self.position}")
        if self.focus is not None:
            params.append(f"focus={self.focus}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"