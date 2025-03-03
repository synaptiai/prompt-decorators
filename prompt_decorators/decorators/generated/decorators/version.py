"""Implementation of the Version decorator.

This module provides the Version decorator class for use in prompt engineering.

Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Version(BaseDecorator):
    """Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.

    Attributes:
        standard: The semantic version of the Prompt Decorators standard to use. (str)
    """

    name = "version"  # Class-level name for serialization
    decorator_name = "version"
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
        standard: str,
    ) -> None:
        """Initialize the Version decorator.

        Args:
            standard: The semantic version of the Prompt Decorators standard to use

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._standard = standard

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._standard = standard

        # Validate parameters
        if self._standard is not None:
            if not isinstance(self._standard, str):
                raise ValidationError(
                    "The parameter 'standard' must be a string type value."
                )

    @property
    def standard(self) -> str:
        """Get the standard parameter value.

        Args:
            self: The decorator instance

        Returns:
            The standard parameter value
        """
        return self._standard

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "version",
            "parameters": {
                "standard": self.standard,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.standard is not None:
            params.append(f"standard={self.standard}")

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
            "description": """Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.""",
            "category": "general",
            "version": cls.version,
        }
