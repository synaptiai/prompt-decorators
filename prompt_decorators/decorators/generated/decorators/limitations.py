"""
Limitations Decorator

Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import LimitationsDetailEnum, LimitationsPositionEnum, LimitationsFocusEnum


class Limitations(BaseDecorator):
    """Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints."""

    def __init__(
        self,
        detail: Optional[LimitationsDetailEnum] = LimitationsDetailEnum.MODERATE,
        position: Optional[LimitationsPositionEnum] = LimitationsPositionEnum.END,
        focus: Optional[LimitationsFocusEnum] = LimitationsFocusEnum.ALL,
    ):
        """
        Initialize Limitations decorator.

        Args:
            detail: The level of detail in the limitations statement
            position: Where to place the limitations statement in the response
            focus: The primary aspect to focus on in the limitations
        """
        super().__init__(
            name="Limitations",
            version="1.0.0",
            parameters={
                "detail": detail,
                "position": position,
                "focus": focus,
            },
            metadata={
                "description": "Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def detail(self) -> LimitationsDetailEnum:
        """The level of detail in the limitations statement"""
        return self.parameters.get("detail")

    @property
    def position(self) -> LimitationsPositionEnum:
        """Where to place the limitations statement in the response"""
        return self.parameters.get("position")

    @property
    def focus(self) -> LimitationsFocusEnum:
        """The primary aspect to focus on in the limitations"""
        return self.parameters.get("focus")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information
        instruction = f"Instructions for {self.name} decorator: "
        if self.detail is not None:
            instruction += f"detail={self.detail}, "
        if self.position is not None:
            instruction += f"position={self.position}, "
        if self.focus is not None:
            instruction += f"focus={self.focus}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"