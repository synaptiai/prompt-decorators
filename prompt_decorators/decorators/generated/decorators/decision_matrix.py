"""
Implementation of the DecisionMatrix decorator.

This module provides the DecisionMatrix decorator class for use in prompt engineering.

Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    DecisionMatrixScaleEnum,
)


class DecisionMatrix(BaseDecorator):
    """
    Structures the response as a decision matrix, evaluating options
    against multiple criteria. This decorator facilitates systematic
    comparison and selection between alternatives based on weighted or
    unweighted criteria.

    Attributes:
        options: Specific options or alternatives to evaluate in the matrix
        criteria: Evaluation criteria to assess each option against
        weighted: Whether to include weights for criteria importance
        scale: Rating scale to use for evaluations
    """

    decorator_name = "decision_matrix"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        options: List[Any] = None,
        criteria: List[Any] = None,
        weighted: bool = False,
        scale: Literal["1-5", "1-10", "qualitative", "percentage"] = "1-5",
    ) -> None:
        """
        Initialize the DecisionMatrix decorator.

        Args:
            options: Specific options or alternatives to evaluate in the matrix
            criteria: Evaluation criteria to assess each option against
            weighted: Whether to include weights for criteria importance
            scale: Rating scale to use for evaluations

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._options = options
        self._criteria = criteria
        self._weighted = weighted
        self._scale = scale

        # Validate parameters
        if self._options is not None:
            if not isinstance(self._options, (list, tuple)):
                raise ValidationError("The parameter 'options' must be an array.")

        if self._criteria is not None:
            if not isinstance(self._criteria, (list, tuple)):
                raise ValidationError("The parameter 'criteria' must be an array.")

        if self._weighted is not None:
            if not isinstance(self._weighted, bool):
                raise ValidationError("The parameter 'weighted' must be a boolean value.")

        if self._scale is not None:
            valid_values = ["1-5", "1-10", "qualitative", "percentage"]
            if self._scale not in valid_values:
                raise ValidationError("The parameter 'scale' must be one of the following values: " + ", ".join(valid_values))


    @property
    def options(self) -> List[Any]:
        """
        Get the options parameter value.

        Args:
            self: The decorator instance

        Returns:
            The options parameter value
        """
        return self._options

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
    def weighted(self) -> bool:
        """
        Get the weighted parameter value.

        Args:
            self: The decorator instance

        Returns:
            The weighted parameter value
        """
        return self._weighted

    @property
    def scale(self) -> Literal["1-5", "1-10", "qualitative", "percentage"]:
        """
        Get the scale parameter value.

        Args:
            self: The decorator instance

        Returns:
            The scale parameter value
        """
        return self._scale

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "decision_matrix",
            "options": self.options,
            "criteria": self.criteria,
            "weighted": self.weighted,
            "scale": self.scale,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.options is not None:
            params.append(f"options={self.options}")
        if self.criteria is not None:
            params.append(f"criteria={self.criteria}")
        if self.weighted is not None:
            params.append(f"weighted={self.weighted}")
        if self.scale is not None:
            params.append(f"scale={self.scale}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"