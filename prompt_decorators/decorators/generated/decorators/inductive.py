"""Implementation of the Inductive decorator.

This module provides the Inductive decorator class for use in prompt engineering.

Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    InductiveStructureEnum,
)


class Inductive(BaseDecorator):
    """Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.

    Attributes:
        examples: Number of specific examples or observations to include before generalizing. (Any)
        confidence: Whether to explicitly state the confidence level of the inductive conclusions. (bool)
        structure: The pattern of inductive reasoning to follow. (Literal["generalization", "causal", "statistical", "analogical"])
    """

    name = "inductive"  # Class-level name for serialization
    decorator_name = "inductive"
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
        examples: Any = 3,
        confidence: bool = False,
        structure: Literal[
            "generalization", "causal", "statistical", "analogical"
        ] = "generalization",
    ) -> None:
        """Initialize the Inductive decorator.

        Args:
            examples: Number of specific examples or observations to include before generalizing
            confidence: Whether to explicitly state the confidence level of the inductive conclusions
            structure: The pattern of inductive reasoning to follow

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._examples = examples
        self._confidence = confidence
        self._structure = structure

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._examples = examples
        self._confidence = confidence
        self._structure = structure

        # Validate parameters
        if self._examples is not None:
            if not isinstance(self._examples, (int, float)):
                raise ValidationError(
                    "The parameter 'examples' must be a numeric type value."
                )
            if self._examples < 2:
                raise ValidationError(
                    "The parameter 'examples' must be greater than or equal to 2."
                )
            if self._examples > 10:
                raise ValidationError(
                    "The parameter 'examples' must be less than or equal to 10."
                )
        if self._confidence is not None:
            if not isinstance(self._confidence, bool):
                raise ValidationError(
                    "The parameter 'confidence' must be a boolean type value."
                )
        if self._structure is not None:
            if not isinstance(self._structure, str):
                raise ValidationError(
                    "The parameter 'structure' must be a string type value."
                )
            if self._structure not in [
                "generalization",
                "causal",
                "statistical",
                "analogical",
            ]:
                raise ValidationError(
                    f"The parameter 'structure' must be one of the allowed enum values: ['generalization', 'causal', 'statistical', 'analogical']. Got {self._structure}"
                )

    @property
    def examples(self) -> Any:
        """Get the examples parameter value.

        Args:
            self: The decorator instance

        Returns:
            The examples parameter value
        """
        return self._examples

    @property
    def confidence(self) -> bool:
        """Get the confidence parameter value.

        Args:
            self: The decorator instance

        Returns:
            The confidence parameter value
        """
        return self._confidence

    @property
    def structure(
        self,
    ) -> Literal["generalization", "causal", "statistical", "analogical"]:
        """Get the structure parameter value.

        Args:
            self: The decorator instance

        Returns:
            The structure parameter value
        """
        return self._structure

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "inductive",
            "parameters": {
                "examples": self.examples,
                "confidence": self.confidence,
                "structure": self.structure,
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
        if self.examples is not None:
            params.append(f"examples={self.examples}")
        if self.confidence is not None:
            params.append(f"confidence={self.confidence}")
        if self.structure is not None:
            params.append(f"structure={self.structure}")

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
            "description": """Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.""",
            "category": "general",
            "version": cls.version,
        }
