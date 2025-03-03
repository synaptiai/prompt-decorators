"""Implementation of the Layered decorator.

This module provides the Layered decorator class for use in prompt engineering.

Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    LayeredLevelsEnum,
    LayeredProgressionEnum,
)


class Layered(BaseDecorator):
    """Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.

    Attributes:
        levels: The granularity of explanation levels to include. (Literal["sentence-paragraph-full", "basic-intermediate-advanced", "summary-detail-technical"])
        count: Number of distinct explanation layers to provide. (Any)
        progression: How to structure the progression between layers. (Literal["separate", "nested", "incremental"])
    """

    decorator_name = "layered"
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
        levels: Literal[
            "sentence-paragraph-full",
            "basic-intermediate-advanced",
            "summary-detail-technical",
        ] = "summary-detail-technical",
        count: Any = 3,
        progression: Literal["separate", "nested", "incremental"] = "separate",
    ) -> None:
        """Initialize the Layered decorator.

        Args:
            levels: The granularity of explanation levels to include
            count: Number of distinct explanation layers to provide
            progression: How to structure the progression between layers

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._levels = levels
        self._count = count
        self._progression = progression

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._levels = levels
        self._count = count
        self._progression = progression

        # Validate parameters
        if self._levels is not None:
            if not isinstance(self._levels, str):
                raise ValidationError(
                    "The parameter 'levels' must be a string type value."
                )
            if self._levels not in [
                "sentence-paragraph-full",
                "basic-intermediate-advanced",
                "summary-detail-technical",
            ]:
                raise ValidationError(
                    f"The parameter 'levels' must be one of the allowed enum values: ['sentence-paragraph-full', 'basic-intermediate-advanced', 'summary-detail-technical']. Got {self._levels}"
                )
        if self._count is not None:
            if not isinstance(self._count, (int, float)):
                raise ValidationError(
                    "The parameter 'count' must be a numeric type value."
                )
            if self._count < 2:
                raise ValidationError(
                    "The parameter 'count' must be greater than or equal to 2."
                )
            if self._count > 5:
                raise ValidationError(
                    "The parameter 'count' must be less than or equal to 5."
                )
        if self._progression is not None:
            if not isinstance(self._progression, str):
                raise ValidationError(
                    "The parameter 'progression' must be a string type value."
                )
            if self._progression not in ["separate", "nested", "incremental"]:
                raise ValidationError(
                    f"The parameter 'progression' must be one of the allowed enum values: ['separate', 'nested', 'incremental']. Got {self._progression}"
                )

    @property
    def levels(
        self,
    ) -> Literal[
        "sentence-paragraph-full",
        "basic-intermediate-advanced",
        "summary-detail-technical",
    ]:
        """Get the levels parameter value.

        Args:
            self: The decorator instance

        Returns:
            The levels parameter value
        """
        return self._levels

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
    def progression(self) -> Literal["separate", "nested", "incremental"]:
        """Get the progression parameter value.

        Args:
            self: The decorator instance

        Returns:
            The progression parameter value
        """
        return self._progression

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "layered",
            "parameters": {
                "levels": self.levels,
                "count": self.count,
                "progression": self.progression,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.levels is not None:
            params.append(f"levels={self.levels}")
        if self.count is not None:
            params.append(f"count={self.count}")
        if self.progression is not None:
            params.append(f"progression={self.progression}")

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
            "description": """Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.""",
            "category": "general",
            "version": cls.version,
        }
