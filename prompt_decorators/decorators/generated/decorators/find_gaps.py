"""
Implementation of the FindGaps decorator.

This module provides the FindGaps decorator class for use in prompt engineering.

Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
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
        aspects: Literal[
            "questions",
            "resources",
            "stakeholders",
            "risks",
            "dependencies",
            "comprehensive",
        ] = "comprehensive",
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
        # Validate parameters
        if self._aspects is not None:
            if not isinstance(self._aspects, str):
                raise ValidationError(
                    "The parameter 'aspects' must be a string type value."
                )
            if self._aspects not in [
                "questions",
                "resources",
                "stakeholders",
                "risks",
                "dependencies",
                "comprehensive",
            ]:
                raise ValidationError(
                    f"The parameter 'aspects' must be one of the allowed enum values: ['questions', 'resources', 'stakeholders', 'risks', 'dependencies', 'comprehensive']. Got {self._aspects}"
                )
        if self._depth is not None:
            if not isinstance(self._depth, str):
                raise ValidationError(
                    "The parameter 'depth' must be a string type value."
                )
            if self._depth not in ["basic", "thorough", "exhaustive"]:
                raise ValidationError(
                    f"The parameter 'depth' must be one of the allowed enum values: ['basic', 'thorough', 'exhaustive']. Got {self._depth}"
                )
        if self._solutions is not None:
            if not isinstance(self._solutions, bool):
                raise ValidationError(
                    "The parameter 'solutions' must be a boolean type value."
                )

    @property
    def aspects(
        self,
    ) -> Literal[
        "questions",
        "resources",
        "stakeholders",
        "risks",
        "dependencies",
        "comprehensive",
    ]:
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
            "parameters": {
                "aspects": self.aspects,
                "depth": self.depth,
                "solutions": self.solutions,
            },
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
            "description": """Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.""",
            "category": "general",
            "version": cls.version,
        }
