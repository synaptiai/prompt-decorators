"""
Implementation of the Motivational decorator.

This module provides the Motivational decorator class for use in prompt engineering.

Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


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
        if self._intensity is not None:
            valid_values = ["mild", "moderate", "high"]
            if self._intensity not in valid_values:
                raise ValidationError(
                    "The parameter 'intensity' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._focus is not None:
            valid_values = [
                "achievement",
                "growth",
                "resilience",
                "purpose",
                "balanced",
            ]
            if self._focus not in valid_values:
                raise ValidationError(
                    "The parameter 'focus' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._actionable is not None:
            if not isinstance(self._actionable, bool):
                raise ValidationError(
                    "The parameter 'actionable' must be a boolean value."
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
            "intensity": self.intensity,
            "focus": self.focus,
            "actionable": self.actionable,
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
