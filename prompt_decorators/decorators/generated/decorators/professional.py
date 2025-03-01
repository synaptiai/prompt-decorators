"""
Professional Decorator

Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import ProfessionalFormalityEnum


class Professional(BaseDecorator):
    """Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant."""

    def __init__(
        self,
        industry: Optional[str] = "general",
        formality: Optional[ProfessionalFormalityEnum] = ProfessionalFormalityEnum.STANDARD,
    ):
        """
        Initialize Professional decorator.

        Args:
            industry: The specific industry context to adapt the language for
            formality: The level of formality to maintain in the response
        """
        super().__init__(
            name="Professional",
            version="1.0.0",
            parameters={
                "industry": industry,
                "formality": formality,
            },
            metadata={
                "description": "Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def industry(self) -> str:
        """The specific industry context to adapt the language for"""
        return self.parameters.get("industry")

    @property
    def formality(self) -> ProfessionalFormalityEnum:
        """The level of formality to maintain in the response"""
        return self.parameters.get("formality")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Adapts the response to use business-oriented language appropriate for professional contexts
        instruction = f"Instructions for {self.name} decorator: "
        if self.industry is not None:
            instruction += f"industry={self.industry}, "
        if self.formality is not None:
            instruction += f"formality={self.formality}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"