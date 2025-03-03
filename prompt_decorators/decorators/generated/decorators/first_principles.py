"""
Implementation of the FirstPrinciples decorator.

This module provides the FirstPrinciples decorator class for use in prompt engineering.

Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError


class FirstPrinciples(BaseDecorator):
    """
    Structures the response by breaking down complex topics into their
    fundamental truths or axioms, then building up from there. This
    decorator promotes a deeper understanding by examining the most basic
    elements of a concept before constructing more complex ideas.

    Attributes:
        depth: Level of detail in breaking down to fundamental principles
    """

    decorator_name = "first_principles"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        depth: Any = 3,
    ) -> None:
        """
        Initialize the FirstPrinciples decorator.

        Args:
            depth: Level of detail in breaking down to fundamental principles

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._depth = depth

        # Validate parameters
        if self._depth is not None:
            if not isinstance(self._depth, (int, float)) or isinstance(self._depth, bool):
                raise ValidationError("The parameter 'depth' must be a numeric value.")


    @property
    def depth(self) -> Any:
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
            "name": "first_principles",
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