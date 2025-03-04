"""Implementation of the Context decorator.

This module provides the Context decorator class for use in prompt engineering.

A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    ContextLevelEnum,
    ContextScopeEnum,
)


class Context(BaseDecorator):
    """A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.

    Attributes:
        domain: The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education'). (str)
        scope: Which aspects of decorators to contextualize. (Literal["terminology", "examples", "structure", "all"])
        level: The expertise level to target within the domain. (Literal["beginner", "intermediate", "expert", "mixed"])
    """

    name = "context"  # Class-level name for serialization
    decorator_name = "context"
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
        domain: str,
        scope: Literal["terminology", "examples", "structure", "all"] = "all",
        level: Literal["beginner", "intermediate", "expert", "mixed"] = "mixed",
    ) -> None:
        """Initialize the Context decorator.

        Args:
            domain: The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education')
            scope: Which aspects of decorators to contextualize
            level: The expertise level to target within the domain

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._domain = domain
        self._scope = scope
        self._level = level

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._domain = domain
        self._scope = scope
        self._level = level

        # Validate parameters
        if self._domain is not None:
            if not isinstance(self._domain, str):
                raise ValidationError(
                    "The parameter 'domain' must be a string type value."
                )
        if self._scope is not None:
            if not isinstance(self._scope, str):
                raise ValidationError(
                    "The parameter 'scope' must be a string type value."
                )
            if self._scope not in ["terminology", "examples", "structure", "all"]:
                raise ValidationError(
                    f"The parameter 'scope' must be one of the allowed enum values: ['terminology', 'examples', 'structure', 'all']. Got {self._scope}"
                )
        if self._level is not None:
            if not isinstance(self._level, str):
                raise ValidationError(
                    "The parameter 'level' must be a string type value."
                )
            if self._level not in ["beginner", "intermediate", "expert", "mixed"]:
                raise ValidationError(
                    f"The parameter 'level' must be one of the allowed enum values: ['beginner', 'intermediate', 'expert', 'mixed']. Got {self._level}"
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
    def scope(self) -> Literal["terminology", "examples", "structure", "all"]:
        """Get the scope parameter value.

        Args:
            self: The decorator instance

        Returns:
            The scope parameter value
        """
        return self._scope

    @property
    def level(self) -> Literal["beginner", "intermediate", "expert", "mixed"]:
        """Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "context",
            "parameters": {
                "domain": self.domain,
                "scope": self.scope,
                "level": self.level,
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
        if self.scope is not None:
            params.append(f"scope={self.scope}")
        if self.level is not None:
            params.append(f"level={self.level}")

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
            "description": """A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.""",
            "category": "general",
            "version": cls.version,
        }
