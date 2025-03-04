"""Implementation of the DecisionMatrix decorator.

This module provides the DecisionMatrix decorator class for use in prompt engineering.

Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    DecisionMatrixScaleEnum,
)


class DecisionMatrix(BaseDecorator):
    """Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.

    Attributes:
        options: Specific options or alternatives to evaluate in the matrix. (List[Any])
        criteria: Evaluation criteria to assess each option against. (List[Any])
        weighted: Whether to include weights for criteria importance. (bool)
        scale: Rating scale to use for evaluations. (Literal["1-5", "1-10", "qualitative", "percentage"])
    """

    name = "decision_matrix"  # Class-level name for serialization
    decorator_name = "decision_matrix"
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
        options: List[Any] = None,
        criteria: List[Any] = None,
        weighted: bool = False,
        scale: Literal["1-5", "1-10", "qualitative", "percentage"] = "1-5",
    ) -> None:
        """Initialize the DecisionMatrix decorator.

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
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._options = options
        self._criteria = criteria
        self._weighted = weighted
        self._scale = scale

        # Validate parameters
        if self._options is not None:
            if not isinstance(self._options, list):
                raise ValidationError(
                    "The parameter 'options' must be an array type value."
                )
        if self._criteria is not None:
            if not isinstance(self._criteria, list):
                raise ValidationError(
                    "The parameter 'criteria' must be an array type value."
                )
        if self._weighted is not None:
            if not isinstance(self._weighted, bool):
                raise ValidationError(
                    "The parameter 'weighted' must be a boolean type value."
                )
        if self._scale is not None:
            if not isinstance(self._scale, str):
                raise ValidationError(
                    "The parameter 'scale' must be a string type value."
                )
            if self._scale not in ["1-5", "1-10", "qualitative", "percentage"]:
                raise ValidationError(
                    f"The parameter 'scale' must be one of the allowed enum values: ['1-5', '1-10', 'qualitative', 'percentage']. Got {self._scale}"
                )

    @property
    def options(self) -> List[Any]:
        """Get the options parameter value.

        Args:
            self: The decorator instance

        Returns:
            The options parameter value
        """
        return self._options

    @property
    def criteria(self) -> List[Any]:
        """Get the criteria parameter value.

        Args:
            self: The decorator instance

        Returns:
            The criteria parameter value
        """
        return self._criteria

    @property
    def weighted(self) -> bool:
        """Get the weighted parameter value.

        Args:
            self: The decorator instance

        Returns:
            The weighted parameter value
        """
        return self._weighted

    @property
    def scale(self) -> Literal["1-5", "1-10", "qualitative", "percentage"]:
        """Get the scale parameter value.

        Args:
            self: The decorator instance

        Returns:
            The scale parameter value
        """
        return self._scale

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "decision_matrix",
            "parameters": {
                "options": self.options,
                "criteria": self.criteria,
                "weighted": self.weighted,
                "scale": self.scale,
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
            "description": """Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.""",
            "category": "general",
            "version": cls.version,
        }
