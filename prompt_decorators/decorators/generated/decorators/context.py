"""
Implementation of the Context decorator.

This module provides the Context decorator class for use in prompt engineering.

A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Context(BaseDecorator):
    """
    A meta-decorator that adapts standard decorators for domain-specific
    contexts. This provides specialized interpretations of decorators
    based on particular fields, industries, or subject matter to ensure
    appropriate adaptation to contextual requirements.

    Attributes:
        domain: The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education')
        scope: Which aspects of decorators to contextualize
        level: The expertise level to target within the domain
    """

    decorator_name = "context"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        domain: str,
        scope: Literal["terminology", "examples", "structure", "all"] = "all",
        level: Literal["beginner", "intermediate", "expert", "mixed"] = "mixed",
    ) -> None:
        """
        Initialize the Context decorator.

        Args:
            domain: The specific domain, field, or industry to contextualize
                decorators for (e.g., 'medicine', 'legal', 'engineering',
                'education')
            scope: Which aspects of decorators to contextualize
            level: The expertise level to target within the domain

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._domain = domain
        self._scope = scope
        self._level = level

        # Validate parameters
        if self._domain is None:
            raise ValidationError(
                "The parameter 'domain' is required for Context decorator."
            )

        if self._domain is not None:
            if not isinstance(self._domain, str):
                raise ValidationError("The parameter 'domain' must be a string value.")

        if self._scope is not None:
            valid_values = ["terminology", "examples", "structure", "all"]
            if self._scope not in valid_values:
                raise ValidationError(
                    "The parameter 'scope' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._level is not None:
            valid_values = ["beginner", "intermediate", "expert", "mixed"]
            if self._level not in valid_values:
                raise ValidationError(
                    "The parameter 'level' must be one of the following values: "
                    + ", ".join(valid_values)
                )

    @property
    def domain(self) -> str:
        """
        Get the domain parameter value.

        Args:
            self: The decorator instance

        Returns:
            The domain parameter value
        """
        return self._domain

    @property
    def scope(self) -> Literal["terminology", "examples", "structure", "all"]:
        """
        Get the scope parameter value.

        Args:
            self: The decorator instance

        Returns:
            The scope parameter value
        """
        return self._scope

    @property
    def level(self) -> Literal["beginner", "intermediate", "expert", "mixed"]:
        """
        Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "context",
            "domain": self.domain,
            "scope": self.scope,
            "level": self.level,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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
