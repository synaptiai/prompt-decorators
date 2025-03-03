"""
Implementation of the Abductive decorator.

This module provides the Abductive decorator class for use in prompt engineering.

Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Abductive(BaseDecorator):
    """
    Structures the response using abductive reasoning, developing the most
    likely explanations for observations or phenomena. This decorator
    emphasizes inference to the best explanation and hypothetical
    reasoning to address incomplete information.

    Attributes:
        hypotheses: Number of alternative hypotheses or explanations to generate
        criteria: Specific criteria to evaluate hypotheses against (e.g., simplicity, explanatory power)
        rank: Whether to explicitly rank hypotheses by likelihood
    """

    decorator_name = "abductive"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        hypotheses: Any = 3,
        criteria: List[Any] = None,
        rank: bool = True,
    ) -> None:
        """
        Initialize the Abductive decorator.

        Args:
            hypotheses: Number of alternative hypotheses or explanations to generate
            criteria: Specific criteria to evaluate hypotheses against (e.g.,
                simplicity, explanatory power)
            rank: Whether to explicitly rank hypotheses by likelihood

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._hypotheses = hypotheses
        self._criteria = criteria
        self._rank = rank

        # Validate parameters
        if self._hypotheses is not None:
            if not isinstance(self._hypotheses, (int, float)) or isinstance(self._hypotheses, bool):
                raise ValidationError("The parameter 'hypotheses' must be a numeric value.")

        if self._criteria is not None:
            if not isinstance(self._criteria, (list, tuple)):
                raise ValidationError("The parameter 'criteria' must be an array.")

        if self._rank is not None:
            if not isinstance(self._rank, bool):
                raise ValidationError("The parameter 'rank' must be a boolean value.")


    @property
    def hypotheses(self) -> Any:
        """
        Get the hypotheses parameter value.

        Args:
            self: The decorator instance

        Returns:
            The hypotheses parameter value
        """
        return self._hypotheses

    @property
    def criteria(self) -> List[Any]:
        """
        Get the criteria parameter value.

        Args:
            self: The decorator instance

        Returns:
            The criteria parameter value
        """
        return self._criteria

    @property
    def rank(self) -> bool:
        """
        Get the rank parameter value.

        Args:
            self: The decorator instance

        Returns:
            The rank parameter value
        """
        return self._rank

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "abductive",
            "hypotheses": self.hypotheses,
            "criteria": self.criteria,
            "rank": self.rank,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.hypotheses is not None:
            params.append(f"hypotheses={self.hypotheses}")
        if self.criteria is not None:
            params.append(f"criteria={self.criteria}")
        if self.rank is not None:
            params.append(f"rank={self.rank}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"