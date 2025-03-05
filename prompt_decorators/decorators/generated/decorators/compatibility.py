"""Implementation of the Compatibility decorator.

This module provides the Compatibility decorator class for use in prompt engineering.

A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Compatibility(BaseDecorator):
    """A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.

    Attributes:
        models: List of specific models to adapt for (e.g., gpt-3.5-turbo, gpt-4, etc.). (List[Any])
        fallback: Decorator to apply if the current model doesn't match any in the models list. (str)
        behaviors: JSON string mapping model names to specific adaptations (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning", "gpt-4": "maximize detailed analysis"}'). (str)
    """

    name = "compatibility"  # Class-level name for serialization
    decorator_name = "compatibility"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please apply model-specific adaptations to ensure optimal performance"
        "on the current language model.",
        "parameterMapping": {
            "models": {
                "format": "Apply the specialized behavior for these specific models: {value}. If the current model is not in this list, use the default or fallback behavior.",
            },
            "fallback": {
                "format": "If the current model is not one of the specified models, fall back to using the {value} decorator instead.",
            },
            "behaviors": {
                "format": "Apply these model-specific behavior adaptations: {value}. Each adaptation should be used only when running on the corresponding model.",
            },
        },
        "placement": "prepend",
        "compositionBehavior": "override",
    }

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
        models: List[Any],
        fallback: str = None,
        behaviors: str = None,
    ) -> None:
        """Initialize the Compatibility decorator.

        Args:
            models: List of specific models to adapt for (e.g., gpt-3.5-turbo, gpt-4, etc.)
            fallback: Decorator to apply if the current model doesn't match any in the models list
            behaviors: JSON string mapping model names to specific adaptations (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning", "gpt-4": "maximize detailed analysis"}')


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
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._models = models
        self._fallback = fallback
        self._behaviors = behaviors

        # Validate parameters
        if self._models is not None:
            if not isinstance(self._models, list):
                raise ValidationError(
                    "The parameter 'models' must be an array type value."
                )
        if self._fallback is not None:
            if not isinstance(self._fallback, str):
                raise ValidationError(
                    "The parameter 'fallback' must be a string type value."
                )
        if self._behaviors is not None:
            if not isinstance(self._behaviors, str):
                raise ValidationError(
                    "The parameter 'behaviors' must be a string type value."
                )

    @property
    def models(self) -> List[Any]:
        """Get the models parameter value.

        Args:
            self: The decorator instance

        Returns:
            The models parameter value
        """
        return self._models

    @property
    def fallback(self) -> str:
        """Get the fallback parameter value.

        Args:
            self: The decorator instance

        Returns:
            The fallback parameter value
        """
        return self._fallback

    @property
    def behaviors(self) -> str:
        """Get the behaviors parameter value.

        Args:
            self: The decorator instance

        Returns:
            The behaviors parameter value
        """
        return self._behaviors

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "compatibility",
            "parameters": {
                "models": self.models,
                "fallback": self.fallback,
                "behaviors": self.behaviors,
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
            "description": """A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.""",
            "category": "general",
            "version": cls.version,
        }

    def apply_to_prompt(self, prompt: str) -> str:
        """Apply the decorator to a prompt.

        This method transforms the prompt using the transformation template.

        Args:
            prompt: The prompt to decorate

        Returns:
            The decorated prompt

        """
        # Use the apply_to_prompt implementation from BaseDecorator
        return super().apply_to_prompt(prompt)
