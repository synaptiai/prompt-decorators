"""
Extremes Decorator

Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import ExtremesVersionsEnum


class Extremes(BaseDecorator):
    """Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision."""

    def __init__(
        self,
        versions: Optional[ExtremesVersionsEnum] = ExtremesVersionsEnum.BOTH,
        dimension: Optional[str] = "ambition",
        compare: Optional[bool] = True,
    ):
        """
        Initialize Extremes decorator.

        Args:
            versions: Which extreme versions to include
            dimension: The specific dimension along which to explore extremes (e.g., 'cost', 'time', 'ambition', 'complexity')
            compare: Whether to include a comparative analysis of the extreme versions
        """
        super().__init__(
            name="Extremes",
            version="1.0.0",
            parameters={
                "versions": versions,
                "dimension": dimension,
                "compare": compare,
            },
            metadata={
                "description": "Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def versions(self) -> ExtremesVersionsEnum:
        """Which extreme versions to include"""
        return self.parameters.get("versions")

    @property
    def dimension(self) -> str:
        """The specific dimension along which to explore extremes (e.g., 'cost', 'time', 'ambition', 'complexity')"""
        return self.parameters.get("dimension")

    @property
    def compare(self) -> bool:
        """Whether to include a comparative analysis of the extreme versions"""
        return self.parameters.get("compare")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version
        instruction = f"Instructions for {self.name} decorator: "
        if self.versions is not None:
            instruction += f"versions={self.versions}, "
        if self.dimension is not None:
            instruction += f"dimension={self.dimension}, "
        if self.compare is not None:
            instruction += f"compare={self.compare}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"