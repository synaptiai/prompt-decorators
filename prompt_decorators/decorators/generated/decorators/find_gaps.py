"""Implementation of the FindGaps decorator.

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
    """Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.

    Attributes:
        aspects: The specific types of gaps to focus on finding. (Literal["questions", "resources", "stakeholders", "risks", "dependencies", "comprehensive"])
        depth: How thoroughly to analyze for gaps. (Literal["basic", "thorough", "exhaustive"])
        solutions: Whether to suggest solutions or approaches for addressing the identified gaps. (bool)
    """

    name = "find_gaps"  # Class-level name for serialization
    decorator_name = "find_gaps"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please first analyze the main content, then methodically identify"
        "missing elements, unanswered questions, or overlooked considerations"
        "that need addressing.",
        "parameterMapping": {
            "aspects": {
                "valueMap": {
                    "questions": "Focus specifically on identifying unanswered questions and unresolved issues that need clarification.",
                    "resources": "Focus specifically on identifying missing resources, tools, skills, or capabilities needed for implementation or success.",
                    "stakeholders": "Focus specifically on identifying overlooked stakeholders, individuals, or groups whose perspectives or needs are not adequately addressed.",
                    "risks": "Focus specifically on identifying potential risks, threats, and vulnerabilities that have not been adequately considered.",
                    "dependencies": "Focus specifically on identifying overlooked dependencies, prerequisites, or contingencies that could affect implementation or outcomes.",
                    "comprehensive": "Comprehensively identify gaps across multiple dimensions, including questions, resources, stakeholders, risks, and dependencies.",
                },
            },
            "depth": {
                "valueMap": {
                    "basic": "Conduct a focused analysis to identify the most obvious and critical gaps.",
                    "thorough": "Conduct a detailed analysis to identify both obvious and subtle gaps that might significantly impact outcomes.",
                    "exhaustive": "Conduct an extremely comprehensive analysis to identify all possible gaps, including edge cases and minor considerations.",
                },
            },
            "solutions": {
                "valueMap": {
                    "true": "For each identified gap, suggest potential solutions, approaches, or strategies to address it.",
                    "false": "Focus solely on identifying gaps without suggesting solutions or remedies.",
                },
            },
        },
        "placement": "prepend",
        "compositionBehavior": "accumulate",
    }

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
        """Initialize the FindGaps decorator.

        Args:
            aspects: The specific types of gaps to focus on finding
            depth: How thoroughly to analyze for gaps
            solutions: Whether to suggest solutions or approaches for addressing the identified gaps


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
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._aspects = aspects
        self._depth = depth
        self._solutions = solutions

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
        """Get the aspects parameter value.

        Args:
            self: The decorator instance

        Returns:
            The aspects parameter value
        """
        return self._aspects

    @property
    def depth(self) -> Literal["basic", "thorough", "exhaustive"]:
        """Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    @property
    def solutions(self) -> bool:
        """Get the solutions parameter value.

        Args:
            self: The decorator instance

        Returns:
            The solutions parameter value
        """
        return self._solutions

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

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
        """Convert the decorator to a string.

        Args:
            self: The decorator instance

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
            "description": """Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.""",
            "category": "general",
            "version": cls.version,
        }

    def apply_to_prompt(self, prompt: str) -> str:
        """Apply the decorator to a prompt.

        This method transforms the prompt using the transformation template.

        Args:
            prompt: The prompt to decorate

        Returns:
            The decorated prompt

        """
        # Use the apply_to_prompt implementation from BaseDecorator
        return super().apply_to_prompt(prompt)
