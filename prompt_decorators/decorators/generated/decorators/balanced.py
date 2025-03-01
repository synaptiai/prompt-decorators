"""
Balanced Decorator

Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import BalancedStructureEnum


class Balanced(BaseDecorator):
    """Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position."""

    def __init__(
        self,
        perspectives: Optional[float] = 2,
        structure: Optional[BalancedStructureEnum] = BalancedStructureEnum.SEQUENTIAL,
        equal: Optional[bool] = True,
    ):
        """
        Initialize Balanced decorator.

        Args:
            perspectives: Number of different perspectives to include
            structure: How to structure the different perspectives
            equal: Whether to strictly enforce equal word count for each perspective
        """
        super().__init__(
            name="Balanced",
            version="1.0.0",
            parameters={
                "perspectives": perspectives,
                "structure": structure,
                "equal": equal,
            },
            metadata={
                "description": "Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def perspectives(self) -> float:
        """Number of different perspectives to include"""
        return self.parameters.get("perspectives")

    @property
    def structure(self) -> BalancedStructureEnum:
        """How to structure the different perspectives"""
        return self.parameters.get("structure")

    @property
    def equal(self) -> bool:
        """Whether to strictly enforce equal word count for each perspective"""
        return self.parameters.get("equal")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.perspectives is not None and self.perspectives < 2:
            raise ValueError(f"perspectives must be at least 2, got {self.perspectives}")
        if self.perspectives is not None and self.perspectives > 5:
            raise ValueError(f"perspectives must be at most 5, got {self.perspectives}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Ensures equal representation of different perspectives or viewpoints on a topic
        instruction = f"Instructions for {self.name} decorator: "
        if self.perspectives is not None:
            instruction += f"perspectives={self.perspectives}, "
        if self.structure is not None:
            instruction += f"structure={self.structure}, "
        if self.equal is not None:
            instruction += f"equal={self.equal}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"