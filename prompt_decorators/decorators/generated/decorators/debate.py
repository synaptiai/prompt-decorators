"""
Debate Decorator

Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Debate(BaseDecorator):
    """Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles."""

    def __init__(
        self,
        perspectives: Optional[float] = 2,
        balanced: Optional[bool] = True,
    ):
        """
        Initialize Debate decorator.

        Args:
            perspectives: Number of different perspectives to include in the debate
            balanced: Whether to ensure equal representation and strength of arguments for each perspective
        """
        super().__init__(
            name="Debate",
            version="1.0.0",
            parameters={
                "perspectives": perspectives,
                "balanced": balanced,
            },
            metadata={
                "description": "Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def perspectives(self) -> float:
        """Number of different perspectives to include in the debate"""
        return self.parameters.get("perspectives")

    @property
    def balanced(self) -> bool:
        """Whether to ensure equal representation and strength of arguments for each perspective"""
        return self.parameters.get("balanced")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.perspectives is not None and self.perspectives < 2:
            raise ValueError(f"perspectives must be at least 2, got {self.perspectives}")
        if self.perspectives is not None and self.perspectives > 5:
            raise ValueError(f"perspectives must be at most 5, got {self.perspectives}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response as a debate between multiple perspectives on a topic
        instruction = f"Instructions for {self.name} decorator: "
        if self.perspectives is not None:
            instruction += f"perspectives={self.perspectives}, "
        if self.balanced is not None:
            instruction += f"balanced={self.balanced}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"