"""
Timeline Decorator

Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import TimelineGranularityEnum, TimelineFormatEnum, TimelineDetailsEnum


class Timeline(BaseDecorator):
    """Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension."""

    def __init__(
        self,
        granularity: Optional[TimelineGranularityEnum] = TimelineGranularityEnum.YEAR,
        format: Optional[TimelineFormatEnum] = TimelineFormatEnum.LIST,
        details: Optional[TimelineDetailsEnum] = TimelineDetailsEnum.MODERATE,
    ):
        """
        Initialize Timeline decorator.

        Args:
            granularity: The level of time detail to include in the timeline
            format: The presentation format for the timeline
            details: The level of detail to include for each timeline event
        """
        super().__init__(
            name="Timeline",
            version="1.0.0",
            parameters={
                "granularity": granularity,
                "format": format,
                "details": details,
            },
            metadata={
                "description": "Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def granularity(self) -> TimelineGranularityEnum:
        """The level of time detail to include in the timeline"""
        return self.parameters.get("granularity")

    @property
    def format(self) -> TimelineFormatEnum:
        """The presentation format for the timeline"""
        return self.parameters.get("format")

    @property
    def details(self) -> TimelineDetailsEnum:
        """The level of detail to include for each timeline event"""
        return self.parameters.get("details")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Organizes information in chronological order, highlighting key events or developments over time
        instruction = f"Instructions for {self.name} decorator: "
        if self.granularity is not None:
            instruction += f"granularity={self.granularity}, "
        if self.format is not None:
            instruction += f"format={self.format}, "
        if self.details is not None:
            instruction += f"details={self.details}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"