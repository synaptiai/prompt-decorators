"""
Implementation of the Precision decorator.

This module provides the Precision decorator class for use in prompt engineering.

Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    PrecisionLevelEnum,
)


class Precision(BaseDecorator):
    """
    Enhances responses with exact, specific, and precisely defined
    information. This decorator prioritizes accuracy in measurements,
    terms, definitions, and claims, avoiding vague language in favor of
    concrete specificity.

    Attributes:
        level: The degree of precision to apply
        units: Whether to consistently provide units for all measurements
        definitions: Whether to include precise definitions for key terms
    """

    decorator_name = "precision"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        level: Literal["moderate", "high", "scientific"] = "high",
        units: bool = True,
        definitions: bool = False,
    ) -> None:
        """
        Initialize the Precision decorator.

        Args:
            level: The degree of precision to apply
            units: Whether to consistently provide units for all measurements
            definitions: Whether to include precise definitions for key terms

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._level = level
        self._units = units
        self._definitions = definitions

        # Validate parameters
        if self._level is not None:
            valid_values = ["moderate", "high", "scientific"]
            if self._level not in valid_values:
                raise ValidationError("The parameter 'level' must be one of the following values: " + ", ".join(valid_values))

        if self._units is not None:
            if not isinstance(self._units, bool):
                raise ValidationError("The parameter 'units' must be a boolean value.")

        if self._definitions is not None:
            if not isinstance(self._definitions, bool):
                raise ValidationError("The parameter 'definitions' must be a boolean value.")


    @property
    def level(self) -> Literal["moderate", "high", "scientific"]:
        """
        Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

    @property
    def units(self) -> bool:
        """
        Get the units parameter value.

        Args:
            self: The decorator instance

        Returns:
            The units parameter value
        """
        return self._units

    @property
    def definitions(self) -> bool:
        """
        Get the definitions parameter value.

        Args:
            self: The decorator instance

        Returns:
            The definitions parameter value
        """
        return self._definitions

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "precision",
            "level": self.level,
            "units": self.units,
            "definitions": self.definitions,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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