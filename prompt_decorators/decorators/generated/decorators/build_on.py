"""
Implementation of the BuildOn decorator.

This module provides the BuildOn decorator class for use in prompt engineering.

A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class BuildOn(BaseDecorator):
    """
    A meta-decorator that builds upon previous context or responses rather
    than starting from scratch. This enables continuity across
    interactions, allowing refinement, extension, or alteration of
    previous outputs in a coherent manner.

    Attributes:
        reference: What to build upon from the previous context
        approach: How to build upon the referenced content
        preserveStructure: Whether to maintain the structure of the referenced content
    """

    decorator_name = "build_on"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        reference: Literal["last", "specific", "all"] = "last",
        approach: Literal["extend", "refine", "contrast", "synthesize"] = "extend",
        preserveStructure: bool = True,
    ) -> None:
        """
        Initialize the BuildOn decorator.

        Args:
            reference: What to build upon from the previous context
            approach: How to build upon the referenced content
            preserveStructure: Whether to maintain the structure of the referenced content

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._reference = reference
        self._approach = approach
        self._preserveStructure = preserveStructure

        # Validate parameters
        if self._reference is not None:
            valid_values = ["last", "specific", "all"]
            if self._reference not in valid_values:
                raise ValidationError(
                    "The parameter 'reference' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._approach is not None:
            valid_values = ["extend", "refine", "contrast", "synthesize"]
            if self._approach not in valid_values:
                raise ValidationError(
                    "The parameter 'approach' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._preserveStructure is not None:
            if not isinstance(self._preserveStructure, bool):
                raise ValidationError(
                    "The parameter 'preserveStructure' must be a boolean value."
                )

    @property
    def reference(self) -> Literal["last", "specific", "all"]:
        """
        Get the reference parameter value.

        Args:
            self: The decorator instance

        Returns:
            The reference parameter value
        """
        return self._reference

    @property
    def approach(self) -> Literal["extend", "refine", "contrast", "synthesize"]:
        """
        Get the approach parameter value.

        Args:
            self: The decorator instance

        Returns:
            The approach parameter value
        """
        return self._approach

    @property
    def preserveStructure(self) -> bool:
        """
        Get the preserveStructure parameter value.

        Args:
            self: The decorator instance

        Returns:
            The preserveStructure parameter value
        """
        return self._preserveStructure

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "build_on",
            "reference": self.reference,
            "approach": self.approach,
            "preserveStructure": self.preserveStructure,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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
