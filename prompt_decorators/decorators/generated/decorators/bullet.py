"""
Bullet Decorator

Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import BulletStyleEnum


class Bullet(BaseDecorator):
    """Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format."""

    def __init__(
        self,
        style: Optional[BulletStyleEnum] = BulletStyleEnum.DASH,
        indented: Optional[bool] = True,
        compact: Optional[bool] = False,
    ):
        """
        Initialize Bullet decorator.

        Args:
            style: The visual marker used for bullet points
            indented: Whether to allow nested, indented bullet points
            compact: Whether to keep bullet points short and concise (true) or allow longer, more detailed points (false)
        """
        super().__init__(
            name="Bullet",
            version="1.0.0",
            parameters={
                "style": style,
                "indented": indented,
                "compact": compact,
            },
            metadata={
                "description": "Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def style(self) -> BulletStyleEnum:
        """The visual marker used for bullet points"""
        return self.parameters.get("style")

    @property
    def indented(self) -> bool:
        """Whether to allow nested, indented bullet points"""
        return self.parameters.get("indented")

    @property
    def compact(self) -> bool:
        """Whether to keep bullet points short and concise (true) or allow longer, more detailed points (false)"""
        return self.parameters.get("compact")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Formats the response as a bulleted list, making information easier to scan and digest
        instruction = f"Instructions for {self.name} decorator: "
        if self.style is not None:
            instruction += f"style={self.style}, "
        if self.indented is not None:
            instruction += f"indented={self.indented}, "
        if self.compact is not None:
            instruction += f"compact={self.compact}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"