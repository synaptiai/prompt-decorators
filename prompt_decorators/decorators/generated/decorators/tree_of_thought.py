"""
Implementation of the TreeOfThought decorator.

This module provides the TreeOfThought decorator class for use in prompt engineering.

Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.
"""

from typing import Any, Dict

from prompt_decorators.core.base import BaseDecorator, ValidationError


class TreeOfThought(BaseDecorator):
    """
    Organizes the response as a branching exploration of multiple
    reasoning paths. This decorator enables the AI to consider several
    possible approaches or hypotheses simultaneously, exploring the
    implications of each before reaching conclusions.

    Attributes:
        branches: Number of different reasoning branches to explore
        depth: Maximum depth of reasoning in each branch
        pruning: Whether to eliminate less promising branches early
    """

    decorator_name = "tree_of_thought"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        branches: Any = 3,
        depth: Any = 3,
        pruning: bool = False,
    ) -> None:
        """
        Initialize the TreeOfThought decorator.

        Args:
            branches: Number of different reasoning branches to explore
            depth: Maximum depth of reasoning in each branch
            pruning: Whether to eliminate less promising branches early

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._branches = branches
        self._depth = depth
        self._pruning = pruning

        # Validate parameters
        if self._branches is not None:
            if not isinstance(self._branches, (int, float)) or isinstance(
                self._branches, bool
            ):
                raise ValidationError(
                    "The parameter 'branches' must be a numeric value."
                )

        if self._depth is not None:
            if not isinstance(self._depth, (int, float)) or isinstance(
                self._depth, bool
            ):
                raise ValidationError("The parameter 'depth' must be a numeric value.")

        if self._pruning is not None:
            if not isinstance(self._pruning, bool):
                raise ValidationError(
                    "The parameter 'pruning' must be a boolean value."
                )

    @property
    def branches(self) -> Any:
        """
        Get the branches parameter value.

        Args:
            self: The decorator instance

        Returns:
            The branches parameter value
        """
        return self._branches

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

    @property
    def pruning(self) -> bool:
        """
        Get the pruning parameter value.

        Args:
            self: The decorator instance

        Returns:
            The pruning parameter value
        """
        return self._pruning

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "tree_of_thought",
            "branches": self.branches,
            "depth": self.depth,
            "pruning": self.pruning,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.branches is not None:
            params.append(f"branches={self.branches}")
        if self.depth is not None:
            params.append(f"depth={self.depth}")
        if self.pruning is not None:
            params.append(f"pruning={self.pruning}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
