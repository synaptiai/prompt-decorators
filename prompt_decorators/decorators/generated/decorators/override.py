"""
Override Decorator

A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Override(BaseDecorator):
    """A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments."""

    def __init__(
        self,
        decorator: str,
        parameters: Optional[str] = None,
        behavior: Optional[str] = None,
    ):
        """
        Initialize Override decorator.

        Args:
            decorator: The specific decorator whose behavior to override
            parameters: JSON string specifying the parameters to override (e.g., '{"depth": "comprehensive", "focus": "methodology"}')
            behavior: Optional custom behavior modification instructions that override the standard decorator interpretation
        """
        super().__init__(
            name="Override",
            version="1.0.0",
            parameters={
                "decorator": decorator,
                "parameters": parameters,
                "behavior": behavior,
            },
            metadata={
                "description": "A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.",
                "author": "Prompt Decorators Working Group",
                "category": "meta",
            },
        )

    @property
    def decorator(self) -> str:
        """The specific decorator whose behavior to override"""
        return self.parameters.get("decorator")

    @property
    def parameters(self) -> str:
        """JSON string specifying the parameters to override (e.g., '{"depth": "comprehensive", "focus": "methodology"}')"""
        return self.parameters.get("parameters")

    @property
    def behavior(self) -> str:
        """Optional custom behavior modification instructions that override the standard decorator interpretation"""
        return self.parameters.get("behavior")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: A meta-decorator that overrides the default parameters or behaviors of other decorators
        instruction = f"Instructions for {self.name} decorator: "
        if self.decorator is not None:
            instruction += f"decorator={self.decorator}, "
        if self.parameters is not None:
            instruction += f"parameters={self.parameters}, "
        if self.behavior is not None:
            instruction += f"behavior={self.behavior}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"