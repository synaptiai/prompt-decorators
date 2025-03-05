"""Implementation of the NegativeSpace decorator.

This module provides the NegativeSpace decorator class for use in prompt engineering.

Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    NegativeSpaceDepthEnum,
    NegativeSpaceFocusEnum,
    NegativeSpaceStructureEnum,
)


class NegativeSpace(BaseDecorator):
    """Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.

    Attributes:
        focus: The specific aspect of negative space to emphasize. (Literal["implications", "missing", "unstated", "comprehensive"])
        depth: How deeply to explore the negative space. (Literal["surface", "moderate", "deep"])
        structure: How to present the negative space analysis. (Literal["before", "after", "integrated", "separate"])
    """

    name = "negative_space"  # Class-level name for serialization
    decorator_name = "negative_space"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please analyze the 'negative space' surrounding this topic - focusing"
        "on what is not explicitly stated, implied, or missing. Identify"
        "unexplored angles, implicit assumptions, unasked questions, and"
        "overlooked contextual elements.",
        "parameterMapping": {
            "focus": {
                "valueMap": {
                    "implications": "Focus primarily on the unstated implications and logical consequences that may not be immediately obvious.",
                    "missing": "Focus primarily on identifying missing elements, overlooked factors, and gaps in the topic or question.",
                    "unstated": "Focus primarily on unstated assumptions, implicit premises, and underlying beliefs that frame the topic.",
                    "comprehensive": "Take a comprehensive approach to negative space, addressing implications, missing elements, unstated assumptions, and other overlooked aspects.",
                },
            },
            "depth": {
                "valueMap": {
                    "surface": "Provide a surface-level exploration of the negative space, identifying the most obvious unstated elements without extensive analysis.",
                    "moderate": "Conduct a moderately deep exploration of the negative space, with substantial attention to important unstated elements and their significance.",
                    "deep": "Perform a deep examination of the negative space, with thorough exploration of subtle, non-obvious unstated elements and their complex interconnections.",
                },
            },
            "structure": {
                "valueMap": {
                    "before": "Present the negative space analysis before addressing the explicit content of the topic.",
                    "after": "First address the explicit content of the topic, then follow with the negative space analysis.",
                    "integrated": "Integrate the negative space analysis throughout your response, addressing both explicit content and unstated elements in parallel.",
                    "separate": "Clearly separate the negative space analysis from the explicit content with distinct sections and headings.",
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
        focus: Literal[
            "implications", "missing", "unstated", "comprehensive"
        ] = "comprehensive",
        depth: Literal["surface", "moderate", "deep"] = "moderate",
        structure: Literal["before", "after", "integrated", "separate"] = "integrated",
    ) -> None:
        """Initialize the NegativeSpace decorator.

        Args:
            focus: The specific aspect of negative space to emphasize
            depth: How deeply to explore the negative space
            structure: How to present the negative space analysis


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._focus = focus
        self._depth = depth
        self._structure = structure

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._focus = focus
        self._depth = depth
        self._structure = structure

        # Validate parameters
        if self._focus is not None:
            if not isinstance(self._focus, str):
                raise ValidationError(
                    "The parameter 'focus' must be a string type value."
                )
            if self._focus not in [
                "implications",
                "missing",
                "unstated",
                "comprehensive",
            ]:
                raise ValidationError(
                    f"The parameter 'focus' must be one of the allowed enum values: ['implications', 'missing', 'unstated', 'comprehensive']. Got {self._focus}"
                )
        if self._depth is not None:
            if not isinstance(self._depth, str):
                raise ValidationError(
                    "The parameter 'depth' must be a string type value."
                )
            if self._depth not in ["surface", "moderate", "deep"]:
                raise ValidationError(
                    f"The parameter 'depth' must be one of the allowed enum values: ['surface', 'moderate', 'deep']. Got {self._depth}"
                )
        if self._structure is not None:
            if not isinstance(self._structure, str):
                raise ValidationError(
                    "The parameter 'structure' must be a string type value."
                )
            if self._structure not in ["before", "after", "integrated", "separate"]:
                raise ValidationError(
                    f"The parameter 'structure' must be one of the allowed enum values: ['before', 'after', 'integrated', 'separate']. Got {self._structure}"
                )

    @property
    def focus(self) -> Literal["implications", "missing", "unstated", "comprehensive"]:
        """Get the focus parameter value.

        Args:
            self: The decorator instance

        Returns:
            The focus parameter value
        """
        return self._focus

    @property
    def depth(self) -> Literal["surface", "moderate", "deep"]:
        """Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    @property
    def structure(self) -> Literal["before", "after", "integrated", "separate"]:
        """Get the structure parameter value.

        Args:
            self: The decorator instance

        Returns:
            The structure parameter value
        """
        return self._structure

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "negative_space",
            "parameters": {
                "focus": self.focus,
                "depth": self.depth,
                "structure": self.structure,
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
        if self.focus is not None:
            params.append(f"focus={self.focus}")
        if self.depth is not None:
            params.append(f"depth={self.depth}")
        if self.structure is not None:
            params.append(f"structure={self.structure}")

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
            "description": """Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.""",
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
