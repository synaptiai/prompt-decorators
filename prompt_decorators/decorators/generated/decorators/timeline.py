"""Implementation of the Timeline decorator.

This module provides the Timeline decorator class for use in prompt engineering.

Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    TimelineDetailsEnum,
    TimelineFormatEnum,
    TimelineGranularityEnum,
)


class Timeline(BaseDecorator):
    """Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.

    Attributes:
        granularity: The level of time detail to include in the timeline. (Literal["day", "month", "year", "decade", "century", "era"])
        format: The presentation format for the timeline. (Literal["list", "narrative", "table"])
        details: The level of detail to include for each timeline event. (Literal["minimal", "moderate", "comprehensive"])
    """

    decorator_name = "timeline"
    version = "1.0.0"  # Initial version

    @property
    def name(self) -> str:
        """Get the name of the decorator.

        Returns:
            The name of the decorator

        """
        return self.decorator_name

    def __init__(
        self,
        granularity: Literal[
            "day", "month", "year", "decade", "century", "era"
        ] = "year",
        format: Literal["list", "narrative", "table"] = "list",
        details: Literal["minimal", "moderate", "comprehensive"] = "moderate",
    ) -> None:
        """Initialize the Timeline decorator.

        Args:
            granularity: The level of time detail to include in the timeline
            format: The presentation format for the timeline
            details: The level of detail to include for each timeline event

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._granularity = granularity
        self._format = format
        self._details = details

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._granularity = granularity
        self._format = format
        self._details = details

        # Validate parameters
        if self._granularity is not None:
            if not isinstance(self._granularity, str):
                raise ValidationError(
                    "The parameter 'granularity' must be a string type value."
                )
            if self._granularity not in [
                "day",
                "month",
                "year",
                "decade",
                "century",
                "era",
            ]:
                raise ValidationError(
                    f"The parameter 'granularity' must be one of the allowed enum values: ['day', 'month', 'year', 'decade', 'century', 'era']. Got {self._granularity}"
                )
        if self._format is not None:
            if not isinstance(self._format, str):
                raise ValidationError(
                    "The parameter 'format' must be a string type value."
                )
            if self._format not in ["list", "narrative", "table"]:
                raise ValidationError(
                    f"The parameter 'format' must be one of the allowed enum values: ['list', 'narrative', 'table']. Got {self._format}"
                )
        if self._details is not None:
            if not isinstance(self._details, str):
                raise ValidationError(
                    "The parameter 'details' must be a string type value."
                )
            if self._details not in ["minimal", "moderate", "comprehensive"]:
                raise ValidationError(
                    f"The parameter 'details' must be one of the allowed enum values: ['minimal', 'moderate', 'comprehensive']. Got {self._details}"
                )

    @property
    def granularity(
        self,
    ) -> Literal["day", "month", "year", "decade", "century", "era"]:
        """Get the granularity parameter value.

        Args:
            self: The decorator instance

        Returns:
            The granularity parameter value
        """
        return self._granularity

    @property
    def format(self) -> Literal["list", "narrative", "table"]:
        """Get the format parameter value.

        Args:
            self: The decorator instance

        Returns:
            The format parameter value
        """
        return self._format

    @property
    def details(self) -> Literal["minimal", "moderate", "comprehensive"]:
        """Get the details parameter value.

        Args:
            self: The decorator instance

        Returns:
            The details parameter value
        """
        return self._details

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "timeline",
            "parameters": {
                "granularity": self.granularity,
                "format": self.format,
                "details": self.details,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

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

    def apply(self, prompt: str) -> str:
        """Apply the decorator to a prompt string.

        Args:
            prompt: The prompt to apply the decorator to


        Returns:
            The modified prompt

        """
        # Subclasses should override this method with specific behavior
        return prompt

    @classmethod
    def is_compatible_with_version(cls, version: str) -> bool:
        """Check if the decorator is compatible with a specific version.

        Args:
            version: The version to check compatibility with.


        Returns:
            True if compatible, False otherwise.


        Raises:
            IncompatibleVersionError: If the version is incompatible.

        """
        # Check version compatibility
        if version > cls.version:
            raise IncompatibleVersionError(
                f"Version {version} is not compatible with {cls.__name__}. "
                f"Maximum compatible version is {cls.version}."
            )
        # For testing purposes, also raise for very old versions
        if version < "0.1.0":
            raise IncompatibleVersionError(
                f"Version {version} is too old for {cls.__name__}. "
                f"Minimum compatible version is 0.1.0."
            )
        return True

    @classmethod
    def get_metadata(cls) -> Dict[str, Any]:
        """Get metadata about the decorator.

        Returns:
            Dictionary containing metadata about the decorator

        """
        return {
            "name": cls.__name__,
            "description": """Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.""",
            "category": "general",
            "version": cls.version,
        }
