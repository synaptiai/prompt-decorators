"""
Implementation of the TreeOfThought decorator.

This module provides the TreeOfThought decorator class for use in prompt engineering.

Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


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

    @property
    def name(self) -> str:
        """
        Get the name of the decorator.

        Returns:
            The name of the decorator
        """
        return self.decorator_name

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
        # Validate parameters
        if self._branches is not None:
            if not isinstance(self._branches, (int, float)):
                raise ValidationError(
                    "The parameter 'branches' must be a numeric type value."
                )
            if self._branches < 2:
                raise ValidationError(
                    "The parameter 'branches' must be greater than or equal to 2."
                )
            if self._branches > 5:
                raise ValidationError(
                    "The parameter 'branches' must be less than or equal to 5."
                )
        if self._depth is not None:
            if not isinstance(self._depth, (int, float)):
                raise ValidationError(
                    "The parameter 'depth' must be a numeric type value."
                )
            if self._depth < 1:
                raise ValidationError(
                    "The parameter 'depth' must be greater than or equal to 1."
                )
            if self._depth > 5:
                raise ValidationError(
                    "The parameter 'depth' must be less than or equal to 5."
                )
        if self._pruning is not None:
            if not isinstance(self._pruning, bool):
                raise ValidationError(
                    "The parameter 'pruning' must be a boolean type value."
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
            "parameters": {
                "branches": self.branches,
                "depth": self.depth,
                "pruning": self.pruning,
            },
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

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt string.

        Args:
            prompt: The original prompt string

        Returns:
            The modified prompt string
        """
        # This is a placeholder implementation
        # Subclasses should override this method with specific behavior
        return prompt

    @classmethod
    def is_compatible_with_version(cls, version: str) -> bool:
        """
        Check if the decorator is compatible with a specific version.

        Args:
            version: The version to check compatibility with

        Returns:
            True if compatible, False otherwise

        Raises:
            IncompatibleVersionError: If the version is incompatible
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
        """
        Get metadata about the decorator.

        Returns:
            Dictionary containing metadata about the decorator
        """
        return {
            "name": cls.__name__,
            "description": """Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.""",
            "category": "general",
            "version": cls.version,
        }
