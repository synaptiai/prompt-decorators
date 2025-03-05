"""Implementation of the Narrative decorator.

This module provides the Narrative decorator class for use in prompt engineering.

Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    NarrativeLengthEnum,
    NarrativeStructureEnum,
)


class Narrative(BaseDecorator):
    """Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.

    Attributes:
        structure: The narrative structure to employ. (Literal["classic", "nonlinear", "case-study"])
        characters: Whether to include character elements in the narrative. (bool)
        length: The relative length of the narrative. (Literal["brief", "moderate", "extended"])
    """

    name = "narrative"  # Class-level name for serialization
    decorator_name = "narrative"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please structure your response as a story-based delivery that uses"
        "narrative elements and storytelling techniques to make the information"
        "engaging, memorable, and contextually rich.",
        "parameterMapping": {
            "structure": {
                "valueMap": {
                    "classic": "Use a traditional narrative arc with a clear beginning, middle, and end, following a logical progression of setup, conflict/challenge, and resolution.",
                    "nonlinear": "Use a nonlinear narrative structure that may include flashbacks, flash-forwards, or parallel storylines to present the information from multiple temporal perspectives.",
                    "case-study": "Structure the response as a real or hypothetical case study that examines specific situations, decisions, and outcomes to illustrate the key points.",
                },
            },
            "characters": {
                "valueMap": {
                    "true": "Include character elements such as personas, stakeholders, or representative individuals that the audience can relate to and follow throughout the narrative.",
                    "false": "Focus on situations, processes, and outcomes without personifying the narrative through specific characters or personas.",
                },
            },
            "length": {
                "valueMap": {
                    "brief": "Keep the narrative concise and focused, using storytelling elements economically while still conveying the essential information.",
                    "moderate": "Develop the narrative with sufficient detail to engage the reader while maintaining a balanced pace and moderate length.",
                    "extended": "Create a fully developed narrative with rich details, multiple story beats, and thorough exploration of the topic through storytelling.",
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
        structure: Literal["classic", "nonlinear", "case-study"] = "classic",
        characters: bool = True,
        length: Literal["brief", "moderate", "extended"] = "moderate",
    ) -> None:
        """Initialize the Narrative decorator.

        Args:
            structure: The narrative structure to employ
            characters: Whether to include character elements in the narrative
            length: The relative length of the narrative


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._structure = structure
        self._characters = characters
        self._length = length

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._structure = structure
        self._characters = characters
        self._length = length

        # Validate parameters
        if self._structure is not None:
            if not isinstance(self._structure, str):
                raise ValidationError(
                    "The parameter 'structure' must be a string type value."
                )
            if self._structure not in ["classic", "nonlinear", "case-study"]:
                raise ValidationError(
                    f"The parameter 'structure' must be one of the allowed enum values: ['classic', 'nonlinear', 'case-study']. Got {self._structure}"
                )
        if self._characters is not None:
            if not isinstance(self._characters, bool):
                raise ValidationError(
                    "The parameter 'characters' must be a boolean type value."
                )
        if self._length is not None:
            if not isinstance(self._length, str):
                raise ValidationError(
                    "The parameter 'length' must be a string type value."
                )
            if self._length not in ["brief", "moderate", "extended"]:
                raise ValidationError(
                    f"The parameter 'length' must be one of the allowed enum values: ['brief', 'moderate', 'extended']. Got {self._length}"
                )

    @property
    def structure(self) -> Literal["classic", "nonlinear", "case-study"]:
        """Get the structure parameter value.

        Args:
            self: The decorator instance

        Returns:
            The structure parameter value
        """
        return self._structure

    @property
    def characters(self) -> bool:
        """Get the characters parameter value.

        Args:
            self: The decorator instance

        Returns:
            The characters parameter value
        """
        return self._characters

    @property
    def length(self) -> Literal["brief", "moderate", "extended"]:
        """Get the length parameter value.

        Args:
            self: The decorator instance

        Returns:
            The length parameter value
        """
        return self._length

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "narrative",
            "parameters": {
                "structure": self.structure,
                "characters": self.characters,
                "length": self.length,
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
        if self.structure is not None:
            params.append(f"structure={self.structure}")
        if self.characters is not None:
            params.append(f"characters={self.characters}")
        if self.length is not None:
            params.append(f"length={self.length}")

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
            "description": """Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.""",
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
