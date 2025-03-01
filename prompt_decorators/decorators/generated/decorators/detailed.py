"""
Detailed Decorator

This module defines the Detailed decorator which enhances responses with comprehensive information.
"""

from enum import Enum
from typing import List, Optional, Dict, Any

from prompt_decorators.core.base import BaseDecorator

class DetailedDepthEnum(Enum):
    """Enumeration of detail levels for the Detailed decorator."""
    MODERATE = "moderate"
    COMPREHENSIVE = "comprehensive" 
    EXHAUSTIVE = "exhaustive"

class Detailed(BaseDecorator):
    """
    Enhances the response with comprehensive information, thorough explanations, and rich context.
    
    This decorator is ideal for in-depth learning, complex topics requiring nuance, 
    or when completeness is valued over brevity.
    """
    
    name = "Detailed"
    version = "1.0.0"
    category = "tone"
    
    def __init__(
        self,
        depth: str = "comprehensive",
        aspects: Optional[List[str]] = None,
        examples: bool = True
    ):
        """
        Initialize the Detailed decorator.
        
        Args:
            depth: The level of detail and comprehensiveness (moderate, comprehensive, exhaustive)
            aspects: Specific aspects or dimensions to explore in detail
            examples: Whether to include detailed examples to illustrate points
        """
        super().__init__()
        self.depth = depth
        self.aspects = aspects or []
        self.examples = examples
        
    def apply(self, prompt: str) -> str:
        """
        Apply the Detailed decorator to a prompt.
        
        Args:
            prompt: The original prompt to decorate
            
        Returns:
            The decorated prompt
        """
        # Build the decoration
        decoration = "Please provide a detailed response with thorough explanations and rich context. "
        
        # Add depth-specific instructions
        if self.depth == DetailedDepthEnum.MODERATE.value:
            decoration += "Include moderate detail, covering the main points thoroughly. "
        elif self.depth == DetailedDepthEnum.COMPREHENSIVE.value:
            decoration += "Be comprehensive, exploring multiple dimensions and providing complete explanations. "
        elif self.depth == DetailedDepthEnum.EXHAUSTIVE.value:
            decoration += "Be exhaustive, leaving no relevant detail unexplored and covering all possible aspects. "
        
        # Add aspect-specific instructions
        if self.aspects:
            aspects_str = ", ".join(self.aspects)
            decoration += f"Focus on these specific aspects in detail: {aspects_str}. "
        
        # Add example-specific instructions
        if self.examples:
            decoration += "Include detailed examples to illustrate your points. "
            
        # Return the decorated prompt
        return f"{decoration}\n\n{prompt}"
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.
        
        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": self.name,
            "version": self.version,
            "parameters": {
                "depth": self.depth,
                "aspects": self.aspects,
                "examples": self.examples
            }
        }