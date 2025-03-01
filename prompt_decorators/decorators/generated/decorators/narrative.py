"""
Narrative Decorator

Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import NarrativeStructureEnum, NarrativeLengthEnum


class Narrative(BaseDecorator):
    """Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich."""

    def __init__(
        self,
        structure: Optional[NarrativeStructureEnum] = NarrativeStructureEnum.CLASSIC,
        characters: Optional[bool] = True,
        length: Optional[NarrativeLengthEnum] = NarrativeLengthEnum.MODERATE,
    ):
        """
        Initialize Narrative decorator.

        Args:
            structure: The narrative structure to employ
            characters: Whether to include character elements in the narrative
            length: The relative length of the narrative
        """
        super().__init__(
            name="Narrative",
            version="1.0.0",
            parameters={
                "structure": structure,
                "characters": characters,
                "length": length,
            },
            metadata={
                "description": "Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def structure(self) -> NarrativeStructureEnum:
        """The narrative structure to employ"""
        return self.parameters.get("structure")

    @property
    def characters(self) -> bool:
        """Whether to include character elements in the narrative"""
        return self.parameters.get("characters")

    @property
    def length(self) -> NarrativeLengthEnum:
        """The relative length of the narrative"""
        return self.parameters.get("length")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response as a story-based delivery with narrative elements
        instruction = f"Instructions for {self.name} decorator: "
        if self.structure is not None:
            instruction += f"structure={self.structure}, "
        if self.characters is not None:
            instruction += f"characters={self.characters}, "
        if self.length is not None:
            instruction += f"length={self.length}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"