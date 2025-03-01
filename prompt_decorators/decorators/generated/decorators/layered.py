"""
Layered Decorator

Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import LayeredLevelsEnum, LayeredProgressionEnum


class Layered(BaseDecorator):
    """Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations."""

    def __init__(
        self,
        levels: Optional[LayeredLevelsEnum] = LayeredLevelsEnum.SUMMARY_DETAIL_TECHNICAL,
        count: Optional[float] = 3,
        progression: Optional[LayeredProgressionEnum] = LayeredProgressionEnum.SEPARATE,
    ):
        """
        Initialize Layered decorator.

        Args:
            levels: The granularity of explanation levels to include
            count: Number of distinct explanation layers to provide
            progression: How to structure the progression between layers
        """
        super().__init__(
            name="Layered",
            version="1.0.0",
            parameters={
                "levels": levels,
                "count": count,
                "progression": progression,
            },
            metadata={
                "description": "Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def levels(self) -> LayeredLevelsEnum:
        """The granularity of explanation levels to include"""
        return self.parameters.get("levels")

    @property
    def count(self) -> float:
        """Number of distinct explanation layers to provide"""
        return self.parameters.get("count")

    @property
    def progression(self) -> LayeredProgressionEnum:
        """How to structure the progression between layers"""
        return self.parameters.get("progression")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.count is not None and self.count < 2:
            raise ValueError(f"count must be at least 2, got {self.count}")
        if self.count is not None and self.count > 5:
            raise ValueError(f"count must be at most 5, got {self.count}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail
        instruction = f"Instructions for {self.name} decorator: "
        if self.levels is not None:
            instruction += f"levels={self.levels}, "
        if self.count is not None:
            instruction += f"count={self.count}, "
        if self.progression is not None:
            instruction += f"progression={self.progression}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"