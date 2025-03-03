"""
Implementation of the Constraints decorator.

This module provides the Constraints decorator class for use in prompt engineering.

Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    ConstraintsVocabularyEnum,
)


class Constraints(BaseDecorator):
    """
    Applies specific limitations to the output format, length, or content.
    This decorator enforces creative constraints that can enhance focus,
    brevity, or precision by requiring the response to work within defined
    boundaries.

    Attributes:
        wordCount: Maximum number of words allowed in the response
        timeframe: Maximum time required to implement or consume the response (e.g., '5min', '1hr', '1week')
        vocabulary: Constraints on vocabulary usage
        custom: Custom constraint to apply (e.g., 'no negatives', 'use only questions', 'each sentence starts with consecutive letters of the alphabet')
    """

    decorator_name = "constraints"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        wordCount: Any = None,
        timeframe: str = None,
        vocabulary: Literal["simple", "technical", "domain-specific", "creative"] = None,
        custom: str = None,
    ) -> None:
        """
        Initialize the Constraints decorator.

        Args:
            wordCount: Maximum number of words allowed in the response
            timeframe: Maximum time required to implement or consume the response
                (e.g., '5min', '1hr', '1week')
            vocabulary: Constraints on vocabulary usage
            custom: Custom constraint to apply (e.g., 'no negatives', 'use only
                questions', 'each sentence starts with consecutive letters
                of the alphabet')

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._wordCount = wordCount
        self._timeframe = timeframe
        self._vocabulary = vocabulary
        self._custom = custom

        # Validate parameters
        if self._wordCount is not None:
            if not isinstance(self._wordCount, (int, float)) or isinstance(self._wordCount, bool):
                raise ValidationError("The parameter 'wordCount' must be a numeric value.")

        if self._timeframe is not None:
            if not isinstance(self._timeframe, str):
                raise ValidationError("The parameter 'timeframe' must be a string value.")

        if self._vocabulary is not None:
            valid_values = ["simple", "technical", "domain-specific", "creative"]
            if self._vocabulary not in valid_values:
                raise ValidationError("The parameter 'vocabulary' must be one of the following values: " + ", ".join(valid_values))

        if self._custom is not None:
            if not isinstance(self._custom, str):
                raise ValidationError("The parameter 'custom' must be a string value.")


    @property
    def wordCount(self) -> Any:
        """
        Get the wordCount parameter value.

        Args:
            self: The decorator instance

        Returns:
            The wordCount parameter value
        """
        return self._wordCount

    @property
    def timeframe(self) -> str:
        """
        Get the timeframe parameter value.

        Args:
            self: The decorator instance

        Returns:
            The timeframe parameter value
        """
        return self._timeframe

    @property
    def vocabulary(self) -> Literal["simple", "technical", "domain-specific", "creative"]:
        """
        Get the vocabulary parameter value.

        Args:
            self: The decorator instance

        Returns:
            The vocabulary parameter value
        """
        return self._vocabulary

    @property
    def custom(self) -> str:
        """
        Get the custom parameter value.

        Args:
            self: The decorator instance

        Returns:
            The custom parameter value
        """
        return self._custom

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "constraints",
            "wordCount": self.wordCount,
            "timeframe": self.timeframe,
            "vocabulary": self.vocabulary,
            "custom": self.custom,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.wordCount is not None:
            params.append(f"wordCount={self.wordCount}")
        if self.timeframe is not None:
            params.append(f"timeframe={self.timeframe}")
        if self.vocabulary is not None:
            params.append(f"vocabulary={self.vocabulary}")
        if self.custom is not None:
            params.append(f"custom={self.custom}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"