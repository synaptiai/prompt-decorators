"""
Implementation of the Detailed decorator.

This module provides the Detailed decorator class for use in prompt engineering.

Enhances the response with comprehensive information, thorough explanations, and rich context. This decorator is ideal for in-depth learning, complex topics requiring nuance, or when completeness is valued over brevity.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    DetailedDepthEnum,
)


class Detailed(BaseDecorator):
    """
    Enhances the response with comprehensive information, thorough
    explanations, and rich context. This decorator is ideal for in-depth
    learning, complex topics requiring nuance, or when completeness is
    valued over brevity.

    Attributes:
        depth: The level of detail and comprehensiveness
        aspects: Specific aspects or dimensions to explore in detail
        examples: Whether to include detailed examples to illustrate points
    """

    decorator_name = "detailed"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        depth: Literal["moderate", "comprehensive", "exhaustive"] = "comprehensive",
        aspects: List[Any] = None,
        examples: bool = True,
    ) -> None:
        """
        Initialize the Detailed decorator.

        Args:
            depth: The level of detail and comprehensiveness
            aspects: Specific aspects or dimensions to explore in detail
            examples: Whether to include detailed examples to illustrate points

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._depth = depth
        self._aspects = aspects
        self._examples = examples

        # Validate parameters
        if self._depth is not None:
            valid_values = ["moderate", "comprehensive", "exhaustive"]
            if self._depth not in valid_values:
                raise ValidationError("The parameter 'depth' must be one of the following values: " + ", ".join(valid_values))

        if self._aspects is not None:
            if not isinstance(self._aspects, (list, tuple)):
                raise ValidationError("The parameter 'aspects' must be an array.")

        if self._examples is not None:
            if not isinstance(self._examples, bool):
                raise ValidationError("The parameter 'examples' must be a boolean value.")


    @property
    def depth(self) -> Literal["moderate", "comprehensive", "exhaustive"]:
        """
        Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    @property
    def aspects(self) -> List[Any]:
        """
        Get the aspects parameter value.

        Args:
            self: The decorator instance

        Returns:
            The aspects parameter value
        """
        return self._aspects

    @property
    def examples(self) -> bool:
        """
        Get the examples parameter value.

        Args:
            self: The decorator instance

        Returns:
            The examples parameter value
        """
        return self._examples

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "detailed",
            "depth": self.depth,
            "aspects": self.aspects,
            "examples": self.examples,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.depth is not None:
            params.append(f"depth={self.depth}")
        if self.aspects is not None:
            params.append(f"aspects={self.aspects}")
        if self.examples is not None:
            params.append(f"examples={self.examples}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"