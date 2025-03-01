#!/usr/bin/env python
"""
Registry Usage Example

This script demonstrates how to use the decorator registry to find, create,
and manage decorators in the framework.
"""

import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from prompt_decorators.utils import get_registry
from prompt_decorators.core import BaseDecorator
from typing import Optional, Dict, Any, List


class ConciseDecorator(BaseDecorator):
    """
    A decorator that requests concise responses.
    
    This decorator adds instructions for the model to provide a concise response,
    optionally with a maximum word count or using bullet points.
    """
    
    name = "Concise"
    version = "1.0.0"
    category = "style"
    
    def __init__(
        self, 
        max_words: Optional[int] = None, 
        bullet_points: bool = False,
        level: int = 1
    ):
        """
        Initialize the concise decorator.
        
        Args:
            max_words: Maximum number of words for the response (optional)
            bullet_points: Whether to format as bullet points
            level: Conciseness level (1-3), higher means more concise
        """
        super().__init__()
        self.max_words = max_words
        self.bullet_points = bullet_points
        self.level = max(1, min(3, level))  # Clamp between 1-3
    
    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        This method adds instructions for conciseness to the prompt.
        
        Args:
            prompt: The prompt to decorate
            
        Returns:
            The decorated prompt with conciseness instructions
        """
        # Create the conciseness instruction based on level
        if self.level == 1:
            instruction = "Please provide a concise response."
        elif self.level == 2:
            instruction = "Please provide a very concise response, focusing only on the most important points."
        else:  # level == 3
            instruction = "Please provide an extremely concise response with only the essential information."
        
        # Add word count limit if specified
        if self.max_words:
            instruction += f" Limit your response to {self.max_words} words or fewer."
        
        # Add bullet point formatting if requested
        if self.bullet_points:
            instruction += " Format your response as bullet points."
        
        # Return the decorated prompt
        return f"{instruction}\n\n{prompt}"


class TechnicalDecorator(BaseDecorator):
    """
    A decorator that requests technical responses.
    
    This decorator adds instructions for the model to provide a technical response,
    optionally focusing on a specific domain or expertise level.
    """
    
    name = "Technical"
    version = "1.0.0"
    category = "style"
    
    def __init__(
        self, 
        domain: Optional[str] = None, 
        expertise_level: str = "expert",
        include_jargon: bool = True
    ):
        """
        Initialize the technical decorator.
        
        Args:
            domain: Specific technical domain (e.g., "computing", "medicine")
            expertise_level: Level of expertise (beginner, intermediate, expert)
            include_jargon: Whether to include technical jargon
        """
        super().__init__()
        self.domain = domain
        self.expertise_level = expertise_level
        self.include_jargon = include_jargon
    
    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        This method adds instructions for technical responses to the prompt.
        
        Args:
            prompt: The prompt to decorate
            
        Returns:
            The decorated prompt with technical instructions
        """
        # Create the technical instruction
        instruction = f"Please provide a technical response at an {self.expertise_level} level."
        
        # Add domain if specified
        if self.domain:
            instruction += f" Focus on the {self.domain} domain."
        
        # Add jargon instruction
        if self.include_jargon:
            instruction += " Feel free to use appropriate technical terminology and jargon."
        else:
            instruction += " Avoid technical jargon and explain concepts simply."
        
        # Return the decorated prompt
        return f"{instruction}\n\n{prompt}"


def demonstrate_registry_basics():
    """Demonstrate basic registry operations."""
    print("\n=== Registry Basics ===")
    
    # Get the registry
    registry = get_registry()
    
    # Register our decorators
    registry.register_decorator(ConciseDecorator)
    registry.register_decorator(TechnicalDecorator)
    
    # Get all registered decorators
    all_decorators = registry.get_all_decorators()
    print(f"Registered decorators: {len(all_decorators)}")
    for name, decorator_class in all_decorators.items():
        print(f"  - {name} (v{decorator_class.version}, category: {decorator_class.category})")


def demonstrate_finding_decorators():
    """Demonstrate finding decorators in the registry."""
    print("\n=== Finding Decorators ===")
    
    # Get the registry
    registry = get_registry()
    
    # Find a specific decorator
    concise_class = registry.get_decorator("Concise")
    if concise_class:
        print(f"Found Concise decorator: {concise_class.__name__} (v{concise_class.version})")
    else:
        print("Concise decorator not found.")
    
    # Find decorators by category
    style_decorators = registry.find_decorators_by_category("style")
    print(f"Style decorators: {len(style_decorators)}")
    for name in style_decorators:
        print(f"  - {name}")
    
    # Get all categories
    categories = registry.get_categories()
    print(f"Available categories: {', '.join(categories)}")


def demonstrate_creating_decorators():
    """Demonstrate creating decorator instances from the registry."""
    print("\n=== Creating Decorators ===")
    
    # Get the registry
    registry = get_registry()
    
    # Create a sample prompt
    prompt = "Explain the concept of neural networks."
    print(f"Original prompt: \"{prompt}\"\n")
    
    # Create a concise decorator instance
    concise = registry.create_decorator(
        "Concise", 
        max_words=100, 
        bullet_points=True,
        level=2
    )
    
    if concise:
        # Apply the decorator
        decorated_prompt = concise.apply(prompt)
        print("Decorated with Concise:")
        print(f"  \"{decorated_prompt}\"\n")
    
    # Create a technical decorator instance
    technical = registry.create_decorator(
        "Technical", 
        domain="computing", 
        expertise_level="intermediate",
        include_jargon=False
    )
    
    if technical:
        # Apply the decorator
        decorated_prompt = technical.apply(prompt)
        print("Decorated with Technical:")
        print(f"  \"{decorated_prompt}\"\n")
    
    # Combine decorators
    if concise and technical:
        # Apply both decorators
        decorated_prompt = concise.apply(technical.apply(prompt))
        print("Decorated with Technical + Concise:")
        print(f"  \"{decorated_prompt}\"")


def main():
    """Main function to demonstrate decorator registry usage."""
    print("=== Decorator Registry Example ===")
    
    # Demonstrate basic registry operations
    demonstrate_registry_basics()
    
    # Demonstrate finding decorators
    demonstrate_finding_decorators()
    
    # Demonstrate creating decorators
    demonstrate_creating_decorators()


if __name__ == "__main__":
    main() 