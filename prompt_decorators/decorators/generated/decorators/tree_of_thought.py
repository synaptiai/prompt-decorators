"""
TreeOfThought Decorator

Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class TreeOfThought(BaseDecorator):
    """Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions."""

    def __init__(
        self,
        branches: Optional[float] = 3,
        depth: Optional[float] = 3,
        pruning: Optional[bool] = False,
    ):
        """
        Initialize TreeOfThought decorator.

        Args:
            branches: Number of different reasoning branches to explore
            depth: Maximum depth of reasoning in each branch
            pruning: Whether to eliminate less promising branches early
        """
        super().__init__(
            name="TreeOfThought",
            version="1.0.0",
            parameters={
                "branches": branches,
                "depth": depth,
                "pruning": pruning,
            },
            metadata={
                "description": "Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def branches(self) -> float:
        """Number of different reasoning branches to explore"""
        return self.parameters.get("branches")

    @property
    def depth(self) -> float:
        """Maximum depth of reasoning in each branch"""
        return self.parameters.get("depth")

    @property
    def pruning(self) -> bool:
        """Whether to eliminate less promising branches early"""
        return self.parameters.get("pruning")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.branches is not None and self.branches < 2:
            raise ValueError(f"branches must be at least 2, got {self.branches}")
        if self.branches is not None and self.branches > 5:
            raise ValueError(f"branches must be at most 5, got {self.branches}")
        if self.depth is not None and self.depth < 1:
            raise ValueError(f"depth must be at least 1, got {self.depth}")
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
        # Apply the decorator: Organizes the response as a branching exploration of multiple reasoning paths
        instruction = f"Instructions for {self.name} decorator: "
        if self.branches is not None:
            instruction += f"branches={self.branches}, "
        if self.depth is not None:
            instruction += f"depth={self.depth}, "
        if self.pruning is not None:
            instruction += f"pruning={self.pruning}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"