"""
Alternatives Decorator

Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import AlternativesDiversityEnum


class Alternatives(BaseDecorator):
    """Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer."""

    def __init__(
        self,
        count: Optional[float] = 3,
        diversity: Optional[AlternativesDiversityEnum] = AlternativesDiversityEnum.MEDIUM,
        comparison: Optional[bool] = False,
    ):
        """
        Initialize Alternatives decorator.

        Args:
            count: Number of alternative options or approaches to generate
            diversity: How different or varied the alternatives should be from each other
            comparison: Whether to include a comparative analysis of the alternatives
        """
        super().__init__(
            name="Alternatives",
            version="1.0.0",
            parameters={
                "count": count,
                "diversity": diversity,
                "comparison": comparison,
            },
            metadata={
                "description": "Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def count(self) -> float:
        """Number of alternative options or approaches to generate"""
        return self.parameters.get("count")

    @property
    def diversity(self) -> AlternativesDiversityEnum:
        """How different or varied the alternatives should be from each other"""
        return self.parameters.get("diversity")

    @property
    def comparison(self) -> bool:
        """Whether to include a comparative analysis of the alternatives"""
        return self.parameters.get("comparison")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.count is not None and self.count < 2:
            raise ValueError(f"count must be at least 2, got {self.count}")
        if self.count is not None and self.count > 7:
            raise ValueError(f"count must be at most 7, got {self.count}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Presents multiple distinct options, approaches, or solutions to a question or problem
        instruction = f"Instructions for {self.name} decorator: "
        if self.count is not None:
            instruction += f"count={self.count}, "
        if self.diversity is not None:
            instruction += f"diversity={self.diversity}, "
        if self.comparison is not None:
            instruction += f"comparison={self.comparison}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"