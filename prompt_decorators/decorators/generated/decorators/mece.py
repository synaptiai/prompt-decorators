"""
MECE Decorator

Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import MECEFrameworkEnum


class MECE(BaseDecorator):
    """Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving."""

    def __init__(
        self,
        dimensions: Optional[float] = 3,
        depth: Optional[float] = 2,
        framework: Optional[MECEFrameworkEnum] = MECEFrameworkEnum.CUSTOM,
    ):
        """
        Initialize MECE decorator.

        Args:
            dimensions: Number of top-level MECE dimensions to use for categorization
            depth: Maximum level of hierarchical breakdown within each dimension
            framework: Optional predefined MECE framework to apply
        """
        super().__init__(
            name="MECE",
            version="1.0.0",
            parameters={
                "dimensions": dimensions,
                "depth": depth,
                "framework": framework,
            },
            metadata={
                "description": "Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def dimensions(self) -> float:
        """Number of top-level MECE dimensions to use for categorization"""
        return self.parameters.get("dimensions")

    @property
    def depth(self) -> float:
        """Maximum level of hierarchical breakdown within each dimension"""
        return self.parameters.get("depth")

    @property
    def framework(self) -> MECEFrameworkEnum:
        """Optional predefined MECE framework to apply"""
        return self.parameters.get("framework")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.dimensions is not None and self.dimensions < 2:
            raise ValueError(f"dimensions must be at least 2, got {self.dimensions}")
        if self.dimensions is not None and self.dimensions > 5:
            raise ValueError(f"dimensions must be at most 5, got {self.dimensions}")
        if self.depth is not None and self.depth < 1:
            raise ValueError(f"depth must be at least 1, got {self.depth}")
        if self.depth is not None and self.depth > 3:
            raise ValueError(f"depth must be at most 3, got {self.depth}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities
        instruction = f"Instructions for {self.name} decorator: "
        if self.dimensions is not None:
            instruction += f"dimensions={self.dimensions}, "
        if self.depth is not None:
            instruction += f"depth={self.depth}, "
        if self.framework is not None:
            instruction += f"framework={self.framework}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"