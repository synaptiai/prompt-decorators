"""
Creative Decorator

Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import CreativeLevelEnum


class Creative(BaseDecorator):
    """Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs."""

    def __init__(
        self,
        level: Optional[CreativeLevelEnum] = CreativeLevelEnum.HIGH,
        elements: Optional[List[Any]] = None,
        constraints: Optional[List[Any]] = None,
    ):
        """
        Initialize Creative decorator.

        Args:
            level: The degree of creative thinking to apply
            elements: Specific creative elements to incorporate (e.g., metaphor, wordplay, narrative)
            constraints: Optional creative constraints to work within
        """
        super().__init__(
            name="Creative",
            version="1.0.0",
            parameters={
                "level": level,
                "elements": elements,
                "constraints": constraints,
            },
            metadata={
                "description": "Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def level(self) -> CreativeLevelEnum:
        """The degree of creative thinking to apply"""
        return self.parameters.get("level")

    @property
    def elements(self) -> List[Any]:
        """Specific creative elements to incorporate (e.g., metaphor, wordplay, narrative)"""
        return self.parameters.get("elements")

    @property
    def constraints(self) -> List[Any]:
        """Optional creative constraints to work within"""
        return self.parameters.get("constraints")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Enhances responses with imaginative, novel, and original content
        instruction = f"Instructions for {self.name} decorator: "
        if self.level is not None:
            instruction += f"level={self.level}, "
        if self.elements is not None:
            instruction += f"elements={self.elements}, "
        if self.constraints is not None:
            instruction += f"constraints={self.constraints}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"