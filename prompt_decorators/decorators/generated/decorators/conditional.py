"""
Conditional Decorator

A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Conditional(BaseDecorator):
    """A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters."""

    def __init__(
        self,
        if_param: str,
        then: str,
        else_param: Optional[str] = None,
    ):
        """
        Initialize Conditional decorator.

        Args:
            if_param: The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}')
            then: The decorator to apply if the condition is true (can be a specific decorator with parameters)
            else_param: The decorator to apply if the condition is false (can be a specific decorator with parameters)
        """
        super().__init__(
            name="Conditional",
            version="1.0.0",
            parameters={
                "if": if_param,
                "then": then,
                "else": else_param,
            },
            metadata={
                "description": "A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.",
                "author": "Prompt Decorators Working Group",
                "category": "meta",
            },
        )

    @property
    def if_param(self) -> str:
        """The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}')"""
        return self.parameters.get("if")

    @property
    def then(self) -> str:
        """The decorator to apply if the condition is true (can be a specific decorator with parameters)"""
        return self.parameters.get("then")

    @property
    def else_param(self) -> str:
        """The decorator to apply if the condition is false (can be a specific decorator with parameters)"""
        return self.parameters.get("else")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: A meta-decorator that applies different decorators based on specified conditions
        instruction = f"Instructions for {self.name} decorator: "
        if self.if_param is not None:
            instruction += f"if={self.if_param}, "
        if self.then is not None:
            instruction += f"then={self.then}, "
        if self.else_param is not None:
            instruction += f"else={self.else_param}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"