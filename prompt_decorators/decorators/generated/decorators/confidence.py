"""
Confidence Decorator

Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import ConfidenceScaleEnum


class Confidence(BaseDecorator):
    """Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content."""

    def __init__(
        self,
        scale: Optional[ConfidenceScaleEnum] = ConfidenceScaleEnum.QUALITATIVE,
        threshold: Optional[float] = 50,
        detailed: Optional[bool] = False,
    ):
        """
        Initialize Confidence decorator.

        Args:
            scale: The method used to express confidence levels
            threshold: Minimum confidence level for including information (as a percentage)
            detailed: Whether to provide explanations for confidence assessments
        """
        super().__init__(
            name="Confidence",
            version="1.0.0",
            parameters={
                "scale": scale,
                "threshold": threshold,
                "detailed": detailed,
            },
            metadata={
                "description": "Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def scale(self) -> ConfidenceScaleEnum:
        """The method used to express confidence levels"""
        return self.parameters.get("scale")

    @property
    def threshold(self) -> float:
        """Minimum confidence level for including information (as a percentage)"""
        return self.parameters.get("threshold")

    @property
    def detailed(self) -> bool:
        """Whether to provide explanations for confidence assessments"""
        return self.parameters.get("detailed")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.threshold is not None and self.threshold < 0:
            raise ValueError(f"threshold must be at least 0, got {self.threshold}")
        if self.threshold is not None and self.threshold > 100:
            raise ValueError(f"threshold must be at most 100, got {self.threshold}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Enhances the response with explicit indications of confidence levels for different statements or claims
        instruction = f"Instructions for {self.name} decorator: "
        if self.scale is not None:
            instruction += f"scale={self.scale}, "
        if self.threshold is not None:
            instruction += f"threshold={self.threshold}, "
        if self.detailed is not None:
            instruction += f"detailed={self.detailed}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"