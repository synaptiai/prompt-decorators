#!/usr/bin/env python
"""
Example demonstrating how to use Prompt Decorators with Anthropic's Claude API.

This script shows how to integrate the Prompt Decorators framework with Anthropic's
Claude models to enhance prompt engineering and standardize interactions.
"""

import os
from typing import Dict, Any, List, Optional
import json
import anthropic
from dotenv import load_dotenv

from prompt_decorators.decorators.generated.decorators.concise import Concise
from prompt_decorators.decorators.generated.decorators.reasoning import Reasoning
from prompt_decorators.decorators.generated.decorators.professional import Professional
from prompt_decorators.decorators.generated.decorators.step_by_step import StepByStep
from prompt_decorators.decorators.generated.decorators.eli5 import ELI5
from prompt_decorators.decorators.generated.decorators.output_format import OutputFormat
from prompt_decorators.core.request import DecoratedRequest
from prompt_decorators.utils.discovery import DecoratorRegistry

# Load environment variables from .env file
load_dotenv()

# Initialize Anthropic client with API key from environment
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def send_to_claude(
    prompt: str,
    model: str = "claude-3-opus-20240229",
    temperature: float = 0.7,
    max_tokens: int = 1000,
    top_p: float = 1.0,
    top_k: int = 0,
) -> str:
    """
    Send a prompt to the Anthropic Claude API and get the response.

    Args:
        prompt: The prompt text to send
        model: The Claude model to use (default: claude-3-opus-20240229)
        temperature: Controls randomness (0-1)
        max_tokens: Maximum number of tokens in response
        top_p: Controls diversity via nucleus sampling
        top_k: Controls diversity via top-k sampling

    Returns:
        The generated text response
    """
    # Create a system prompt that helps Claude understand the context
    system_prompt = "You are Claude, an AI assistant using prompt decorators to structure your responses."
    
    response = client.messages.create(
        model=model,
        system=system_prompt,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        top_k=top_k
    )
    
    return response.content[0].text


def example_basic_decorator() -> None:
    """
    Example of using a single decorator with Claude.
    """
    print("\n==== Basic Decorator Example ====")
    
    # Create a prompt
    original_prompt = "Explain the concept of quantum entanglement"
    
    # Create a decorator instance
    concise = Concise(max_words=150)
    
    # Apply the decorator to the prompt
    decorated_prompt = concise.apply(original_prompt)
    
    print(f"Original prompt: {original_prompt}")
    print(f"Decorated prompt: {decorated_prompt}")
    
    # Send to Claude
    response = send_to_claude(decorated_prompt)
    
    print("\nResponse:")
    print(response)


def example_multiple_decorators() -> None:
    """
    Example of combining multiple decorators with Claude.
    """
    print("\n==== Multiple Decorators Example ====")
    
    # Create a prompt
    original_prompt = "Explain the ethical considerations of autonomous vehicles"
    
    # Create decorator instances
    reasoning = Reasoning(depth="comprehensive")
    professional = Professional()
    step_by_step = StepByStep(numbered=True)
    
    # Apply decorators in sequence (order matters!)
    decorated_prompt = original_prompt
    decorated_prompt = reasoning.apply(decorated_prompt)
    decorated_prompt = professional.apply(decorated_prompt)
    decorated_prompt = step_by_step.apply(decorated_prompt)
    
    print(f"Original prompt: {original_prompt}")
    print(f"Decorated prompt: {decorated_prompt}")
    
    # Send to Claude
    response = send_to_claude(decorated_prompt)
    
    print("\nResponse:")
    print(response)


def example_using_request_class() -> None:
    """
    Example of using the DecoratedRequest class with Claude.
    """
    print("\n==== DecoratedRequest Example ====")
    
    # Create a prompt
    original_prompt = "Design a sustainable smart city infrastructure"
    
    # Create decorator instances
    step_by_step = StepByStep(numbered=True)
    output_format = OutputFormat(format_type="markdown")
    
    # Create a decorated request
    request = DecoratedRequest(
        prompt=original_prompt,
        decorators=[step_by_step, output_format],
        model="claude-3-sonnet-20240229",
        api_params={"temperature": 0.8, "max_tokens": 1500}
    )
    
    # Apply all decorators
    decorated_prompt = request.apply_decorators()
    
    print(f"Original prompt: {original_prompt}")
    print(f"Decorated prompt: {decorated_prompt}")
    
    # Access model and parameters from request
    model = request.model
    params = request.api_params
    
    # Adapt model name if needed (in case the model naming is different)
    claude_model = model if model.startswith("claude") else "claude-3-sonnet-20240229"
    
    # Send to Claude (using parameters from request)
    response = send_to_claude(
        decorated_prompt,
        model=claude_model,
        temperature=params.get("temperature", 0.7),
        max_tokens=params.get("max_tokens", 1000)
    )
    
    print("\nResponse:")
    print(response)


