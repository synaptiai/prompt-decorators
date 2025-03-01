"""
BlindSpots Decorator

Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import BlindSpotsDepthEnum, BlindSpotsPositionEnum


class BlindSpots(BaseDecorator):
    """Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis."""

    def __init__(
        self,
        categories: Optional[List[Any]] = None,
        depth: Optional[BlindSpotsDepthEnum] = BlindSpotsDepthEnum.THOROUGH,
        position: Optional[BlindSpotsPositionEnum] = BlindSpotsPositionEnum.AFTER,
    ):
        """
        Initialize BlindSpots decorator.

        Args:
            categories: Specific categories of blind spots to check for (e.g., cultural, temporal, confirmation bias)
            depth: How thoroughly to analyze for blind spots
            position: Where to place the blind spots analysis
        """
        super().__init__(
            name="BlindSpots",
            version="1.0.0",
            parameters={
                "categories": categories,
                "depth": depth,
                "position": position,
            },
            metadata={
                "description": "Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def categories(self) -> List[Any]:
        """Specific categories of blind spots to check for (e.g., cultural, temporal, confirmation bias)"""
        return self.parameters.get("categories")

    @property
    def depth(self) -> BlindSpotsDepthEnum:
        """How thoroughly to analyze for blind spots"""
        return self.parameters.get("depth")

    @property
    def position(self) -> BlindSpotsPositionEnum:
        """Where to place the blind spots analysis"""
        return self.parameters.get("position")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response
        instruction = f"Instructions for {self.name} decorator: "
        if self.categories is not None:
            instruction += f"categories={self.categories}, "
        if self.depth is not None:
            instruction += f"depth={self.depth}, "
        if self.position is not None:
            instruction += f"position={self.position}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"