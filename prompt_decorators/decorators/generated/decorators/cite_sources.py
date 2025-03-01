"""
CiteSources Decorator

Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import CiteSourcesStyleEnum, CiteSourcesFormatEnum


class CiteSources(BaseDecorator):
    """Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics."""

    def __init__(
        self,
        style: Optional[CiteSourcesStyleEnum] = CiteSourcesStyleEnum.INLINE,
        format: Optional[CiteSourcesFormatEnum] = CiteSourcesFormatEnum.APA,
        comprehensive: Optional[bool] = False,
    ):
        """
        Initialize CiteSources decorator.

        Args:
            style: The placement and format of citations within the response
            format: The citation format to use
            comprehensive: Whether to cite every claim (true) or only major claims (false)
        """
        super().__init__(
            name="CiteSources",
            version="1.0.0",
            parameters={
                "style": style,
                "format": format,
                "comprehensive": comprehensive,
            },
            metadata={
                "description": "Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def style(self) -> CiteSourcesStyleEnum:
        """The placement and format of citations within the response"""
        return self.parameters.get("style")

    @property
    def format(self) -> CiteSourcesFormatEnum:
        """The citation format to use"""
        return self.parameters.get("format")

    @property
    def comprehensive(self) -> bool:
        """Whether to cite every claim (true) or only major claims (false)"""
        return self.parameters.get("comprehensive")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response to include citations for claims and information
        instruction = f"Instructions for {self.name} decorator: "
        if self.style is not None:
            instruction += f"style={self.style}, "
        if self.format is not None:
            instruction += f"format={self.format}, "
        if self.comprehensive is not None:
            instruction += f"comprehensive={self.comprehensive}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"