def example_registry_discovery() -> None:
    """
    Example of using the decorator registry with Claude.
    """
    print("\n==== Registry Discovery Example ====")
    
    # Get the registry instance
    registry = DecoratorRegistry()
    
    # Find available decorators
    format_decorators = registry.find_decorators_by_category("format")
    
    print(f"Available format decorators: {[d.__name__ for d in format_decorators]}")
    
    # Get a decorator by name
    eli5_class = registry.get_decorator("ELI5")
    
    # Create an instance
    eli5 = eli5_class()
    
    # Apply to a prompt
    original_prompt = "Explain how CRISPR gene editing works"
    decorated_prompt = eli5.apply(original_prompt)
    
    print(f"Original prompt: {original_prompt}")
    print(f"Decorated prompt: {decorated_prompt}")
    
    # Send to Claude
    response = send_to_claude(decorated_prompt)
    
    print("\nResponse:")
    print(response)


def example_claude_specific_features() -> None:
    """
    Example showing Claude-specific considerations when using decorators.
    """
    print("\n==== Claude-Specific Features Example ====")
    
    # Claude models have great abilities with XML tagging, so we can enhance our decorators
    
    # Create a custom XML wrapper function for Claude
    def xml_tag_response(prompt: str, tag: str = "response") -> str:
        """Wrap prompt with XML tags for better Claude responses"""
        return f"{prompt}\n\nPlease provide your response inside <{tag}> tags."
    
    # Create a prompt
    original_prompt = "Explain the basics of prompt engineering"
    
    # Create decorator instances
    reasoning = Reasoning(depth="moderate")
    
    # Apply decorator
    decorated_prompt = reasoning.apply(original_prompt)
    
    # Add Claude-specific XML enhancement
    claude_prompt = xml_tag_response(decorated_prompt)
    
    print(f"Original prompt: {original_prompt}")
    print(f"Claude-enhanced prompt: {claude_prompt}")
    
    # Send to Claude
    response = send_to_claude(claude_prompt)
    
    print("\nResponse:")
    print(response)


def example_model_specific_usage() -> None:
    """
    Example of adapting decorators based on Claude model capabilities.
    """
    print("\n==== Model-Specific Usage Example ====")
    
    # Define model capabilities (simplified version)
    model_capabilities = {
        "claude-3-opus-20240229": {
            "supports_markdown": True,
            "supports_reasoning": True,
            "supports_xml_tags": True,
            "token_limit": 200000  # Claude 3 Opus has extremely large context
        },
        "claude-3-sonnet-20240229": {
            "supports_markdown": True,
            "supports_reasoning": True,
            "supports_xml_tags": True,
            "token_limit": 180000
        },
        "claude-3-haiku-20240229": {
            "supports_markdown": True,
            "supports_reasoning": True,
            "supports_xml_tags": True,
            "token_limit": 150000
        }
    }
    
    # Select model
    model = "claude-3-haiku-20240229"
    
    # Create a prompt
    original_prompt = "Explain the key theories in modern cosmology"
    
    # Choose decorators based on model capabilities
    decorators = []
    
    if model_capabilities[model]["supports_reasoning"]:
        # For the smaller model, use a less comprehensive reasoning approach
        if model == "claude-3-haiku-20240229":
            decorators.append(Reasoning(depth="basic"))
        else:
            decorators.append(Reasoning(depth="comprehensive"))
    
    if model_capabilities[model]["supports_markdown"]:
        decorators.append(OutputFormat(format_type="markdown"))
    
    # Apply decorators
    decorated_prompt = original_prompt
    for decorator in decorators:
        decorated_prompt = decorator.apply(decorated_prompt)
    
    # Optionally add XML tags for Claude
    if model_capabilities[model]["supports_xml_tags"]:
        decorated_prompt += "\n\nPlease provide your response inside <answer> tags."
    
    print(f"Model: {model}")
    print(f"Original prompt: {original_prompt}")
    print(f"Decorated prompt: {decorated_prompt}")
    
    # Send to Claude
    response = send_to_claude(decorated_prompt, model=model)
    
    print("\nResponse:")
    print(response)


if __name__ == "__main__":
    print("======= Prompt Decorators with Anthropic Claude Examples =======")
    
    # Run examples
    example_basic_decorator()
    example_multiple_decorators()
    example_using_request_class()
    example_registry_discovery()
    example_claude_specific_features()
    example_model_specific_usage()
    
    print("\n======= Examples Complete =======") 