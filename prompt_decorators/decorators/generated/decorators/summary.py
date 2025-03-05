"""Implementation of the Summary decorator.

This module provides the Summary decorator class for use in prompt engineering.

Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    SummaryLengthEnum,
    SummaryPositionEnum,
)


class Summary(BaseDecorator):
    """Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.

    Attributes:
        length: Relative length of the summary. (Literal["short", "medium", "long"])
        wordCount: Approximate target word count for the summary. (Any)
        position: Where to position the summary in relation to any full content. (Literal["beginning", "end", "standalone"])
    """

    name = "summary"  # Class-level name for serialization
    decorator_name = "summary"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please provide a condensed summary of the information in your"
        "response.",
        "parameterMapping": {
            "length": {
                "valueMap": {
                    "short": "Make the summary very concise (approximately 2-3 sentences) capturing only the most essential points.",
                    "medium": "Create a moderate-length summary that includes main ideas and key supporting details (approximately 1 paragraph).",
                    "long": "Provide a comprehensive summary that covers all significant points while still being more condensed than a full explanation (approximately 2-3 paragraphs).",
                },
            },
            "wordCount": {
                "format": "The summary should be approximately {value} words in length.",
            },
            "position": {
                "valueMap": {
                    "beginning": "Place the summary at the beginning of your response, before any detailed content.",
                    "end": "Place the summary at the end of your response, after providing the detailed content.",
                    "standalone": "Provide only the summary without additional detailed content.",
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
        length: Literal["short", "medium", "long"] = "medium",
        wordCount: Any = None,
        position: Literal["beginning", "end", "standalone"] = "standalone",
    ) -> None:
        """Initialize the Summary decorator.

        Args:
            length: Relative length of the summary
            wordCount: Approximate target word count for the summary
            position: Where to position the summary in relation to any full content


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._length = length
        self._wordCount = wordCount
        self._position = position

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._length = length
        self._wordCount = wordCount
        self._position = position

        # Validate parameters
        if self._length is not None:
            if not isinstance(self._length, str):
                raise ValidationError(
                    "The parameter 'length' must be a string type value."
                )
            if self._length not in ["short", "medium", "long"]:
                raise ValidationError(
                    f"The parameter 'length' must be one of the allowed enum values: ['short', 'medium', 'long']. Got {self._length}"
                )
        if self._wordCount is not None:
            if not isinstance(self._wordCount, (int, float)):
                raise ValidationError(
                    "The parameter 'wordCount' must be a numeric type value."
                )
            if self._wordCount < 10:
                raise ValidationError(
                    "The parameter 'wordCount' must be greater than or equal to 10."
                )
            if self._wordCount > 500:
                raise ValidationError(
                    "The parameter 'wordCount' must be less than or equal to 500."
                )
        if self._position is not None:
            if not isinstance(self._position, str):
                raise ValidationError(
                    "The parameter 'position' must be a string type value."
                )
            if self._position not in ["beginning", "end", "standalone"]:
                raise ValidationError(
                    f"The parameter 'position' must be one of the allowed enum values: ['beginning', 'end', 'standalone']. Got {self._position}"
                )

    @property
    def length(self) -> Literal["short", "medium", "long"]:
        """Get the length parameter value.

        Args:
            self: The decorator instance

        Returns:
            The length parameter value
        """
        return self._length

    @property
    def wordCount(self) -> Any:
        """Get the wordCount parameter value.

        Args:
            self: The decorator instance

        Returns:
            The wordCount parameter value
        """
        return self._wordCount

    @property
    def position(self) -> Literal["beginning", "end", "standalone"]:
        """Get the position parameter value.

        Args:
            self: The decorator instance

        Returns:
            The position parameter value
        """
        return self._position

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "summary",
            "parameters": {
                "length": self.length,
                "wordCount": self.wordCount,
                "position": self.position,
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
        if self.length is not None:
            params.append(f"length={self.length}")
        if self.wordCount is not None:
            params.append(f"wordCount={self.wordCount}")
        if self.position is not None:
            params.append(f"position={self.position}")

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
            "description": """Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.""",
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
