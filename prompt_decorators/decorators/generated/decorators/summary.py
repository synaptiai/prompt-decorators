"""
Summary Decorator

Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import SummaryLengthEnum, SummaryPositionEnum


class Summary(BaseDecorator):
    """Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics."""

    def __init__(
        self,
        length: Optional[SummaryLengthEnum] = SummaryLengthEnum.MEDIUM,
        wordCount: Optional[float] = None,
        position: Optional[SummaryPositionEnum] = SummaryPositionEnum.STANDALONE,
    ):
        """
        Initialize Summary decorator.

        Args:
            length: Relative length of the summary
            wordCount: Approximate target word count for the summary
            position: Where to position the summary in relation to any full content
        """
        super().__init__(
            name="Summary",
            version="1.0.0",
            parameters={
                "length": length,
                "wordCount": wordCount,
                "position": position,
            },
            metadata={
                "description": "Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def length(self) -> SummaryLengthEnum:
        """Relative length of the summary"""
        return self.parameters.get("length")

    @property
    def wordCount(self) -> float:
        """Approximate target word count for the summary"""
        return self.parameters.get("wordCount")

    @property
    def position(self) -> SummaryPositionEnum:
        """Where to position the summary in relation to any full content"""
        return self.parameters.get("position")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.wordCount is not None and self.wordCount < 10:
            raise ValueError(f"wordCount must be at least 10, got {self.wordCount}")
        if self.wordCount is not None and self.wordCount > 500:
            raise ValueError(f"wordCount must be at most 500, got {self.wordCount}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Provides a condensed summary of information that would otherwise be presented in a more detailed format
        instruction = f"Instructions for {self.name} decorator: "
        if self.length is not None:
            instruction += f"length={self.length}, "
        if self.wordCount is not None:
            instruction += f"wordCount={self.wordCount}, "
        if self.position is not None:
            instruction += f"position={self.position}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"