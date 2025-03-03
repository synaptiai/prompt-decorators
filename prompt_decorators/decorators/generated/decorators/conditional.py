"""
Implementation of the Conditional decorator.

This module provides the Conditional decorator class for use in prompt engineering.

A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.
"""

from typing import Any, Dict

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Conditional(BaseDecorator):
    """
    A meta-decorator that applies different decorators based on specified
    conditions. This enables dynamic behavior where the response
    formatting and approach changes depending on the content, context, or
    user-specified parameters.

    Attributes:
        if_param: The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}')
        then: The decorator to apply if the condition is true (can be a specific decorator with parameters)
        else_param: The decorator to apply if the condition is false (can be a specific decorator with parameters)
    """

    decorator_name = "conditional"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        if_param: str,
        then: str,
        else_param: str = None,
    ) -> None:
        """
        Initialize the Conditional decorator.

        Args:
            if_param: The condition to evaluate (e.g., 'technical', 'complex',
                'controversial', or a parameter like '{param}')
            then: The decorator to apply if the condition is true (can be a
                specific decorator with parameters)
            else_param: The decorator to apply if the condition is false (can be a
                specific decorator with parameters)

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._if_param = if_param
        self._then = then
        self._else_param = else_param

        # Validate parameters
        if self._if_param is None:
            raise ValidationError(
                "The parameter 'if_param' is required for Conditional decorator."
            )

        if self._if_param is not None:
            if not isinstance(self._if_param, str):
                raise ValidationError(
                    "The parameter 'if_param' must be a string value."
                )

        if self._then is None:
            raise ValidationError(
                "The parameter 'then' is required for Conditional decorator."
            )

        if self._then is not None:
            if not isinstance(self._then, str):
                raise ValidationError("The parameter 'then' must be a string value.")

        if self._else_param is not None:
            if not isinstance(self._else_param, str):
                raise ValidationError(
                    "The parameter 'else_param' must be a string value."
                )

    @property
    def if_param(self) -> str:
        """
        Get the if_param parameter value.

        Args:
            self: The decorator instance

        Returns:
            The if_param parameter value
        """
        return self._if_param

    @property
    def then(self) -> str:
        """
        Get the then parameter value.

        Args:
            self: The decorator instance

        Returns:
            The then parameter value
        """
        return self._then

    @property
    def else_param(self) -> str:
        """
        Get the else_param parameter value.

        Args:
            self: The decorator instance

        Returns:
            The else_param parameter value
        """
        return self._else_param

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "conditional",
            "if_param": self.if_param,
            "then": self.then,
            "else_param": self.else_param,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.if_param is not None:
            params.append(f"if_param={self.if_param}")
        if self.then is not None:
            params.append(f"then={self.then}")
        if self.else_param is not None:
            params.append(f"else_param={self.else_param}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
