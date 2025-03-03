"""
Implementation of the OutputFormat decorator.

This module provides the OutputFormat decorator class for use in prompt engineering.

Specifies the format of the AI's response. This decorator ensures the output follows a specific format, making it easier to parse, display, or process the response in a consistent way.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class OutputFormat(BaseDecorator):
    """
    Specifies the format of the AI's response. This decorator ensures the
    output follows a specific format, making it easier to parse, display,
    or process the response in a consistent way.

    Attributes:
        format: The format to use for the response
    """

    decorator_name = "output_format"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        format: Literal["json", "markdown", "yaml", "xml", "plaintext"],
    ) -> None:
        """
        Initialize the OutputFormat decorator.

        Args:
            format: The format to use for the response

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._format = format

        # Validate parameters
        if self._format is None:
            raise ValidationError(
                "The parameter 'format' is required for OutputFormat decorator."
            )

        if self._format is not None:
            valid_values = ["json", "markdown", "yaml", "xml", "plaintext"]
            if self._format not in valid_values:
                raise ValidationError(
                    "The parameter 'format' must be one of the following values: "
                    + ", ".join(valid_values)
                )

    @property
    def format(self) -> Literal["json", "markdown", "yaml", "xml", "plaintext"]:
        """
        Get the format parameter value.

        Args:
            self: The decorator instance

        Returns:
            The format parameter value
        """
        return self._format

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "output_format",
            "format": self.format,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.format is not None:
            params.append(f"format={self.format}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
