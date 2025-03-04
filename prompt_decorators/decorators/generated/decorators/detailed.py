"""Implementation of the Detailed decorator.

This module provides the Detailed decorator class for use in prompt engineering.

Enhances the response with comprehensive information, thorough explanations, and rich context. This decorator is ideal for in-depth learning, complex topics requiring nuance, or when completeness is valued over brevity.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import DetailedDepthEnum


class Detailed(BaseDecorator):
    """Enhances the response with comprehensive information, thorough explanations, and rich context. This decorator is ideal for in-depth learning, complex topics requiring nuance, or when completeness is valued over brevity.

    Attributes:
        depth: The level of detail and comprehensiveness. (Literal["moderate", "comprehensive", "exhaustive"])
        aspects: Specific aspects or dimensions to explore in detail. (List[Any])
        examples: Whether to include detailed examples to illustrate points. (bool)
    """

    name = "detailed"  # Class-level name for serialization
    decorator_name = "detailed"
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
        depth: Literal["moderate", "comprehensive", "exhaustive"] = "comprehensive",
        aspects: List[Any] = None,
        examples: bool = True,
    ) -> None:
        """Initialize the Detailed decorator.

        Args:
            depth: The level of detail and comprehensiveness
            aspects: Specific aspects or dimensions to explore in detail
            examples: Whether to include detailed examples to illustrate points

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._depth = depth
        self._aspects = aspects
        self._examples = examples

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._depth = depth
        self._aspects = aspects
        self._examples = examples

        # Validate parameters
        if self._depth is not None:
            if not isinstance(self._depth, str):
                raise ValidationError(
                    "The parameter 'depth' must be a string type value."
                )
            if self._depth not in ["moderate", "comprehensive", "exhaustive"]:
                raise ValidationError(
                    f"The parameter 'depth' must be one of the allowed enum values: ['moderate', 'comprehensive', 'exhaustive']. Got {self._depth}"
                )
        if self._aspects is not None:
            if not isinstance(self._aspects, list):
                raise ValidationError(
                    "The parameter 'aspects' must be an array type value."
                )
        if self._examples is not None:
            if not isinstance(self._examples, bool):
                raise ValidationError(
                    "The parameter 'examples' must be a boolean type value."
                )

    @property
    def depth(self) -> Literal["moderate", "comprehensive", "exhaustive"]:
        """Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    @property
    def aspects(self) -> List[Any]:
        """Get the aspects parameter value.

        Args:
            self: The decorator instance

        Returns:
            The aspects parameter value
        """
        return self._aspects

    @property
    def examples(self) -> bool:
        """Get the examples parameter value.

        Args:
            self: The decorator instance

        Returns:
            The examples parameter value
        """
        return self._examples

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "detailed",
            "parameters": {
                "depth": self.depth,
                "aspects": self.aspects,
                "examples": self.examples,
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
        if self.depth is not None:
            params.append(f"depth={self.depth}")
        if self.aspects is not None:
            params.append(f"aspects={self.aspects}")
        if self.examples is not None:
            params.append(f"examples={self.examples}")

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
            "description": """Enhances the response with comprehensive information, thorough explanations, and rich context. This decorator is ideal for in-depth learning, complex topics requiring nuance, or when completeness is valued over brevity.""",
            "category": "general",
            "version": cls.version,
        }
