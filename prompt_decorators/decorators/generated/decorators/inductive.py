"""
Implementation of the Inductive decorator.

This module provides the Inductive decorator class for use in prompt engineering.

Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    InductiveStructureEnum,
)


class Inductive(BaseDecorator):
    """
    Structures the response using inductive reasoning, moving from
    specific observations to broader generalizations and theories. This
    decorator emphasizes pattern recognition and the derivation of general
    principles from particular instances.

    Attributes:
        examples: Number of specific examples or observations to include before generalizing
        confidence: Whether to explicitly state the confidence level of the inductive conclusions
        structure: The pattern of inductive reasoning to follow
    """

    decorator_name = "inductive"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        examples: Any = 3,
        confidence: bool = False,
        structure: Literal["generalization", "causal", "statistical", "analogical"] = "generalization",
    ) -> None:
        """
        Initialize the Inductive decorator.

        Args:
            examples: Number of specific examples or observations to include
                before generalizing
            confidence: Whether to explicitly state the confidence level of the
                inductive conclusions
            structure: The pattern of inductive reasoning to follow

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._examples = examples
        self._confidence = confidence
        self._structure = structure

        # Validate parameters
        if self._examples is not None:
            if not isinstance(self._examples, (int, float)) or isinstance(self._examples, bool):
                raise ValidationError("The parameter 'examples' must be a numeric value.")

        if self._confidence is not None:
            if not isinstance(self._confidence, bool):
                raise ValidationError("The parameter 'confidence' must be a boolean value.")

        if self._structure is not None:
            valid_values = ["generalization", "causal", "statistical", "analogical"]
            if self._structure not in valid_values:
                raise ValidationError("The parameter 'structure' must be one of the following values: " + ", ".join(valid_values))


    @property
    def examples(self) -> Any:
        """
        Get the examples parameter value.

        Args:
            self: The decorator instance

        Returns:
            The examples parameter value
        """
        return self._examples

    @property
    def confidence(self) -> bool:
        """
        Get the confidence parameter value.

        Args:
            self: The decorator instance

        Returns:
            The confidence parameter value
        """
        return self._confidence

    @property
    def structure(self) -> Literal["generalization", "causal", "statistical", "analogical"]:
        """
        Get the structure parameter value.

        Args:
            self: The decorator instance

        Returns:
            The structure parameter value
        """
        return self._structure

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "inductive",
            "examples": self.examples,
            "confidence": self.confidence,
            "structure": self.structure,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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