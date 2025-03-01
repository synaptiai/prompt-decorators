"""
Tone Decorator

Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import ToneStyleEnum


class Tone(BaseDecorator):
    """Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations."""

    def __init__(
        self,
        style: ToneStyleEnum,
    ):
        """
        Initialize Tone decorator.

        Args:
            style: The desired tone and style for the response
        """
        super().__init__(
            name="Tone",
            version="1.0.0",
            parameters={
                "style": style,
            },
            metadata={
                "description": "Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.",
                "author": "Prompt Decorators Working Group",
                "category": "minimal",
            },
        )

    @property
    def style(self) -> ToneStyleEnum:
        """The desired tone and style for the response"""
        return self.parameters.get("style")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Adjusts the writing style and tone of the AI's response
        instruction = f"Instructions for {self.name} decorator: "
        if self.style is not None:
            instruction += f"style={self.style}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"