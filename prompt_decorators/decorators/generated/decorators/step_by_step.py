"""
StepByStep Decorator

Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class StepByStep(BaseDecorator):
    """Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding."""

    def __init__(
        self,
        numbered: Optional[bool] = True,
    ):
        """
        Initialize StepByStep decorator.

        Args:
            numbered: Whether to number the steps or use bullet points
        """
        super().__init__(
            name="StepByStep",
            version="1.0.0",
            parameters={
                "numbered": numbered,
            },
            metadata={
                "description": "Structures the AI's response as a sequence of clearly labeled steps. This decorator helps break down complex processes, explanations, or solutions into manageable, sequential parts for better understanding.",
                "author": "Prompt Decorators Working Group",
                "category": "minimal",
            },
        )

    @property
    def numbered(self) -> bool:
        """Whether to number the steps or use bullet points"""
        return self.parameters.get("numbered")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the AI's response as a sequence of clearly labeled steps
        instruction = f"Instructions for {self.name} decorator: "
        if self.numbered is not None:
            instruction += f"numbered={self.numbered}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"