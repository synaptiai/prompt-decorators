"""
Deductive Decorator

Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Deductive(BaseDecorator):
    """Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions."""

    def __init__(
        self,
        premises: Optional[float] = 2,
        formal: Optional[bool] = False,
        steps: Optional[float] = 3,
    ):
        """
        Initialize Deductive decorator.

        Args:
            premises: Number of main premises to include before deducing conclusions
            formal: Whether to use formal logical structures with explicit syllogisms
            steps: Number of logical steps to include in the deductive process
        """
        super().__init__(
            name="Deductive",
            version="1.0.0",
            parameters={
                "premises": premises,
                "formal": formal,
                "steps": steps,
            },
            metadata={
                "description": "Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def premises(self) -> float:
        """Number of main premises to include before deducing conclusions"""
        return self.parameters.get("premises")

    @property
    def formal(self) -> bool:
        """Whether to use formal logical structures with explicit syllogisms"""
        return self.parameters.get("formal")

    @property
    def steps(self) -> float:
        """Number of logical steps to include in the deductive process"""
        return self.parameters.get("steps")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.premises is not None and self.premises < 1:
            raise ValueError(f"premises must be at least 1, got {self.premises}")
        if self.premises is not None and self.premises > 5:
            raise ValueError(f"premises must be at most 5, got {self.premises}")
        if self.steps is not None and self.steps < 2:
            raise ValueError(f"steps must be at least 2, got {self.steps}")
        if self.steps is not None and self.steps > 7:
            raise ValueError(f"steps must be at most 7, got {self.steps}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response using deductive reasoning, moving from general principles to specific conclusions
        instruction = f"Instructions for {self.name} decorator: "
        if self.premises is not None:
            instruction += f"premises={self.premises}, "
        if self.formal is not None:
            instruction += f"formal={self.formal}, "
        if self.steps is not None:
            instruction += f"steps={self.steps}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"