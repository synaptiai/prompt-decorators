"""
Implementation of the Abductive decorator.

This module provides the Abductive decorator class for use in prompt engineering.

Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Abductive(BaseDecorator):
    """
    Structures the response using abductive reasoning, developing the most
    likely explanations for observations or phenomena. This decorator
    emphasizes inference to the best explanation and hypothetical
    reasoning to address incomplete information.

    Attributes:
        hypotheses: Number of alternative hypotheses or explanations to generate
        criteria: Specific criteria to evaluate hypotheses against (e.g., simplicity, explanatory power)
        rank: Whether to explicitly rank hypotheses by likelihood
    """

    decorator_name = "abductive"
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
        hypotheses: Any = 3,
        criteria: List[Any] = None,
        rank: bool = True,
    ) -> None:
        """
        Initialize the Abductive decorator.

        Args:
            hypotheses: Number of alternative hypotheses or explanations to generate
            criteria: Specific criteria to evaluate hypotheses against (e.g.,
                simplicity, explanatory power)
            rank: Whether to explicitly rank hypotheses by likelihood

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._hypotheses = hypotheses
        self._criteria = criteria
        self._rank = rank

        # Validate parameters
        # Validate parameters
        if self._hypotheses is not None:
            if not isinstance(self._hypotheses, (int, float)):
                raise ValidationError("The parameter 'hypotheses' must be a numeric type value.")
            if self._hypotheses < 2:
                raise ValidationError("The parameter 'hypotheses' must be greater than or equal to 2.")
            if self._hypotheses > 5:
                raise ValidationError("The parameter 'hypotheses' must be less than or equal to 5.")
        if self._criteria is not None:
            if not isinstance(self._criteria, list):
                raise ValidationError("The parameter 'criteria' must be an array type value.")
        if self._rank is not None:
            if not isinstance(self._rank, bool):
                raise ValidationError("The parameter 'rank' must be a boolean type value.")

    @property
    def hypotheses(self) -> Any:
        """
        Get the hypotheses parameter value.

        Args:
            self: The decorator instance

        Returns:
            The hypotheses parameter value
        """
        return self._hypotheses

    @property
    def criteria(self) -> List[Any]:
        """
        Get the criteria parameter value.

        Args:
            self: The decorator instance

        Returns:
            The criteria parameter value
        """
        return self._criteria

    @property
    def rank(self) -> bool:
        """
        Get the rank parameter value.

        Args:
            self: The decorator instance

        Returns:
            The rank parameter value
        """
        return self._rank

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "abductive",
            "parameters": {
                "hypotheses": self.hypotheses,
                "criteria": self.criteria,
                "rank": self.rank,
            }
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.hypotheses is not None:
            params.append(f"hypotheses={self.hypotheses}")
        if self.criteria is not None:
            params.append(f"criteria={self.criteria}")
        if self.rank is not None:
            params.append(f"rank={self.rank}")

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
        if version < '0.1.0':
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
            "description": """Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.""",
            "category": "general",
            "version": cls.version,
        }