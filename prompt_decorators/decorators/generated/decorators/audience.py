"""
Implementation of the Audience decorator.

This module provides the Audience decorator class for use in prompt engineering.

Adapts the response for a specific audience expertise level. This decorator ensures content is appropriately tailored to the knowledge, vocabulary, and needs of different audience types, from beginners to technical experts.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Audience(BaseDecorator):
    """
    Adapts the response for a specific audience expertise level. This
    decorator ensures content is appropriately tailored to the knowledge,
    vocabulary, and needs of different audience types, from beginners to
    technical experts.

    Attributes:
        level: The expertise level of the target audience
        domain: Specific knowledge domain or field for domain-specific terminology adaptation
        examples: Whether to include additional examples for clarity
    """

    decorator_name = "audience"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        level: Literal[
            "beginner", "intermediate", "expert", "technical"
        ] = "intermediate",
        domain: str = "general",
        examples: bool = True,
    ) -> None:
        """
        Initialize the Audience decorator.

        Args:
            level: The expertise level of the target audience
            domain: Specific knowledge domain or field for domain-specific
                terminology adaptation
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
        if self._level is not None:
            valid_values = ["beginner", "intermediate", "expert", "technical"]
            if self._level not in valid_values:
                raise ValidationError(
                    "The parameter 'level' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._domain is not None:
            if not isinstance(self._domain, str):
                raise ValidationError("The parameter 'domain' must be a string value.")

        if self._examples is not None:
            if not isinstance(self._examples, bool):
                raise ValidationError(
                    "The parameter 'examples' must be a boolean value."
                )

    @property
    def level(self) -> Literal["beginner", "intermediate", "expert", "technical"]:
        """
        Get the level parameter value.

        Args:
            self: The decorator instance

        Returns:
            The level parameter value
        """
        return self._level

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
    def examples(self) -> bool:
        """
        Get the examples parameter value.

        Args:
            self: The decorator instance

        Returns:
            The examples parameter value
        """
        return self._examples

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "audience",
            "level": self.level,
            "domain": self.domain,
            "examples": self.examples,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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
