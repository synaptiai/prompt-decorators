"""Implementation of the Confidence decorator.

This module provides the Confidence decorator class for use in prompt engineering.

Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import ConfidenceScaleEnum


class Confidence(BaseDecorator):
    """Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.

    Attributes:
        scale: The method used to express confidence levels. (Literal["percent", "qualitative", "stars", "numeric"])
        threshold: Minimum confidence level for including information (as a percentage). (Any)
        detailed: Whether to provide explanations for confidence assessments. (bool)
    """

    name = "confidence"  # Class-level name for serialization
    decorator_name = "confidence"
    version = "1.0.0"  # Initial version

    @property
    def name(self) -> str:
        """Get the name of the decorator.

        Returns:
            The name of the decorator

        """
        return self.decorator_name

    def __init__(
        self,
        scale: Literal["percent", "qualitative", "stars", "numeric"] = "qualitative",
        threshold: Any = 50,
        detailed: bool = False,
    ) -> None:
        """Initialize the Confidence decorator.

        Args:
            scale: The method used to express confidence levels
            threshold: Minimum confidence level for including information (as a percentage)
            detailed: Whether to provide explanations for confidence assessments

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._scale = scale
        self._threshold = threshold
        self._detailed = detailed

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._scale = scale
        self._threshold = threshold
        self._detailed = detailed

        # Validate parameters
        if self._scale is not None:
            if not isinstance(self._scale, str):
                raise ValidationError(
                    "The parameter 'scale' must be a string type value."
                )
            if self._scale not in ["percent", "qualitative", "stars", "numeric"]:
                raise ValidationError(
                    f"The parameter 'scale' must be one of the allowed enum values: ['percent', 'qualitative', 'stars', 'numeric']. Got {self._scale}"
                )
        if self._threshold is not None:
            if not isinstance(self._threshold, (int, float)):
                raise ValidationError(
                    "The parameter 'threshold' must be a numeric type value."
                )
            if self._threshold < 0:
                raise ValidationError(
                    "The parameter 'threshold' must be greater than or equal to 0."
                )
            if self._threshold > 100:
                raise ValidationError(
                    "The parameter 'threshold' must be less than or equal to 100."
                )
        if self._detailed is not None:
            if not isinstance(self._detailed, bool):
                raise ValidationError(
                    "The parameter 'detailed' must be a boolean type value."
                )

    @property
    def scale(self) -> Literal["percent", "qualitative", "stars", "numeric"]:
        """Get the scale parameter value.

        Args:
            self: The decorator instance

        Returns:
            The scale parameter value
        """
        return self._scale

    @property
    def threshold(self) -> Any:
        """Get the threshold parameter value.

        Args:
            self: The decorator instance

        Returns:
            The threshold parameter value
        """
        return self._threshold

    @property
    def detailed(self) -> bool:
        """Get the detailed parameter value.

        Args:
            self: The decorator instance

        Returns:
            The detailed parameter value
        """
        return self._detailed

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "confidence",
            "parameters": {
                "scale": self.scale,
                "threshold": self.threshold,
                "detailed": self.detailed,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.scale is not None:
            params.append(f"scale={self.scale}")
        if self.threshold is not None:
            params.append(f"threshold={self.threshold}")
        if self.detailed is not None:
            params.append(f"detailed={self.detailed}")

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

        """
        return {
            "name": cls.__name__,
            "description": """Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.""",
            "category": "general",
            "version": cls.version,
        }
