"""
Analogical Decorator

Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import AnalogicalDepthEnum


class Analogical(BaseDecorator):
    """Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences."""

    def __init__(
        self,
        domain: Optional[str] = "general",
        count: Optional[float] = 1,
        depth: Optional[AnalogicalDepthEnum] = AnalogicalDepthEnum.MODERATE,
    ):
        """
        Initialize Analogical decorator.

        Args:
            domain: Specific domain or context to draw analogies from (if not specified, will choose appropriate domains)
            count: Number of distinct analogies to provide
            depth: Level of detail in developing the analogy
        """
        super().__init__(
            name="Analogical",
            version="1.0.0",
            parameters={
                "domain": domain,
                "count": count,
                "depth": depth,
            },
            metadata={
                "description": "Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def domain(self) -> str:
        """Specific domain or context to draw analogies from (if not specified, will choose appropriate domains)"""
        return self.parameters.get("domain")

    @property
    def count(self) -> float:
        """Number of distinct analogies to provide"""
        return self.parameters.get("count")

    @property
    def depth(self) -> AnalogicalDepthEnum:
        """Level of detail in developing the analogy"""
        return self.parameters.get("depth")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.count is not None and self.count < 1:
            raise ValueError(f"count must be at least 1, got {self.count}")
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
        # Apply the decorator: Enhances explanations through the use of analogies and metaphors
        instruction = f"Instructions for {self.name} decorator: "
        if self.domain is not None:
            instruction += f"domain={self.domain}, "
        if self.count is not None:
            instruction += f"count={self.count}, "
        if self.depth is not None:
            instruction += f"depth={self.depth}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"