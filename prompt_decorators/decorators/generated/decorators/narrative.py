"""
Implementation of the Narrative decorator.

This module provides the Narrative decorator class for use in prompt engineering.

Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    NarrativeStructureEnum,
    NarrativeLengthEnum,
)


class Narrative(BaseDecorator):
    """
    Structures the response as a story-based delivery with narrative
    elements. This decorator employs storytelling techniques to make
    information more engaging, memorable, and contextually rich.

    Attributes:
        structure: The narrative structure to employ
        characters: Whether to include character elements in the narrative
        length: The relative length of the narrative
    """

    decorator_name = "narrative"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        structure: Literal["classic", "nonlinear", "case-study"] = "classic",
        characters: bool = True,
        length: Literal["brief", "moderate", "extended"] = "moderate",
    ) -> None:
        """
        Initialize the Narrative decorator.

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
        if self._structure is not None:
            valid_values = ["classic", "nonlinear", "case-study"]
            if self._structure not in valid_values:
                raise ValidationError("The parameter 'structure' must be one of the following values: " + ", ".join(valid_values))

        if self._characters is not None:
            if not isinstance(self._characters, bool):
                raise ValidationError("The parameter 'characters' must be a boolean value.")

        if self._length is not None:
            valid_values = ["brief", "moderate", "extended"]
            if self._length not in valid_values:
                raise ValidationError("The parameter 'length' must be one of the following values: " + ", ".join(valid_values))


    @property
    def structure(self) -> Literal["classic", "nonlinear", "case-study"]:
        """
        Get the structure parameter value.

        Args:
            self: The decorator instance

        Returns:
            The structure parameter value
        """
        return self._structure

    @property
    def characters(self) -> bool:
        """
        Get the characters parameter value.

        Args:
            self: The decorator instance

        Returns:
            The characters parameter value
        """
        return self._characters

    @property
    def length(self) -> Literal["brief", "moderate", "extended"]:
        """
        Get the length parameter value.

        Args:
            self: The decorator instance

        Returns:
            The length parameter value
        """
        return self._length

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "narrative",
            "structure": self.structure,
            "characters": self.characters,
            "length": self.length,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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