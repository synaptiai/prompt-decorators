"""
Implementation of the Override decorator.

This module provides the Override decorator class for use in prompt engineering.

A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.
"""

from typing import Any, Dict

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Override(BaseDecorator):
    """
    A meta-decorator that overrides the default parameters or behaviors of
    other decorators. This enables customization of standard decorators
    without modifying their definitions, allowing for reuse of established
    patterns with specific adjustments.

    Attributes:
        decorator: The specific decorator whose behavior to override
        parameters: JSON string specifying the parameters to override (e.g., '{"depth": "comprehensive", "focus": "methodology"}')
        behavior: Optional custom behavior modification instructions that override the standard decorator interpretation
    """

    decorator_name = "override"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        decorator: str,
        parameters: str = None,
        behavior: str = None,
    ) -> None:
        """
        Initialize the Override decorator.

        Args:
            decorator: The specific decorator whose behavior to override
            parameters: JSON string specifying the parameters to override (e.g.,
                '{"depth": "comprehensive", "focus": "methodology"}')
            behavior: Optional custom behavior modification instructions that
                override the standard decorator interpretation

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._decorator = decorator
        self._parameters = parameters
        self._behavior = behavior

        # Validate parameters
        if self._decorator is None:
            raise ValidationError(
                "The parameter 'decorator' is required for Override decorator."
            )

        if self._decorator is not None:
            if not isinstance(self._decorator, str):
                raise ValidationError(
                    "The parameter 'decorator' must be a string value."
                )

        if self._parameters is not None:
            if not isinstance(self._parameters, str):
                raise ValidationError(
                    "The parameter 'parameters' must be a string value."
                )

        if self._behavior is not None:
            if not isinstance(self._behavior, str):
                raise ValidationError(
                    "The parameter 'behavior' must be a string value."
                )

    @property
    def decorator(self) -> str:
        """
        Get the decorator parameter value.

        Args:
            self: The decorator instance

        Returns:
            The decorator parameter value
        """
        return self._decorator

    @property
    def parameters(self) -> str:
        """
        Get the parameters parameter value.

        Args:
            self: The decorator instance

        Returns:
            The parameters parameter value
        """
        return self._parameters

    @property
    def behavior(self) -> str:
        """
        Get the behavior parameter value.

        Args:
            self: The decorator instance

        Returns:
            The behavior parameter value
        """
        return self._behavior

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "override",
            "decorator": self.decorator,
            "parameters": self.parameters,
            "behavior": self.behavior,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.decorator is not None:
            params.append(f"decorator={self.decorator}")
        if self.parameters is not None:
            params.append(f"parameters={self.parameters}")
        if self.behavior is not None:
            params.append(f"behavior={self.behavior}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
