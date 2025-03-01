"""
NegativeSpace Decorator

Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import NegativeSpaceFocusEnum, NegativeSpaceDepthEnum, NegativeSpaceStructureEnum


class NegativeSpace(BaseDecorator):
    """Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked."""

    def __init__(
        self,
        focus: Optional[NegativeSpaceFocusEnum] = NegativeSpaceFocusEnum.COMPREHENSIVE,
        depth: Optional[NegativeSpaceDepthEnum] = NegativeSpaceDepthEnum.MODERATE,
        structure: Optional[NegativeSpaceStructureEnum] = NegativeSpaceStructureEnum.INTEGRATED,
    ):
        """
        Initialize NegativeSpace decorator.

        Args:
            focus: The specific aspect of negative space to emphasize
            depth: How deeply to explore the negative space
            structure: How to present the negative space analysis
        """
        super().__init__(
            name="NegativeSpace",
            version="1.0.0",
            parameters={
                "focus": focus,
                "depth": depth,
                "structure": structure,
            },
            metadata={
                "description": "Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def focus(self) -> NegativeSpaceFocusEnum:
        """The specific aspect of negative space to emphasize"""
        return self.parameters.get("focus")

    @property
    def depth(self) -> NegativeSpaceDepthEnum:
        """How deeply to explore the negative space"""
        return self.parameters.get("depth")

    @property
    def structure(self) -> NegativeSpaceStructureEnum:
        """How to present the negative space analysis"""
        return self.parameters.get("structure")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question
        instruction = f"Instructions for {self.name} decorator: "
        if self.focus is not None:
            instruction += f"focus={self.focus}, "
        if self.depth is not None:
            instruction += f"depth={self.depth}, "
        if self.structure is not None:
            instruction += f"structure={self.structure}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"