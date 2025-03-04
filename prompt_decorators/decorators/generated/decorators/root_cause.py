"""Implementation of the RootCause decorator.

This module provides the RootCause decorator class for use in prompt engineering.

Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import RootCauseMethodEnum


class RootCause(BaseDecorator):
    """Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.

    Attributes:
        method: The specific root cause analysis methodology to apply. (Literal["fivewhys", "fishbone", "pareto"])
        depth: Level of detail in the analysis (for fivewhys, represents number of 'why' iterations). (Any)
    """

    name = "root_cause"  # Class-level name for serialization
    decorator_name = "root_cause"
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
        method: Literal["fivewhys", "fishbone", "pareto"] = "fivewhys",
        depth: Any = 5,
    ) -> None:
        """Initialize the RootCause decorator.

        Args:
            method: The specific root cause analysis methodology to apply
            depth: Level of detail in the analysis (for fivewhys, represents number of 'why' iterations)


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._method = method
        self._depth = depth

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._method = method
        self._depth = depth

        # Validate parameters
        if self._method is not None:
            if not isinstance(self._method, str):
                raise ValidationError(
                    "The parameter 'method' must be a string type value."
                )
            if self._method not in ["fivewhys", "fishbone", "pareto"]:
                raise ValidationError(
                    f"The parameter 'method' must be one of the allowed enum values: ['fivewhys', 'fishbone', 'pareto']. Got {self._method}"
                )
        if self._depth is not None:
            if not isinstance(self._depth, (int, float)):
                raise ValidationError(
                    "The parameter 'depth' must be a numeric type value."
                )
            if self._depth < 3:
                raise ValidationError(
                    "The parameter 'depth' must be greater than or equal to 3."
                )
            if self._depth > 7:
                raise ValidationError(
                    "The parameter 'depth' must be less than or equal to 7."
                )

    @property
    def method(self) -> Literal["fivewhys", "fishbone", "pareto"]:
        """Get the method parameter value.

        Args:
            self: The decorator instance

        Returns:
            The method parameter value
        """
        return self._method

    @property
    def depth(self) -> Any:
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
            "name": "root_cause",
            "parameters": {
                "method": self.method,
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
        if self.method is not None:
            params.append(f"method={self.method}")
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
            "description": """Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.""",
            "category": "general",
            "version": cls.version,
        }
