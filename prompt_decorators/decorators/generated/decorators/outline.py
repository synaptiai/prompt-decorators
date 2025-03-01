"""
Outline Decorator

Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import OutlineStyleEnum


class Outline(BaseDecorator):
    """Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics."""

    def __init__(
        self,
        depth: Optional[float] = 3,
        style: Optional[OutlineStyleEnum] = OutlineStyleEnum.NUMERIC,
        detailed: Optional[bool] = False,
    ):
        """
        Initialize Outline decorator.

        Args:
            depth: Maximum nesting level of the outline
            style: Numbering or bullet style for the outline
            detailed: Whether to include brief explanations under each outline point
        """
        super().__init__(
            name="Outline",
            version="1.0.0",
            parameters={
                "depth": depth,
                "style": style,
                "detailed": detailed,
            },
            metadata={
                "description": "Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def depth(self) -> float:
        """Maximum nesting level of the outline"""
        return self.parameters.get("depth")

    @property
    def style(self) -> OutlineStyleEnum:
        """Numbering or bullet style for the outline"""
        return self.parameters.get("style")

    @property
    def detailed(self) -> bool:
        """Whether to include brief explanations under each outline point"""
        return self.parameters.get("detailed")

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
        # Apply the decorator: Structures the response as a hierarchical outline with headings and subheadings
        instruction = f"Instructions for {self.name} decorator: "
        if self.depth is not None:
            instruction += f"depth={self.depth}, "
        if self.style is not None:
            instruction += f"style={self.style}, "
        if self.detailed is not None:
            instruction += f"detailed={self.detailed}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"