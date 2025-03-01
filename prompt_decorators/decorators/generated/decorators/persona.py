"""
Persona Decorator

Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Persona(BaseDecorator):
    """Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic."""

    def __init__(
        self,
        role: str,
        traits: Optional[List[Any]] = None,
        goals: Optional[List[Any]] = None,
    ):
        """
        Initialize Persona decorator.

        Args:
            role: The specific persona or stakeholder role to adopt
            traits: Key personality traits or characteristics of the persona
            goals: Primary goals or concerns of the persona
        """
        super().__init__(
            name="Persona",
            version="1.0.0",
            parameters={
                "role": role,
                "traits": traits,
                "goals": goals,
            },
            metadata={
                "description": "Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic.",
                "author": "Prompt Decorators Working Group",
                "category": "tone",
            },
        )

    @property
    def role(self) -> str:
        """The specific persona or stakeholder role to adopt"""
        return self.parameters.get("role")

    @property
    def traits(self) -> List[Any]:
        """Key personality traits or characteristics of the persona"""
        return self.parameters.get("traits")

    @property
    def goals(self) -> List[Any]:
        """Primary goals or concerns of the persona"""
        return self.parameters.get("goals")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Adapts the response to reflect the perspective and concerns of a specific persona
        instruction = f"Instructions for {self.name} decorator: "
        if self.role is not None:
            instruction += f"role={self.role}, "
        if self.traits is not None:
            instruction += f"traits={self.traits}, "
        if self.goals is not None:
            instruction += f"goals={self.goals}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"