"""Implementation of the FactCheck decorator.

This module provides the FactCheck decorator class for use in prompt engineering.

Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    FactCheckStrictnessEnum,
    FactCheckUncertainEnum,
)


class FactCheck(BaseDecorator):
    """Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.

    Attributes:
        confidence: Whether to include explicit confidence levels for claims. (bool)
        uncertain: How to handle uncertain information. (Literal["mark", "exclude", "qualify"])
        strictness: The threshold for considering information verified. (Literal["low", "moderate", "high"])
    """

    name = "fact_check"  # Class-level name for serialization
    decorator_name = "fact_check"
    version = "1.0.0"  # Initial version

    @property
    def name(self) -> str:
        """Get the name of the decorator.

        Args:
            self: The decorator instance


        Returns:
            The name of the decorator

        """
        return self.decorator_name

    def __init__(
        self,
        confidence: bool = True,
        uncertain: Literal["mark", "exclude", "qualify"] = "mark",
        strictness: Literal["low", "moderate", "high"] = "moderate",
    ) -> None:
        """Initialize the FactCheck decorator.

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
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._confidence = confidence
        self._uncertain = uncertain
        self._strictness = strictness

        # Validate parameters
        if self._confidence is not None:
            if not isinstance(self._confidence, bool):
                raise ValidationError(
                    "The parameter 'confidence' must be a boolean type value."
                )
        if self._uncertain is not None:
            if not isinstance(self._uncertain, str):
                raise ValidationError(
                    "The parameter 'uncertain' must be a string type value."
                )
            if self._uncertain not in ["mark", "exclude", "qualify"]:
                raise ValidationError(
                    f"The parameter 'uncertain' must be one of the allowed enum values: ['mark', 'exclude', 'qualify']. Got {self._uncertain}"
                )
        if self._strictness is not None:
            if not isinstance(self._strictness, str):
                raise ValidationError(
                    "The parameter 'strictness' must be a string type value."
                )
            if self._strictness not in ["low", "moderate", "high"]:
                raise ValidationError(
                    f"The parameter 'strictness' must be one of the allowed enum values: ['low', 'moderate', 'high']. Got {self._strictness}"
                )

    @property
    def confidence(self) -> bool:
        """Get the confidence parameter value.

        Args:
            self: The decorator instance

        Returns:
            The confidence parameter value
        """
        return self._confidence

    @property
    def uncertain(self) -> Literal["mark", "exclude", "qualify"]:
        """Get the uncertain parameter value.

        Args:
            self: The decorator instance

        Returns:
            The uncertain parameter value
        """
        return self._uncertain

    @property
    def strictness(self) -> Literal["low", "moderate", "high"]:
        """Get the strictness parameter value.

        Args:
            self: The decorator instance

        Returns:
            The strictness parameter value
        """
        return self._strictness

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "fact_check",
            "parameters": {
                "confidence": self.confidence,
                "uncertain": self.uncertain,
                "strictness": self.strictness,
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


        Args:
            cls: The decorator class

        """
        return {
            "name": cls.__name__,
            "description": """Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.""",
            "category": "general",
            "version": cls.version,
        }
