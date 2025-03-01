#!/usr/bin/env python
"""
Model-Specific Decorator Example

This script demonstrates how to create and use model-specific decorators.
"""

import os
import sys
import json
from pathlib import Path
import argparse

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from prompt_decorators.core import BaseDecorator, ModelSpecificDecorator, ModelSpecificDecoratorFactory
from prompt_decorators.utils import get_model_detector
from prompt_decorators.utils.discovery import get_registry


class ReasoningDecorator(BaseDecorator):
    """
    Reasoning decorator for demonstration purposes.
    
    This decorator adds instructions for using reasoning in responses.
    """
    
    name = "Reasoning"
    version = "1.0.0"
    category = "reasoning"
    
    def __init__(self, depth: str = "moderate", show_steps: bool = True):
        """
        Initialize the reasoning decorator.
        
        Args:
            depth: Depth of reasoning (basic, moderate, comprehensive)
            show_steps: Whether to show reasoning steps
        """
        super().__init__()
        self.depth = depth
        self.show_steps = show_steps
    
    def apply(self, prompt: str) -> str:
        """
        Apply the reasoning decorator to a prompt.
        
        Args:
            prompt: The original prompt to decorate
            
        Returns:
            The decorated prompt
        """
        # Build the reasoning instruction
        instruction = "Please use explicit reasoning in your response. "
        
        if self.depth == "basic":
            instruction += "Provide basic reasoning steps. "
        elif self.depth == "moderate":
            instruction += "Provide moderately detailed reasoning steps. "
        elif self.depth == "comprehensive":
            instruction += "Provide comprehensive and detailed reasoning steps. "
        
        if self.show_steps:
            instruction += "Show your reasoning step by step. "
        else:
            instruction += "Summarize your reasoning process. "
        
        # Combine with the original prompt
        return f"{instruction}\n\n{prompt}"


class ModelSpecificReasoningDecorator(ModelSpecificDecorator):
    """
    Model-specific reasoning decorator.
    
    This decorator adapts the reasoning instructions based on the model's capabilities.
    """
    
    name = "Reasoning"
    version = "1.0.0"
    category = "reasoning"
    
    def __init__(
        self, 
        model_id: str, 
        depth: str = "moderate", 
        show_steps: bool = True
    ):
        """
        Initialize the model-specific reasoning decorator.
        
        Args:
            model_id: ID of the model to adapt for
            depth: Depth of reasoning (basic, moderate, comprehensive)
            show_steps: Whether to show reasoning steps
        """
        super().__init__(model_id=model_id)
        self.depth = depth
        self.show_steps = show_steps
    
    def apply_for_model(self, prompt: str) -> str:
        """
        Apply the reasoning decorator with model-specific adaptations.
        
        Args:
            prompt: The original prompt to decorate
            
        Returns:
            The decorated prompt
        """
        # Get model capabilities
        if not self.model_capabilities:
            # If no model capabilities, use default behavior
            return self._default_reasoning(prompt)
        
        # Check model capabilities and adapt instructions
        if self.model_capabilities.supports_feature("multi_tool_use"):
            # Advanced reasoning for capable models
            return self._advanced_reasoning(prompt)
        elif self.model_capabilities.supports_feature("reasoning"):
            # Standard reasoning for models with basic reasoning support
            return self._standard_reasoning(prompt)
        else:
            # Simple instructions for limited models
            return self._simple_reasoning(prompt)
    
    def apply_fallback(self, prompt: str) -> str:
        """
        Apply a fallback implementation when model doesn't support reasoning.
        
        Args:
            prompt: The original prompt to decorate
            
        Returns:
            The decorated prompt
        """
        # Simplified reasoning instructions
        return f"""Note: The model {self.model_id} may have limited reasoning capabilities.

Please explain your thinking process when answering:

{prompt}"""
    
    def _advanced_reasoning(self, prompt: str) -> str:
        """Advanced reasoning for capable models."""
        instruction = f"""Please use advanced, structured reasoning in your response. 

For depth="{self.depth}", provide {"detailed explanations of each step" if self.depth == "comprehensive" else 
                                 "clear explanations of main steps" if self.depth == "moderate" else 
                                 "concise explanations of key steps"}.

{"Present your reasoning as a step-by-step process." if self.show_steps else "Summarize your reasoning process."}

Consider multiple approaches, analyze trade-offs, and explain your choices.

Question: {prompt}"""
        return instruction
    
    def _standard_reasoning(self, prompt: str) -> str:
        """Standard reasoning for models with basic reasoning support."""
        instruction = f"""Please use clear reasoning in your response.

For depth="{self.depth}", provide {"detailed" if self.depth == "comprehensive" else 
                                 "moderate" if self.depth == "moderate" else 
                                 "basic"} reasoning steps.

{"Show your reasoning step by step." if self.show_steps else "Summarize your reasoning process."}

Question: {prompt}"""
        return instruction
    
    def _simple_reasoning(self, prompt: str) -> str:
        """Simple instructions for limited models."""
        instruction = f"""Please explain how you reach your conclusion.

{"Think step by step." if self.show_steps else "Summarize your thinking."}

Question: {prompt}"""
        return instruction
    
    def _default_reasoning(self, prompt: str) -> str:
        """Default reasoning when no model information is available."""
        instruction = "Please use explicit reasoning in your response. "
        
        if self.depth == "basic":
            instruction += "Provide basic reasoning steps. "
        elif self.depth == "moderate":
            instruction += "Provide moderately detailed reasoning steps. "
        elif self.depth == "comprehensive":
            instruction += "Provide comprehensive and detailed reasoning steps. "
        
        if self.show_steps:
            instruction += "Show your reasoning step by step."
        else:
            instruction += "Summarize your reasoning process."
        
        return f"{instruction}\n\n{prompt}"


