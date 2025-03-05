"""Implementation of the Concise decorator.

This module provides the Concise decorator class for use in prompt engineering.

Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import ConciseLevelEnum


class Concise(BaseDecorator):
    """Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited.

    Attributes:
        maxWords: Maximum word count for the entire response. (Any)
        bulletPoints: Whether to use bullet points for maximum brevity. (bool)
        level: The degree of conciseness to apply. (Literal["moderate", "high", "extreme"])
    """

    name = "concise"  # Class-level name for serialization
    decorator_name = "concise"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please provide a concise, to-the-point response without unnecessary"
        "details or verbose language.",
        "parameterMapping": {
            "maxWords": {
                "format": "Limit your entire response to no more than {value} words.",
            },
            "bulletPoints": {
                "valueMap": {
                    "true": "Use bullet points to present information in the most concise format possible.",
                    "false": "Use concise paragraphs rather than bullet points.",
                },
            },
            "level": {
                "valueMap": {
                    "moderate": "Focus on the most important information while maintaining readability and essential context.",
                    "high": "Include only key points and critical information, eliminating all non-essential details.",
                    "extreme": "Provide only the absolute minimum information required to answer the question - be as brief as possible.",
                },
            },
        },
        "placement": "prepend",
        "compositionBehavior": "accumulate",
    }

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
        maxWords: Any = None,
        bulletPoints: bool = False,
        level: Literal["moderate", "high", "extreme"] = "moderate",
    ) -> None:
        """Initialize the Concise decorator.

        Args:
            maxWords: Maximum word count for the entire response
            bulletPoints: Whether to use bullet points for maximum brevity
            level: The degree of conciseness to apply


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._maxWords = maxWords
        self._bulletPoints = bulletPoints
        self._level = level

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._maxWords = maxWords
        self._bulletPoints = bulletPoints
        self._level = level

        # Validate parameters
        if self._maxWords is not None:
            if not isinstance(self._maxWords, (int, float)):
                raise ValidationError(
                    "The parameter 'maxWords' must be a numeric type value."
                )
            if self._maxWords < 10:
                raise ValidationError(
                    "The parameter 'maxWords' must be greater than or equal to 10."
                )
            if self._maxWords > 500:
                raise ValidationError(
                    "The parameter 'maxWords' must be less than or equal to 500."
                )
        if self._bulletPoints is not None:
            if not isinstance(self._bulletPoints, bool):
                raise ValidationError(
                    "The parameter 'bulletPoints' must be a boolean type value."
                )
        if self._level is not None:
            if not isinstance(self._level, str):
                raise ValidationError(
                    "The parameter 'level' must be a string type value."
                )
            if self._level not in ["moderate", "high", "extreme"]:
                raise ValidationError(
                    f"The parameter 'level' must be one of the allowed enum values: ['moderate', 'high', 'extreme']. Got {self._level}"
                )

    @property
    def maxWords(self) -> Any:
        """Get the maxWords parameter value.

        Args:
            self: The decorator instance

        Returns:
            The maxWords parameter value
        """
        return self._maxWords

    @property
    def bulletPoints(self) -> bool:
        """Get the bulletPoints parameter value.

        Args:
            self: The decorator instance

        Returns:
            The bulletPoints parameter value
        """
        return self._bulletPoints

    @property
    def level(self) -> Literal["moderate", "high", "extreme"]:
        """Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "concise",
            "parameters": {
                "maxWords": self.maxWords,
                "bulletPoints": self.bulletPoints,
                "level": self.level,
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
        if self.maxWords is not None:
            params.append(f"maxWords={self.maxWords}")
        if self.bulletPoints is not None:
            params.append(f"bulletPoints={self.bulletPoints}")
        if self.level is not None:
            params.append(f"level={self.level}")

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
            "description": """Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited.""",
            "category": "general",
            "version": cls.version,
        }

    def apply_to_prompt(self, prompt: str) -> str:
        """Apply the decorator to a prompt.

        This method transforms the prompt using the transformation template.

        Args:
            prompt: The prompt to decorate

        Returns:
            The decorated prompt

        """
        # Use the apply_to_prompt implementation from BaseDecorator
        return super().apply_to_prompt(prompt)
