"""
Implementation of the AsExpert decorator.

This module provides the AsExpert decorator class for use in prompt engineering.

Generates responses from the perspective of a specified domain expert or specialist. This decorator provides authoritative content that reflects the knowledge, terminology, and analytical approach of an expert in the specified field.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    AsExpertExperienceEnum,
)


class AsExpert(BaseDecorator):
    """
    Generates responses from the perspective of a specified domain expert
    or specialist. This decorator provides authoritative content that
    reflects the knowledge, terminology, and analytical approach of an
    expert in the specified field.

    Attributes:
        domain: The specific field or discipline the expert specializes in
        experience: The experience level of the expert
        technical: Whether to use highly technical language and domain-specific terminology
    """

    decorator_name = "as_expert"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        domain: str,
        experience: Literal["junior", "senior", "leading", "pioneering"] = "senior",
        technical: bool = True,
    ) -> None:
        """
        Initialize the AsExpert decorator.

        Args:
            domain: The specific field or discipline the expert specializes in
            experience: The experience level of the expert
            technical: Whether to use highly technical language and domain-specific
                terminology

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._domain = domain
        self._experience = experience
        self._technical = technical

        # Validate parameters
        if self._domain is None:
            raise ValidationError("The parameter 'domain' is required for AsExpert decorator.")

        if self._domain is not None:
            if not isinstance(self._domain, str):
                raise ValidationError("The parameter 'domain' must be a string value.")

        if self._experience is not None:
            valid_values = ["junior", "senior", "leading", "pioneering"]
            if self._experience not in valid_values:
                raise ValidationError("The parameter 'experience' must be one of the following values: " + ", ".join(valid_values))

        if self._technical is not None:
            if not isinstance(self._technical, bool):
                raise ValidationError("The parameter 'technical' must be a boolean value.")


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
    def experience(self) -> Literal["junior", "senior", "leading", "pioneering"]:
        """
        Get the experience parameter value.

        Args:
            self: The decorator instance

        Returns:
            The experience parameter value
        """
        return self._experience

    @property
    def technical(self) -> bool:
        """
        Get the technical parameter value.

        Args:
            self: The decorator instance

        Returns:
            The technical parameter value
        """
        return self._technical

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "as_expert",
            "domain": self.domain,
            "experience": self.experience,
            "technical": self.technical,
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
        if self.experience is not None:
            params.append(f"experience={self.experience}")
        if self.technical is not None:
            params.append(f"technical={self.technical}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"