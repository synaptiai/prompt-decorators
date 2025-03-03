"""
Implementation of the BreakAndBuild decorator.

This module provides the BreakAndBuild decorator class for use in prompt engineering.

Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    BreakAndBuildBreakdownEnum,
    BreakAndBuildIntensityEnum,
)


class BreakAndBuild(BaseDecorator):
    """
    Structures responses in two distinct phases: first critically
    analyzing and 'breaking down' an idea by identifying flaws,
    assumptions, and weaknesses, then 'building it back up' with
    improvements, refinements, and solutions. This decorator enhances
    critical thinking while maintaining constructive output.

    Attributes:
        breakdown: Primary approach for the critical breakdown phase
        intensity: How thorough and challenging the breakdown phase should be
        buildRatio: Approximate ratio of build-up content to breakdown content (e.g., 2 means twice as much reconstruction as critique)
    """

    decorator_name = "break_and_build"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        breakdown: Literal["weaknesses", "assumptions", "risks", "comprehensive"] = "comprehensive",
        intensity: Literal["mild", "thorough", "intense"] = "thorough",
        buildRatio: Any = 1,
    ) -> None:
        """
        Initialize the BreakAndBuild decorator.

        Args:
            breakdown: Primary approach for the critical breakdown phase
            intensity: How thorough and challenging the breakdown phase should be
            buildRatio: Approximate ratio of build-up content to breakdown content
                (e.g., 2 means twice as much reconstruction as critique)

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._breakdown = breakdown
        self._intensity = intensity
        self._buildRatio = buildRatio

        # Validate parameters
        if self._breakdown is not None:
            valid_values = ["weaknesses", "assumptions", "risks", "comprehensive"]
            if self._breakdown not in valid_values:
                raise ValidationError("The parameter 'breakdown' must be one of the following values: " + ", ".join(valid_values))

        if self._intensity is not None:
            valid_values = ["mild", "thorough", "intense"]
            if self._intensity not in valid_values:
                raise ValidationError("The parameter 'intensity' must be one of the following values: " + ", ".join(valid_values))

        if self._buildRatio is not None:
            if not isinstance(self._buildRatio, (int, float)) or isinstance(self._buildRatio, bool):
                raise ValidationError("The parameter 'buildRatio' must be a numeric value.")


    @property
    def breakdown(self) -> Literal["weaknesses", "assumptions", "risks", "comprehensive"]:
        """
        Get the breakdown parameter value.

        Args:
            self: The decorator instance

        Returns:
            The breakdown parameter value
        """
        return self._breakdown

    @property
    def intensity(self) -> Literal["mild", "thorough", "intense"]:
        """
        Get the intensity parameter value.

        Args:
            self: The decorator instance

        Returns:
            The intensity parameter value
        """
        return self._intensity

    @property
    def buildRatio(self) -> Any:
        """
        Get the buildRatio parameter value.

        Args:
            self: The decorator instance

        Returns:
            The buildRatio parameter value
        """
        return self._buildRatio

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "break_and_build",
            "breakdown": self.breakdown,
            "intensity": self.intensity,
            "buildRatio": self.buildRatio,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.breakdown is not None:
            params.append(f"breakdown={self.breakdown}")
        if self.intensity is not None:
            params.append(f"intensity={self.intensity}")
        if self.buildRatio is not None:
            params.append(f"buildRatio={self.buildRatio}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"