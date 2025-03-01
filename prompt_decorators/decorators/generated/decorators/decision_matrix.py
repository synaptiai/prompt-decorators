"""
DecisionMatrix Decorator

Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import DecisionMatrixScaleEnum


class DecisionMatrix(BaseDecorator):
    """Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria."""

    def __init__(
        self,
        options: Optional[List[Any]] = None,
        criteria: Optional[List[Any]] = None,
        weighted: Optional[bool] = False,
        scale: Optional[DecisionMatrixScaleEnum] = DecisionMatrixScaleEnum.VALUE_1_5,
    ):
        """
        Initialize DecisionMatrix decorator.

        Args:
            options: Specific options or alternatives to evaluate in the matrix
            criteria: Evaluation criteria to assess each option against
            weighted: Whether to include weights for criteria importance
            scale: Rating scale to use for evaluations
        """
        super().__init__(
            name="DecisionMatrix",
            version="1.0.0",
            parameters={
                "options": options,
                "criteria": criteria,
                "weighted": weighted,
                "scale": scale,
            },
            metadata={
                "description": "Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.",
                "author": "Prompt Decorators Working Group",
                "category": "structure",
            },
        )

    @property
    def options(self) -> List[Any]:
        """Specific options or alternatives to evaluate in the matrix"""
        return self.parameters.get("options")

    @property
    def criteria(self) -> List[Any]:
        """Evaluation criteria to assess each option against"""
        return self.parameters.get("criteria")

    @property
    def weighted(self) -> bool:
        """Whether to include weights for criteria importance"""
        return self.parameters.get("weighted")

    @property
    def scale(self) -> DecisionMatrixScaleEnum:
        """Rating scale to use for evaluations"""
        return self.parameters.get("scale")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Structures the response as a decision matrix, evaluating options against multiple criteria
        instruction = f"Instructions for {self.name} decorator: "
        if self.options is not None:
            instruction += f"options={self.options}, "
        if self.criteria is not None:
            instruction += f"criteria={self.criteria}, "
        if self.weighted is not None:
            instruction += f"weighted={self.weighted}, "
        if self.scale is not None:
            instruction += f"scale={self.scale}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"