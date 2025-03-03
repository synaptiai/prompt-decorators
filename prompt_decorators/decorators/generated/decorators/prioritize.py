"""
Implementation of the Prioritize decorator.

This module provides the Prioritize decorator class for use in prompt engineering.

Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Prioritize(BaseDecorator):
    """
    Structures the response by ranking information according to
    importance, urgency, or impact. This decorator helps identify the most
    critical aspects of a topic and presents information in a hierarchical
    manner from most to least important.

    Attributes:
        criteria: The specific criterion to use for prioritization (e.g., importance, urgency, ROI)
        count: Number of prioritized items to include
        showRationale: Whether to explain the reasoning behind each priority ranking
    """

    decorator_name = "prioritize"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        criteria: str = "importance",
        count: Any = 5,
        showRationale: bool = False,
    ) -> None:
        """
        Initialize the Prioritize decorator.

        Args:
            criteria: The specific criterion to use for prioritization (e.g.,
                importance, urgency, ROI)
            count: Number of prioritized items to include
            showRationale: Whether to explain the reasoning behind each priority
                ranking

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._criteria = criteria
        self._count = count
        self._showRationale = showRationale

        # Validate parameters
        if self._criteria is not None:
            if not isinstance(self._criteria, str):
                raise ValidationError("The parameter 'criteria' must be a string value.")

        if self._count is not None:
            if not isinstance(self._count, (int, float)) or isinstance(self._count, bool):
                raise ValidationError("The parameter 'count' must be a numeric value.")

        if self._showRationale is not None:
            if not isinstance(self._showRationale, bool):
                raise ValidationError("The parameter 'showRationale' must be a boolean value.")


    @property
    def criteria(self) -> str:
        """
        Get the criteria parameter value.

        Args:
            self: The decorator instance

        Returns:
            The criteria parameter value
        """
        return self._criteria

    @property
    def count(self) -> Any:
        """
        Get the count parameter value.

        Args:
            self: The decorator instance

        Returns:
            The count parameter value
        """
        return self._count

    @property
    def showRationale(self) -> bool:
        """
        Get the showRationale parameter value.

        Args:
            self: The decorator instance

        Returns:
            The showRationale parameter value
        """
        return self._showRationale

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "prioritize",
            "criteria": self.criteria,
            "count": self.count,
            "showRationale": self.showRationale,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.criteria is not None:
            params.append(f"criteria={self.criteria}")
        if self.count is not None:
            params.append(f"count={self.count}")
        if self.showRationale is not None:
            params.append(f"showRationale={self.showRationale}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"