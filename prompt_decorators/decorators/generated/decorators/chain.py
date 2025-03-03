"""
Implementation of the Chain decorator.

This module provides the Chain decorator class for use in prompt engineering.

A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Chain(BaseDecorator):
    """
    A meta-decorator that applies multiple decorators in sequence, with
    each decorator processing the output of the previous one. This enables
    complex transformations by combining multiple simpler decorators in a
    pipeline.

    Attributes:
        decorators: Ordered list of decorators to apply in sequence
        showSteps: Whether to show intermediate outputs after each decorator in the chain
        stopOnFailure: Whether to stop the chain if a decorator fails to apply correctly
    """

    decorator_name = "chain"
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
        decorators: List[Any],
        showSteps: bool = False,
        stopOnFailure: bool = True,
    ) -> None:
        """
        Initialize the Chain decorator.

        Args:
            decorators: Ordered list of decorators to apply in sequence
            showSteps: Whether to show intermediate outputs after each decorator in
                the chain
            stopOnFailure: Whether to stop the chain if a decorator fails to apply
                correctly

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._decorators = decorators
        self._showSteps = showSteps
        self._stopOnFailure = stopOnFailure

        # Validate parameters
        # Validate parameters
        if self._decorators is not None:
            if not isinstance(self._decorators, list):
                raise ValidationError("The parameter 'decorators' must be an array type value.")
        if self._showSteps is not None:
            if not isinstance(self._showSteps, bool):
                raise ValidationError("The parameter 'showSteps' must be a boolean type value.")
        if self._stopOnFailure is not None:
            if not isinstance(self._stopOnFailure, bool):
                raise ValidationError("The parameter 'stopOnFailure' must be a boolean type value.")

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
    def showSteps(self) -> bool:
        """
        Get the showSteps parameter value.

        Args:
            self: The decorator instance

        Returns:
            The showSteps parameter value
        """
        return self._showSteps

    @property
    def stopOnFailure(self) -> bool:
        """
        Get the stopOnFailure parameter value.

        Args:
            self: The decorator instance

        Returns:
            The stopOnFailure parameter value
        """
        return self._stopOnFailure

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "chain",
            "parameters": {
                "decorators": self.decorators,
                "showSteps": self.showSteps,
                "stopOnFailure": self.stopOnFailure,
            }
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
        if self.showSteps is not None:
            params.append(f"showSteps={self.showSteps}")
        if self.stopOnFailure is not None:
            params.append(f"stopOnFailure={self.stopOnFailure}")

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
            "description": """A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.""",
            "category": "general",
            "version": cls.version,
        }