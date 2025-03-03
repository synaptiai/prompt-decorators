"""Implementation of the Deductive decorator.

This module provides the Deductive decorator class for use in prompt engineering.

Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Deductive(BaseDecorator):
    """Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.

    Attributes:
        premises: Number of main premises to include before deducing conclusions. (Any)
        formal: Whether to use formal logical structures with explicit syllogisms. (bool)
        steps: Number of logical steps to include in the deductive process. (Any)
    """

    name = "deductive"  # Class-level name for serialization
    decorator_name = "deductive"
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
        premises: Any = 2,
        formal: bool = False,
        steps: Any = 3,
    ) -> None:
        """Initialize the Deductive decorator.

        Args:
            premises: Number of main premises to include before deducing conclusions
            formal: Whether to use formal logical structures with explicit syllogisms
            steps: Number of logical steps to include in the deductive process

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._premises = premises
        self._formal = formal
        self._steps = steps

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._premises = premises
        self._formal = formal
        self._steps = steps

        # Validate parameters
        if self._premises is not None:
            if not isinstance(self._premises, (int, float)):
                raise ValidationError(
                    "The parameter 'premises' must be a numeric type value."
                )
            if self._premises < 1:
                raise ValidationError(
                    "The parameter 'premises' must be greater than or equal to 1."
                )
            if self._premises > 5:
                raise ValidationError(
                    "The parameter 'premises' must be less than or equal to 5."
                )
        if self._formal is not None:
            if not isinstance(self._formal, bool):
                raise ValidationError(
                    "The parameter 'formal' must be a boolean type value."
                )
        if self._steps is not None:
            if not isinstance(self._steps, (int, float)):
                raise ValidationError(
                    "The parameter 'steps' must be a numeric type value."
                )
            if self._steps < 2:
                raise ValidationError(
                    "The parameter 'steps' must be greater than or equal to 2."
                )
            if self._steps > 7:
                raise ValidationError(
                    "The parameter 'steps' must be less than or equal to 7."
                )

    @property
    def premises(self) -> Any:
        """Get the premises parameter value.

        Args:
            self: The decorator instance

        Returns:
            The premises parameter value
        """
        return self._premises

    @property
    def formal(self) -> bool:
        """Get the formal parameter value.

        Args:
            self: The decorator instance

        Returns:
            The formal parameter value
        """
        return self._formal

    @property
    def steps(self) -> Any:
        """Get the steps parameter value.

        Args:
            self: The decorator instance

        Returns:
            The steps parameter value
        """
        return self._steps

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "deductive",
            "parameters": {
                "premises": self.premises,
                "formal": self.formal,
                "steps": self.steps,
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
        if self.premises is not None:
            params.append(f"premises={self.premises}")
        if self.formal is not None:
            params.append(f"formal={self.formal}")
        if self.steps is not None:
            params.append(f"steps={self.steps}")

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
            "description": """Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.""",
            "category": "general",
            "version": cls.version,
        }
