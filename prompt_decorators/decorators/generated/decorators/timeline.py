"""
Implementation of the Timeline decorator.

This module provides the Timeline decorator class for use in prompt engineering.

Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    TimelineGranularityEnum,
    TimelineFormatEnum,
    TimelineDetailsEnum,
)


class Timeline(BaseDecorator):
    """
    Organizes information in chronological order, highlighting key events
    or developments over time. This decorator is ideal for historical
    accounts, project planning, process evolution, or any topic with a
    temporal dimension.

    Attributes:
        granularity: The level of time detail to include in the timeline
        format: The presentation format for the timeline
        details: The level of detail to include for each timeline event
    """

    decorator_name = "timeline"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        granularity: Literal["day", "month", "year", "decade", "century", "era"] = "year",
        format: Literal["list", "narrative", "table"] = "list",
        details: Literal["minimal", "moderate", "comprehensive"] = "moderate",
    ) -> None:
        """
        Initialize the Timeline decorator.

        Args:
            granularity: The level of time detail to include in the timeline
            format: The presentation format for the timeline
            details: The level of detail to include for each timeline event

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._granularity = granularity
        self._format = format
        self._details = details

        # Validate parameters
        if self._granularity is not None:
            valid_values = ["day", "month", "year", "decade", "century", "era"]
            if self._granularity not in valid_values:
                raise ValidationError("The parameter 'granularity' must be one of the following values: " + ", ".join(valid_values))

        if self._format is not None:
            valid_values = ["list", "narrative", "table"]
            if self._format not in valid_values:
                raise ValidationError("The parameter 'format' must be one of the following values: " + ", ".join(valid_values))

        if self._details is not None:
            valid_values = ["minimal", "moderate", "comprehensive"]
            if self._details not in valid_values:
                raise ValidationError("The parameter 'details' must be one of the following values: " + ", ".join(valid_values))


    @property
    def granularity(self) -> Literal["day", "month", "year", "decade", "century", "era"]:
        """
        Get the granularity parameter value.

        Args:
            self: The decorator instance

        Returns:
            The granularity parameter value
        """
        return self._granularity

    @property
    def format(self) -> Literal["list", "narrative", "table"]:
        """
        Get the format parameter value.

        Args:
            self: The decorator instance

        Returns:
            The format parameter value
        """
        return self._format

    @property
    def details(self) -> Literal["minimal", "moderate", "comprehensive"]:
        """
        Get the details parameter value.

        Args:
            self: The decorator instance

        Returns:
            The details parameter value
        """
        return self._details

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "timeline",
            "granularity": self.granularity,
            "format": self.format,
            "details": self.details,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.granularity is not None:
            params.append(f"granularity={self.granularity}")
        if self.format is not None:
            params.append(f"format={self.format}")
        if self.details is not None:
            params.append(f"details={self.details}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"