"""Implementation of the TableFormat decorator.

This module provides the TableFormat decorator class for use in prompt engineering.

Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    TableFormatAlignmentEnum,
    TableFormatFormatEnum,
)


class TableFormat(BaseDecorator):
    """Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.

    Attributes:
        columns: List of column names for the table. (List[Any])
        format: Format style for the table representation. (Literal["markdown", "ascii", "csv"])
        alignment: Text alignment within table cells. (Literal["left", "center", "right"])
    """

    name = "table_format"  # Class-level name for serialization
    decorator_name = "table_format"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please present your response in a tabular format with clearly defined"
        "columns to organize the information effectively.",
        "parameterMapping": {
            "columns": {
                "format": "The table should include the following columns: {value}.",
            },
            "format": {
                "valueMap": {
                    "markdown": "Format the table using markdown syntax with headers and cell separators (e.g., | Column1 | Column2 |).",
                    "ascii": "Format the table using ASCII characters for borders and separators to create a plain text table.",
                    "csv": "Format the table as comma-separated values (CSV) with each row on a new line and values separated by commas.",
                },
            },
            "alignment": {
                "valueMap": {
                    "left": "Align all text within cells to the left.",
                    "center": "Center all text within cells.",
                    "right": "Align all text within cells to the right.",
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
        columns: List[Any],
        format: Literal["markdown", "ascii", "csv"] = "markdown",
        alignment: Literal["left", "center", "right"] = "left",
    ) -> None:
        """Initialize the TableFormat decorator.

        Args:
            columns: List of column names for the table
            format: Format style for the table representation
            alignment: Text alignment within table cells


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._columns = columns
        self._format = format
        self._alignment = alignment

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._columns = columns
        self._format = format
        self._alignment = alignment

        # Validate parameters
        if self._columns is not None:
            if not isinstance(self._columns, list):
                raise ValidationError(
                    "The parameter 'columns' must be an array type value."
                )
        if self._format is not None:
            if not isinstance(self._format, str):
                raise ValidationError(
                    "The parameter 'format' must be a string type value."
                )
            if self._format not in ["markdown", "ascii", "csv"]:
                raise ValidationError(
                    f"The parameter 'format' must be one of the allowed enum values: ['markdown', 'ascii', 'csv']. Got {self._format}"
                )
        if self._alignment is not None:
            if not isinstance(self._alignment, str):
                raise ValidationError(
                    "The parameter 'alignment' must be a string type value."
                )
            if self._alignment not in ["left", "center", "right"]:
                raise ValidationError(
                    f"The parameter 'alignment' must be one of the allowed enum values: ['left', 'center', 'right']. Got {self._alignment}"
                )

    @property
    def columns(self) -> List[Any]:
        """Get the columns parameter value.

        Args:
            self: The decorator instance

        Returns:
            The columns parameter value
        """
        return self._columns

    @property
    def format(self) -> Literal["markdown", "ascii", "csv"]:
        """Get the format parameter value.

        Args:
            self: The decorator instance

        Returns:
            The format parameter value
        """
        return self._format

    @property
    def alignment(self) -> Literal["left", "center", "right"]:
        """Get the alignment parameter value.

        Args:
            self: The decorator instance

        Returns:
            The alignment parameter value
        """
        return self._alignment

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "table_format",
            "parameters": {
                "columns": self.columns,
                "format": self.format,
                "alignment": self.alignment,
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
        if self.columns is not None:
            params.append(f"columns={self.columns}")
        if self.format is not None:
            params.append(f"format={self.format}")
        if self.alignment is not None:
            params.append(f"alignment={self.alignment}")

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
            "description": """Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.""",
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
