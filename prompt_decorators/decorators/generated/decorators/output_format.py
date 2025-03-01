"""
OutputFormat Decorator

Specifies the format of the AI's response. This decorator ensures the output follows a specific format, making it easier to parse, display, or process the response in a consistent way.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import OutputFormatFormatEnum


class OutputFormat(BaseDecorator):
    """Specifies the format of the AI's response. This decorator ensures the output follows a specific format, making it easier to parse, display, or process the response in a consistent way."""

    def __init__(
        self,
        format: OutputFormatFormatEnum,
    ):
        """
        Initialize OutputFormat decorator.

        Args:
            format: The format to use for the response
        """
        super().__init__(
            name="OutputFormat",
            version="1.0.0",
            parameters={
                "format": format,
            },
            metadata={
                "description": "Specifies the format of the AI's response. This decorator ensures the output follows a specific format, making it easier to parse, display, or process the response in a consistent way.",
                "author": "Prompt Decorators Working Group",
                "category": "minimal",
            },
        )

    @property
    def format(self) -> OutputFormatFormatEnum:
        """The format to use for the response"""
        return self.parameters.get("format")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Specifies the format of the AI's response
        instruction = f"Instructions for {self.name} decorator: "
        if self.format is not None:
            instruction += f"format={self.format}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"