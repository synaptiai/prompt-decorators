"""Implementation of the Alternatives decorator.

This module provides the Alternatives decorator class for use in prompt engineering.

Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    AlternativesDiversityEnum,
)


class Alternatives(BaseDecorator):
    """Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.

    Attributes:
        count: Number of alternative options or approaches to generate. (Any)
        diversity: How different or varied the alternatives should be from each other. (Literal["low", "medium", "high"])
        comparison: Whether to include a comparative analysis of the alternatives. (bool)
    """

    name = "alternatives"  # Class-level name for serialization
    decorator_name = "alternatives"
    version = "1.0.0"  # Initial version

    @property
    def name(self) -> str:
        """Get the name of the decorator.

        Args:
            self: The decorator instance


        Returns:
            The name of the decorator

        """
        return self.decorator_name

    def __init__(
        self,
        count: Any = 3,
        diversity: Literal["low", "medium", "high"] = "medium",
        comparison: bool = False,
    ) -> None:
        """Initialize the Alternatives decorator.

        Args:
            count: Number of alternative options or approaches to generate
            diversity: How different or varied the alternatives should be from each other
            comparison: Whether to include a comparative analysis of the alternatives


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._count = count
        self._diversity = diversity
        self._comparison = comparison

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._count = count
        self._diversity = diversity
        self._comparison = comparison

        # Validate parameters
        if self._count is not None:
            if not isinstance(self._count, (int, float)):
                raise ValidationError(
                    "The parameter 'count' must be a numeric type value."
                )
            if self._count < 2:
                raise ValidationError(
                    "The parameter 'count' must be greater than or equal to 2."
                )
            if self._count > 7:
                raise ValidationError(
                    "The parameter 'count' must be less than or equal to 7."
                )
        if self._diversity is not None:
            if not isinstance(self._diversity, str):
                raise ValidationError(
                    "The parameter 'diversity' must be a string type value."
                )
            if self._diversity not in ["low", "medium", "high"]:
                raise ValidationError(
                    f"The parameter 'diversity' must be one of the allowed enum values: ['low', 'medium', 'high']. Got {self._diversity}"
                )
        if self._comparison is not None:
            if not isinstance(self._comparison, bool):
                raise ValidationError(
                    "The parameter 'comparison' must be a boolean type value."
                )

    @property
    def count(self) -> Any:
        """Get the count parameter value.

        Args:
            self: The decorator instance

        Returns:
            The count parameter value
        """
        return self._count

    @property
    def diversity(self) -> Literal["low", "medium", "high"]:
        """Get the diversity parameter value.

        Args:
            self: The decorator instance

        Returns:
            The diversity parameter value
        """
        return self._diversity

    @property
    def comparison(self) -> bool:
        """Get the comparison parameter value.

        Args:
            self: The decorator instance

        Returns:
            The comparison parameter value
        """
        return self._comparison

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "alternatives",
            "parameters": {
                "count": self.count,
                "diversity": self.diversity,
                "comparison": self.comparison,
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
        if self.count is not None:
            params.append(f"count={self.count}")
        if self.diversity is not None:
            params.append(f"diversity={self.diversity}")
        if self.comparison is not None:
            params.append(f"comparison={self.comparison}")

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


        Args:
            cls: The decorator class

        """
        return {
            "name": cls.__name__,
            "description": """Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.""",
            "category": "general",
            "version": cls.version,
        }
