"""
Implementation of the Summary decorator.

This module provides the Summary decorator class for use in prompt engineering.

Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Summary(BaseDecorator):
    """
    Provides a condensed summary of information that would otherwise be
    presented in a more detailed format. This decorator is useful for
    generating executive summaries, article summaries, or concise
    overviews of complex topics.

    Attributes:
        length: Relative length of the summary
        wordCount: Approximate target word count for the summary
        position: Where to position the summary in relation to any full content
    """

    decorator_name = "summary"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        length: Literal["short", "medium", "long"] = "medium",
        wordCount: Any = None,
        position: Literal["beginning", "end", "standalone"] = "standalone",
    ) -> None:
        """
        Initialize the Summary decorator.

        Args:
            length: Relative length of the summary
            wordCount: Approximate target word count for the summary
            position: Where to position the summary in relation to any full
                content

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._length = length
        self._wordCount = wordCount
        self._position = position

        # Validate parameters
        if self._length is not None:
            valid_values = ["short", "medium", "long"]
            if self._length not in valid_values:
                raise ValidationError(
                    "The parameter 'length' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._wordCount is not None:
            if not isinstance(self._wordCount, (int, float)) or isinstance(
                self._wordCount, bool
            ):
                raise ValidationError(
                    "The parameter 'wordCount' must be a numeric value."
                )

        if self._position is not None:
            valid_values = ["beginning", "end", "standalone"]
            if self._position not in valid_values:
                raise ValidationError(
                    "The parameter 'position' must be one of the following values: "
                    + ", ".join(valid_values)
                )

    @property
    def length(self) -> Literal["short", "medium", "long"]:
        """
        Get the length parameter value.

        Args:
            self: The decorator instance

        Returns:
            The length parameter value
        """
        return self._length

    @property
    def wordCount(self) -> Any:
        """
        Get the wordCount parameter value.

        Args:
            self: The decorator instance

        Returns:
            The wordCount parameter value
        """
        return self._wordCount

    @property
    def position(self) -> Literal["beginning", "end", "standalone"]:
        """
        Get the position parameter value.

        Args:
            self: The decorator instance

        Returns:
            The position parameter value
        """
        return self._position

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "summary",
            "length": self.length,
            "wordCount": self.wordCount,
            "position": self.position,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.length is not None:
            params.append(f"length={self.length}")
        if self.wordCount is not None:
            params.append(f"wordCount={self.wordCount}")
        if self.position is not None:
            params.append(f"position={self.position}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
