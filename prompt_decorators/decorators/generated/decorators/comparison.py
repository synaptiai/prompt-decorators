"""
Comparison Decorator

Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import ComparisonFormatEnum


class Comparison(BaseDecorator):
    """Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria."""

    def __init__(
        self,
        aspects: Optional[List[Any]] = None,
        format: Optional[ComparisonFormatEnum] = ComparisonFormatEnum.TABLE,
        highlight: Optional[bool] = True,
    ):
        """
        Initialize Comparison decorator.

        Args:
            aspects: Specific aspects or dimensions to compare
            format: The presentation format for the comparison
            highlight: Whether to explicitly emphasize key differences
        """
        super().__init__(
            name="Comparison",
            version="1.0.0",
            parameters={
                "aspects": aspects,
                "format": format,
                "highlight": highlight,
            },
            metadata={
                "description": "Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def aspects(self) -> List[Any]:
        """Specific aspects or dimensions to compare"""
        return self.parameters.get("aspects")

    @property
    def format(self) -> ComparisonFormatEnum:
        """The presentation format for the comparison"""
        return self.parameters.get("format")

    @property
    def highlight(self) -> bool:
        """Whether to explicitly emphasize key differences"""
        return self.parameters.get("highlight")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response as a direct comparison between multiple items, concepts, or approaches
        instruction = f"Instructions for {self.name} decorator: "
        if self.aspects is not None:
            instruction += f"aspects={self.aspects}, "
        if self.format is not None:
            instruction += f"format={self.format}, "
        if self.highlight is not None:
            instruction += f"highlight={self.highlight}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"