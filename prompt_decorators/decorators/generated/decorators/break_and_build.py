"""Implementation of the BreakAndBuild decorator.

This module provides the BreakAndBuild decorator class for use in prompt engineering.

Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    BreakAndBuildBreakdownEnum,
    BreakAndBuildIntensityEnum,
)


class BreakAndBuild(BaseDecorator):
    """Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.

    Attributes:
        breakdown: Primary approach for the critical breakdown phase. (Literal["weaknesses", "assumptions", "risks", "comprehensive"])
        intensity: How thorough and challenging the breakdown phase should be. (Literal["mild", "thorough", "intense"])
        buildRatio: Approximate ratio of build-up content to breakdown content (e.g., 2 means twice as much reconstruction as critique). (Any)
    """

    name = "break_and_build"  # Class-level name for serialization
    decorator_name = "break_and_build"
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
        breakdown: Literal[
            "weaknesses", "assumptions", "risks", "comprehensive"
        ] = "comprehensive",
        intensity: Literal["mild", "thorough", "intense"] = "thorough",
        buildRatio: Any = 1,
    ) -> None:
        """Initialize the BreakAndBuild decorator.

        Args:
            breakdown: Primary approach for the critical breakdown phase
            intensity: How thorough and challenging the breakdown phase should be
            buildRatio: Approximate ratio of build-up content to breakdown content (e.g., 2 means twice as much reconstruction as critique)

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._breakdown = breakdown
        self._intensity = intensity
        self._buildRatio = buildRatio

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._breakdown = breakdown
        self._intensity = intensity
        self._buildRatio = buildRatio

        # Validate parameters
        if self._breakdown is not None:
            if not isinstance(self._breakdown, str):
                raise ValidationError(
                    "The parameter 'breakdown' must be a string type value."
                )
            if self._breakdown not in [
                "weaknesses",
                "assumptions",
                "risks",
                "comprehensive",
            ]:
                raise ValidationError(
                    f"The parameter 'breakdown' must be one of the allowed enum values: ['weaknesses', 'assumptions', 'risks', 'comprehensive']. Got {self._breakdown}"
                )
        if self._intensity is not None:
            if not isinstance(self._intensity, str):
                raise ValidationError(
                    "The parameter 'intensity' must be a string type value."
                )
            if self._intensity not in ["mild", "thorough", "intense"]:
                raise ValidationError(
                    f"The parameter 'intensity' must be one of the allowed enum values: ['mild', 'thorough', 'intense']. Got {self._intensity}"
                )
        if self._buildRatio is not None:
            if not isinstance(self._buildRatio, (int, float)):
                raise ValidationError(
                    "The parameter 'buildRatio' must be a numeric type value."
                )
            if self._buildRatio < 0.5:
                raise ValidationError(
                    "The parameter 'buildRatio' must be greater than or equal to 0.5."
                )
            if self._buildRatio > 3:
                raise ValidationError(
                    "The parameter 'buildRatio' must be less than or equal to 3."
                )

    @property
    def breakdown(
        self,
    ) -> Literal["weaknesses", "assumptions", "risks", "comprehensive"]:
        """Get the breakdown parameter value.

        Args:
            self: The decorator instance

        Returns:
            The breakdown parameter value
        """
        return self._breakdown

    @property
    def intensity(self) -> Literal["mild", "thorough", "intense"]:
        """Get the intensity parameter value.

        Args:
            self: The decorator instance

        Returns:
            The intensity parameter value
        """
        return self._intensity

    @property
    def buildRatio(self) -> Any:
        """Get the buildRatio parameter value.

        Args:
            self: The decorator instance

        Returns:
            The buildRatio parameter value
        """
        return self._buildRatio

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "break_and_build",
            "parameters": {
                "breakdown": self.breakdown,
                "intensity": self.intensity,
                "buildRatio": self.buildRatio,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

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
            "description": """Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.""",
            "category": "general",
            "version": cls.version,
        }
