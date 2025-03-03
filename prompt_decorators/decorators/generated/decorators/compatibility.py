"""
Implementation of the Compatibility decorator.

This module provides the Compatibility decorator class for use in prompt engineering.

A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Compatibility(BaseDecorator):
    """
    A meta-decorator that specifies model-specific adaptations or fall-
    back behaviors. This enables graceful degradation of decorator
    functionalities across different LLM capabilities and ensures optimal
    performance across model variants.

    Attributes:
        models: List of specific models to adapt for (e.g., gpt-3.5-turbo, gpt-4, etc.)
        fallback: Decorator to apply if the current model doesn't match any in the models list
        behaviors: JSON string mapping model names to specific adaptations (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning", "gpt-4": "maximize detailed analysis"}')
    """

    decorator_name = "compatibility"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        models: List[Any],
        fallback: str = None,
        behaviors: str = None,
    ) -> None:
        """
        Initialize the Compatibility decorator.

        Args:
            models: List of specific models to adapt for (e.g., gpt-3.5-turbo,
                gpt-4, etc.)
            fallback: Decorator to apply if the current model doesn't match any in
                the models list
            behaviors: JSON string mapping model names to specific adaptations
                (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning",
                "gpt-4": "maximize detailed analysis"}')

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._models = models
        self._fallback = fallback
        self._behaviors = behaviors

        # Validate parameters
        if self._models is None:
            raise ValidationError("The parameter 'models' is required for Compatibility decorator.")

        if self._models is not None:
            if not isinstance(self._models, (list, tuple)):
                raise ValidationError("The parameter 'models' must be an array.")

        if self._fallback is not None:
            if not isinstance(self._fallback, str):
                raise ValidationError("The parameter 'fallback' must be a string value.")

        if self._behaviors is not None:
            if not isinstance(self._behaviors, str):
                raise ValidationError("The parameter 'behaviors' must be a string value.")


    @property
    def models(self) -> List[Any]:
        """
        Get the models parameter value.

        Args:
            self: The decorator instance

        Returns:
            The models parameter value
        """
        return self._models

    @property
    def fallback(self) -> str:
        """
        Get the fallback parameter value.

        Args:
            self: The decorator instance

        Returns:
            The fallback parameter value
        """
        return self._fallback

    @property
    def behaviors(self) -> str:
        """
        Get the behaviors parameter value.

        Args:
            self: The decorator instance

        Returns:
            The behaviors parameter value
        """
        return self._behaviors

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "compatibility",
            "models": self.models,
            "fallback": self.fallback,
            "behaviors": self.behaviors,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.models is not None:
            params.append(f"models={self.models}")
        if self.fallback is not None:
            params.append(f"fallback={self.fallback}")
        if self.behaviors is not None:
            params.append(f"behaviors={self.behaviors}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"