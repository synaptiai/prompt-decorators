"""
Concise Decorator

Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import ConciseLevelEnum


class Concise(BaseDecorator):
    """Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited."""

    def __init__(
        self,
        maxWords: Optional[float] = None,
        bulletPoints: Optional[bool] = False,
        level: Optional[ConciseLevelEnum] = ConciseLevelEnum.MODERATE,
    ):
        """
        Initialize Concise decorator.

        Args:
            maxWords: Maximum word count for the entire response
            bulletPoints: Whether to use bullet points for maximum brevity
            level: The degree of conciseness to apply
        """
        super().__init__(
            name="Concise",
            version="1.0.0",
            parameters={
                "maxWords": maxWords,
                "bulletPoints": bulletPoints,
                "level": level,
            },
            metadata={
                "description": "Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def maxWords(self) -> float:
        """Maximum word count for the entire response"""
        return self.parameters.get("maxWords")

    @property
    def bulletPoints(self) -> bool:
        """Whether to use bullet points for maximum brevity"""
        return self.parameters.get("bulletPoints")

    @property
    def level(self) -> ConciseLevelEnum:
        """The degree of conciseness to apply"""
        return self.parameters.get("level")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.maxWords is not None and self.maxWords < 10:
            raise ValueError(f"maxWords must be at least 10, got {self.maxWords}")
        if self.maxWords is not None and self.maxWords > 500:
            raise ValueError(f"maxWords must be at most 500, got {self.maxWords}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language
        instruction = f"Instructions for {self.name} decorator: "
        if self.maxWords is not None:
            instruction += f"maxWords={self.maxWords}, "
        if self.bulletPoints is not None:
            instruction += f"bulletPoints={self.bulletPoints}, "
        if self.level is not None:
            instruction += f"level={self.level}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"