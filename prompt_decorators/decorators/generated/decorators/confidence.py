"""
Implementation of the Confidence decorator.

This module provides the Confidence decorator class for use in prompt engineering.

Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Confidence(BaseDecorator):
    """
    Enhances the response with explicit indications of confidence levels
    for different statements or claims. This decorator promotes
    transparency about knowledge certainty and helps differentiate between
    well-established facts and more speculative content.

    Attributes:
        scale: The method used to express confidence levels
        threshold: Minimum confidence level for including information (as a percentage)
        detailed: Whether to provide explanations for confidence assessments
    """

    decorator_name = "confidence"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        scale: Literal["percent", "qualitative", "stars", "numeric"] = "qualitative",
        threshold: Any = 50,
        detailed: bool = False,
    ) -> None:
        """
        Initialize the Confidence decorator.

        Args:
            scale: The method used to express confidence levels
            threshold: Minimum confidence level for including information (as a
                percentage)
            detailed: Whether to provide explanations for confidence assessments

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._scale = scale
        self._threshold = threshold
        self._detailed = detailed

        # Validate parameters
        if self._scale is not None:
            valid_values = ["percent", "qualitative", "stars", "numeric"]
            if self._scale not in valid_values:
                raise ValidationError(
                    "The parameter 'scale' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._threshold is not None:
            if not isinstance(self._threshold, (int, float)) or isinstance(
                self._threshold, bool
            ):
                raise ValidationError(
                    "The parameter 'threshold' must be a numeric value."
                )

        if self._detailed is not None:
            if not isinstance(self._detailed, bool):
                raise ValidationError(
                    "The parameter 'detailed' must be a boolean value."
                )

    @property
    def scale(self) -> Literal["percent", "qualitative", "stars", "numeric"]:
        """
        Get the scale parameter value.

        Args:
            self: The decorator instance

        Returns:
            The scale parameter value
        """
        return self._scale

    @property
    def threshold(self) -> Any:
        """
        Get the threshold parameter value.

        Args:
            self: The decorator instance

        Returns:
            The threshold parameter value
        """
        return self._threshold

    @property
    def detailed(self) -> bool:
        """
        Get the detailed parameter value.

        Args:
            self: The decorator instance

        Returns:
            The detailed parameter value
        """
        return self._detailed

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "confidence",
            "scale": self.scale,
            "threshold": self.threshold,
            "detailed": self.detailed,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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
