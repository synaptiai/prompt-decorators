#!/usr/bin/env python
"""
Decorator Basics Example

This script demonstrates the basic usage of prompt decorators in the framework.
It shows how to create, initialize, and apply decorators to prompts.
"""

import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from prompt_decorators.core import BaseDecorator
from typing import Optional, Dict, Any, List


class SimpleDecorator(BaseDecorator):
    """
    A simple example decorator that demonstrates basic functionality.
    
    This decorator adds instructions to the beginning of a prompt based on
    the provided parameters. It serves as a minimal example of how to create
    a custom decorator.
    """
    
    name = "Simple"
    version = "1.0.0"
    category = "example"
    
    def __init__(self, prefix: str = "Please note:", emphasis: int = 1):
        """
        Initialize the simple decorator.
        
        Args:
            prefix: Text to prefix the instruction with
            emphasis: Level of emphasis (1-3), affects formatting
        """
        super().__init__()
        self.prefix = prefix
        self.emphasis = max(1, min(3, emphasis))  # Clamp between 1-3
    
    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        This method adds the instruction with appropriate emphasis to the beginning
        of the provided prompt.
        
        Args:
            prompt: The prompt to decorate
            
        Returns:
            The decorated prompt with added instructions
        """
        # Create the instruction with the specified emphasis
        if self.emphasis == 1:
            instruction = f"{self.prefix} The following is important."
        elif self.emphasis == 2:
            instruction = f"{self.prefix} The following is very important!"
        else:  # emphasis == 3
            instruction = f"{self.prefix} THE FOLLOWING IS EXTREMELY IMPORTANT!!!"
        
        # Return the decorated prompt
        return f"{instruction}\n\n{prompt}"


class FormattingDecorator(BaseDecorator):
    """
    A decorator that formats the response in a specific way.
    
    This decorator adds instructions for formatting the response according 
    to the specified parameters, such as bullet points, numbered lists, etc.
    """
    
    name = "Formatting"
    version = "1.0.0"
    category = "format"
    
    def __init__(
        self, 
        format_type: str = "bullet", 
        max_points: Optional[int] = None,
        include_summary: bool = False
    ):
        """
        Initialize the formatting decorator.
        
        Args:
            format_type: Type of formatting (bullet, numbered, paragraphs)
            max_points: Maximum number of points to include (optional)
            include_summary: Whether to include a summary at the end
        """
        super().__init__()
        self.format_type = format_type
        self.max_points = max_points
        self.include_summary = include_summary
    
    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        This method adds formatting instructions to the prompt based on the
        specified parameters.
        
        Args:
            prompt: The prompt to decorate
            
        Returns:
            The decorated prompt with formatting instructions
        """
        # Create the formatting instruction
        if self.format_type == "bullet":
            format_instruction = "Please provide your answer as a bullet point list."
        elif self.format_type == "numbered":
            format_instruction = "Please provide your answer as a numbered list."
        elif self.format_type == "paragraphs":
            format_instruction = "Please structure your answer in clear paragraphs."
        else:
            format_instruction = f"Please format your answer as {self.format_type}."
        
        # Add max points constraint if specified
        if self.max_points:
            format_instruction += f" Include at most {self.max_points} points."
        
        # Add summary instruction if requested
        if self.include_summary:
            format_instruction += " End with a brief summary of the key points."
        
        # Return the decorated prompt
        return f"{format_instruction}\n\n{prompt}"


def main():
    """
    Demonstrate the usage of basic decorators.
    
    This function shows how to create decorator instances with different
    parameters and apply them to prompts.
    """
    print("=== Decorator Basics Example ===\n")
    
    # Create a sample prompt
    prompt = "Explain the concept of quantum entanglement."
    print(f"Original prompt: \"{prompt}\"\n")
    
    # Example 1: Simple decorator with default parameters
    simple = SimpleDecorator()
    decorated_prompt = simple.apply(prompt)
    print("Example 1: Simple decorator with default parameters")
    print(f"Decorated prompt: \"{decorated_prompt}\"\n")
    
    # Example 2: Simple decorator with custom parameters
    simple_custom = SimpleDecorator(prefix="Warning:", emphasis=3)
    decorated_prompt = simple_custom.apply(prompt)
    print("Example 2: Simple decorator with custom parameters")
    print(f"Decorated prompt: \"{decorated_prompt}\"\n")
    
    # Example 3: Formatting decorator for bullet points
    formatting = FormattingDecorator(format_type="bullet", max_points=5)
    decorated_prompt = formatting.apply(prompt)
    print("Example 3: Formatting decorator for bullet points")
    print(f"Decorated prompt: \"{decorated_prompt}\"\n")
    
    # Example 4: Formatting decorator for numbered list with summary
    formatting_summary = FormattingDecorator(
        format_type="numbered", 
        max_points=3,
        include_summary=True
    )
    decorated_prompt = formatting_summary.apply(prompt)
    print("Example 4: Formatting decorator for numbered list with summary")
    print(f"Decorated prompt: \"{decorated_prompt}\"\n")
    
    # Example 5: Combining decorators
    decorated_prompt = formatting.apply(simple.apply(prompt))
    print("Example 5: Combining decorators (Simple + Formatting)")
    print(f"Decorated prompt: \"{decorated_prompt}\"\n")


if __name__ == "__main__":
    main() 