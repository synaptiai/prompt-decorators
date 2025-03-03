"""
Implementation of the Professional decorator.

This module provides the Professional decorator class for use in prompt engineering.

Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Professional(BaseDecorator):
    """
    Adapts the response to use business-oriented language appropriate for
    professional contexts. This decorator generates content using formal
    business terminology, clear and concise phrasing, and industry-
    appropriate jargon when relevant.

    Attributes:
        industry: The specific industry context to adapt the language for
        formality: The level of formality to maintain in the response
    """

    decorator_name = "professional"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        industry: str = "general",
        formality: Literal["standard", "high", "executive"] = "standard",
    ) -> None:
        """
        Initialize the Professional decorator.

        Args:
            industry: The specific industry context to adapt the language for
            formality: The level of formality to maintain in the response

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._industry = industry
        self._formality = formality

        # Validate parameters
        if self._industry is not None:
            if not isinstance(self._industry, str):
                raise ValidationError(
                    "The parameter 'industry' must be a string value."
                )

        if self._formality is not None:
            valid_values = ["standard", "high", "executive"]
            if self._formality not in valid_values:
                raise ValidationError(
                    "The parameter 'formality' must be one of the following values: "
                    + ", ".join(valid_values)
                )

    @property
    def industry(self) -> str:
        """
        Get the industry parameter value.

        Args:
            self: The decorator instance

        Returns:
            The industry parameter value
        """
        return self._industry

    @property
    def formality(self) -> Literal["standard", "high", "executive"]:
        """
        Get the formality parameter value.

        Args:
            self: The decorator instance

        Returns:
            The formality parameter value
        """
        return self._formality

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "professional",
            "industry": self.industry,
            "formality": self.formality,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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
