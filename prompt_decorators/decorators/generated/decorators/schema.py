"""
Schema Decorator

Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Schema(BaseDecorator):
    """Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs."""

    def __init__(
        self,
        schema: str,
        strict: Optional[bool] = False,
    ):
        """
        Initialize Schema decorator.

        Args:
            schema: JSON Schema definition or reference to a predefined schema that defines the structure of the response
            strict: Whether to enforce strict schema compliance or allow flexibility
        """
        super().__init__(
            name="Schema",
            version="1.0.0",
            parameters={
                "schema": schema,
                "strict": strict,
            },
            metadata={
                "description": "Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def schema(self) -> str:
        """JSON Schema definition or reference to a predefined schema that defines the structure of the response"""
        return self.parameters.get("schema")

    @property
    def strict(self) -> bool:
        """Whether to enforce strict schema compliance or allow flexibility"""
        return self.parameters.get("strict")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Defines a custom structure for the AI's response using a specified schema format
        instruction = f"Instructions for {self.name} decorator: "
        if self.schema is not None:
            instruction += f"schema={self.schema}, "
        if self.strict is not None:
            instruction += f"strict={self.strict}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"