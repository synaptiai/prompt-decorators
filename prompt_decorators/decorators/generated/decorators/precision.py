"""Implementation of the Precision decorator.

This module provides the Precision decorator class for use in prompt engineering.

Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import PrecisionLevelEnum


class Precision(BaseDecorator):
    """Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.

    Attributes:
        level: The degree of precision to apply. (Literal["moderate", "high", "scientific"])
        units: Whether to consistently provide units for all measurements. (bool)
        definitions: Whether to include precise definitions for key terms. (bool)
    """

    name = "precision"  # Class-level name for serialization
    decorator_name = "precision"
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
        level: Literal["moderate", "high", "scientific"] = "high",
        units: bool = True,
        definitions: bool = False,
    ) -> None:
        """Initialize the Precision decorator.

        Args:
            level: The degree of precision to apply
            units: Whether to consistently provide units for all measurements
            definitions: Whether to include precise definitions for key terms

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._level = level
        self._units = units
        self._definitions = definitions

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._level = level
        self._units = units
        self._definitions = definitions

        # Validate parameters
        if self._level is not None:
            if not isinstance(self._level, str):
                raise ValidationError(
                    "The parameter 'level' must be a string type value."
                )
            if self._level not in ["moderate", "high", "scientific"]:
                raise ValidationError(
                    f"The parameter 'level' must be one of the allowed enum values: ['moderate', 'high', 'scientific']. Got {self._level}"
                )
        if self._units is not None:
            if not isinstance(self._units, bool):
                raise ValidationError(
                    "The parameter 'units' must be a boolean type value."
                )
        if self._definitions is not None:
            if not isinstance(self._definitions, bool):
                raise ValidationError(
                    "The parameter 'definitions' must be a boolean type value."
                )

    @property
    def level(self) -> Literal["moderate", "high", "scientific"]:
        """Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

    @property
    def units(self) -> bool:
        """Get the units parameter value.

        Args:
            self: The decorator instance

        Returns:
            The units parameter value
        """
        return self._units

    @property
    def definitions(self) -> bool:
        """Get the definitions parameter value.

        Args:
            self: The decorator instance

        Returns:
            The definitions parameter value
        """
        return self._definitions

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "precision",
            "parameters": {
                "level": self.level,
                "units": self.units,
                "definitions": self.definitions,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Args:
            self: The decorator instance

        Returns:
            String representation of the decorator
        """
        params = []
        if self.level is not None:
            params.append(f"level={self.level}")
        if self.units is not None:
            params.append(f"units={self.units}")
        if self.definitions is not None:
            params.append(f"definitions={self.definitions}")

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
            "description": """Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.""",
            "category": "general",
            "version": cls.version,
        }
