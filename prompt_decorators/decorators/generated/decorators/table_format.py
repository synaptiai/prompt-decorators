"""
Implementation of the TableFormat decorator.

This module provides the TableFormat decorator class for use in prompt engineering.

Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    TableFormatFormatEnum,
    TableFormatAlignmentEnum,
)


class TableFormat(BaseDecorator):
    """
    Structures the AI's response in a tabular format with defined columns.
    This decorator is ideal for presenting comparative data, lists of
    items with attributes, or any information that benefits from clear
    columnar organization.

    Attributes:
        columns: List of column names for the table
        format: Format style for the table representation
        alignment: Text alignment within table cells
    """

    decorator_name = "table_format"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        columns: List[Any],
        format: Literal["markdown", "ascii", "csv"] = "markdown",
        alignment: Literal["left", "center", "right"] = "left",
    ) -> None:
        """
        Initialize the TableFormat decorator.

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
        if self._columns is None:
            raise ValidationError("The parameter 'columns' is required for TableFormat decorator.")

        if self._columns is not None:
            if not isinstance(self._columns, (list, tuple)):
                raise ValidationError("The parameter 'columns' must be an array.")

        if self._format is not None:
            valid_values = ["markdown", "ascii", "csv"]
            if self._format not in valid_values:
                raise ValidationError("The parameter 'format' must be one of the following values: " + ", ".join(valid_values))

        if self._alignment is not None:
            valid_values = ["left", "center", "right"]
            if self._alignment not in valid_values:
                raise ValidationError("The parameter 'alignment' must be one of the following values: " + ", ".join(valid_values))


    @property
    def columns(self) -> List[Any]:
        """
        Get the columns parameter value.

        Args:
            self: The decorator instance

        Returns:
            The columns parameter value
        """
        return self._columns

    @property
    def format(self) -> Literal["markdown", "ascii", "csv"]:
        """
        Get the format parameter value.

        Args:
            self: The decorator instance

        Returns:
            The format parameter value
        """
        return self._format

    @property
    def alignment(self) -> Literal["left", "center", "right"]:
        """
        Get the alignment parameter value.

        Args:
            self: The decorator instance

        Returns:
            The alignment parameter value
        """
        return self._alignment

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "table_format",
            "columns": self.columns,
            "format": self.format,
            "alignment": self.alignment,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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