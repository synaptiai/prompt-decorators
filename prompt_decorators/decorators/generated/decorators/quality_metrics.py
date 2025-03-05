"""Implementation of the QualityMetrics decorator.

This module provides the QualityMetrics decorator class for use in prompt engineering.

Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    QualityMetricsScaleEnum,
)


class QualityMetrics(BaseDecorator):
    """Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.

    Attributes:
        metrics: Specific quality metrics to measure (e.g., accuracy, completeness, clarity, usefulness). (List[Any])
        scale: Rating scale to use for evaluations. (Literal["1-5", "1-10", "percentage", "qualitative"])
        explanation: Whether to provide detailed explanations for each metric score. (bool)
    """

    name = "quality_metrics"  # Class-level name for serialization
    decorator_name = "quality_metrics"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please include a quality assessment of your response using specific"
        "metrics. After presenting your main content, evaluate it against"
        "defined quality criteria with appropriate ratings and explanations"
        "where needed.",
        "parameterMapping": {
            "metrics": {
                "format": "Evaluate your response against these specific quality metrics: {value}. For each metric, provide a rating and assess how well the content meets that particular quality standard.",
            },
            "scale": {
                "valueMap": {
                    "1-5": "Use a 1-5 scale for your ratings, where 1 represents the lowest quality and 5 represents the highest quality.",
                    "1-10": "Use a 1-10 scale for your ratings, where 1 represents the lowest quality and 10 represents the highest quality.",
                    "percentage": "Express your ratings as percentages, ranging from 0% (lowest quality) to 100% (highest quality).",
                    "qualitative": "Use qualitative ratings (poor, fair, good, excellent) rather than numerical scores.",
                },
            },
            "explanation": {
                "valueMap": {
                    "true": "For each metric, provide a detailed explanation that justifies the rating, citing specific aspects of the content.",
                    "false": "Provide ratings for each metric without detailed explanations.",
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
        metrics: List[Any] = None,
        scale: Literal["1-5", "1-10", "percentage", "qualitative"] = "1-5",
        explanation: bool = True,
    ) -> None:
        """Initialize the QualityMetrics decorator.

        Args:
            metrics: Specific quality metrics to measure (e.g., accuracy, completeness, clarity, usefulness)
            scale: Rating scale to use for evaluations
            explanation: Whether to provide detailed explanations for each metric score


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._metrics = metrics
        self._scale = scale
        self._explanation = explanation

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._metrics = metrics
        self._scale = scale
        self._explanation = explanation

        # Validate parameters
        if self._metrics is not None:
            if not isinstance(self._metrics, list):
                raise ValidationError(
                    "The parameter 'metrics' must be an array type value."
                )
        if self._scale is not None:
            if not isinstance(self._scale, str):
                raise ValidationError(
                    "The parameter 'scale' must be a string type value."
                )
            if self._scale not in ["1-5", "1-10", "percentage", "qualitative"]:
                raise ValidationError(
                    f"The parameter 'scale' must be one of the allowed enum values: ['1-5', '1-10', 'percentage', 'qualitative']. Got {self._scale}"
                )
        if self._explanation is not None:
            if not isinstance(self._explanation, bool):
                raise ValidationError(
                    "The parameter 'explanation' must be a boolean type value."
                )

    @property
    def metrics(self) -> List[Any]:
        """Get the metrics parameter value.

        Args:
            self: The decorator instance

        Returns:
            The metrics parameter value
        """
        return self._metrics

    @property
    def scale(self) -> Literal["1-5", "1-10", "percentage", "qualitative"]:
        """Get the scale parameter value.

        Args:
            self: The decorator instance

        Returns:
            The scale parameter value
        """
        return self._scale

    @property
    def explanation(self) -> bool:
        """Get the explanation parameter value.

        Args:
            self: The decorator instance

        Returns:
            The explanation parameter value
        """
        return self._explanation

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "quality_metrics",
            "parameters": {
                "metrics": self.metrics,
                "scale": self.scale,
                "explanation": self.explanation,
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
        if self.metrics is not None:
            params.append(f"metrics={self.metrics}")
        if self.scale is not None:
            params.append(f"scale={self.scale}")
        if self.explanation is not None:
            params.append(f"explanation={self.explanation}")

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
            "description": """Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.""",
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
