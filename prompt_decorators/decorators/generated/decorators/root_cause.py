"""
Implementation of the RootCause decorator.

This module provides the RootCause decorator class for use in prompt engineering.

Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    RootCauseMethodEnum,
)


class RootCause(BaseDecorator):
    """
    Structures the response to systematically analyze underlying causes of
    problems or situations. This decorator applies formal root cause
    analysis methodologies to identify fundamental factors rather than
    just symptoms or immediate causes.

    Attributes:
        method: The specific root cause analysis methodology to apply
        depth: Level of detail in the analysis (for 5whys, represents number of 'why' iterations)
    """

    decorator_name = "root_cause"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        method: Literal["5whys", "fishbone", "pareto"] = "5whys",
        depth: Any = 5,
    ) -> None:
        """
        Initialize the RootCause decorator.

        Args:
            method: The specific root cause analysis methodology to apply
            depth: Level of detail in the analysis (for 5whys, represents
                number of 'why' iterations)

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._method = method
        self._depth = depth

        # Validate parameters
        if self._method is not None:
            valid_values = ["5whys", "fishbone", "pareto"]
            if self._method not in valid_values:
                raise ValidationError("The parameter 'method' must be one of the following values: " + ", ".join(valid_values))

        if self._depth is not None:
            if not isinstance(self._depth, (int, float)) or isinstance(self._depth, bool):
                raise ValidationError("The parameter 'depth' must be a numeric value.")


    @property
    def method(self) -> Literal["5whys", "fishbone", "pareto"]:
        """
        Get the method parameter value.

        Args:
            self: The decorator instance

        Returns:
            The method parameter value
        """
        return self._method

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
            "name": "root_cause",
            "method": self.method,
            "depth": self.depth,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.method is not None:
            params.append(f"method={self.method}")
        if self.depth is not None:
            params.append(f"depth={self.depth}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"