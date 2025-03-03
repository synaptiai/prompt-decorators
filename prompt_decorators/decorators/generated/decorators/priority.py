"""
Implementation of the Priority decorator.

This module provides the Priority decorator class for use in prompt engineering.

A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.
"""

from typing import Any, Dict, List, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Priority(BaseDecorator):
    """
    A meta-decorator that establishes a precedence hierarchy among
    multiple decorators. This allows explicit control over which
    decorator's parameters or behaviors take precedence when conflicts
    arise, overriding the default last-decorator-wins behavior.

    Attributes:
        decorators: Ordered list of decorators by priority (highest priority first)
        explicit: Whether to explicitly mention overridden behaviors in the response
        mode: How to handle conflicts between decorators
    """

    decorator_name = "priority"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        decorators: List[Any],
        explicit: bool = False,
        mode: Literal["override", "merge", "cascade"] = "override",
    ) -> None:
        """
        Initialize the Priority decorator.

        Args:
            decorators: Ordered list of decorators by priority (highest priority
                first)
            explicit: Whether to explicitly mention overridden behaviors in the
                response
            mode: How to handle conflicts between decorators

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._decorators = decorators
        self._explicit = explicit
        self._mode = mode

        # Validate parameters
        if self._decorators is None:
            raise ValidationError(
                "The parameter 'decorators' is required for Priority decorator."
            )

        if self._decorators is not None:
            if not isinstance(self._decorators, (list, tuple)):
                raise ValidationError("The parameter 'decorators' must be an array.")

        if self._explicit is not None:
            if not isinstance(self._explicit, bool):
                raise ValidationError(
                    "The parameter 'explicit' must be a boolean value."
                )

        if self._mode is not None:
            valid_values = ["override", "merge", "cascade"]
            if self._mode not in valid_values:
                raise ValidationError(
                    "The parameter 'mode' must be one of the following values: "
                    + ", ".join(valid_values)
                )

    @property
    def decorators(self) -> List[Any]:
        """
        Get the decorators parameter value.

        Args:
            self: The decorator instance

        Returns:
            The decorators parameter value
        """
        return self._decorators

    @property
    def explicit(self) -> bool:
        """
        Get the explicit parameter value.

        Args:
            self: The decorator instance

        Returns:
            The explicit parameter value
        """
        return self._explicit

    @property
    def mode(self) -> Literal["override", "merge", "cascade"]:
        """
        Get the mode parameter value.

        Args:
            self: The decorator instance

        Returns:
            The mode parameter value
        """
        return self._mode

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "priority",
            "decorators": self.decorators,
            "explicit": self.explicit,
            "mode": self.mode,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.decorators is not None:
            params.append(f"decorators={self.decorators}")
        if self.explicit is not None:
            params.append(f"explicit={self.explicit}")
        if self.mode is not None:
            params.append(f"mode={self.mode}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
