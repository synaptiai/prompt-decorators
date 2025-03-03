"""
Implementation of the StyleShift decorator.

This module provides the StyleShift decorator class for use in prompt engineering.

Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.
"""

from typing import Any, Dict, List, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class StyleShift(BaseDecorator):
    """
    Modifies specific style characteristics of responses such as
    formality, persuasiveness, or urgency. This decorator enables fine-
    tuned control over particular aspects of communication style without
    changing the overall tone.

    Attributes:
        aspect: The specific style aspect to modify
        level: The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal)
        maintain: Style aspects to explicitly maintain while modifying the target aspect
    """

    decorator_name = "style_shift"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        aspect: Literal[
            "formality", "persuasion", "urgency", "confidence", "complexity"
        ],
        level: Any = 3,
        maintain: List[Any] = None,
    ) -> None:
        """
        Initialize the StyleShift decorator.

        Args:
            aspect: The specific style aspect to modify
            level: The intensity level of the style aspect (1-5, where 1 is
                minimal and 5 is maximal)
            maintain: Style aspects to explicitly maintain while modifying the
                target aspect

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._aspect = aspect
        self._level = level
        self._maintain = maintain

        # Validate parameters
        if self._aspect is None:
            raise ValidationError(
                "The parameter 'aspect' is required for StyleShift decorator."
            )

        if self._aspect is not None:
            valid_values = [
                "formality",
                "persuasion",
                "urgency",
                "confidence",
                "complexity",
            ]
            if self._aspect not in valid_values:
                raise ValidationError(
                    "The parameter 'aspect' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._level is not None:
            if not isinstance(self._level, (int, float)) or isinstance(
                self._level, bool
            ):
                raise ValidationError("The parameter 'level' must be a numeric value.")

        if self._maintain is not None:
            if not isinstance(self._maintain, (list, tuple)):
                raise ValidationError("The parameter 'maintain' must be an array.")

    @property
    def aspect(
        self,
    ) -> Literal["formality", "persuasion", "urgency", "confidence", "complexity"]:
        """
        Get the aspect parameter value.

        Args:
            self: The decorator instance

        Returns:
            The aspect parameter value
        """
        return self._aspect

    @property
    def level(self) -> Any:
        """
        Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

    @property
    def maintain(self) -> List[Any]:
        """
        Get the maintain parameter value.

        Args:
            self: The decorator instance

        Returns:
            The maintain parameter value
        """
        return self._maintain

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "style_shift",
            "aspect": self.aspect,
            "level": self.level,
            "maintain": self.maintain,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.aspect is not None:
            params.append(f"aspect={self.aspect}")
        if self.level is not None:
            params.append(f"level={self.level}")
        if self.maintain is not None:
            params.append(f"maintain={self.maintain}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
