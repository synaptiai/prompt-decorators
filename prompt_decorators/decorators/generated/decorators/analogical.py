"""Implementation of the Analogical decorator.

This module provides the Analogical decorator class for use in prompt engineering.

Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import AnalogicalDepthEnum


class Analogical(BaseDecorator):
    """Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.

    Attributes:
        domain: Specific domain or context to draw analogies from (if not specified, will choose appropriate domains). (str)
        count: Number of distinct analogies to provide. (Any)
        depth: Level of detail in developing the analogy. (Literal["brief", "moderate", "extended"])
    """

    name = "analogical"  # Class-level name for serialization
    decorator_name = "analogical"
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
        domain: str = "general",
        count: Any = 1,
        depth: Literal["brief", "moderate", "extended"] = "moderate",
    ) -> None:
        """Initialize the Analogical decorator.

        Args:
            domain: Specific domain or context to draw analogies from (if not specified, will choose appropriate domains)
            count: Number of distinct analogies to provide
            depth: Level of detail in developing the analogy


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._domain = domain
        self._count = count
        self._depth = depth

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._domain = domain
        self._count = count
        self._depth = depth

        # Validate parameters
        if self._domain is not None:
            if not isinstance(self._domain, str):
                raise ValidationError(
                    "The parameter 'domain' must be a string type value."
                )
        if self._count is not None:
            if not isinstance(self._count, (int, float)):
                raise ValidationError(
                    "The parameter 'count' must be a numeric type value."
                )
            if self._count < 1:
                raise ValidationError(
                    "The parameter 'count' must be greater than or equal to 1."
                )
            if self._count > 5:
                raise ValidationError(
                    "The parameter 'count' must be less than or equal to 5."
                )
        if self._depth is not None:
            if not isinstance(self._depth, str):
                raise ValidationError(
                    "The parameter 'depth' must be a string type value."
                )
            if self._depth not in ["brief", "moderate", "extended"]:
                raise ValidationError(
                    f"The parameter 'depth' must be one of the allowed enum values: ['brief', 'moderate', 'extended']. Got {self._depth}"
                )

    @property
    def domain(self) -> str:
        """Get the domain parameter value.

        Args:
            self: The decorator instance

        Returns:
            The domain parameter value
        """
        return self._domain

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
    def depth(self) -> Literal["brief", "moderate", "extended"]:
        """Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "analogical",
            "parameters": {
                "domain": self.domain,
                "count": self.count,
                "depth": self.depth,
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
        if self.domain is not None:
            params.append(f"domain={self.domain}")
        if self.count is not None:
            params.append(f"count={self.count}")
        if self.depth is not None:
            params.append(f"depth={self.depth}")

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
            "description": """Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.""",
            "category": "general",
            "version": cls.version,
        }
