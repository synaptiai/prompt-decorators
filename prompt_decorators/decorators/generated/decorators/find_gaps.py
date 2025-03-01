"""
FindGaps Decorator

Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import FindGapsAspectsEnum, FindGapsDepthEnum


class FindGaps(BaseDecorator):
    """Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing."""

    def __init__(
        self,
        aspects: Optional[FindGapsAspectsEnum] = FindGapsAspectsEnum.COMPREHENSIVE,
        depth: Optional[FindGapsDepthEnum] = FindGapsDepthEnum.THOROUGH,
        solutions: Optional[bool] = True,
    ):
        """
        Initialize FindGaps decorator.

        Args:
            aspects: The specific types of gaps to focus on finding
            depth: How thoroughly to analyze for gaps
            solutions: Whether to suggest solutions or approaches for addressing the identified gaps
        """
        super().__init__(
            name="FindGaps",
            version="1.0.0",
            parameters={
                "aspects": aspects,
                "depth": depth,
                "solutions": solutions,
            },
            metadata={
                "description": "Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def aspects(self) -> FindGapsAspectsEnum:
        """The specific types of gaps to focus on finding"""
        return self.parameters.get("aspects")

    @property
    def depth(self) -> FindGapsDepthEnum:
        """How thoroughly to analyze for gaps"""
        return self.parameters.get("depth")

    @property
    def solutions(self) -> bool:
        """Whether to suggest solutions or approaches for addressing the identified gaps"""
        return self.parameters.get("solutions")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument
        instruction = f"Instructions for {self.name} decorator: "
        if self.aspects is not None:
            instruction += f"aspects={self.aspects}, "
        if self.depth is not None:
            instruction += f"depth={self.depth}, "
        if self.solutions is not None:
            instruction += f"solutions={self.solutions}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"