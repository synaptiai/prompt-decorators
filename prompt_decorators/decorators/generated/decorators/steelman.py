"""
Steelman Decorator

Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Steelman(BaseDecorator):
    """Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form."""

    def __init__(
        self,
        sides: Optional[float] = 2,
        critique: Optional[bool] = False,
        separation: Optional[bool] = True,
    ):
        """
        Initialize Steelman decorator.

        Args:
            sides: Number of different viewpoints to steel-man
            critique: Whether to include critique after presenting the steel-manned arguments
            separation: Whether to clearly separate the steel-manned presentations from any analysis
        """
        super().__init__(
            name="Steelman",
            version="1.0.0",
            parameters={
                "sides": sides,
                "critique": critique,
                "separation": separation,
            },
            metadata={
                "description": "Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def sides(self) -> float:
        """Number of different viewpoints to steel-man"""
        return self.parameters.get("sides")

    @property
    def critique(self) -> bool:
        """Whether to include critique after presenting the steel-manned arguments"""
        return self.parameters.get("critique")

    @property
    def separation(self) -> bool:
        """Whether to clearly separate the steel-manned presentations from any analysis"""
        return self.parameters.get("separation")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.sides is not None and self.sides < 1:
            raise ValueError(f"sides must be at least 1, got {self.sides}")
        if self.sides is not None and self.sides > 5:
            raise ValueError(f"sides must be at most 5, got {self.sides}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Presents the strongest possible version of an argument or position, even those the AI might not agree with
        instruction = f"Instructions for {self.name} decorator: "
        if self.sides is not None:
            instruction += f"sides={self.sides}, "
        if self.critique is not None:
            instruction += f"critique={self.critique}, "
        if self.separation is not None:
            instruction += f"separation={self.separation}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"