def demonstrate_model_specific_decorator():
    """Demonstrate the creation and use of model-specific decorators."""
    print("\n=== Model-Specific Decorator Example ===")
    
    # Get the model detector
    detector = get_model_detector()
    
    # Define a prompt
    prompt = "What are the implications of quantum entanglement for secure communications?"
    
    # Define models to try
    models = ["gpt-4", "gpt-3.5-turbo", "mistral-7b-instruct"]
    
    # Try regular decorator first
    print("\n--- Regular Decorator ---")
    
    regular_decorator = ReasoningDecorator(depth="comprehensive", show_steps=True)
    decorated_prompt = regular_decorator.apply(prompt)
    
    print(f"Original prompt: {prompt}")
    print(f"\nDecorated prompt (regular):\n{decorated_prompt}")
    
    # Try model-specific decorator with different models
    print("\n--- Model-Specific Decorator ---")
    
    for model_id in models:
        print(f"\nModel: {model_id}")
        
        # Create a model-specific decorator
        model_decorator = ModelSpecificReasoningDecorator(
            model_id=model_id,
            depth="comprehensive",
            show_steps=True
        )
        
        # Apply the decorator
        model_decorated_prompt = model_decorator.apply(prompt)
        
        print(f"Decorated prompt:\n{model_decorated_prompt}")
    
    # Alternative: Use the factory to create model-specific decorators
    print("\n--- Factory-Created Model-Specific Decorators ---")
    
    for model_id in models:
        print(f"\nModel: {model_id}")
        
        # Create a model-specific decorator using the factory
        factory_decorator = ModelSpecificDecoratorFactory.create_for_model(
            ReasoningDecorator,
            model_id,
            depth="comprehensive",
            show_steps=True
        )
        
        # Apply the decorator
        factory_decorated_prompt = factory_decorator.apply(prompt)
        
        print(f"Decorated prompt:\n{factory_decorated_prompt}")


if __name__ == "__main__":
    demonstrate_model_specific_decorator() 