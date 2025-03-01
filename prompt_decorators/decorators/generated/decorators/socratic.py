"""
Socratic Decorator

Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Socratic(BaseDecorator):
    """Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding."""

    def __init__(
        self,
        iterations: Optional[float] = 3,
    ):
        """
        Initialize Socratic decorator.

        Args:
            iterations: Number of question-answer cycles to include
        """
        super().__init__(
            name="Socratic",
            version="1.0.0",
            parameters={
                "iterations": iterations,
            },
            metadata={
                "description": "Structures the response as a series of questions that guide the user through a problem or topic. This decorator encourages critical thinking through question-based exploration, helping to uncover assumptions and lead to deeper understanding.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def iterations(self) -> float:
        """Number of question-answer cycles to include"""
        return self.parameters.get("iterations")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.iterations is not None and self.iterations < 1:
            raise ValueError(f"iterations must be at least 1, got {self.iterations}")
        if self.iterations is not None and self.iterations > 5:
            raise ValueError(f"iterations must be at most 5, got {self.iterations}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response as a series of questions that guide the user through a problem or topic
        instruction = f"Instructions for {self.name} decorator: "
        if self.iterations is not None:
            instruction += f"iterations={self.iterations}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"