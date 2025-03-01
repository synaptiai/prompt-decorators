"""
Remix Decorator

Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import RemixPreserveEnum


class Remix(BaseDecorator):
    """Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics."""

    def __init__(
        self,
        target: str,
        preserve: Optional[RemixPreserveEnum] = RemixPreserveEnum.FACTS,
        contrast: Optional[bool] = False,
    ):
        """
        Initialize Remix decorator.

        Args:
            target: The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch')
            preserve: What aspects of the original content to prioritize preserving
            contrast: Whether to highlight differences between the original framing and the remixed version
        """
        super().__init__(
            name="Remix",
            version="1.0.0",
            parameters={
                "target": target,
                "preserve": preserve,
                "contrast": contrast,
            },
            metadata={
                "description": "Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def target(self) -> str:
        """The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch')"""
        return self.parameters.get("target")

    @property
    def preserve(self) -> RemixPreserveEnum:
        """What aspects of the original content to prioritize preserving"""
        return self.parameters.get("preserve")

    @property
    def contrast(self) -> bool:
        """Whether to highlight differences between the original framing and the remixed version"""
        return self.parameters.get("contrast")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Reframes or adapts content for a different context, purpose, or audience than originally intended
        instruction = f"Instructions for {self.name} decorator: "
        if self.target is not None:
            instruction += f"target={self.target}, "
        if self.preserve is not None:
            instruction += f"preserve={self.preserve}, "
        if self.contrast is not None:
            instruction += f"contrast={self.contrast}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"