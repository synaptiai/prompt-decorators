"""
Compatibility Decorator

A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Compatibility(BaseDecorator):
    """A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants."""

    def __init__(
        self,
        models: List[Any],
        fallback: Optional[str] = None,
        behaviors: Optional[str] = None,
    ):
        """
        Initialize Compatibility decorator.

        Args:
            models: List of specific models to adapt for (e.g., gpt-3.5-turbo, gpt-4, etc.)
            fallback: Decorator to apply if the current model doesn't match any in the models list
            behaviors: JSON string mapping model names to specific adaptations (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning", "gpt-4": "maximize detailed analysis"}')
        """
        super().__init__(
            name="Compatibility",
            version="1.0.0",
            parameters={
                "models": models,
                "fallback": fallback,
                "behaviors": behaviors,
            },
            metadata={
                "description": "A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.",
                "author": "Prompt Decorators Working Group",
                "category": "meta",
            },
        )

    @property
    def models(self) -> List[Any]:
        """List of specific models to adapt for (e.g., gpt-3.5-turbo, gpt-4, etc.)"""
        return self.parameters.get("models")

    @property
    def fallback(self) -> str:
        """Decorator to apply if the current model doesn't match any in the models list"""
        return self.parameters.get("fallback")

    @property
    def behaviors(self) -> str:
        """JSON string mapping model names to specific adaptations (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning", "gpt-4": "maximize detailed analysis"}')"""
        return self.parameters.get("behaviors")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: A meta-decorator that specifies model-specific adaptations or fall-back behaviors
        instruction = f"Instructions for {self.name} decorator: "
        if self.models is not None:
            instruction += f"models={self.models}, "
        if self.fallback is not None:
            instruction += f"fallback={self.fallback}, "
        if self.behaviors is not None:
            instruction += f"behaviors={self.behaviors}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"