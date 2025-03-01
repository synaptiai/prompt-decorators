"""
Prioritize Decorator

Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Prioritize(BaseDecorator):
    """Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important."""

    def __init__(
        self,
        criteria: Optional[str] = "importance",
        count: Optional[float] = 5,
        showRationale: Optional[bool] = False,
    ):
        """
        Initialize Prioritize decorator.

        Args:
            criteria: The specific criterion to use for prioritization (e.g., importance, urgency, ROI)
            count: Number of prioritized items to include
            showRationale: Whether to explain the reasoning behind each priority ranking
        """
        super().__init__(
            name="Prioritize",
            version="1.0.0",
            parameters={
                "criteria": criteria,
                "count": count,
                "showRationale": showRationale,
            },
            metadata={
                "description": "Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def criteria(self) -> str:
        """The specific criterion to use for prioritization (e.g., importance, urgency, ROI)"""
        return self.parameters.get("criteria")

    @property
    def count(self) -> float:
        """Number of prioritized items to include"""
        return self.parameters.get("count")

    @property
    def showRationale(self) -> bool:
        """Whether to explain the reasoning behind each priority ranking"""
        return self.parameters.get("showRationale")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.count is not None and self.count < 1:
            raise ValueError(f"count must be at least 1, got {self.count}")
        if self.count is not None and self.count > 10:
            raise ValueError(f"count must be at most 10, got {self.count}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response by ranking information according to importance, urgency, or impact
        instruction = f"Instructions for {self.name} decorator: "
        if self.criteria is not None:
            instruction += f"criteria={self.criteria}, "
        if self.count is not None:
            instruction += f"count={self.count}, "
        if self.showRationale is not None:
            instruction += f"showRationale={self.showRationale}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"