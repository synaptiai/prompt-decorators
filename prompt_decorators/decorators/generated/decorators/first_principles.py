"""
FirstPrinciples Decorator

Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class FirstPrinciples(BaseDecorator):
    """Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas."""

    def __init__(
        self,
        depth: Optional[float] = 3,
    ):
        """
        Initialize FirstPrinciples decorator.

        Args:
            depth: Level of detail in breaking down to fundamental principles
        """
        super().__init__(
            name="FirstPrinciples",
            version="1.0.0",
            parameters={
                "depth": depth,
            },
            metadata={
                "description": "Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def depth(self) -> float:
        """Level of detail in breaking down to fundamental principles"""
        return self.parameters.get("depth")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.depth is not None and self.depth < 1:
            raise ValueError(f"depth must be at least 1, got {self.depth}")
        if self.depth is not None and self.depth > 5:
            raise ValueError(f"depth must be at most 5, got {self.depth}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there
        instruction = f"Instructions for {self.name} decorator: "
        if self.depth is not None:
            instruction += f"depth={self.depth}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"