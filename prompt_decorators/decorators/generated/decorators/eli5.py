"""Implementation of the ELI5 decorator.

This module provides the ELI5 decorator class for use in prompt engineering.

Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class ELI5(BaseDecorator):
    """Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.

    Attributes:
        strictness: Whether to strictly maintain a child-appropriate level of simplicity or allow slightly more complexity when necessary. (bool)
    """

    name = "eli5"  # Class-level name for serialization
    decorator_name = "eli5"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please explain this concept as you would to a 5-year-old child. Use"
        "simple vocabulary, concrete examples, and relatable analogies.",
        "parameterMapping": {
            "strictness": {
                "valueMap": {
                    "true": "Maintain an extremely simplified approach that a young child would understand, using only basic vocabulary and very concrete analogies. Avoid any technical terms or complex explanations entirely.",
                    "false": "Keep explanations simple and child-friendly, but you may introduce slightly more advanced concepts when absolutely necessary for understanding, as long as they're explained with simple analogies.",
                },
            },
        },
        "placement": "prepend",
        "compositionBehavior": "accumulate",
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
        strictness: bool = False,
    ) -> None:
        """Initialize the ELI5 decorator.

        Args:
            strictness: Whether to strictly maintain a child-appropriate level of simplicity or allow slightly more complexity when necessary


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._strictness = strictness

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._strictness = strictness

        # Validate parameters
        if self._strictness is not None:
            if not isinstance(self._strictness, bool):
                raise ValidationError(
                    "The parameter 'strictness' must be a boolean type value."
                )

    @property
    def strictness(self) -> bool:
        """Get the strictness parameter value.

        Args:
            self: The decorator instance

        Returns:
            The strictness parameter value
        """
        return self._strictness

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "eli5",
            "parameters": {
                "strictness": self.strictness,
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
        if self.strictness is not None:
            params.append(f"strictness={self.strictness}")

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
            "description": """Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.""",
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
