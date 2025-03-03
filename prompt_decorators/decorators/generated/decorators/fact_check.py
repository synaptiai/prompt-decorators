"""
Implementation of the FactCheck decorator.

This module provides the FactCheck decorator class for use in prompt engineering.

Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    FactCheckUncertainEnum,
    FactCheckStrictnessEnum,
)


class FactCheck(BaseDecorator):
    """
    Enhances the response with verification of factual claims and explicit
    indication of confidence levels. This decorator promotes accuracy by
    distinguishing between well-established facts, likely facts, and
    uncertain or speculative information.

    Attributes:
        confidence: Whether to include explicit confidence levels for claims
        uncertain: How to handle uncertain information
        strictness: The threshold for considering information verified
    """

    decorator_name = "fact_check"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        confidence: bool = True,
        uncertain: Literal["mark", "exclude", "qualify"] = "mark",
        strictness: Literal["low", "moderate", "high"] = "moderate",
    ) -> None:
        """
        Initialize the FactCheck decorator.

        Args:
            confidence: Whether to include explicit confidence levels for claims
            uncertain: How to handle uncertain information
            strictness: The threshold for considering information verified

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._confidence = confidence
        self._uncertain = uncertain
        self._strictness = strictness

        # Validate parameters
        if self._confidence is not None:
            if not isinstance(self._confidence, bool):
                raise ValidationError("The parameter 'confidence' must be a boolean value.")

        if self._uncertain is not None:
            valid_values = ["mark", "exclude", "qualify"]
            if self._uncertain not in valid_values:
                raise ValidationError("The parameter 'uncertain' must be one of the following values: " + ", ".join(valid_values))

        if self._strictness is not None:
            valid_values = ["low", "moderate", "high"]
            if self._strictness not in valid_values:
                raise ValidationError("The parameter 'strictness' must be one of the following values: " + ", ".join(valid_values))


    @property
    def confidence(self) -> bool:
        """
        Get the confidence parameter value.

        Args:
            self: The decorator instance

        Returns:
            The confidence parameter value
        """
        return self._confidence

    @property
    def uncertain(self) -> Literal["mark", "exclude", "qualify"]:
        """
        Get the uncertain parameter value.

        Args:
            self: The decorator instance

        Returns:
            The uncertain parameter value
        """
        return self._uncertain

    @property
    def strictness(self) -> Literal["low", "moderate", "high"]:
        """
        Get the strictness parameter value.

        Args:
            self: The decorator instance

        Returns:
            The strictness parameter value
        """
        return self._strictness

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "fact_check",
            "confidence": self.confidence,
            "uncertain": self.uncertain,
            "strictness": self.strictness,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.confidence is not None:
            params.append(f"confidence={self.confidence}")
        if self.uncertain is not None:
            params.append(f"uncertain={self.uncertain}")
        if self.strictness is not None:
            params.append(f"strictness={self.strictness}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"