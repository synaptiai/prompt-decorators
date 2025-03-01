"""
Constraints Decorator

Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import ConstraintsVocabularyEnum


class Constraints(BaseDecorator):
    """Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries."""

    def __init__(
        self,
        wordCount: Optional[float] = None,
        timeframe: Optional[str] = None,
        vocabulary: Optional[ConstraintsVocabularyEnum] = None,
        custom: Optional[str] = None,
    ):
        """
        Initialize Constraints decorator.

        Args:
            wordCount: Maximum number of words allowed in the response
            timeframe: Maximum time required to implement or consume the response (e.g., '5min', '1hr', '1week')
            vocabulary: Constraints on vocabulary usage
            custom: Custom constraint to apply (e.g., 'no negatives', 'use only questions', 'each sentence starts with consecutive letters of the alphabet')
        """
        super().__init__(
            name="Constraints",
            version="1.0.0",
            parameters={
                "wordCount": wordCount,
                "timeframe": timeframe,
                "vocabulary": vocabulary,
                "custom": custom,
            },
            metadata={
                "description": "Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def wordCount(self) -> float:
        """Maximum number of words allowed in the response"""
        return self.parameters.get("wordCount")

    @property
    def timeframe(self) -> str:
        """Maximum time required to implement or consume the response (e.g., '5min', '1hr', '1week')"""
        return self.parameters.get("timeframe")

    @property
    def vocabulary(self) -> ConstraintsVocabularyEnum:
        """Constraints on vocabulary usage"""
        return self.parameters.get("vocabulary")

    @property
    def custom(self) -> str:
        """Custom constraint to apply (e.g., 'no negatives', 'use only questions', 'each sentence starts with consecutive letters of the alphabet')"""
        return self.parameters.get("custom")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.wordCount is not None and self.wordCount < 10:
            raise ValueError(f"wordCount must be at least 10, got {self.wordCount}")
        if self.wordCount is not None and self.wordCount > 1000:
            raise ValueError(f"wordCount must be at most 1000, got {self.wordCount}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Applies specific limitations to the output format, length, or content
        instruction = f"Instructions for {self.name} decorator: "
        if self.wordCount is not None:
            instruction += f"wordCount={self.wordCount}, "
        if self.timeframe is not None:
            instruction += f"timeframe={self.timeframe}, "
        if self.vocabulary is not None:
            instruction += f"vocabulary={self.vocabulary}, "
        if self.custom is not None:
            instruction += f"custom={self.custom}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"