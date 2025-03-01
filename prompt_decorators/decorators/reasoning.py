"""
Reasoning Decorator

This decorator instructs the model to explicitly reason through a problem step by step.
"""

from enum import Enum
from typing import Dict, Any, Optional

from ..core.base import BaseDecorator, ValidationError


class ReasoningStyle(Enum):
    """Enumeration of reasoning styles."""
    STANDARD = "standard"
    DETAILED = "detailed"
    CONCISE = "concise"
    SOCRATIC = "socratic"
    

class Reasoning(BaseDecorator):
    """
    Decorator that instructs the model to use explicit reasoning.
    
    This decorator enhances responses by prompting the model to:
    1. Break down complex problems into steps
    2. Show its thought process explicitly
    3. Consider multiple perspectives where relevant
    """
    
    name = "Reasoning"
    description = "Instructs the model to reason step by step through problems"
    category = "ThoughtProcess"
    version = "1.0.0"
    min_compatible_version = "1.0.0"
    
    def __init__(
        self,
        style: str = ReasoningStyle.STANDARD.value,
        show_working: bool = True,
        consider_alternatives: bool = False,
        depth: int = 3,
        name: Optional[str] = None,
        version: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize a Reasoning decorator.
        
        Args:
            style: Reasoning style to use (standard, detailed, concise, socratic)
            show_working: Whether to show intermediate steps
            consider_alternatives: Whether to consider alternative approaches
            depth: Depth of reasoning (1-5)
            name: Optional decorator name override
            version: Optional version override
            parameters: Optional parameter dictionary (overrides individual parameters)
            metadata: Optional metadata dictionary
        """
        # If parameters are explicitly provided, use them instead of individual args
        if parameters is None:
            parameters = {
                "style": style,
                "show_working": show_working,
                "consider_alternatives": consider_alternatives,
                "depth": depth
            }
        
        super().__init__(name, version, parameters, metadata)
    
    def validate(self) -> None:
        """
        Validate decorator parameters.
        
        Raises:
            ValidationError: If any parameter fails validation
        """
        # Validate style parameter
        self._validate_enum("style", ReasoningStyle)
        
        # Validate boolean parameters
        self._validate_type("show_working", bool)
        self._validate_type("consider_alternatives", bool)
        
        # Validate depth parameter
        self._validate_range("depth", minimum=1, maximum=5)
    
    def apply(self, prompt: str) -> str:
        """
        Apply the reasoning decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with reasoning instructions
        """
        style = self._validate_enum("style", ReasoningStyle)
        show_working = self._validate_type("show_working", bool)
        consider_alternatives = self._validate_type("consider_alternatives", bool)
        depth = self._validate_range("depth", minimum=1, maximum=5)
        
        # Build style-specific instructions
        style_instructions = {
            ReasoningStyle.STANDARD: "Think through this step by step.",
            ReasoningStyle.DETAILED: "Provide a detailed analysis with thorough reasoning.",
            ReasoningStyle.CONCISE: "Reason efficiently, focusing only on key points.",
            ReasoningStyle.SOCRATIC: "Use Socratic questioning to explore the problem."
        }
        
        instruction = style_instructions.get(style, style_instructions[ReasoningStyle.STANDARD])
        
        # Add additional instructions based on parameters
        if show_working:
            instruction += " Show your work and thought process."
        
        if consider_alternatives:
            instruction += " Consider multiple approaches or perspectives."
        
        # Adjust depth of reasoning
        depth_instructions = {
            1: "Focus on the most essential reasoning only.",
            2: "Include key reasoning steps.",
            3: "Provide a balanced level of detail in your reasoning.",
            4: "Explore the reasoning in good detail.",
            5: "Provide highly detailed, comprehensive reasoning."
        }
        
        instruction += f" {depth_instructions.get(depth, '')}"
        
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}" 