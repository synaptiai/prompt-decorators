"""Implementation of the Constraints decorator.

This module provides the Constraints decorator class for use in prompt engineering.

Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    ConstraintsVocabularyEnum,
)


class Constraints(BaseDecorator):
    """Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries.

    Attributes:
        wordCount: Maximum number of words allowed in the response. (Any)
        timeframe: Maximum time required to implement or consume the response (e.g., '5min', '1hr', '1week'). (str)
        vocabulary: Constraints on vocabulary usage. (Literal["simple", "technical", "domain-specific", "creative"])
        custom: Custom constraint to apply (e.g., 'no negatives', 'use only questions', 'each sentence starts with consecutive letters of the alphabet'). (str)
    """

    name = "constraints"  # Class-level name for serialization
    decorator_name = "constraints"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please craft your response within specific constraints that limit"
        "aspects of the output format, length, or content.",
        "parameterMapping": {
            "wordCount": {
                "format": "Limit your response to exactly {value} words. Count carefully to ensure you meet this constraint precisely.",
            },
            "timeframe": {
                "format": "Ensure your response describes solutions or content that could be implemented or consumed within a {value} timeframe.",
            },
            "vocabulary": {
                "valueMap": {
                    "simple": "Use only simple, everyday vocabulary that would be understood by elementary school students. Avoid jargon, technical terms, and complex words.",
                    "technical": "Use precise technical vocabulary appropriate to the subject matter, including field-specific terminology and concepts.",
                    "domain-specific": "Employ specialized vocabulary from the relevant domain or field, using terms of art and professional language.",
                    "creative": "Use varied, vivid, and evocative vocabulary that enhances engagement, including metaphors, sensory language, and uncommon word choices.",
                },
            },
            "custom": {
                "format": "Apply this additional custom constraint: {value}.",
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
        wordCount: Any = None,
        timeframe: str = None,
        vocabulary: Literal[
            "simple", "technical", "domain-specific", "creative"
        ] = None,
        custom: str = None,
    ) -> None:
        """Initialize the Constraints decorator.

        Args:
            wordCount: Maximum number of words allowed in the response
            timeframe: Maximum time required to implement or consume the response (e.g., '5min', '1hr', '1week')
            vocabulary: Constraints on vocabulary usage
            custom: Custom constraint to apply (e.g., 'no negatives', 'use only questions', 'each sentence starts with consecutive letters of the alphabet')


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
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._wordCount = wordCount
        self._timeframe = timeframe
        self._vocabulary = vocabulary
        self._custom = custom

        # Validate parameters
        if self._wordCount is not None:
            if not isinstance(self._wordCount, (int, float)):
                raise ValidationError(
                    "The parameter 'wordCount' must be a numeric type value."
                )
            if self._wordCount < 10:
                raise ValidationError(
                    "The parameter 'wordCount' must be greater than or equal to 10."
                )
            if self._wordCount > 1000:
                raise ValidationError(
                    "The parameter 'wordCount' must be less than or equal to 1000."
                )
        if self._timeframe is not None:
            if not isinstance(self._timeframe, str):
                raise ValidationError(
                    "The parameter 'timeframe' must be a string type value."
                )
        if self._vocabulary is not None:
            if not isinstance(self._vocabulary, str):
                raise ValidationError(
                    "The parameter 'vocabulary' must be a string type value."
                )
            if self._vocabulary not in [
                "simple",
                "technical",
                "domain-specific",
                "creative",
            ]:
                raise ValidationError(
                    f"The parameter 'vocabulary' must be one of the allowed enum values: ['simple', 'technical', 'domain-specific', 'creative']. Got {self._vocabulary}"
                )
        if self._custom is not None:
            if not isinstance(self._custom, str):
                raise ValidationError(
                    "The parameter 'custom' must be a string type value."
                )

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
    def timeframe(self) -> str:
        """Get the timeframe parameter value.

        Args:
            self: The decorator instance

        Returns:
            The timeframe parameter value
        """
        return self._timeframe

    @property
    def vocabulary(
        self,
    ) -> Literal["simple", "technical", "domain-specific", "creative"]:
        """Get the vocabulary parameter value.

        Args:
            self: The decorator instance

        Returns:
            The vocabulary parameter value
        """
        return self._vocabulary

    @property
    def custom(self) -> str:
        """Get the custom parameter value.

        Args:
            self: The decorator instance

        Returns:
            The custom parameter value
        """
        return self._custom

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "constraints",
            "parameters": {
                "wordCount": self.wordCount,
                "timeframe": self.timeframe,
                "vocabulary": self.vocabulary,
                "custom": self.custom,
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
            "description": """Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries.""",
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
