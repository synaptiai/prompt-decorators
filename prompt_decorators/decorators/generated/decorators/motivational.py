"""
Implementation of the Motivational decorator.

This module provides the Motivational decorator class for use in prompt engineering.

Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    MotivationalFocusEnum,
    MotivationalIntensityEnum,
)


class Motivational(BaseDecorator):
    """
    Enhances responses with encouraging, inspiring, and empowering
    language. This decorator is designed to motivate action, build
    confidence, and create a positive emotional impact while still
    delivering substantive content.

    Attributes:
        intensity: The level of motivational energy and enthusiasm
        focus: The primary motivational approach to emphasize
        actionable: Whether to include specific actionable steps or only inspirational content
    """

    decorator_name = "motivational"
    version = "1.0.0"  # Initial version

    @property
    def name(self) -> str:
        """
        Get the name of the decorator.

        Returns:
            The name of the decorator
        """
        return self.decorator_name

    def __init__(
        self,
        intensity: Literal["mild", "moderate", "high"] = "moderate",
        focus: Literal[
            "achievement", "growth", "resilience", "purpose", "balanced"
        ] = "balanced",
        actionable: bool = True,
    ) -> None:
        """
        Initialize the Motivational decorator.

        Args:
            intensity: The level of motivational energy and enthusiasm
            focus: The primary motivational approach to emphasize
            actionable: Whether to include specific actionable steps or only
                inspirational content

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._intensity = intensity
        self._focus = focus
        self._actionable = actionable

        # Validate parameters
        # Validate parameters
        if self._intensity is not None:
            if not isinstance(self._intensity, str):
                raise ValidationError(
                    "The parameter 'intensity' must be a string type value."
                )
            if self._intensity not in ["mild", "moderate", "high"]:
                raise ValidationError(
                    f"The parameter 'intensity' must be one of the allowed enum values: ['mild', 'moderate', 'high']. Got {self._intensity}"
                )
        if self._focus is not None:
            if not isinstance(self._focus, str):
                raise ValidationError(
                    "The parameter 'focus' must be a string type value."
                )
            if self._focus not in [
                "achievement",
                "growth",
                "resilience",
                "purpose",
                "balanced",
            ]:
                raise ValidationError(
                    f"The parameter 'focus' must be one of the allowed enum values: ['achievement', 'growth', 'resilience', 'purpose', 'balanced']. Got {self._focus}"
                )
        if self._actionable is not None:
            if not isinstance(self._actionable, bool):
                raise ValidationError(
                    "The parameter 'actionable' must be a boolean type value."
                )

    @property
    def intensity(self) -> Literal["mild", "moderate", "high"]:
        """
        Get the intensity parameter value.

        Args:
            self: The decorator instance

        Returns:
            The intensity parameter value
        """
        return self._intensity

    @property
    def focus(
        self,
    ) -> Literal["achievement", "growth", "resilience", "purpose", "balanced"]:
        """
        Get the focus parameter value.

        Args:
            self: The decorator instance

        Returns:
            The focus parameter value
        """
        return self._focus

    @property
    def actionable(self) -> bool:
        """
        Get the actionable parameter value.

        Args:
            self: The decorator instance

        Returns:
            The actionable parameter value
        """
        return self._actionable

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "motivational",
            "parameters": {
                "intensity": self.intensity,
                "focus": self.focus,
                "actionable": self.actionable,
            },
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.intensity is not None:
            params.append(f"intensity={self.intensity}")
        if self.focus is not None:
            params.append(f"focus={self.focus}")
        if self.actionable is not None:
            params.append(f"actionable={self.actionable}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt string.

        Args:
            prompt: The original prompt string

        Returns:
            The modified prompt string
        """
        # This is a placeholder implementation
        # Subclasses should override this method with specific behavior
        return prompt

    @classmethod
    def is_compatible_with_version(cls, version: str) -> bool:
        """
        Check if the decorator is compatible with a specific version.

        Args:
            version: The version to check compatibility with

        Returns:
            True if compatible, False otherwise

        Raises:
            IncompatibleVersionError: If the version is incompatible
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
        """
        Get metadata about the decorator.

        Returns:
            Dictionary containing metadata about the decorator
        """
        return {
            "name": cls.__name__,
            "description": """Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.""",
            "category": "general",
            "version": cls.version,
        }
