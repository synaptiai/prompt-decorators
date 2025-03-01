"""
Version Decorator

Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Version(BaseDecorator):
    """Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version."""

    def __init__(
        self,
        standard: str,
    ):
        """
        Initialize Version decorator.

        Args:
            standard: The semantic version of the Prompt Decorators standard to use
        """
        super().__init__(
            name="Version",
            version="1.0.0",
            parameters={
                "standard": standard,
            },
            metadata={
                "description": "Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.",
                "author": "Prompt Decorators Working Group",
                "category": "minimal",
            },
        )

    @property
    def standard(self) -> str:
        """The semantic version of the Prompt Decorators standard to use"""
        return self.parameters.get("standard")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Specifies the version of the Prompt Decorators standard to use
        instruction = f"Instructions for {self.name} decorator: "
        if self.standard is not None:
            instruction += f"standard={self.standard}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"