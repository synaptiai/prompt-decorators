"""Implementation of the Creative decorator.

This module provides the Creative decorator class for use in prompt engineering.

Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import CreativeLevelEnum


class Creative(BaseDecorator):
    """Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.

    Attributes:
        level: The degree of creative thinking to apply. (Literal["moderate", "high", "unconventional"])
        elements: Specific creative elements to incorporate (e.g., metaphor, wordplay, narrative). (List[Any])
        constraints: Optional creative constraints to work within. (List[Any])
    """

    name = "creative"  # Class-level name for serialization
    decorator_name = "creative"
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
        level: Literal["moderate", "high", "unconventional"] = "high",
        elements: List[Any] = None,
        constraints: List[Any] = None,
    ) -> None:
        """Initialize the Creative decorator.

        Args:
            level: The degree of creative thinking to apply
            elements: Specific creative elements to incorporate (e.g., metaphor, wordplay, narrative)
            constraints: Optional creative constraints to work within

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._level = level
        self._elements = elements
        self._constraints = constraints

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._level = level
        self._elements = elements
        self._constraints = constraints

        # Validate parameters
        if self._level is not None:
            if not isinstance(self._level, str):
                raise ValidationError(
                    "The parameter 'level' must be a string type value."
                )
            if self._level not in ["moderate", "high", "unconventional"]:
                raise ValidationError(
                    f"The parameter 'level' must be one of the allowed enum values: ['moderate', 'high', 'unconventional']. Got {self._level}"
                )
        if self._elements is not None:
            if not isinstance(self._elements, list):
                raise ValidationError(
                    "The parameter 'elements' must be an array type value."
                )
        if self._constraints is not None:
            if not isinstance(self._constraints, list):
                raise ValidationError(
                    "The parameter 'constraints' must be an array type value."
                )

    @property
    def level(self) -> Literal["moderate", "high", "unconventional"]:
        """Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

    @property
    def elements(self) -> List[Any]:
        """Get the elements parameter value.

        Args:
            self: The decorator instance

        Returns:
            The elements parameter value
        """
        return self._elements

    @property
    def constraints(self) -> List[Any]:
        """Get the constraints parameter value.

        Args:
            self: The decorator instance

        Returns:
            The constraints parameter value
        """
        return self._constraints

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "creative",
            "parameters": {
                "level": self.level,
                "elements": self.elements,
                "constraints": self.constraints,
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
        if self.elements is not None:
            params.append(f"elements={self.elements}")
        if self.constraints is not None:
            params.append(f"constraints={self.constraints}")

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
            "description": """Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.""",
            "category": "general",
            "version": cls.version,
        }
