"""Implementation of the Academic decorator.

This module provides the Academic decorator class for use in prompt engineering.

Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    AcademicFormatEnum,
    AcademicStyleEnum,
)


class Academic(BaseDecorator):
    """Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.

    Attributes:
        style: The academic discipline style to follow. (Literal["humanities", "scientific", "legal"])
        format: The citation format to use for references. (Literal["APA", "MLA", "Chicago", "Harvard", "IEEE"])
    """

    name = "academic"  # Class-level name for serialization
    decorator_name = "academic"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please structure your response following scholarly writing conventions"
        "appropriate for academic publications, using formal language,"
        "structured argumentation, and proper citations.",
        "parameterMapping": {
            "style": {
                "valueMap": {
                    "humanities": "Use conventions typical of humanities scholarship, including interpretive analysis, theoretical frameworks, and engagement with cultural, historical, or philosophical contexts.",
                    "scientific": "Follow scientific writing conventions, including clear methodology descriptions, evidence-based claims, objective tone, and precise technical terminology.",
                    "legal": "Adopt legal academic writing style, including careful statutory interpretation, case analysis, precedent citation, and attention to doctrinal frameworks.",
                },
            },
            "format": {
                "valueMap": {
                    "APA": "Format all citations and references according to APA (American Psychological Association) style, 7th edition.",
                    "MLA": "Format all citations and references according to MLA (Modern Language Association) style, 9th edition.",
                    "Chicago": "Format all citations and references according to Chicago style (Chicago Manual of Style), 17th edition.",
                    "Harvard": "Format all citations and references according to Harvard referencing style.",
                    "IEEE": "Format all citations and references according to IEEE citation style used in engineering and computer science.",
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
        style: Literal["humanities", "scientific", "legal"] = "scientific",
        format: Literal["APA", "MLA", "Chicago", "Harvard", "IEEE"] = "APA",
    ) -> None:
        """Initialize the Academic decorator.

        Args:
            style: The academic discipline style to follow
            format: The citation format to use for references


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._style = style
        self._format = format

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._style = style
        self._format = format

        # Validate parameters
        if self._style is not None:
            if not isinstance(self._style, str):
                raise ValidationError(
                    "The parameter 'style' must be a string type value."
                )
            if self._style not in ["humanities", "scientific", "legal"]:
                raise ValidationError(
                    f"The parameter 'style' must be one of the allowed enum values: ['humanities', 'scientific', 'legal']. Got {self._style}"
                )
        if self._format is not None:
            if not isinstance(self._format, str):
                raise ValidationError(
                    "The parameter 'format' must be a string type value."
                )
            if self._format not in ["APA", "MLA", "Chicago", "Harvard", "IEEE"]:
                raise ValidationError(
                    f"The parameter 'format' must be one of the allowed enum values: ['APA', 'MLA', 'Chicago', 'Harvard', 'IEEE']. Got {self._format}"
                )

    @property
    def style(self) -> Literal["humanities", "scientific", "legal"]:
        """Get the style parameter value.

        Args:
            self: The decorator instance

        Returns:
            The style parameter value
        """
        return self._style

    @property
    def format(self) -> Literal["APA", "MLA", "Chicago", "Harvard", "IEEE"]:
        """Get the format parameter value.

        Args:
            self: The decorator instance

        Returns:
            The format parameter value
        """
        return self._format

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "academic",
            "parameters": {
                "style": self.style,
                "format": self.format,
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
        if self.style is not None:
            params.append(f"style={self.style}")
        if self.format is not None:
            params.append(f"format={self.format}")

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
            "description": """Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.""",
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
