"""
Custom Decorator

A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import CustomPriorityEnum


class Custom(BaseDecorator):
    """A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators."""

    def __init__(
        self,
        rules: str,
        name: Optional[str] = None,
        priority: Optional[CustomPriorityEnum] = CustomPriorityEnum.OVERRIDE,
    ):
        """
        Initialize Custom decorator.

        Args:
            rules: Explicit instructions defining the custom behavior (e.g., 'present all examples in a numbered list with exactly three items')
            name: Optional name for the custom decorator to reference in documentation or explanations
            priority: How to prioritize custom rules relative to other decorators
        """
        super().__init__(
            name="Custom",
            version="1.0.0",
            parameters={
                "rules": rules,
                "name": name,
                "priority": priority,
            },
            metadata={
                "description": "A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.",
                "author": "Prompt Decorators Working Group",
                "category": "meta",
            },
        )

    @property
    def rules(self) -> str:
        """Explicit instructions defining the custom behavior (e.g., 'present all examples in a numbered list with exactly three items')"""
        return self.parameters.get("rules")

    @property
    def name(self) -> str:
        """Optional name for the custom decorator to reference in documentation or explanations"""
        return self.parameters.get("name")

    @property
    def priority(self) -> CustomPriorityEnum:
        """How to prioritize custom rules relative to other decorators"""
        return self.parameters.get("priority")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions
        instruction = f"Instructions for {self.name} decorator: "
        if self.rules is not None:
            instruction += f"rules={self.rules}, "
        if self.name is not None:
            instruction += f"name={self.name}, "
        if self.priority is not None:
            instruction += f"priority={self.priority}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"