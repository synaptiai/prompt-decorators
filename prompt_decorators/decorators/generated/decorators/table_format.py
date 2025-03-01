"""
TableFormat Decorator

Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import TableFormatFormatEnum, TableFormatAlignmentEnum


class TableFormat(BaseDecorator):
    """Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization."""

    def __init__(
        self,
        columns: List[Any],
        format: Optional[TableFormatFormatEnum] = TableFormatFormatEnum.MARKDOWN,
        alignment: Optional[TableFormatAlignmentEnum] = TableFormatAlignmentEnum.LEFT,
    ):
        """
        Initialize TableFormat decorator.

        Args:
            columns: List of column names for the table
            format: Format style for the table representation
            alignment: Text alignment within table cells
        """
        super().__init__(
            name="TableFormat",
            version="1.0.0",
            parameters={
                "columns": columns,
                "format": format,
                "alignment": alignment,
            },
            metadata={
                "description": "Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def columns(self) -> List[Any]:
        """List of column names for the table"""
        return self.parameters.get("columns")

    @property
    def format(self) -> TableFormatFormatEnum:
        """Format style for the table representation"""
        return self.parameters.get("format")

    @property
    def alignment(self) -> TableFormatAlignmentEnum:
        """Text alignment within table cells"""
        return self.parameters.get("alignment")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the AI's response in a tabular format with defined columns
        instruction = f"Instructions for {self.name} decorator: "
        if self.columns is not None:
            instruction += f"columns={self.columns}, "
        if self.format is not None:
            instruction += f"format={self.format}, "
        if self.alignment is not None:
            instruction += f"alignment={self.alignment}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"