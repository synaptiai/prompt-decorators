"""
Implementation of the Analogical decorator.

This module provides the Analogical decorator class for use in prompt engineering.

Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Analogical(BaseDecorator):
    """
    Enhances explanations through the use of analogies and metaphors. This
    decorator helps make complex or abstract concepts more accessible by
    systematically comparing them to more familiar domains or experiences.

    Attributes:
        domain: Specific domain or context to draw analogies from (if not specified, will choose appropriate domains)
        count: Number of distinct analogies to provide
        depth: Level of detail in developing the analogy
    """

    decorator_name = "analogical"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        domain: str = "general",
        count: Any = 1,
        depth: Literal["brief", "moderate", "extended"] = "moderate",
    ) -> None:
        """
        Initialize the Analogical decorator.

        Args:
            domain: Specific domain or context to draw analogies from (if not
                specified, will choose appropriate domains)
            count: Number of distinct analogies to provide
            depth: Level of detail in developing the analogy

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._domain = domain
        self._count = count
        self._depth = depth

        # Validate parameters
        if self._domain is not None:
            if not isinstance(self._domain, str):
                raise ValidationError("The parameter 'domain' must be a string value.")

        if self._count is not None:
            if not isinstance(self._count, (int, float)) or isinstance(
                self._count, bool
            ):
                raise ValidationError("The parameter 'count' must be a numeric value.")

        if self._depth is not None:
            valid_values = ["brief", "moderate", "extended"]
            if self._depth not in valid_values:
                raise ValidationError(
                    "The parameter 'depth' must be one of the following values: "
                    + ", ".join(valid_values)
                )

    @property
    def domain(self) -> str:
        """
        Get the domain parameter value.

        Args:
            self: The decorator instance

        Returns:
            The domain parameter value
        """
        return self._domain

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
    def depth(self) -> Literal["brief", "moderate", "extended"]:
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
            "name": "analogical",
            "domain": self.domain,
            "count": self.count,
            "depth": self.depth,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.domain is not None:
            params.append(f"domain={self.domain}")
        if self.count is not None:
            params.append(f"count={self.count}")
        if self.depth is not None:
            params.append(f"depth={self.depth}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
