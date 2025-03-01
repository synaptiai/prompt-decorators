"""
Nested Decorator

Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import NestedStyleEnum


class Nested(BaseDecorator):
    """Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns."""

    def __init__(
        self,
        depth: Optional[float] = 3,
        style: Optional[NestedStyleEnum] = NestedStyleEnum.MIXED,
        collapsible: Optional[bool] = False,
    ):
        """
        Initialize Nested decorator.

        Args:
            depth: Maximum nesting level of the hierarchy
            style: Visual style for hierarchical levels
            collapsible: Whether to suggest the hierarchy could be rendered as collapsible sections (for UI implementations)
        """
        super().__init__(
            name="Nested",
            version="1.0.0",
            parameters={
                "depth": depth,
                "style": style,
                "collapsible": collapsible,
            },
            metadata={
                "description": "Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def depth(self) -> float:
        """Maximum nesting level of the hierarchy"""
        return self.parameters.get("depth")

    @property
    def style(self) -> NestedStyleEnum:
        """Visual style for hierarchical levels"""
        return self.parameters.get("style")

    @property
    def collapsible(self) -> bool:
        """Whether to suggest the hierarchy could be rendered as collapsible sections (for UI implementations)"""
        return self.parameters.get("collapsible")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.depth is not None and self.depth < 2:
            raise ValueError(f"depth must be at least 2, got {self.depth}")
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
        # Apply the decorator: Organizes information in a deeply hierarchical structure with multiple levels of nesting
        instruction = f"Instructions for {self.name} decorator: "
        if self.depth is not None:
            instruction += f"depth={self.depth}, "
        if self.style is not None:
            instruction += f"style={self.style}, "
        if self.collapsible is not None:
            instruction += f"collapsible={self.collapsible}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"