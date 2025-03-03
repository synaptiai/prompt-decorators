"""
Implementation of the QualityMetrics decorator.

This module provides the QualityMetrics decorator class for use in prompt engineering.

Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.
"""

from typing import Any, Dict, List, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class QualityMetrics(BaseDecorator):
    """
    Applies specific quality measurements to evaluate content against
    defined criteria. This decorator enhances verification by providing
    quantifiable assessments of aspects like accuracy, completeness,
    clarity, or other custom metrics.

    Attributes:
        metrics: Specific quality metrics to measure (e.g., accuracy, completeness, clarity, usefulness)
        scale: Rating scale to use for evaluations
        explanation: Whether to provide detailed explanations for each metric score
    """

    decorator_name = "quality_metrics"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        metrics: List[Any] = None,
        scale: Literal["1-5", "1-10", "percentage", "qualitative"] = "1-5",
        explanation: bool = True,
    ) -> None:
        """
        Initialize the QualityMetrics decorator.

        Args:
            metrics: Specific quality metrics to measure (e.g., accuracy,
                completeness, clarity, usefulness)
            scale: Rating scale to use for evaluations
            explanation: Whether to provide detailed explanations for each metric
                score

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
        if self._metrics is not None:
            if not isinstance(self._metrics, (list, tuple)):
                raise ValidationError("The parameter 'metrics' must be an array.")

        if self._scale is not None:
            valid_values = ["1-5", "1-10", "percentage", "qualitative"]
            if self._scale not in valid_values:
                raise ValidationError(
                    "The parameter 'scale' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._explanation is not None:
            if not isinstance(self._explanation, bool):
                raise ValidationError(
                    "The parameter 'explanation' must be a boolean value."
                )

    @property
    def metrics(self) -> List[Any]:
        """
        Get the metrics parameter value.

        Args:
            self: The decorator instance

        Returns:
            The metrics parameter value
        """
        return self._metrics

    @property
    def scale(self) -> Literal["1-5", "1-10", "percentage", "qualitative"]:
        """
        Get the scale parameter value.

        Args:
            self: The decorator instance

        Returns:
            The scale parameter value
        """
        return self._scale

    @property
    def explanation(self) -> bool:
        """
        Get the explanation parameter value.

        Args:
            self: The decorator instance

        Returns:
            The explanation parameter value
        """
        return self._explanation

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "quality_metrics",
            "metrics": self.metrics,
            "scale": self.scale,
            "explanation": self.explanation,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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
