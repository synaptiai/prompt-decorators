"""
Reasoning Decorator

Modifies the AI's response to provide explicit reasoning paths before reaching conclusions. This decorator encourages the model to show its thought process, making responses more transparent and trustworthy.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import ReasoningDepthEnum


class Reasoning(BaseDecorator):
    """Modifies the AI's response to provide explicit reasoning paths before reaching conclusions. This decorator encourages the model to show its thought process, making responses more transparent and trustworthy."""

    def __init__(
        self,
        depth: Optional[ReasoningDepthEnum] = ReasoningDepthEnum.MODERATE,
    ):
        """
        Initialize Reasoning decorator.

        Args:
            depth: The level of detail in the reasoning process
        """
        super().__init__(
            name="Reasoning",
            version="1.0.0",
            parameters={
                "depth": depth,
            },
            metadata={
                "description": "Modifies the AI's response to provide explicit reasoning paths before reaching conclusions. This decorator encourages the model to show its thought process, making responses more transparent and trustworthy.",
                "author": "Prompt Decorators Working Group",
                "category": "minimal",
            },
        )

    @property
    def depth(self) -> ReasoningDepthEnum:
        """The level of detail in the reasoning process"""
        return self.parameters.get("depth")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Modifies the AI's response to provide explicit reasoning paths before reaching conclusions
        instruction = f"Instructions for {self.name} decorator: "
        if self.depth is not None:
            instruction += f"depth={self.depth}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"