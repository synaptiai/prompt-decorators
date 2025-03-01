"""
ELI5 Decorator

Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class ELI5(BaseDecorator):
    """Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject."""

    def __init__(
        self,
        strictness: Optional[bool] = False,
    ):
        """
        Initialize ELI5 decorator.

        Args:
            strictness: Whether to strictly maintain a child-appropriate level of simplicity or allow slightly more complexity when necessary
        """
        super().__init__(
            name="ELI5",
            version="1.0.0",
            parameters={
                "strictness": strictness,
            },
            metadata={
                "description": "Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def strictness(self) -> bool:
        """Whether to strictly maintain a child-appropriate level of simplicity or allow slightly more complexity when necessary"""
        return self.parameters.get("strictness")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Adapts the response to explain a concept as if to a 5-year-old child
        instruction = f"Instructions for {self.name} decorator: "
        if self.strictness is not None:
            instruction += f"strictness={self.strictness}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"