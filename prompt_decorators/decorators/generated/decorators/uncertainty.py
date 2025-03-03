"""
Implementation of the Uncertainty decorator.

This module provides the Uncertainty decorator class for use in prompt engineering.

Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    UncertaintyFormatEnum,
    UncertaintyThresholdEnum,
)


class Uncertainty(BaseDecorator):
    """
    Explicitly highlights areas of uncertainty in the response. This
    decorator promotes intellectual honesty by clearly indicating what is
    known with confidence versus what is speculative, unknown, or subject
    to debate.

    Attributes:
        format: How to format uncertainty indications in the response
        threshold: The threshold for flagging uncertain content
        reason: Whether to explain the reason for uncertainty
    """

    decorator_name = "uncertainty"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        format: Literal["inline", "section", "confidence"] = "inline",
        threshold: Literal["low", "medium", "high"] = "medium",
        reason: bool = False,
    ) -> None:
        """
        Initialize the Uncertainty decorator.

        Args:
            format: How to format uncertainty indications in the response
            threshold: The threshold for flagging uncertain content
            reason: Whether to explain the reason for uncertainty

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._format = format
        self._threshold = threshold
        self._reason = reason

        # Validate parameters
        if self._format is not None:
            valid_values = ["inline", "section", "confidence"]
            if self._format not in valid_values:
                raise ValidationError("The parameter 'format' must be one of the following values: " + ", ".join(valid_values))

        if self._threshold is not None:
            valid_values = ["low", "medium", "high"]
            if self._threshold not in valid_values:
                raise ValidationError("The parameter 'threshold' must be one of the following values: " + ", ".join(valid_values))

        if self._reason is not None:
            if not isinstance(self._reason, bool):
                raise ValidationError("The parameter 'reason' must be a boolean value.")


    @property
    def format(self) -> Literal["inline", "section", "confidence"]:
        """
        Get the format parameter value.

        Args:
            self: The decorator instance

        Returns:
            The format parameter value
        """
        return self._format

    @property
    def threshold(self) -> Literal["low", "medium", "high"]:
        """
        Get the threshold parameter value.

        Args:
            self: The decorator instance

        Returns:
            The threshold parameter value
        """
        return self._threshold

    @property
    def reason(self) -> bool:
        """
        Get the reason parameter value.

        Args:
            self: The decorator instance

        Returns:
            The reason parameter value
        """
        return self._reason

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "uncertainty",
            "format": self.format,
            "threshold": self.threshold,
            "reason": self.reason,
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
        if self.threshold is not None:
            params.append(f"threshold={self.threshold}")
        if self.reason is not None:
            params.append(f"reason={self.reason}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"