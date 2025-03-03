"""
Implementation of the Remix decorator.

This module provides the Remix decorator class for use in prompt engineering.

Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Remix(BaseDecorator):
    """
    Reframes or adapts content for a different context, purpose, or
    audience than originally intended. This decorator transforms the
    presentation style while preserving core information, making it
    accessible and relevant to specific scenarios or demographics.

    Attributes:
        target: The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch')
        preserve: What aspects of the original content to prioritize preserving
        contrast: Whether to highlight differences between the original framing and the remixed version
    """

    decorator_name = "remix"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        target: str,
        preserve: Literal["facts", "structure", "tone", "comprehensiveness"] = "facts",
        contrast: bool = False,
    ) -> None:
        """
        Initialize the Remix decorator.

        Args:
            target: The specific audience or context to adapt the content for
                (e.g., 'executives', 'teenagers', 'technical team', 'sales
                pitch')
            preserve: What aspects of the original content to prioritize
                preserving
            contrast: Whether to highlight differences between the original
                framing and the remixed version

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._target = target
        self._preserve = preserve
        self._contrast = contrast

        # Validate parameters
        if self._target is None:
            raise ValidationError(
                "The parameter 'target' is required for Remix decorator."
            )

        if self._target is not None:
            if not isinstance(self._target, str):
                raise ValidationError("The parameter 'target' must be a string value.")

        if self._preserve is not None:
            valid_values = ["facts", "structure", "tone", "comprehensiveness"]
            if self._preserve not in valid_values:
                raise ValidationError(
                    "The parameter 'preserve' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._contrast is not None:
            if not isinstance(self._contrast, bool):
                raise ValidationError(
                    "The parameter 'contrast' must be a boolean value."
                )

    @property
    def target(self) -> str:
        """
        Get the target parameter value.

        Args:
            self: The decorator instance

        Returns:
            The target parameter value
        """
        return self._target

    @property
    def preserve(self) -> Literal["facts", "structure", "tone", "comprehensiveness"]:
        """
        Get the preserve parameter value.

        Args:
            self: The decorator instance

        Returns:
            The preserve parameter value
        """
        return self._preserve

    @property
    def contrast(self) -> bool:
        """
        Get the contrast parameter value.

        Args:
            self: The decorator instance

        Returns:
            The contrast parameter value
        """
        return self._contrast

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "remix",
            "target": self.target,
            "preserve": self.preserve,
            "contrast": self.contrast,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.target is not None:
            params.append(f"target={self.target}")
        if self.preserve is not None:
            params.append(f"preserve={self.preserve}")
        if self.contrast is not None:
            params.append(f"contrast={self.contrast}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"
