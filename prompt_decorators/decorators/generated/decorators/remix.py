"""Implementation of the Remix decorator.

This module provides the Remix decorator class for use in prompt engineering.

Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import RemixPreserveEnum


class Remix(BaseDecorator):
    """Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.

    Attributes:
        target: The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch'). (str)
        preserve: What aspects of the original content to prioritize preserving. (Literal["facts", "structure", "tone", "comprehensiveness"])
        contrast: Whether to highlight differences between the original framing and the remixed version. (bool)
    """

    name = "remix"  # Class-level name for serialization
    decorator_name = "remix"
    version = "1.0.0"  # Initial version

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
        target: str,
        preserve: Literal["facts", "structure", "tone", "comprehensiveness"] = "facts",
        contrast: bool = False,
    ) -> None:
        """Initialize the Remix decorator.

        Args:
            target: The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch')
            preserve: What aspects of the original content to prioritize preserving
            contrast: Whether to highlight differences between the original framing and the remixed version

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._target = target
        self._preserve = preserve
        self._contrast = contrast

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._target = target
        self._preserve = preserve
        self._contrast = contrast

        # Validate parameters
        if self._target is not None:
            if not isinstance(self._target, str):
                raise ValidationError(
                    "The parameter 'target' must be a string type value."
                )
        if self._preserve is not None:
            if not isinstance(self._preserve, str):
                raise ValidationError(
                    "The parameter 'preserve' must be a string type value."
                )
            if self._preserve not in [
                "facts",
                "structure",
                "tone",
                "comprehensiveness",
            ]:
                raise ValidationError(
                    f"The parameter 'preserve' must be one of the allowed enum values: ['facts', 'structure', 'tone', 'comprehensiveness']. Got {self._preserve}"
                )
        if self._contrast is not None:
            if not isinstance(self._contrast, bool):
                raise ValidationError(
                    "The parameter 'contrast' must be a boolean type value."
                )

    @property
    def target(self) -> str:
        """Get the target parameter value.

        Args:
            self: The decorator instance

        Returns:
            The target parameter value
        """
        return self._target

    @property
    def preserve(self) -> Literal["facts", "structure", "tone", "comprehensiveness"]:
        """Get the preserve parameter value.

        Args:
            self: The decorator instance

        Returns:
            The preserve parameter value
        """
        return self._preserve

    @property
    def contrast(self) -> bool:
        """Get the contrast parameter value.

        Args:
            self: The decorator instance

        Returns:
            The contrast parameter value
        """
        return self._contrast

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "remix",
            "parameters": {
                "target": self.target,
                "preserve": self.preserve,
                "contrast": self.contrast,
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
            "description": """Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.""",
            "category": "general",
            "version": cls.version,
        }
