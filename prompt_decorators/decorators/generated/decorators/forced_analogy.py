"""
ForcedAnalogy Decorator

Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import ForcedAnalogyComprehensivenessEnum


class ForcedAnalogy(BaseDecorator):
    """Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable."""

    def __init__(
        self,
        source: str,
        comprehensiveness: Optional[ForcedAnalogyComprehensivenessEnum] = ForcedAnalogyComprehensivenessEnum.COMPREHENSIVE,
        mappings: Optional[float] = 3,
    ):
        """
        Initialize ForcedAnalogy decorator.

        Args:
            source: The specific domain, field, or context to draw analogies from
            comprehensiveness: How comprehensively to map concepts between domains
            mappings: Number of distinct concept mappings to create between domains
        """
        super().__init__(
            name="ForcedAnalogy",
            version="1.0.0",
            parameters={
                "source": source,
                "comprehensiveness": comprehensiveness,
                "mappings": mappings,
            },
            metadata={
                "description": "Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.",
                "author": "Prompt Decorators Working Group",
                "category": "reasoning",
            },
        )

    @property
    def source(self) -> str:
        """The specific domain, field, or context to draw analogies from"""
        return self.parameters.get("source")

    @property
    def comprehensiveness(self) -> ForcedAnalogyComprehensivenessEnum:
        """How comprehensively to map concepts between domains"""
        return self.parameters.get("comprehensiveness")

    @property
    def mappings(self) -> float:
        """Number of distinct concept mappings to create between domains"""
        return self.parameters.get("mappings")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.mappings is not None and self.mappings < 1:
            raise ValueError(f"mappings must be at least 1, got {self.mappings}")
        if self.mappings is not None and self.mappings > 7:
            raise ValueError(f"mappings must be at most 7, got {self.mappings}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Explains concepts by specifically comparing them to a particular domain or field
        instruction = f"Instructions for {self.name} decorator: "
        if self.source is not None:
            instruction += f"source={self.source}, "
        if self.comprehensiveness is not None:
            instruction += f"comprehensiveness={self.comprehensiveness}, "
        if self.mappings is not None:
            instruction += f"mappings={self.mappings}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"