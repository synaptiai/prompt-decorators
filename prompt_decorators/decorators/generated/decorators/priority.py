"""
Priority Decorator

A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import PriorityModeEnum


class Priority(BaseDecorator):
    """A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior."""

    def __init__(
        self,
        decorators: List[Any],
        explicit: Optional[bool] = False,
        mode: Optional[PriorityModeEnum] = PriorityModeEnum.OVERRIDE,
    ):
        """
        Initialize Priority decorator.

        Args:
            decorators: Ordered list of decorators by priority (highest priority first)
            explicit: Whether to explicitly mention overridden behaviors in the response
            mode: How to handle conflicts between decorators
        """
        super().__init__(
            name="Priority",
            version="1.0.0",
            parameters={
                "decorators": decorators,
                "explicit": explicit,
                "mode": mode,
            },
            metadata={
                "description": "A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.",
                "author": "Prompt Decorators Working Group",
                "category": "meta",
            },
        )

    @property
    def decorators(self) -> List[Any]:
        """Ordered list of decorators by priority (highest priority first)"""
        return self.parameters.get("decorators")

    @property
    def explicit(self) -> bool:
        """Whether to explicitly mention overridden behaviors in the response"""
        return self.parameters.get("explicit")

    @property
    def mode(self) -> PriorityModeEnum:
        """How to handle conflicts between decorators"""
        return self.parameters.get("mode")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: A meta-decorator that establishes a precedence hierarchy among multiple decorators
        instruction = f"Instructions for {self.name} decorator: "
        if self.decorators is not None:
            instruction += f"decorators={self.decorators}, "
        if self.explicit is not None:
            instruction += f"explicit={self.explicit}, "
        if self.mode is not None:
            instruction += f"mode={self.mode}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"