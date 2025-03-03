"""
Implementation of the Chain decorator.

This module provides the Chain decorator class for use in prompt engineering.

A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.
"""

from typing import Any, Dict, List

from prompt_decorators.core.base import BaseDecorator, ValidationError


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
        if self._decorators is None:
            raise ValidationError(
                "The parameter 'decorators' is required for Chain decorator."
            )

        if self._decorators is not None:
            if not isinstance(self._decorators, (list, tuple)):
                raise ValidationError("The parameter 'decorators' must be an array.")

        if self._showSteps is not None:
            if not isinstance(self._showSteps, bool):
                raise ValidationError(
                    "The parameter 'showSteps' must be a boolean value."
                )

        if self._stopOnFailure is not None:
            if not isinstance(self._stopOnFailure, bool):
                raise ValidationError(
                    "The parameter 'stopOnFailure' must be a boolean value."
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
            "decorators": self.decorators,
            "showSteps": self.showSteps,
            "stopOnFailure": self.stopOnFailure,
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
