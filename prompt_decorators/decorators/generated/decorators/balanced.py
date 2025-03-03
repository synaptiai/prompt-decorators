"""Implementation of the Balanced decorator.

This module provides the Balanced decorator class for use in prompt engineering.

Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    BalancedStructureEnum,
)


class Balanced(BaseDecorator):
    """Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position.

    Attributes:
        perspectives: Number of different perspectives to include. (Any)
        structure: How to structure the different perspectives. (Literal["alternating", "sequential", "comparative"])
        equal: Whether to strictly enforce equal word count for each perspective. (bool)
    """

    name = "balanced"  # Class-level name for serialization
    decorator_name = "balanced"
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
        perspectives: Any = 2,
        structure: Literal["alternating", "sequential", "comparative"] = "sequential",
        equal: bool = True,
    ) -> None:
        """Initialize the Balanced decorator.

        Args:
            perspectives: Number of different perspectives to include
            structure: How to structure the different perspectives
            equal: Whether to strictly enforce equal word count for each perspective

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._perspectives = perspectives
        self._structure = structure
        self._equal = equal

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._perspectives = perspectives
        self._structure = structure
        self._equal = equal

        # Validate parameters
        if self._perspectives is not None:
            if not isinstance(self._perspectives, (int, float)):
                raise ValidationError(
                    "The parameter 'perspectives' must be a numeric type value."
                )
            if self._perspectives < 2:
                raise ValidationError(
                    "The parameter 'perspectives' must be greater than or equal to 2."
                )
            if self._perspectives > 5:
                raise ValidationError(
                    "The parameter 'perspectives' must be less than or equal to 5."
                )
        if self._structure is not None:
            if not isinstance(self._structure, str):
                raise ValidationError(
                    "The parameter 'structure' must be a string type value."
                )
            if self._structure not in ["alternating", "sequential", "comparative"]:
                raise ValidationError(
                    f"The parameter 'structure' must be one of the allowed enum values: ['alternating', 'sequential', 'comparative']. Got {self._structure}"
                )
        if self._equal is not None:
            if not isinstance(self._equal, bool):
                raise ValidationError(
                    "The parameter 'equal' must be a boolean type value."
                )

    @property
    def perspectives(self) -> Any:
        """Get the perspectives parameter value.

        Args:
            self: The decorator instance

        Returns:
            The perspectives parameter value
        """
        return self._perspectives

    @property
    def structure(self) -> Literal["alternating", "sequential", "comparative"]:
        """Get the structure parameter value.

        Args:
            self: The decorator instance

        Returns:
            The structure parameter value
        """
        return self._structure

    @property
    def equal(self) -> bool:
        """Get the equal parameter value.

        Args:
            self: The decorator instance

        Returns:
            The equal parameter value
        """
        return self._equal

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "balanced",
            "parameters": {
                "perspectives": self.perspectives,
                "structure": self.structure,
                "equal": self.equal,
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
        if self.perspectives is not None:
            params.append(f"perspectives={self.perspectives}")
        if self.structure is not None:
            params.append(f"structure={self.structure}")
        if self.equal is not None:
            params.append(f"equal={self.equal}")

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
            "description": """Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position.""",
            "category": "general",
            "version": cls.version,
        }
