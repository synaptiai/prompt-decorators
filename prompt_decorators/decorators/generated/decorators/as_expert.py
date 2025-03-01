"""
AsExpert Decorator

Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import AsExpertExperienceEnum


class AsExpert(BaseDecorator):
    """Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field."""

    def __init__(
        self,
        domain: str,
        experience: Optional[AsExpertExperienceEnum] = AsExpertExperienceEnum.SENIOR,
        technical: Optional[bool] = True,
    ):
        """
        Initialize AsExpert decorator.

        Args:
            domain: The specific field or discipline the expert specializes in
            experience: The experience level of the expert
            technical: Whether to use highly technical language and domain-specific terminology
        """
        super().__init__(
            name="AsExpert",
            version="1.0.0",
            parameters={
                "domain": domain,
                "experience": experience,
                "technical": technical,
            },
            metadata={
                "description": "Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def domain(self) -> str:
        """The specific field or discipline the expert specializes in"""
        return self.parameters.get("domain")

    @property
    def experience(self) -> AsExpertExperienceEnum:
        """The experience level of the expert"""
        return self.parameters.get("experience")

    @property
    def technical(self) -> bool:
        """Whether to use highly technical language and domain-specific terminology"""
        return self.parameters.get("technical")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Generates responses from the perspective of a specified domain expert or specialist
        instruction = f"Instructions for {self.name} decorator: "
        if self.domain is not None:
            instruction += f"domain={self.domain}, "
        if self.experience is not None:
            instruction += f"experience={self.experience}, "
        if self.technical is not None:
            instruction += f"technical={self.technical}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"