"""Implementation of the Custom decorator.

This module provides the Custom decorator class for use in prompt engineering.

A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import CustomPriorityEnum


class Custom(BaseDecorator):
    """A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.

    Attributes:
        rules: Explicit instructions defining the custom behavior (e.g., 'present all examples in a numbered list with exactly three items'). (str)
        name: Optional name for the custom decorator to reference in documentation or explanations. (str)
        priority: How to prioritize custom rules relative to other decorators. (Literal["override", "supplement", "fallback"])
    """

    name = "custom"  # Class-level name for serialization
    decorator_name = "custom"
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
        rules: str,
        name: str = None,
        priority: Literal["override", "supplement", "fallback"] = "override",
    ) -> None:
        """Initialize the Custom decorator.

        Args:
            rules: Explicit instructions defining the custom behavior (e.g., 'present all examples in a numbered list with exactly three items')
            name: Optional name for the custom decorator to reference in documentation or explanations
            priority: How to prioritize custom rules relative to other decorators

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._rules = rules
        self._name = name
        self._priority = priority

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._rules = rules
        self._name = name
        self._priority = priority

        # Validate parameters
        if self._rules is not None:
            if not isinstance(self._rules, str):
                raise ValidationError(
                    "The parameter 'rules' must be a string type value."
                )
        if self._name is not None:
            if not isinstance(self._name, str):
                raise ValidationError(
                    "The parameter 'name' must be a string type value."
                )
        if self._priority is not None:
            if not isinstance(self._priority, str):
                raise ValidationError(
                    "The parameter 'priority' must be a string type value."
                )
            if self._priority not in ["override", "supplement", "fallback"]:
                raise ValidationError(
                    f"The parameter 'priority' must be one of the allowed enum values: ['override', 'supplement', 'fallback']. Got {self._priority}"
                )

    @property
    def rules(self) -> str:
        """Get the rules parameter value.

        Args:
            self: The decorator instance

        Returns:
            The rules parameter value
        """
        return self._rules

    @property
    def name(self) -> str:
        """Get the name parameter value.

        Args:
            self: The decorator instance

        Returns:
            The name parameter value
        """
        return self._name

    @property
    def priority(self) -> Literal["override", "supplement", "fallback"]:
        """Get the priority parameter value.

        Args:
            self: The decorator instance

        Returns:
            The priority parameter value
        """
        return self._priority

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "custom",
            "parameters": {
                "rules": self.rules,
                "name": self.name,
                "priority": self.priority,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.rules is not None:
            params.append(f"rules={self.rules}")
        if self.name is not None:
            params.append(f"name={self.name}")
        if self.priority is not None:
            params.append(f"priority={self.priority}")

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
            "description": """A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.""",
            "category": "general",
            "version": cls.version,
        }
