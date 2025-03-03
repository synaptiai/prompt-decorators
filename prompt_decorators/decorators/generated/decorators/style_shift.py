"""Implementation of the StyleShift decorator.

This module provides the StyleShift decorator class for use in prompt engineering.

Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import StyleShiftAspectEnum


class StyleShift(BaseDecorator):
    """Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.

    Attributes:
        aspect: The specific style aspect to modify. (Literal["formality", "persuasion", "urgency", "confidence", "complexity"])
        level: The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal). (Any)
        maintain: Style aspects to explicitly maintain while modifying the target aspect. (List[Any])
    """

    name = "style_shift"  # Class-level name for serialization
    decorator_name = "style_shift"
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
        aspect: Literal[
            "formality", "persuasion", "urgency", "confidence", "complexity"
        ],
        level: Any = 3,
        maintain: List[Any] = None,
    ) -> None:
        """Initialize the StyleShift decorator.

        Args:
            aspect: The specific style aspect to modify
            level: The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal)
            maintain: Style aspects to explicitly maintain while modifying the target aspect

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._aspect = aspect
        self._level = level
        self._maintain = maintain

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._aspect = aspect
        self._level = level
        self._maintain = maintain

        # Validate parameters
        if self._aspect is not None:
            if not isinstance(self._aspect, str):
                raise ValidationError(
                    "The parameter 'aspect' must be a string type value."
                )
            if self._aspect not in [
                "formality",
                "persuasion",
                "urgency",
                "confidence",
                "complexity",
            ]:
                raise ValidationError(
                    f"The parameter 'aspect' must be one of the allowed enum values: ['formality', 'persuasion', 'urgency', 'confidence', 'complexity']. Got {self._aspect}"
                )
        if self._level is not None:
            if not isinstance(self._level, (int, float)):
                raise ValidationError(
                    "The parameter 'level' must be a numeric type value."
                )
            if self._level < 1:
                raise ValidationError(
                    "The parameter 'level' must be greater than or equal to 1."
                )
            if self._level > 5:
                raise ValidationError(
                    "The parameter 'level' must be less than or equal to 5."
                )
        if self._maintain is not None:
            if not isinstance(self._maintain, list):
                raise ValidationError(
                    "The parameter 'maintain' must be an array type value."
                )

    @property
    def aspect(
        self,
    ) -> Literal["formality", "persuasion", "urgency", "confidence", "complexity"]:
        """Get the aspect parameter value.

        Args:
            self: The decorator instance

        Returns:
            The aspect parameter value
        """
        return self._aspect

    @property
    def level(self) -> Any:
        """Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

    @property
    def maintain(self) -> List[Any]:
        """Get the maintain parameter value.

        Args:
            self: The decorator instance

        Returns:
            The maintain parameter value
        """
        return self._maintain

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "style_shift",
            "parameters": {
                "aspect": self.aspect,
                "level": self.level,
                "maintain": self.maintain,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

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
            "description": """Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.""",
            "category": "general",
            "version": cls.version,
        }
