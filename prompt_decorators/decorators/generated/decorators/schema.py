"""
Implementation of the Schema decorator.

This module provides the Schema decorator class for use in prompt engineering.

Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Schema(BaseDecorator):
    """
    Defines a custom structure for the AI's response using a specified
    schema format. This decorator enables precise control over the output
    structure, ensuring responses follow a consistent, well-defined format
    optimized for specific use cases or data processing needs.

    Attributes:
        schema: JSON Schema definition or reference to a predefined schema that defines the structure of the response
        strict: Whether to enforce strict schema compliance or allow flexibility
    """

    decorator_name = "schema"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        schema: str,
        strict: bool = False,
    ) -> None:
        """
        Initialize the Schema decorator.

        Args:
            schema: JSON Schema definition or reference to a predefined schema
                that defines the structure of the response
            strict: Whether to enforce strict schema compliance or allow
                flexibility

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._schema = schema
        self._strict = strict

        # Validate parameters
        if self._schema is None:
            raise ValidationError("The parameter 'schema' is required for Schema decorator.")

        if self._schema is not None:
            if not isinstance(self._schema, str):
                raise ValidationError("The parameter 'schema' must be a string value.")

        if self._strict is not None:
            if not isinstance(self._strict, bool):
                raise ValidationError("The parameter 'strict' must be a boolean value.")


    @property
    def schema(self) -> str:
        """
        Get the schema parameter value.

        Args:
            self: The decorator instance

        Returns:
            The schema parameter value
        """
        return self._schema

    @property
    def strict(self) -> bool:
        """
        Get the strict parameter value.

        Args:
            self: The decorator instance

        Returns:
            The strict parameter value
        """
        return self._strict

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "schema",
            "schema": self.schema,
            "strict": self.strict,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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