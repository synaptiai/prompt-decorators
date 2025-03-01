"""
FactCheck Decorator

Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import FactCheckUncertainEnum, FactCheckStrictnessEnum


class FactCheck(BaseDecorator):
    """Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information."""

    def __init__(
        self,
        confidence: Optional[bool] = True,
        uncertain: Optional[FactCheckUncertainEnum] = FactCheckUncertainEnum.MARK,
        strictness: Optional[FactCheckStrictnessEnum] = FactCheckStrictnessEnum.MODERATE,
    ):
        """
        Initialize FactCheck decorator.

        Args:
            confidence: Whether to include explicit confidence levels for claims
            uncertain: How to handle uncertain information
            strictness: The threshold for considering information verified
        """
        super().__init__(
            name="FactCheck",
            version="1.0.0",
            parameters={
                "confidence": confidence,
                "uncertain": uncertain,
                "strictness": strictness,
            },
            metadata={
                "description": "Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def confidence(self) -> bool:
        """Whether to include explicit confidence levels for claims"""
        return self.parameters.get("confidence")

    @property
    def uncertain(self) -> FactCheckUncertainEnum:
        """How to handle uncertain information"""
        return self.parameters.get("uncertain")

    @property
    def strictness(self) -> FactCheckStrictnessEnum:
        """The threshold for considering information verified"""
        return self.parameters.get("strictness")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Enhances the response with verification of factual claims and explicit indication of confidence levels
        instruction = f"Instructions for {self.name} decorator: "
        if self.confidence is not None:
            instruction += f"confidence={self.confidence}, "
        if self.uncertain is not None:
            instruction += f"uncertain={self.uncertain}, "
        if self.strictness is not None:
            instruction += f"strictness={self.strictness}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"