"""
Implementation of the FindGaps decorator.

This module provides the FindGaps decorator class for use in prompt engineering.

Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    FindGapsAspectsEnum,
    FindGapsDepthEnum,
)


class FindGaps(BaseDecorator):
    """
    Identifies missing elements, unanswered questions, or overlooked
    considerations in an idea, plan, or argument. This decorator helps
    improve completeness by systematically discovering and highlighting
    gaps that need addressing.

    Attributes:
        aspects: The specific types of gaps to focus on finding
        depth: How thoroughly to analyze for gaps
        solutions: Whether to suggest solutions or approaches for addressing the identified gaps
    """

    decorator_name = "find_gaps"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        aspects: Literal["questions", "resources", "stakeholders", "risks", "dependencies", "comprehensive"] = "comprehensive",
        depth: Literal["basic", "thorough", "exhaustive"] = "thorough",
        solutions: bool = True,
    ) -> None:
        """
        Initialize the FindGaps decorator.

        Args:
            aspects: The specific types of gaps to focus on finding
            depth: How thoroughly to analyze for gaps
            solutions: Whether to suggest solutions or approaches for addressing
                the identified gaps

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._aspects = aspects
        self._depth = depth
        self._solutions = solutions

        # Validate parameters
        if self._aspects is not None:
            valid_values = ["questions", "resources", "stakeholders", "risks", "dependencies", "comprehensive"]
            if self._aspects not in valid_values:
                raise ValidationError("The parameter 'aspects' must be one of the following values: " + ", ".join(valid_values))

        if self._depth is not None:
            valid_values = ["basic", "thorough", "exhaustive"]
            if self._depth not in valid_values:
                raise ValidationError("The parameter 'depth' must be one of the following values: " + ", ".join(valid_values))

        if self._solutions is not None:
            if not isinstance(self._solutions, bool):
                raise ValidationError("The parameter 'solutions' must be a boolean value.")


    @property
    def aspects(self) -> Literal["questions", "resources", "stakeholders", "risks", "dependencies", "comprehensive"]:
        """
        Get the aspects parameter value.

        Args:
            self: The decorator instance

        Returns:
            The aspects parameter value
        """
        return self._aspects

    @property
    def depth(self) -> Literal["basic", "thorough", "exhaustive"]:
        """
        Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    @property
    def solutions(self) -> bool:
        """
        Get the solutions parameter value.

        Args:
            self: The decorator instance

        Returns:
            The solutions parameter value
        """
        return self._solutions

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "find_gaps",
            "aspects": self.aspects,
            "depth": self.depth,
            "solutions": self.solutions,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.aspects is not None:
            params.append(f"aspects={self.aspects}")
        if self.depth is not None:
            params.append(f"depth={self.depth}")
        if self.solutions is not None:
            params.append(f"solutions={self.solutions}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"