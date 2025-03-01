"""
Audience Decorator

Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import AudienceLevelEnum


class Audience(BaseDecorator):
    """Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts."""

    def __init__(
        self,
        level: Optional[AudienceLevelEnum] = AudienceLevelEnum.INTERMEDIATE,
        domain: Optional[str] = "general",
        examples: Optional[bool] = True,
    ):
        """
        Initialize Audience decorator.

        Args:
            level: The expertise level of the target audience
            domain: Specific knowledge domain or field for domain-specific terminology adaptation
            examples: Whether to include additional examples for clarity
        """
        super().__init__(
            name="Audience",
            version="1.0.0",
            parameters={
                "level": level,
                "domain": domain,
                "examples": examples,
            },
            metadata={
                "description": "Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def level(self) -> AudienceLevelEnum:
        """The expertise level of the target audience"""
        return self.parameters.get("level")

    @property
    def domain(self) -> str:
        """Specific knowledge domain or field for domain-specific terminology adaptation"""
        return self.parameters.get("domain")

    @property
    def examples(self) -> bool:
        """Whether to include additional examples for clarity"""
        return self.parameters.get("examples")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Adapts the response for a specific audience expertise level
        instruction = f"Instructions for {self.name} decorator: "
        if self.level is not None:
            instruction += f"level={self.level}, "
        if self.domain is not None:
            instruction += f"domain={self.domain}, "
        if self.examples is not None:
            instruction += f"examples={self.examples}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"