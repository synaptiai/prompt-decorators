"""
Motivational Decorator

Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import MotivationalIntensityEnum, MotivationalFocusEnum


class Motivational(BaseDecorator):
    """Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content."""

    def __init__(
        self,
        intensity: Optional[MotivationalIntensityEnum] = MotivationalIntensityEnum.MODERATE,
        focus: Optional[MotivationalFocusEnum] = MotivationalFocusEnum.BALANCED,
        actionable: Optional[bool] = True,
    ):
        """
        Initialize Motivational decorator.

        Args:
            intensity: The level of motivational energy and enthusiasm
            focus: The primary motivational approach to emphasize
            actionable: Whether to include specific actionable steps or only inspirational content
        """
        super().__init__(
            name="Motivational",
            version="1.0.0",
            parameters={
                "intensity": intensity,
                "focus": focus,
                "actionable": actionable,
            },
            metadata={
                "description": "Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def intensity(self) -> MotivationalIntensityEnum:
        """The level of motivational energy and enthusiasm"""
        return self.parameters.get("intensity")

    @property
    def focus(self) -> MotivationalFocusEnum:
        """The primary motivational approach to emphasize"""
        return self.parameters.get("focus")

    @property
    def actionable(self) -> bool:
        """Whether to include specific actionable steps or only inspirational content"""
        return self.parameters.get("actionable")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Enhances responses with encouraging, inspiring, and empowering language
        instruction = f"Instructions for {self.name} decorator: "
        if self.intensity is not None:
            instruction += f"intensity={self.intensity}, "
        if self.focus is not None:
            instruction += f"focus={self.focus}, "
        if self.actionable is not None:
            instruction += f"actionable={self.actionable}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"