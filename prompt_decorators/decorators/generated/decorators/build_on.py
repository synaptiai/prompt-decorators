"""
BuildOn Decorator

A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import BuildOnReferenceEnum, BuildOnApproachEnum


class BuildOn(BaseDecorator):
    """A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner."""

    def __init__(
        self,
        reference: Optional[BuildOnReferenceEnum] = BuildOnReferenceEnum.LAST,
        approach: Optional[BuildOnApproachEnum] = BuildOnApproachEnum.EXTEND,
        preserveStructure: Optional[bool] = True,
    ):
        """
        Initialize BuildOn decorator.

        Args:
            reference: What to build upon from the previous context
            approach: How to build upon the referenced content
            preserveStructure: Whether to maintain the structure of the referenced content
        """
        super().__init__(
            name="BuildOn",
            version="1.0.0",
            parameters={
                "reference": reference,
                "approach": approach,
                "preserveStructure": preserveStructure,
            },
            metadata={
                "description": "A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.",
                "author": "Prompt Decorators Working Group",
                "category": "meta",
            },
        )

    @property
    def reference(self) -> BuildOnReferenceEnum:
        """What to build upon from the previous context"""
        return self.parameters.get("reference")

    @property
    def approach(self) -> BuildOnApproachEnum:
        """How to build upon the referenced content"""
        return self.parameters.get("approach")

    @property
    def preserveStructure(self) -> bool:
        """Whether to maintain the structure of the referenced content"""
        return self.parameters.get("preserveStructure")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: A meta-decorator that builds upon previous context or responses rather than starting from scratch
        instruction = f"Instructions for {self.name} decorator: "
        if self.reference is not None:
            instruction += f"reference={self.reference}, "
        if self.approach is not None:
            instruction += f"approach={self.approach}, "
        if self.preserveStructure is not None:
            instruction += f"preserveStructure={self.preserveStructure}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"