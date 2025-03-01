"""
Inductive Decorator

Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import InductiveStructureEnum


class Inductive(BaseDecorator):
    """Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances."""

    def __init__(
        self,
        examples: Optional[float] = 3,
        confidence: Optional[bool] = False,
        structure: Optional[InductiveStructureEnum] = InductiveStructureEnum.GENERALIZATION,
    ):
        """
        Initialize Inductive decorator.

        Args:
            examples: Number of specific examples or observations to include before generalizing
            confidence: Whether to explicitly state the confidence level of the inductive conclusions
            structure: The pattern of inductive reasoning to follow
        """
        super().__init__(
            name="Inductive",
            version="1.0.0",
            parameters={
                "examples": examples,
                "confidence": confidence,
                "structure": structure,
            },
            metadata={
                "description": "Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def examples(self) -> float:
        """Number of specific examples or observations to include before generalizing"""
        return self.parameters.get("examples")

    @property
    def confidence(self) -> bool:
        """Whether to explicitly state the confidence level of the inductive conclusions"""
        return self.parameters.get("confidence")

    @property
    def structure(self) -> InductiveStructureEnum:
        """The pattern of inductive reasoning to follow"""
        return self.parameters.get("structure")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.examples is not None and self.examples < 2:
            raise ValueError(f"examples must be at least 2, got {self.examples}")
        if self.examples is not None and self.examples > 10:
            raise ValueError(f"examples must be at most 10, got {self.examples}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories
        instruction = f"Instructions for {self.name} decorator: "
        if self.examples is not None:
            instruction += f"examples={self.examples}, "
        if self.confidence is not None:
            instruction += f"confidence={self.confidence}, "
        if self.structure is not None:
            instruction += f"structure={self.structure}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"