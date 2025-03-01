"""
BreakAndBuild Decorator

Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import BreakAndBuildBreakdownEnum, BreakAndBuildIntensityEnum


class BreakAndBuild(BaseDecorator):
    """Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output."""

    def __init__(
        self,
        breakdown: Optional[BreakAndBuildBreakdownEnum] = BreakAndBuildBreakdownEnum.COMPREHENSIVE,
        intensity: Optional[BreakAndBuildIntensityEnum] = BreakAndBuildIntensityEnum.THOROUGH,
        buildRatio: Optional[float] = 1,
    ):
        """
        Initialize BreakAndBuild decorator.

        Args:
            breakdown: Primary approach for the critical breakdown phase
            intensity: How thorough and challenging the breakdown phase should be
            buildRatio: Approximate ratio of build-up content to breakdown content (e.g., 2 means twice as much reconstruction as critique)
        """
        super().__init__(
            name="BreakAndBuild",
            version="1.0.0",
            parameters={
                "breakdown": breakdown,
                "intensity": intensity,
                "buildRatio": buildRatio,
            },
            metadata={
                "description": "Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def breakdown(self) -> BreakAndBuildBreakdownEnum:
        """Primary approach for the critical breakdown phase"""
        return self.parameters.get("breakdown")

    @property
    def intensity(self) -> BreakAndBuildIntensityEnum:
        """How thorough and challenging the breakdown phase should be"""
        return self.parameters.get("intensity")

    @property
    def buildRatio(self) -> float:
        """Approximate ratio of build-up content to breakdown content (e.g., 2 means twice as much reconstruction as critique)"""
        return self.parameters.get("buildRatio")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.buildRatio is not None and self.buildRatio < 0.5:
            raise ValueError(f"buildRatio must be at least 0.5, got {self.buildRatio}")
        if self.buildRatio is not None and self.buildRatio > 3:
            raise ValueError(f"buildRatio must be at most 3, got {self.buildRatio}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions
        instruction = f"Instructions for {self.name} decorator: "
        if self.breakdown is not None:
            instruction += f"breakdown={self.breakdown}, "
        if self.intensity is not None:
            instruction += f"intensity={self.intensity}, "
        if self.buildRatio is not None:
            instruction += f"buildRatio={self.buildRatio}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"