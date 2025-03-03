"""Implementation of the AsExpert decorator.

This module provides the AsExpert decorator class for use in prompt engineering.

Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    AsExpertExperienceEnum,
)


class AsExpert(BaseDecorator):
    """Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.

    Attributes:
        domain: The specific field or discipline the expert specializes in. (str)
        experience: The experience level of the expert. (Literal["junior", "senior", "leading", "pioneering"])
        technical: Whether to use highly technical language and domain-specific terminology. (bool)
    """

    name = "as_expert"  # Class-level name for serialization
    decorator_name = "as_expert"
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
        domain: str,
        experience: Literal["junior", "senior", "leading", "pioneering"] = "senior",
        technical: bool = True,
    ) -> None:
        """Initialize the AsExpert decorator.

        Args:
            domain: The specific field or discipline the expert specializes in
            experience: The experience level of the expert
            technical: Whether to use highly technical language and domain-specific terminology

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._domain = domain
        self._experience = experience
        self._technical = technical

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._domain = domain
        self._experience = experience
        self._technical = technical

        # Validate parameters
        if self._domain is not None:
            if not isinstance(self._domain, str):
                raise ValidationError(
                    "The parameter 'domain' must be a string type value."
                )
        if self._experience is not None:
            if not isinstance(self._experience, str):
                raise ValidationError(
                    "The parameter 'experience' must be a string type value."
                )
            if self._experience not in ["junior", "senior", "leading", "pioneering"]:
                raise ValidationError(
                    f"The parameter 'experience' must be one of the allowed enum values: ['junior', 'senior', 'leading', 'pioneering']. Got {self._experience}"
                )
        if self._technical is not None:
            if not isinstance(self._technical, bool):
                raise ValidationError(
                    "The parameter 'technical' must be a boolean type value."
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
    def experience(self) -> Literal["junior", "senior", "leading", "pioneering"]:
        """Get the experience parameter value.

        Args:
            self: The decorator instance

        Returns:
            The experience parameter value
        """
        return self._experience

    @property
    def technical(self) -> bool:
        """Get the technical parameter value.

        Args:
            self: The decorator instance

        Returns:
            The technical parameter value
        """
        return self._technical

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "as_expert",
            "parameters": {
                "domain": self.domain,
                "experience": self.experience,
                "technical": self.technical,
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
        if self.experience is not None:
            params.append(f"experience={self.experience}")
        if self.technical is not None:
            params.append(f"technical={self.technical}")

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
            "description": """Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.""",
            "category": "general",
            "version": cls.version,
        }
