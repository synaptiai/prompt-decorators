"""
RedTeam Decorator

Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws. This decorator simulates how an opponent or critic would evaluate and attack ideas, plans, or arguments.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import RedTeamStrengthEnum


class RedTeam(BaseDecorator):
    """Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws. This decorator simulates how an opponent or critic would evaluate and attack ideas, plans, or arguments."""

    def __init__(
        self,
        strength: Optional[RedTeamStrengthEnum] = RedTeamStrengthEnum.MODERATE,
        focus: Optional[List[Any]] = None,
        constructive: Optional[bool] = True,
    ):
        """
        Initialize RedTeam decorator.

        Args:
            strength: How aggressive or challenging the red team analysis should be
            focus: Specific aspects to focus the red team analysis on
            constructive: Whether to include constructive suggestions for improvement after critiques
        """
        super().__init__(
            name="RedTeam",
            version="1.0.0",
            parameters={
                "strength": strength,
                "focus": focus,
                "constructive": constructive,
            },
            metadata={
                "description": "Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws. This decorator simulates how an opponent or critic would evaluate and attack ideas, plans, or arguments.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def strength(self) -> RedTeamStrengthEnum:
        """How aggressive or challenging the red team analysis should be"""
        return self.parameters.get("strength")

    @property
    def focus(self) -> List[Any]:
        """Specific aspects to focus the red team analysis on"""
        return self.parameters.get("focus")

    @property
    def constructive(self) -> bool:
        """Whether to include constructive suggestions for improvement after critiques"""
        return self.parameters.get("constructive")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws
        instruction = f"Instructions for {self.name} decorator: "
        if self.strength is not None:
            instruction += f"strength={self.strength}, "
        if self.focus is not None:
            instruction += f"focus={self.focus}, "
        if self.constructive is not None:
            instruction += f"constructive={self.constructive}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"