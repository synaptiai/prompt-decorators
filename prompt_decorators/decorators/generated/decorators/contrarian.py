"""
Contrarian Decorator

Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import ContrarianApproachEnum


class Contrarian(BaseDecorator):
    """Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic."""

    def __init__(
        self,
        approach: Optional[ContrarianApproachEnum] = ContrarianApproachEnum.DEVIL_S_ADVOCATE,
        maintain: Optional[bool] = False,
        focus: Optional[str] = None,
    ):
        """
        Initialize Contrarian decorator.

        Args:
            approach: The specific contrarian approach to take
            maintain: Whether to maintain contrarian stance throughout (true) or provide balanced view at the end (false)
            focus: Optional specific aspect of the topic to focus contrarian analysis on
        """
        super().__init__(
            name="Contrarian",
            version="1.0.0",
            parameters={
                "approach": approach,
                "maintain": maintain,
                "focus": focus,
            },
            metadata={
                "description": "Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def approach(self) -> ContrarianApproachEnum:
        """The specific contrarian approach to take"""
        return self.parameters.get("approach")

    @property
    def maintain(self) -> bool:
        """Whether to maintain contrarian stance throughout (true) or provide balanced view at the end (false)"""
        return self.parameters.get("maintain")

    @property
    def focus(self) -> str:
        """Optional specific aspect of the topic to focus contrarian analysis on"""
        return self.parameters.get("focus")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Generates responses that deliberately challenge conventional wisdom or mainstream perspectives
        instruction = f"Instructions for {self.name} decorator: "
        if self.approach is not None:
            instruction += f"approach={self.approach}, "
        if self.maintain is not None:
            instruction += f"maintain={self.maintain}, "
        if self.focus is not None:
            instruction += f"focus={self.focus}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"