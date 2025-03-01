"""
Academic Decorator

Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import AcademicStyleEnum, AcademicCitationstyleEnum


class Academic(BaseDecorator):
    """Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles."""

    def __init__(
        self,
        style: Optional[AcademicStyleEnum] = AcademicStyleEnum.SCIENTIFIC,
        citationStyle: Optional[AcademicCitationstyleEnum] = AcademicCitationstyleEnum.APA,
    ):
        """
        Initialize Academic decorator.

        Args:
            style: The academic discipline style to follow
            citationStyle: The citation format to use for references
        """
        super().__init__(
            name="Academic",
            version="1.0.0",
            parameters={
                "style": style,
                "citationStyle": citationStyle,
            },
            metadata={
                "description": "Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def style(self) -> AcademicStyleEnum:
        """The academic discipline style to follow"""
        return self.parameters.get("style")

    @property
    def citationStyle(self) -> AcademicCitationstyleEnum:
        """The citation format to use for references"""
        return self.parameters.get("citationStyle")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Adapts the response to follow scholarly writing conventions appropriate for academic publications
        instruction = f"Instructions for {self.name} decorator: "
        if self.style is not None:
            instruction += f"style={self.style}, "
        if self.citationStyle is not None:
            instruction += f"citationStyle={self.citationStyle}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"