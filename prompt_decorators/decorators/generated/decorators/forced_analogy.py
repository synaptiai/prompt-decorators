"""
Implementation of the ForcedAnalogy decorator.

This module provides the ForcedAnalogy decorator class for use in prompt engineering.

Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    ForcedAnalogyComprehensivenessEnum,
)


class ForcedAnalogy(BaseDecorator):
    """
    Explains concepts by specifically comparing them to a particular
    domain or field. This decorator forces analogies from a specified
    source domain to make complex or unfamiliar topics more relatable and
    understandable.

    Attributes:
        source: The specific domain, field, or context to draw analogies from
        comprehensiveness: How comprehensively to map concepts between domains
        mappings: Number of distinct concept mappings to create between domains
    """

    decorator_name = "forced_analogy"
    version = "1.0.0"  # Initial version

    @property
    def name(self) -> str:
        """
        Get the name of the decorator.

        Returns:
            The name of the decorator
        """
        return self.decorator_name

    def __init__(
        self,
        source: str,
        comprehensiveness: Literal[
            "basic", "comprehensive", "detailed"
        ] = "comprehensive",
        mappings: Any = 3,
    ) -> None:
        """
        Initialize the ForcedAnalogy decorator.

        Args:
            source: The specific domain, field, or context to draw analogies
                from
            comprehensiveness: How comprehensively to map concepts between domains
            mappings: Number of distinct concept mappings to create between
                domains

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._source = source
        self._comprehensiveness = comprehensiveness
        self._mappings = mappings

        # Validate parameters
        # Validate parameters
        if self._source is not None:
            if not isinstance(self._source, str):
                raise ValidationError(
                    "The parameter 'source' must be a string type value."
                )
        if self._comprehensiveness is not None:
            if not isinstance(self._comprehensiveness, str):
                raise ValidationError(
                    "The parameter 'comprehensiveness' must be a string type value."
                )
            if self._comprehensiveness not in ["basic", "comprehensive", "detailed"]:
                raise ValidationError(
                    f"The parameter 'comprehensiveness' must be one of the allowed enum values: ['basic', 'comprehensive', 'detailed']. Got {self._comprehensiveness}"
                )
        if self._mappings is not None:
            if not isinstance(self._mappings, (int, float)):
                raise ValidationError(
                    "The parameter 'mappings' must be a numeric type value."
                )
            if self._mappings < 1:
                raise ValidationError(
                    "The parameter 'mappings' must be greater than or equal to 1."
                )
            if self._mappings > 7:
                raise ValidationError(
                    "The parameter 'mappings' must be less than or equal to 7."
                )

    @property
    def source(self) -> str:
        """
        Get the source parameter value.

        Args:
            self: The decorator instance

        Returns:
            The source parameter value
        """
        return self._source

    @property
    def comprehensiveness(self) -> Literal["basic", "comprehensive", "detailed"]:
        """
        Get the comprehensiveness parameter value.

        Args:
            self: The decorator instance

        Returns:
            The comprehensiveness parameter value
        """
        return self._comprehensiveness

    @property
    def mappings(self) -> Any:
        """
        Get the mappings parameter value.

        Args:
            self: The decorator instance

        Returns:
            The mappings parameter value
        """
        return self._mappings

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "forced_analogy",
            "parameters": {
                "source": self.source,
                "comprehensiveness": self.comprehensiveness,
                "mappings": self.mappings,
            },
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.source is not None:
            params.append(f"source={self.source}")
        if self.comprehensiveness is not None:
            params.append(f"comprehensiveness={self.comprehensiveness}")
        if self.mappings is not None:
            params.append(f"mappings={self.mappings}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt string.

        Args:
            prompt: The original prompt string

        Returns:
            The modified prompt string
        """
        # This is a placeholder implementation
        # Subclasses should override this method with specific behavior
        return prompt

    @classmethod
    def is_compatible_with_version(cls, version: str) -> bool:
        """
        Check if the decorator is compatible with a specific version.

        Args:
            version: The version to check compatibility with

        Returns:
            True if compatible, False otherwise

        Raises:
            IncompatibleVersionError: If the version is incompatible
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
        """
        Get metadata about the decorator.

        Returns:
            Dictionary containing metadata about the decorator
        """
        return {
            "name": cls.__name__,
            "description": """Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.""",
            "category": "general",
            "version": cls.version,
        }
