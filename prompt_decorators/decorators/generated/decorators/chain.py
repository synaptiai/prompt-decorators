"""
Chain Decorator

A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Chain(BaseDecorator):
    """A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline."""

    def __init__(
        self,
        decorators: List[Any],
        showSteps: Optional[bool] = False,
        stopOnFailure: Optional[bool] = True,
    ):
        """
        Initialize Chain decorator.

        Args:
            decorators: Ordered list of decorators to apply in sequence
            showSteps: Whether to show intermediate outputs after each decorator in the chain
            stopOnFailure: Whether to stop the chain if a decorator fails to apply correctly
        """
        super().__init__(
            name="Chain",
            version="1.0.0",
            parameters={
                "decorators": decorators,
                "showSteps": showSteps,
                "stopOnFailure": stopOnFailure,
            },
            metadata={
                "description": "A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.",
                "author": "Prompt Decorators Working Group",
                "category": "meta",
            },
        )

    @property
    def decorators(self) -> List[Any]:
        """Ordered list of decorators to apply in sequence"""
        return self.parameters.get("decorators")

    @property
    def showSteps(self) -> bool:
        """Whether to show intermediate outputs after each decorator in the chain"""
        return self.parameters.get("showSteps")

    @property
    def stopOnFailure(self) -> bool:
        """Whether to stop the chain if a decorator fails to apply correctly"""
        return self.parameters.get("stopOnFailure")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one
        instruction = f"Instructions for {self.name} decorator: "
        if self.decorators is not None:
            instruction += f"decorators={self.decorators}, "
        if self.showSteps is not None:
            instruction += f"showSteps={self.showSteps}, "
        if self.stopOnFailure is not None:
            instruction += f"stopOnFailure={self.stopOnFailure}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"