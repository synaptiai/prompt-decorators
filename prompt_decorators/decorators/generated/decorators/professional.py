"""Implementation of the Professional decorator.

This module provides the Professional decorator class for use in prompt engineering.

Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    ProfessionalFormalityEnum,
)


class Professional(BaseDecorator):
    """Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.

    Attributes:
        industry: The specific industry context to adapt the language for. (str)
        formality: The level of formality to maintain in the response. (Literal["standard", "high", "executive"])
    """

    name = "professional"  # Class-level name for serialization
    decorator_name = "professional"
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
        industry: str = "general",
        formality: Literal["standard", "high", "executive"] = "standard",
    ) -> None:
        """Initialize the Professional decorator.

        Args:
            industry: The specific industry context to adapt the language for
            formality: The level of formality to maintain in the response

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._industry = industry
        self._formality = formality

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._industry = industry
        self._formality = formality

        # Validate parameters
        if self._industry is not None:
            if not isinstance(self._industry, str):
                raise ValidationError(
                    "The parameter 'industry' must be a string type value."
                )
        if self._formality is not None:
            if not isinstance(self._formality, str):
                raise ValidationError(
                    "The parameter 'formality' must be a string type value."
                )
            if self._formality not in ["standard", "high", "executive"]:
                raise ValidationError(
                    f"The parameter 'formality' must be one of the allowed enum values: ['standard', 'high', 'executive']. Got {self._formality}"
                )

    @property
    def industry(self) -> str:
        """Get the industry parameter value.

        Args:
            self: The decorator instance

        Returns:
            The industry parameter value
        """
        return self._industry

    @property
    def formality(self) -> Literal["standard", "high", "executive"]:
        """Get the formality parameter value.

        Args:
            self: The decorator instance

        Returns:
            The formality parameter value
        """
        return self._formality

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "professional",
            "parameters": {
                "industry": self.industry,
                "formality": self.formality,
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
        if self.industry is not None:
            params.append(f"industry={self.industry}")
        if self.formality is not None:
            params.append(f"formality={self.formality}")

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
            "description": """Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.""",
            "category": "general",
            "version": cls.version,
        }
