"""Implementation of the CiteSources decorator.

This module provides the CiteSources decorator class for use in prompt engineering.

Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    CiteSourcesFormatEnum,
    CiteSourcesStyleEnum,
)


class CiteSources(BaseDecorator):
    """Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.

    Attributes:
        style: The placement and format of citations within the response. (Literal["inline", "footnote", "endnote"])
        format: The citation format to use. (Literal["APA", "MLA", "Chicago", "Harvard", "IEEE"])
        comprehensive: Whether to cite every claim (true) or only major claims (false). (bool)
    """

    name = "cite_sources"  # Class-level name for serialization
    decorator_name = "cite_sources"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please include citations for factual claims in your response to"
        "enhance credibility and enable verification.",
        "parameterMapping": {
            "style": {
                "valueMap": {
                    "inline": "Add citations directly in the text using parenthetical references.",
                    "footnote": "Use numbered footnotes for citations, with footnotes appearing at the bottom of relevant sections.",
                    "endnote": "Use numbered endnotes for citations, with all notes appearing in a References section at the end.",
                },
            },
            "format": {
                "valueMap": {
                    "APA": "Format citations according to APA style guidelines.",
                    "MLA": "Format citations according to MLA style guidelines.",
                    "Chicago": "Format citations according to Chicago Manual of Style guidelines.",
                    "Harvard": "Format citations according to Harvard referencing style guidelines.",
                    "IEEE": "Format citations according to IEEE citation style guidelines.",
                },
            },
            "comprehensive": {
                "valueMap": {
                    "true": "Cite every factual claim, including commonly known facts.",
                    "false": "Only cite major claims, specialized knowledge, statistics, and direct quotes.",
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
        style: Literal["inline", "footnote", "endnote"] = "inline",
        format: Literal["APA", "MLA", "Chicago", "Harvard", "IEEE"] = "APA",
        comprehensive: bool = False,
    ) -> None:
        """Initialize the CiteSources decorator.

        Args:
            style: The placement and format of citations within the response
            format: The citation format to use
            comprehensive: Whether to cite every claim (true) or only major claims (false)


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._style = style
        self._format = format
        self._comprehensive = comprehensive

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._style = style
        self._format = format
        self._comprehensive = comprehensive

        # Validate parameters
        if self._style is not None:
            if not isinstance(self._style, str):
                raise ValidationError(
                    "The parameter 'style' must be a string type value."
                )
            if self._style not in ["inline", "footnote", "endnote"]:
                raise ValidationError(
                    f"The parameter 'style' must be one of the allowed enum values: ['inline', 'footnote', 'endnote']. Got {self._style}"
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
        if self._comprehensive is not None:
            if not isinstance(self._comprehensive, bool):
                raise ValidationError(
                    "The parameter 'comprehensive' must be a boolean type value."
                )

    @property
    def style(self) -> Literal["inline", "footnote", "endnote"]:
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

    @property
    def comprehensive(self) -> bool:
        """Get the comprehensive parameter value.

        Args:
            self: The decorator instance

        Returns:
            The comprehensive parameter value
        """
        return self._comprehensive

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "cite_sources",
            "parameters": {
                "style": self.style,
                "format": self.format,
                "comprehensive": self.comprehensive,
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
        if self.comprehensive is not None:
            params.append(f"comprehensive={self.comprehensive}")

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
            "description": """Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.""",
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
