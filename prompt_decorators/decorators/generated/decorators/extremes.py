"""Implementation of the Extremes decorator.

This module provides the Extremes decorator class for use in prompt engineering.

Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import ExtremesVersionsEnum


class Extremes(BaseDecorator):
    """Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.

    Attributes:
        versions: Which extreme versions to include. (Literal["radical", "minimal", "both"])
        dimension: The specific dimension along which to explore extremes (e.g., 'cost', 'time', 'ambition', 'complexity'). (str)
        compare: Whether to include a comparative analysis of the extreme versions. (bool)
    """

    decorator_name = "extremes"
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
        versions: Literal["radical", "minimal", "both"] = "both",
        dimension: str = "ambition",
        compare: bool = True,
    ) -> None:
        """Initialize the Extremes decorator.

        Args:
            versions: Which extreme versions to include
            dimension: The specific dimension along which to explore extremes (e.g., 'cost', 'time', 'ambition', 'complexity')
            compare: Whether to include a comparative analysis of the extreme versions

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._versions = versions
        self._dimension = dimension
        self._compare = compare

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._versions = versions
        self._dimension = dimension
        self._compare = compare

        # Validate parameters
        if self._versions is not None:
            if not isinstance(self._versions, str):
                raise ValidationError(
                    "The parameter 'versions' must be a string type value."
                )
            if self._versions not in ["radical", "minimal", "both"]:
                raise ValidationError(
                    f"The parameter 'versions' must be one of the allowed enum values: ['radical', 'minimal', 'both']. Got {self._versions}"
                )
        if self._dimension is not None:
            if not isinstance(self._dimension, str):
                raise ValidationError(
                    "The parameter 'dimension' must be a string type value."
                )
        if self._compare is not None:
            if not isinstance(self._compare, bool):
                raise ValidationError(
                    "The parameter 'compare' must be a boolean type value."
                )

    @property
    def versions(self) -> Literal["radical", "minimal", "both"]:
        """Get the versions parameter value.

        Args:
            self: The decorator instance

        Returns:
            The versions parameter value
        """
        return self._versions

    @property
    def dimension(self) -> str:
        """Get the dimension parameter value.

        Args:
            self: The decorator instance

        Returns:
            The dimension parameter value
        """
        return self._dimension

    @property
    def compare(self) -> bool:
        """Get the compare parameter value.

        Args:
            self: The decorator instance

        Returns:
            The compare parameter value
        """
        return self._compare

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "extremes",
            "parameters": {
                "versions": self.versions,
                "dimension": self.dimension,
                "compare": self.compare,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.versions is not None:
            params.append(f"versions={self.versions}")
        if self.dimension is not None:
            params.append(f"dimension={self.dimension}")
        if self.compare is not None:
            params.append(f"compare={self.compare}")

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
            "description": """Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.""",
            "category": "general",
            "version": cls.version,
        }
