"""
Implementation of the NegativeSpace decorator.

This module provides the NegativeSpace decorator class for use in prompt engineering.

Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class NegativeSpace(BaseDecorator):
    """
    Focuses on analyzing what is not explicitly stated, implied, or
    missing from a topic or question. This decorator explores the
    'negative space' by identifying unexplored angles, implicit
    assumptions, unasked questions, and contextual elements that may have
    been overlooked.

    Attributes:
        focus: The specific aspect of negative space to emphasize
        depth: How deeply to explore the negative space
        structure: How to present the negative space analysis
    """

    decorator_name = "negative_space"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        focus: Literal[
            "implications", "missing", "unstated", "comprehensive"
        ] = "comprehensive",
        depth: Literal["surface", "moderate", "deep"] = "moderate",
        structure: Literal["before", "after", "integrated", "separate"] = "integrated",
    ) -> None:
        """
        Initialize the NegativeSpace decorator.

        Args:
            focus: The specific aspect of negative space to emphasize
            depth: How deeply to explore the negative space
            structure: How to present the negative space analysis

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._focus = focus
        self._depth = depth
        self._structure = structure

        # Validate parameters
        if self._focus is not None:
            valid_values = ["implications", "missing", "unstated", "comprehensive"]
            if self._focus not in valid_values:
                raise ValidationError(
                    "The parameter 'focus' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._depth is not None:
            valid_values = ["surface", "moderate", "deep"]
            if self._depth not in valid_values:
                raise ValidationError(
                    "The parameter 'depth' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._structure is not None:
            valid_values = ["before", "after", "integrated", "separate"]
            if self._structure not in valid_values:
                raise ValidationError(
                    "The parameter 'structure' must be one of the following values: "
                    + ", ".join(valid_values)
                )

    @property
    def focus(self) -> Literal["implications", "missing", "unstated", "comprehensive"]:
        """
        Get the focus parameter value.

        Args:
            self: The decorator instance

        Returns:
            The focus parameter value
        """
        return self._focus

    @property
    def depth(self) -> Literal["surface", "moderate", "deep"]:
        """
        Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    @property
    def structure(self) -> Literal["before", "after", "integrated", "separate"]:
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
            "name": "negative_space",
            "focus": self.focus,
            "depth": self.depth,
            "structure": self.structure,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.focus is not None:
            params.append(f"focus={self.focus}")
        if self.depth is not None:
            params.append(f"depth={self.depth}")
        if self.structure is not None:
            params.append(f"structure={self.structure}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
