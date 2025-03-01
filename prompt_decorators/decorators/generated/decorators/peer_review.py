"""
PeerReview Decorator

Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import PeerReviewCriteriaEnum, PeerReviewStyleEnum, PeerReviewPositionEnum


class PeerReview(BaseDecorator):
    """Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would."""

    def __init__(
        self,
        criteria: Optional[PeerReviewCriteriaEnum] = PeerReviewCriteriaEnum.ALL,
        style: Optional[PeerReviewStyleEnum] = PeerReviewStyleEnum.BALANCED,
        position: Optional[PeerReviewPositionEnum] = PeerReviewPositionEnum.AFTER,
    ):
        """
        Initialize PeerReview decorator.

        Args:
            criteria: Primary criteria to focus on in the review
            style: The tone and approach of the peer review
            position: Where to place the peer review relative to the main content
        """
        super().__init__(
            name="PeerReview",
            version="1.0.0",
            parameters={
                "criteria": criteria,
                "style": style,
                "position": position,
            },
            metadata={
                "description": "Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def criteria(self) -> PeerReviewCriteriaEnum:
        """Primary criteria to focus on in the review"""
        return self.parameters.get("criteria")

    @property
    def style(self) -> PeerReviewStyleEnum:
        """The tone and approach of the peer review"""
        return self.parameters.get("style")

    @property
    def position(self) -> PeerReviewPositionEnum:
        """Where to place the peer review relative to the main content"""
        return self.parameters.get("position")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Augments the response with a simulated peer review of the content
        instruction = f"Instructions for {self.name} decorator: "
        if self.criteria is not None:
            instruction += f"criteria={self.criteria}, "
        if self.style is not None:
            instruction += f"style={self.style}, "
        if self.position is not None:
            instruction += f"position={self.position}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"