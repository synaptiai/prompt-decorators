"""
Refine Decorator

A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Refine(BaseDecorator):
    """A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response."""

    def __init__(
        self,
        iterations: Optional[float] = 2,
        focus: Optional[List[Any]] = None,
        showProcess: Optional[bool] = False,
    ):
        """
        Initialize Refine decorator.

        Args:
            iterations: Number of refinement cycles to perform
            focus: Specific aspects to focus on during refinement (e.g., clarity, conciseness, evidence)
            showProcess: Whether to show the intermediate steps in the refinement process
        """
        super().__init__(
            name="Refine",
            version="1.0.0",
            parameters={
                "iterations": iterations,
                "focus": focus,
                "showProcess": showProcess,
            },
            metadata={
                "description": "A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response.",
                "author": "Prompt Decorators Working Group",
                "category": "meta",
            },
        )

    @property
    def iterations(self) -> float:
        """Number of refinement cycles to perform"""
        return self.parameters.get("iterations")

    @property
    def focus(self) -> List[Any]:
        """Specific aspects to focus on during refinement (e.g., clarity, conciseness, evidence)"""
        return self.parameters.get("focus")

    @property
    def showProcess(self) -> bool:
        """Whether to show the intermediate steps in the refinement process"""
        return self.parameters.get("showProcess")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.iterations is not None and self.iterations < 1:
            raise ValueError(f"iterations must be at least 1, got {self.iterations}")
        if self.iterations is not None and self.iterations > 3:
            raise ValueError(f"iterations must be at most 3, got {self.iterations}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: A meta-decorator that iteratively improves the output based on specified criteria or dimensions
        instruction = f"Instructions for {self.name} decorator: "
        if self.iterations is not None:
            instruction += f"iterations={self.iterations}, "
        if self.focus is not None:
            instruction += f"focus={self.focus}, "
        if self.showProcess is not None:
            instruction += f"showProcess={self.showProcess}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"