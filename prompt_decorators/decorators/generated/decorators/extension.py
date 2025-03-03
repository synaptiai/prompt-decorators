"""Implementation of the Extension decorator.

This module provides the Extension decorator class for use in prompt engineering.

A meta-decorator that enables loading of community-defined decorators from external sources. This facilitates the use of specialized decorator packages, domain-specific extensions, or custom decorator libraries maintained by communities or organizations.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Extension(BaseDecorator):
    """A meta-decorator that enables loading of community-defined decorators from external sources. This facilitates the use of specialized decorator packages, domain-specific extensions, or custom decorator libraries maintained by communities or organizations.

    Attributes:
        source: URI or identifier for the extension package (e.g., URL, namespace, or registry identifier). (str)
        version: Specific version of the extension package to use. (str)
        decorators: Specific decorators to load from the extension (if empty, loads all decorators from the package). (List[Any])
    """

    name = "extension"  # Class-level name for serialization
    decorator_name = "extension"
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
        source: str,
        version: str = None,
        decorators: List[Any] = None,
    ) -> None:
        """Initialize the Extension decorator.

        Args:
            source: URI or identifier for the extension package (e.g., URL, namespace, or registry identifier)
            version: Specific version of the extension package to use
            decorators: Specific decorators to load from the extension (if empty, loads all decorators from the package)

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._source = source
        self._version = version
        self._decorators = decorators

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._source = source
        self._version = version
        self._decorators = decorators

        # Validate parameters
        if self._source is not None:
            if not isinstance(self._source, str):
                raise ValidationError(
                    "The parameter 'source' must be a string type value."
                )
        if self._version is not None:
            if not isinstance(self._version, str):
                raise ValidationError(
                    "The parameter 'version' must be a string type value."
                )
        if self._decorators is not None:
            if not isinstance(self._decorators, list):
                raise ValidationError(
                    "The parameter 'decorators' must be an array type value."
                )

    @property
    def source(self) -> str:
        """Get the source parameter value.

        Args:
            self: The decorator instance

        Returns:
            The source parameter value
        """
        return self._source

    @property
    def version(self) -> str:
        """Get the version parameter value.

        Args:
            self: The decorator instance

        Returns:
            The version parameter value
        """
        return self._version

    @property
    def decorators(self) -> List[Any]:
        """Get the decorators parameter value.

        Args:
            self: The decorator instance

        Returns:
            The decorators parameter value
        """
        return self._decorators

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "extension",
            "parameters": {
                "source": self.source,
                "version": self.version,
                "decorators": self.decorators,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.source is not None:
            params.append(f"source={self.source}")
        if self.version is not None:
            params.append(f"version={self.version}")
        if self.decorators is not None:
            params.append(f"decorators={self.decorators}")

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
            "description": """A meta-decorator that enables loading of community-defined decorators from external sources. This facilitates the use of specialized decorator packages, domain-specific extensions, or custom decorator libraries maintained by communities or organizations.""",
            "category": "general",
            "version": cls.version,
        }
