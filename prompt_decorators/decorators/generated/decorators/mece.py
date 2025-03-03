"""Implementation of the MECE decorator.

This module provides the MECE decorator class for use in prompt engineering.

Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import MECEFrameworkEnum


class MECE(BaseDecorator):
    """Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.

    Attributes:
        dimensions: Number of top-level MECE dimensions to use for categorization. (Any)
        depth: Maximum level of hierarchical breakdown within each dimension. (Any)
        framework: Optional predefined MECE framework to apply. (Literal["issue tree", "value chain", "business segments", "stakeholders", "custom"])
    """

    name = "mece"  # Class-level name for serialization
    decorator_name = "mece"
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
        dimensions: Any = 3,
        depth: Any = 2,
        framework: Literal[
            "issue tree", "value chain", "business segments", "stakeholders", "custom"
        ] = "custom",
    ) -> None:
        """Initialize the MECE decorator.

        Args:
            dimensions: Number of top-level MECE dimensions to use for categorization
            depth: Maximum level of hierarchical breakdown within each dimension
            framework: Optional predefined MECE framework to apply

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._dimensions = dimensions
        self._depth = depth
        self._framework = framework

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._dimensions = dimensions
        self._depth = depth
        self._framework = framework

        # Validate parameters
        if self._dimensions is not None:
            if not isinstance(self._dimensions, (int, float)):
                raise ValidationError(
                    "The parameter 'dimensions' must be a numeric type value."
                )
            if self._dimensions < 2:
                raise ValidationError(
                    "The parameter 'dimensions' must be greater than or equal to 2."
                )
            if self._dimensions > 5:
                raise ValidationError(
                    "The parameter 'dimensions' must be less than or equal to 5."
                )
        if self._depth is not None:
            if not isinstance(self._depth, (int, float)):
                raise ValidationError(
                    "The parameter 'depth' must be a numeric type value."
                )
            if self._depth < 1:
                raise ValidationError(
                    "The parameter 'depth' must be greater than or equal to 1."
                )
            if self._depth > 3:
                raise ValidationError(
                    "The parameter 'depth' must be less than or equal to 3."
                )
        if self._framework is not None:
            if not isinstance(self._framework, str):
                raise ValidationError(
                    "The parameter 'framework' must be a string type value."
                )
            if self._framework not in [
                "issue tree",
                "value chain",
                "business segments",
                "stakeholders",
                "custom",
            ]:
                raise ValidationError(
                    f"The parameter 'framework' must be one of the allowed enum values: ['issue tree', 'value chain', 'business segments', 'stakeholders', 'custom']. Got {self._framework}"
                )

    @property
    def dimensions(self) -> Any:
        """Get the dimensions parameter value.

        Args:
            self: The decorator instance

        Returns:
            The dimensions parameter value
        """
        return self._dimensions

    @property
    def depth(self) -> Any:
        """Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    @property
    def framework(
        self,
    ) -> Literal[
        "issue tree", "value chain", "business segments", "stakeholders", "custom"
    ]:
        """Get the framework parameter value.

        Args:
            self: The decorator instance

        Returns:
            The framework parameter value
        """
        return self._framework

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "mece",
            "parameters": {
                "dimensions": self.dimensions,
                "depth": self.depth,
                "framework": self.framework,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.dimensions is not None:
            params.append(f"dimensions={self.dimensions}")
        if self.depth is not None:
            params.append(f"depth={self.depth}")
        if self.framework is not None:
            params.append(f"framework={self.framework}")

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
            "description": """Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.""",
            "category": "general",
            "version": cls.version,
        }
