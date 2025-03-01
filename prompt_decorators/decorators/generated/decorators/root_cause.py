"""
RootCause Decorator

Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import RootCauseMethodEnum


class RootCause(BaseDecorator):
    """Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes."""

    def __init__(
        self,
        method: Optional[RootCauseMethodEnum] = RootCauseMethodEnum.VALUE_5WHYS,
        depth: Optional[float] = 5,
    ):
        """
        Initialize RootCause decorator.

        Args:
            method: The specific root cause analysis methodology to apply
            depth: Level of detail in the analysis (for 5whys, represents number of 'why' iterations)
        """
        super().__init__(
            name="RootCause",
            version="1.0.0",
            parameters={
                "method": method,
                "depth": depth,
            },
            metadata={
                "description": "Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def method(self) -> RootCauseMethodEnum:
        """The specific root cause analysis methodology to apply"""
        return self.parameters.get("method")

    @property
    def depth(self) -> float:
        """Level of detail in the analysis (for 5whys, represents number of 'why' iterations)"""
        return self.parameters.get("depth")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.depth is not None and self.depth < 3:
            raise ValueError(f"depth must be at least 3, got {self.depth}")
        if self.depth is not None and self.depth > 7:
            raise ValueError(f"depth must be at most 7, got {self.depth}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response to systematically analyze underlying causes of problems or situations
        instruction = f"Instructions for {self.name} decorator: "
        if self.method is not None:
            instruction += f"method={self.method}, "
        if self.depth is not None:
            instruction += f"depth={self.depth}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"