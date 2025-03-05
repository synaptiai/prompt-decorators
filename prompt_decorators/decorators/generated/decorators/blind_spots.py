"""Implementation of the BlindSpots decorator.

This module provides the BlindSpots decorator class for use in prompt engineering.

Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    BlindSpotsDepthEnum,
    BlindSpotsPositionEnum,
)


class BlindSpots(BaseDecorator):
    """Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.

    Attributes:
        categories: Specific categories of blind spots to check for (e.g., cultural, temporal, confirmation bias). (List[Any])
        depth: How thoroughly to analyze for blind spots. (Literal["basic", "thorough", "comprehensive"])
        position: Where to place the blind spots analysis. (Literal["after", "before", "integrated"])
    """

    name = "blind_spots"  # Class-level name for serialization
    decorator_name = "blind_spots"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please identify potential cognitive blind spots, unstated assumptions,"
        "and overlooked perspectives in your response. Explicitly acknowledge"
        "the limitations and biases that might affect your analysis of the"
        "topic.",
        "parameterMapping": {
            "categories": {
                "format": "Focus specifically on identifying these categories of blind spots: {value}. For each category, explain how it might influence the analysis.",
            },
            "depth": {
                "valueMap": {
                    "basic": "Provide a basic assessment of key blind spots, focusing on the most significant limitations without extensive elaboration.",
                    "thorough": "Conduct a thorough analysis of blind spots, with substantial attention to underlying assumptions and alternative perspectives.",
                    "comprehensive": "Perform a comprehensive examination of blind spots, including detailed exploration of subtle biases, edge cases, and interconnected limitations.",
                },
            },
            "position": {
                "valueMap": {
                    "after": "Present your main analysis first, then follow it with a separate section that identifies blind spots and limitations in your reasoning.",
                    "before": "Begin with an acknowledgment of potential blind spots and limitations that might affect your analysis, then proceed with your main response.",
                    "integrated": "Integrate the identification of blind spots throughout your analysis, pointing out limitations and alternative perspectives as they become relevant to each aspect of the topic.",
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
        categories: List[Any] = None,
        depth: Literal["basic", "thorough", "comprehensive"] = "thorough",
        position: Literal["after", "before", "integrated"] = "after",
    ) -> None:
        """Initialize the BlindSpots decorator.

        Args:
            categories: Specific categories of blind spots to check for (e.g., cultural, temporal, confirmation bias)
            depth: How thoroughly to analyze for blind spots
            position: Where to place the blind spots analysis


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._categories = categories
        self._depth = depth
        self._position = position

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._categories = categories
        self._depth = depth
        self._position = position

        # Validate parameters
        if self._categories is not None:
            if not isinstance(self._categories, list):
                raise ValidationError(
                    "The parameter 'categories' must be an array type value."
                )
        if self._depth is not None:
            if not isinstance(self._depth, str):
                raise ValidationError(
                    "The parameter 'depth' must be a string type value."
                )
            if self._depth not in ["basic", "thorough", "comprehensive"]:
                raise ValidationError(
                    f"The parameter 'depth' must be one of the allowed enum values: ['basic', 'thorough', 'comprehensive']. Got {self._depth}"
                )
        if self._position is not None:
            if not isinstance(self._position, str):
                raise ValidationError(
                    "The parameter 'position' must be a string type value."
                )
            if self._position not in ["after", "before", "integrated"]:
                raise ValidationError(
                    f"The parameter 'position' must be one of the allowed enum values: ['after', 'before', 'integrated']. Got {self._position}"
                )

    @property
    def categories(self) -> List[Any]:
        """Get the categories parameter value.

        Args:
            self: The decorator instance

        Returns:
            The categories parameter value
        """
        return self._categories

    @property
    def depth(self) -> Literal["basic", "thorough", "comprehensive"]:
        """Get the depth parameter value.

        Args:
            self: The decorator instance

        Returns:
            The depth parameter value
        """
        return self._depth

    @property
    def position(self) -> Literal["after", "before", "integrated"]:
        """Get the position parameter value.

        Args:
            self: The decorator instance

        Returns:
            The position parameter value
        """
        return self._position

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "blind_spots",
            "parameters": {
                "categories": self.categories,
                "depth": self.depth,
                "position": self.position,
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
        if self.categories is not None:
            params.append(f"categories={self.categories}")
        if self.depth is not None:
            params.append(f"depth={self.depth}")
        if self.position is not None:
            params.append(f"position={self.position}")

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
            "description": """Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.""",
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
