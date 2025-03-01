"""
Abductive Decorator

Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Abductive(BaseDecorator):
    """Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information."""

    def __init__(
        self,
        hypotheses: Optional[float] = 3,
        criteria: Optional[List[Any]] = None,
        rank: Optional[bool] = True,
    ):
        """
        Initialize Abductive decorator.

        Args:
            hypotheses: Number of alternative hypotheses or explanations to generate
            criteria: Specific criteria to evaluate hypotheses against (e.g., simplicity, explanatory power)
            rank: Whether to explicitly rank hypotheses by likelihood
        """
        super().__init__(
            name="Abductive",
            version="1.0.0",
            parameters={
                "hypotheses": hypotheses,
                "criteria": criteria,
                "rank": rank,
            },
            metadata={
                "description": "Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def hypotheses(self) -> float:
        """Number of alternative hypotheses or explanations to generate"""
        return self.parameters.get("hypotheses")

    @property
    def criteria(self) -> List[Any]:
        """Specific criteria to evaluate hypotheses against (e.g., simplicity, explanatory power)"""
        return self.parameters.get("criteria")

    @property
    def rank(self) -> bool:
        """Whether to explicitly rank hypotheses by likelihood"""
        return self.parameters.get("rank")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.hypotheses is not None and self.hypotheses < 2:
            raise ValueError(f"hypotheses must be at least 2, got {self.hypotheses}")
        if self.hypotheses is not None and self.hypotheses > 5:
            raise ValueError(f"hypotheses must be at most 5, got {self.hypotheses}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena
        instruction = f"Instructions for {self.name} decorator: "
        if self.hypotheses is not None:
            instruction += f"hypotheses={self.hypotheses}, "
        if self.criteria is not None:
            instruction += f"criteria={self.criteria}, "
        if self.rank is not None:
            instruction += f"rank={self.rank}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"