"""
Implementation of the Custom decorator.

This module provides the Custom decorator class for use in prompt engineering.

A meta-decorator that enables user-defined decorator behaviors through explicit rules or instructions. This provides maximum flexibility for creating specialized behaviors not covered by standard decorators.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Custom(BaseDecorator):
    """
    A meta-decorator that enables user-defined decorator behaviors through
    explicit rules or instructions. This provides maximum flexibility for
    creating specialized behaviors not covered by standard decorators.

    Attributes:
        rules: Explicit instructions defining the custom behavior (e.g., 'present all examples in a numbered list with exactly three items')
        name: Optional name for the custom decorator to reference in documentation or explanations
        priority: How to prioritize custom rules relative to other decorators
    """

    decorator_name = "custom"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        rules: str,
        name: str = None,
        priority: Literal["override", "supplement", "fallback"] = "override",
    ) -> None:
        """
        Initialize the Custom decorator.

        Args:
            rules: Explicit instructions defining the custom behavior (e.g.,
                'present all examples in a numbered list with exactly three
                items')
            name: Optional name for the custom decorator to reference in
                documentation or explanations
            priority: How to prioritize custom rules relative to other decorators

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._rules = rules
        self._name = name
        self._priority = priority

        # Validate parameters
        if self._rules is None:
            raise ValidationError(
                "The parameter 'rules' is required for Custom decorator."
            )

        if self._rules is not None:
            if not isinstance(self._rules, str):
                raise ValidationError("The parameter 'rules' must be a string value.")

        if self._name is not None:
            if not isinstance(self._name, str):
                raise ValidationError("The parameter 'name' must be a string value.")

        if self._priority is not None:
            valid_values = ["override", "supplement", "fallback"]
            if self._priority not in valid_values:
                raise ValidationError(
                    "The parameter 'priority' must be one of the following values: "
                    + ", ".join(valid_values)
                )

    @property
    def rules(self) -> str:
        """
        Get the rules parameter value.

        Args:
            self: The decorator instance

        Returns:
            The rules parameter value
        """
        return self._rules

    @property
    def name(self) -> str:
        """
        Get the name parameter value.

        Args:
            self: The decorator instance

        Returns:
            The name parameter value
        """
        return self._name

    @property
    def priority(self) -> Literal["override", "supplement", "fallback"]:
        """
        Get the priority parameter value.

        Args:
            self: The decorator instance

        Returns:
            The priority parameter value
        """
        return self._priority

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "custom",
            "rules": self.rules,
            "name": self.name,
            "priority": self.priority,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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
