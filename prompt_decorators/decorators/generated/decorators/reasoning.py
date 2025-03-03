"""
Implementation of the Reasoning decorator.

This module provides the Reasoning decorator class for use in prompt engineering.

Modifies the AI's response to provide explicit reasoning paths before reaching conclusions. This decorator encourages the model to show its thought process, making responses more transparent and trustworthy.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    ReasoningDepthEnum,
)


class Reasoning(BaseDecorator):
    """
    Modifies the AI's response to provide explicit reasoning paths before
    reaching conclusions. This decorator encourages the model to show its
    thought process, making responses more transparent and trustworthy.

    Attributes:
        depth: The level of detail in the reasoning process
    """

    decorator_name = "reasoning"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        depth: Literal["basic", "moderate", "comprehensive"] = "moderate",
    ) -> None:
        """
        Initialize the Reasoning decorator.

        Args:
            depth: The level of detail in the reasoning process

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._depth = depth

        # Validate parameters
        if self._depth is not None:
            valid_values = ["basic", "moderate", "comprehensive"]
            if self._depth not in valid_values:
                raise ValidationError("The parameter 'depth' must be one of the following values: " + ", ".join(valid_values))


    @property
    def depth(self) -> Literal["basic", "moderate", "comprehensive"]:
        """
        Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "reasoning",
            "depth": self.depth,
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

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"