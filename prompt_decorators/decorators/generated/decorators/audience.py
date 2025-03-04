"""Implementation of the Audience decorator.

This module provides the Audience decorator class for use in prompt engineering.

Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import AudienceLevelEnum


class Audience(BaseDecorator):
    """Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.

    Attributes:
        level: The expertise level of the target audience. (Literal["beginner", "intermediate", "expert", "technical"])
        domain: Specific knowledge domain or field for domain-specific terminology adaptation. (str)
        examples: Whether to include additional examples for clarity. (bool)
    """

    name = "audience"  # Class-level name for serialization
    decorator_name = "audience"
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
        level: Literal[
            "beginner", "intermediate", "expert", "technical"
        ] = "intermediate",
        domain: str = "general",
        examples: bool = True,
    ) -> None:
        """Initialize the Audience decorator.

        Args:
            level: The expertise level of the target audience
            domain: Specific knowledge domain or field for domain-specific terminology adaptation
            examples: Whether to include additional examples for clarity


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._level = level
        self._domain = domain
        self._examples = examples

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._level = level
        self._domain = domain
        self._examples = examples

        # Validate parameters
        if self._level is not None:
            if not isinstance(self._level, str):
                raise ValidationError(
                    "The parameter 'level' must be a string type value."
                )
            if self._level not in ["beginner", "intermediate", "expert", "technical"]:
                raise ValidationError(
                    f"The parameter 'level' must be one of the allowed enum values: ['beginner', 'intermediate', 'expert', 'technical']. Got {self._level}"
                )
        if self._domain is not None:
            if not isinstance(self._domain, str):
                raise ValidationError(
                    "The parameter 'domain' must be a string type value."
                )
        if self._examples is not None:
            if not isinstance(self._examples, bool):
                raise ValidationError(
                    "The parameter 'examples' must be a boolean type value."
                )

    @property
    def level(self) -> Literal["beginner", "intermediate", "expert", "technical"]:
        """Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

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
    def examples(self) -> bool:
        """Get the examples parameter value.

        Args:
            self: The decorator instance

        Returns:
            The examples parameter value
        """
        return self._examples

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "audience",
            "parameters": {
                "level": self.level,
                "domain": self.domain,
                "examples": self.examples,
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
        if self.level is not None:
            params.append(f"level={self.level}")
        if self.domain is not None:
            params.append(f"domain={self.domain}")
        if self.examples is not None:
            params.append(f"examples={self.examples}")

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
            "description": """Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.""",
            "category": "general",
            "version": cls.version,
        }
