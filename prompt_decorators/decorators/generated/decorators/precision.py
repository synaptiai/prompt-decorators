"""
Precision Decorator

Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import PrecisionLevelEnum


class Precision(BaseDecorator):
    """Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity."""

    def __init__(
        self,
        level: Optional[PrecisionLevelEnum] = PrecisionLevelEnum.HIGH,
        units: Optional[bool] = True,
        definitions: Optional[bool] = False,
    ):
        """
        Initialize Precision decorator.

        Args:
            level: The degree of precision to apply
            units: Whether to consistently provide units for all measurements
            definitions: Whether to include precise definitions for key terms
        """
        super().__init__(
            name="Precision",
            version="1.0.0",
            parameters={
                "level": level,
                "units": units,
                "definitions": definitions,
            },
            metadata={
                "description": "Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def level(self) -> PrecisionLevelEnum:
        """The degree of precision to apply"""
        return self.parameters.get("level")

    @property
    def units(self) -> bool:
        """Whether to consistently provide units for all measurements"""
        return self.parameters.get("units")

    @property
    def definitions(self) -> bool:
        """Whether to include precise definitions for key terms"""
        return self.parameters.get("definitions")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Enhances responses with exact, specific, and precisely defined information
        instruction = f"Instructions for {self.name} decorator: "
        if self.level is not None:
            instruction += f"level={self.level}, "
        if self.units is not None:
            instruction += f"units={self.units}, "
        if self.definitions is not None:
            instruction += f"definitions={self.definitions}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"