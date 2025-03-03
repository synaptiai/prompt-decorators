"""Implementation of the Persona decorator.

This module provides the Persona decorator class for use in prompt engineering.

Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Persona(BaseDecorator):
    """Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic.

    Attributes:
        role: The specific persona or stakeholder role to adopt. (str)
        traits: Key personality traits or characteristics of the persona. (List[Any])
        goals: Primary goals or concerns of the persona. (List[Any])
    """

    name = "persona"  # Class-level name for serialization
    decorator_name = "persona"
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
        role: str,
        traits: List[Any] = None,
        goals: List[Any] = None,
    ) -> None:
        """Initialize the Persona decorator.

        Args:
            role: The specific persona or stakeholder role to adopt
            traits: Key personality traits or characteristics of the persona
            goals: Primary goals or concerns of the persona

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._role = role
        self._traits = traits
        self._goals = goals

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._role = role
        self._traits = traits
        self._goals = goals

        # Validate parameters
        if self._role is not None:
            if not isinstance(self._role, str):
                raise ValidationError(
                    "The parameter 'role' must be a string type value."
                )
        if self._traits is not None:
            if not isinstance(self._traits, list):
                raise ValidationError(
                    "The parameter 'traits' must be an array type value."
                )
        if self._goals is not None:
            if not isinstance(self._goals, list):
                raise ValidationError(
                    "The parameter 'goals' must be an array type value."
                )

    @property
    def role(self) -> str:
        """Get the role parameter value.

        Args:
            self: The decorator instance

        Returns:
            The role parameter value
        """
        return self._role

    @property
    def traits(self) -> List[Any]:
        """Get the traits parameter value.

        Args:
            self: The decorator instance

        Returns:
            The traits parameter value
        """
        return self._traits

    @property
    def goals(self) -> List[Any]:
        """Get the goals parameter value.

        Args:
            self: The decorator instance

        Returns:
            The goals parameter value
        """
        return self._goals

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "persona",
            "parameters": {
                "role": self.role,
                "traits": self.traits,
                "goals": self.goals,
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
        if self.role is not None:
            params.append(f"role={self.role}")
        if self.traits is not None:
            params.append(f"traits={self.traits}")
        if self.goals is not None:
            params.append(f"goals={self.goals}")

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
            "description": """Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic.""",
            "category": "general",
            "version": cls.version,
        }
