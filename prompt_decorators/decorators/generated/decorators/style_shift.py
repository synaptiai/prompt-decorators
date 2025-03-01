"""
StyleShift Decorator

Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import StyleShiftAspectEnum


class StyleShift(BaseDecorator):
    """Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone."""

    def __init__(
        self,
        aspect: StyleShiftAspectEnum,
        level: Optional[float] = 3,
        maintain: Optional[List[Any]] = None,
    ):
        """
        Initialize StyleShift decorator.

        Args:
            aspect: The specific style aspect to modify
            level: The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal)
            maintain: Style aspects to explicitly maintain while modifying the target aspect
        """
        super().__init__(
            name="StyleShift",
            version="1.0.0",
            parameters={
                "aspect": aspect,
                "level": level,
                "maintain": maintain,
            },
            metadata={
                "description": "Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def aspect(self) -> StyleShiftAspectEnum:
        """The specific style aspect to modify"""
        return self.parameters.get("aspect")

    @property
    def level(self) -> float:
        """The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal)"""
        return self.parameters.get("level")

    @property
    def maintain(self) -> List[Any]:
        """Style aspects to explicitly maintain while modifying the target aspect"""
        return self.parameters.get("maintain")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.level is not None and self.level < 1:
            raise ValueError(f"level must be at least 1, got {self.level}")
        if self.level is not None and self.level > 5:
            raise ValueError(f"level must be at most 5, got {self.level}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency
        instruction = f"Instructions for {self.name} decorator: "
        if self.aspect is not None:
            instruction += f"aspect={self.aspect}, "
        if self.level is not None:
            instruction += f"level={self.level}, "
        if self.maintain is not None:
            instruction += f"maintain={self.maintain}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"