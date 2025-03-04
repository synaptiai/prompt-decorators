"""Implementation of the Priority decorator.

This module provides the Priority decorator class for use in prompt engineering.

A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import PriorityModeEnum


class Priority(BaseDecorator):
    """A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.

    Attributes:
        decorators: Ordered list of decorators by priority (highest priority first). (List[Any])
        explicit: Whether to explicitly mention overridden behaviors in the response. (bool)
        mode: How to handle conflicts between decorators. (Literal["override", "merge", "cascade"])
    """

    name = "priority"  # Class-level name for serialization
    decorator_name = "priority"
    version = "1.0.0"  # Initial version

    @property
    def name(self) -> str:
        """Get the name of the decorator.

        Args:
            self: The decorator instance


        Returns:
            The name of the decorator

        """
        return self.decorator_name

    def __init__(
        self,
        decorators: List[Any],
        explicit: bool = False,
        mode: Literal["override", "merge", "cascade"] = "override",
    ) -> None:
        """Initialize the Priority decorator.

        Args:
            decorators: Ordered list of decorators by priority (highest priority first)
            explicit: Whether to explicitly mention overridden behaviors in the response
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
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._decorators = decorators
        self._explicit = explicit
        self._mode = mode

        # Validate parameters
        if self._decorators is not None:
            if not isinstance(self._decorators, list):
                raise ValidationError(
                    "The parameter 'decorators' must be an array type value."
                )
        if self._explicit is not None:
            if not isinstance(self._explicit, bool):
                raise ValidationError(
                    "The parameter 'explicit' must be a boolean type value."
                )
        if self._mode is not None:
            if not isinstance(self._mode, str):
                raise ValidationError(
                    "The parameter 'mode' must be a string type value."
                )
            if self._mode not in ["override", "merge", "cascade"]:
                raise ValidationError(
                    f"The parameter 'mode' must be one of the allowed enum values: ['override', 'merge', 'cascade']. Got {self._mode}"
                )

    @property
    def decorators(self) -> List[Any]:
        """Get the decorators parameter value.

        Args:
            self: The decorator instance

        Returns:
            The decorators parameter value
        """
        return self._decorators

    @property
    def explicit(self) -> bool:
        """Get the explicit parameter value.

        Args:
            self: The decorator instance

        Returns:
            The explicit parameter value
        """
        return self._explicit

    @property
    def mode(self) -> Literal["override", "merge", "cascade"]:
        """Get the mode parameter value.

        Args:
            self: The decorator instance

        Returns:
            The mode parameter value
        """
        return self._mode

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "priority",
            "parameters": {
                "decorators": self.decorators,
                "explicit": self.explicit,
                "mode": self.mode,
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


        Args:
            cls: The decorator class

        """
        return {
            "name": cls.__name__,
            "description": """A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.""",
            "category": "general",
            "version": cls.version,
        }
