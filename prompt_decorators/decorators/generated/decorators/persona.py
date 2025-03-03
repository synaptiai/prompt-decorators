"""
Implementation of the Persona decorator.

This module provides the Persona decorator class for use in prompt engineering.

Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Persona(BaseDecorator):
    """
    Adapts the response to reflect the perspective and concerns of a
    specific persona. This decorator helps explore how different
    stakeholders or personality types would view a situation or topic.

    Attributes:
        role: The specific persona or stakeholder role to adopt
        traits: Key personality traits or characteristics of the persona
        goals: Primary goals or concerns of the persona
    """

    decorator_name = "persona"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        role: str,
        traits: List[Any] = None,
        goals: List[Any] = None,
    ) -> None:
        """
        Initialize the Persona decorator.

        Args:
            role: The specific persona or stakeholder role to adopt
            traits: Key personality traits or characteristics of the persona
            goals: Primary goals or concerns of the persona

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._role = role
        self._traits = traits
        self._goals = goals

        # Validate parameters
        if self._role is None:
            raise ValidationError("The parameter 'role' is required for Persona decorator.")

        if self._role is not None:
            if not isinstance(self._role, str):
                raise ValidationError("The parameter 'role' must be a string value.")

        if self._traits is not None:
            if not isinstance(self._traits, (list, tuple)):
                raise ValidationError("The parameter 'traits' must be an array.")

        if self._goals is not None:
            if not isinstance(self._goals, (list, tuple)):
                raise ValidationError("The parameter 'goals' must be an array.")


    @property
    def role(self) -> str:
        """
        Get the role parameter value.

        Args:
            self: The decorator instance

        Returns:
            The role parameter value
        """
        return self._role

    @property
    def traits(self) -> List[Any]:
        """
        Get the traits parameter value.

        Args:
            self: The decorator instance

        Returns:
            The traits parameter value
        """
        return self._traits

    @property
    def goals(self) -> List[Any]:
        """
        Get the goals parameter value.

        Args:
            self: The decorator instance

        Returns:
            The goals parameter value
        """
        return self._goals

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "persona",
            "role": self.role,
            "traits": self.traits,
            "goals": self.goals,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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