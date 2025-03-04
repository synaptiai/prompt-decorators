"""Implementation of the Schema decorator.

This module provides the Schema decorator class for use in prompt engineering.

Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Schema(BaseDecorator):
    """Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs.

    Attributes:
        schema: JSON Schema definition or reference to a predefined schema that defines the structure of the response. (str)
        strict: Whether to enforce strict schema compliance or allow flexibility. (bool)
    """

    name = "schema"  # Class-level name for serialization
    decorator_name = "schema"
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
        schema: str,
        strict: bool = False,
    ) -> None:
        """Initialize the Schema decorator.

        Args:
            schema: JSON Schema definition or reference to a predefined schema that defines the structure of the response
            strict: Whether to enforce strict schema compliance or allow flexibility

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._schema = schema
        self._strict = strict

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._schema = schema
        self._strict = strict

        # Validate parameters
        if self._schema is not None:
            if not isinstance(self._schema, str):
                raise ValidationError(
                    "The parameter 'schema' must be a string type value."
                )
        if self._strict is not None:
            if not isinstance(self._strict, bool):
                raise ValidationError(
                    "The parameter 'strict' must be a boolean type value."
                )

    @property
    def schema(self) -> str:
        """Get the schema parameter value.

        Args:
            self: The decorator instance

        Returns:
            The schema parameter value
        """
        return self._schema

    @property
    def strict(self) -> bool:
        """Get the strict parameter value.

        Args:
            self: The decorator instance

        Returns:
            The strict parameter value
        """
        return self._strict

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "schema",
            "parameters": {
                "schema": self.schema,
                "strict": self.strict,
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
        if self.schema is not None:
            params.append(f"schema={self.schema}")
        if self.strict is not None:
            params.append(f"strict={self.strict}")

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
            "description": """Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs.""",
            "category": "general",
            "version": cls.version,
        }
