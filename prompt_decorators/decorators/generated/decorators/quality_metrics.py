"""
QualityMetrics Decorator

Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import QualityMetricsScaleEnum


class QualityMetrics(BaseDecorator):
    """Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics."""

    def __init__(
        self,
        metrics: Optional[List[Any]] = None,
        scale: Optional[QualityMetricsScaleEnum] = QualityMetricsScaleEnum.VALUE_1_5,
        explanation: Optional[bool] = True,
    ):
        """
        Initialize QualityMetrics decorator.

        Args:
            metrics: Specific quality metrics to measure (e.g., accuracy, completeness, clarity, usefulness)
            scale: Rating scale to use for evaluations
            explanation: Whether to provide detailed explanations for each metric score
        """
        super().__init__(
            name="QualityMetrics",
            version="1.0.0",
            parameters={
                "metrics": metrics,
                "scale": scale,
                "explanation": explanation,
            },
            metadata={
                "description": "Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def metrics(self) -> List[Any]:
        """Specific quality metrics to measure (e.g., accuracy, completeness, clarity, usefulness)"""
        return self.parameters.get("metrics")

    @property
    def scale(self) -> QualityMetricsScaleEnum:
        """Rating scale to use for evaluations"""
        return self.parameters.get("scale")

    @property
    def explanation(self) -> bool:
        """Whether to provide detailed explanations for each metric score"""
        return self.parameters.get("explanation")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Applies specific quality measurements to evaluate content against defined criteria
        instruction = f"Instructions for {self.name} decorator: "
        if self.metrics is not None:
            instruction += f"metrics={self.metrics}, "
        if self.scale is not None:
            instruction += f"scale={self.scale}, "
        if self.explanation is not None:
            instruction += f"explanation={self.explanation}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"