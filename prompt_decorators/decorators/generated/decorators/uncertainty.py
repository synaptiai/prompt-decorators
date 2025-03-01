"""
Uncertainty Decorator

Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import UncertaintyFormatEnum, UncertaintyThresholdEnum


class Uncertainty(BaseDecorator):
    """Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate."""

    def __init__(
        self,
        format: Optional[UncertaintyFormatEnum] = UncertaintyFormatEnum.INLINE,
        threshold: Optional[UncertaintyThresholdEnum] = UncertaintyThresholdEnum.MEDIUM,
        reason: Optional[bool] = False,
    ):
        """
        Initialize Uncertainty decorator.

        Args:
            format: How to format uncertainty indications in the response
            threshold: The threshold for flagging uncertain content
            reason: Whether to explain the reason for uncertainty
        """
        super().__init__(
            name="Uncertainty",
            version="1.0.0",
            parameters={
                "format": format,
                "threshold": threshold,
                "reason": reason,
            },
            metadata={
                "description": "Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def format(self) -> UncertaintyFormatEnum:
        """How to format uncertainty indications in the response"""
        return self.parameters.get("format")

    @property
    def threshold(self) -> UncertaintyThresholdEnum:
        """The threshold for flagging uncertain content"""
        return self.parameters.get("threshold")

    @property
    def reason(self) -> bool:
        """Whether to explain the reason for uncertainty"""
        return self.parameters.get("reason")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Explicitly highlights areas of uncertainty in the response
        instruction = f"Instructions for {self.name} decorator: "
        if self.format is not None:
            instruction += f"format={self.format}, "
        if self.threshold is not None:
            instruction += f"threshold={self.threshold}, "
        if self.reason is not None:
            instruction += f"reason={self.reason}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"