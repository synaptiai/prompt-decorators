"""Implementation of the BuildOn decorator.

This module provides the BuildOn decorator class for use in prompt engineering.

A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    BuildOnApproachEnum,
    BuildOnReferenceEnum,
)


class BuildOn(BaseDecorator):
    """A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.

    Attributes:
        reference: What to build upon from the previous context. (Literal["last", "specific", "all"])
        approach: How to build upon the referenced content. (Literal["extend", "refine", "contrast", "synthesize"])
        preserveStructure: Whether to maintain the structure of the referenced content. (bool)
    """

    decorator_name = "build_on"
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
        reference: Literal["last", "specific", "all"] = "last",
        approach: Literal["extend", "refine", "contrast", "synthesize"] = "extend",
        preserveStructure: bool = True,
    ) -> None:
        """Initialize the BuildOn decorator.

        Args:
            reference: What to build upon from the previous context
            approach: How to build upon the referenced content
            preserveStructure: Whether to maintain the structure of the referenced content

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._reference = reference
        self._approach = approach
        self._preserveStructure = preserveStructure

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._reference = reference
        self._approach = approach
        self._preserveStructure = preserveStructure

        # Validate parameters
        if self._reference is not None:
            if not isinstance(self._reference, str):
                raise ValidationError(
                    "The parameter 'reference' must be a string type value."
                )
            if self._reference not in ["last", "specific", "all"]:
                raise ValidationError(
                    f"The parameter 'reference' must be one of the allowed enum values: ['last', 'specific', 'all']. Got {self._reference}"
                )
        if self._approach is not None:
            if not isinstance(self._approach, str):
                raise ValidationError(
                    "The parameter 'approach' must be a string type value."
                )
            if self._approach not in ["extend", "refine", "contrast", "synthesize"]:
                raise ValidationError(
                    f"The parameter 'approach' must be one of the allowed enum values: ['extend', 'refine', 'contrast', 'synthesize']. Got {self._approach}"
                )
        if self._preserveStructure is not None:
            if not isinstance(self._preserveStructure, bool):
                raise ValidationError(
                    "The parameter 'preserveStructure' must be a boolean type value."
                )

    @property
    def reference(self) -> Literal["last", "specific", "all"]:
        """Get the reference parameter value.

        Args:
            self: The decorator instance

        Returns:
            The reference parameter value
        """
        return self._reference

    @property
    def approach(self) -> Literal["extend", "refine", "contrast", "synthesize"]:
        """Get the approach parameter value.

        Args:
            self: The decorator instance

        Returns:
            The approach parameter value
        """
        return self._approach

    @property
    def preserveStructure(self) -> bool:
        """Get the preserveStructure parameter value.

        Args:
            self: The decorator instance

        Returns:
            The preserveStructure parameter value
        """
        return self._preserveStructure

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "build_on",
            "parameters": {
                "reference": self.reference,
                "approach": self.approach,
                "preserveStructure": self.preserveStructure,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.reference is not None:
            params.append(f"reference={self.reference}")
        if self.approach is not None:
            params.append(f"approach={self.approach}")
        if self.preserveStructure is not None:
            params.append(f"preserveStructure={self.preserveStructure}")

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
            "description": """A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.""",
            "category": "general",
            "version": cls.version,
        }
