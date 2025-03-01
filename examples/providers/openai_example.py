#!/usr/bin/env python
"""
Example demonstrating how to use Prompt Decorators with OpenAI's API.

This script shows how to integrate the Prompt Decorators framework with OpenAI's
GPT models to enhance prompt engineering and standardize interactions.
"""

import os
from typing import Dict, Any, List, Optional
import json
import openai
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

# Initialize OpenAI client with API key from environment
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def send_to_openai(
    prompt: str,
    model: str = "gpt-4",
    temperature: float = 0.7,
    max_tokens: int = 1000,
    top_p: float = 1.0,
    frequency_penalty: float = 0.0,
    presence_penalty: float = 0.0,
) -> str:
    """
    Send a prompt to the OpenAI API and get the response.

    Args:
        prompt: The prompt text to send
        model: The model to use (default: gpt-4)
        temperature: Controls randomness (0-1)
        max_tokens: Maximum number of tokens in response
        top_p: Controls diversity via nucleus sampling
        frequency_penalty: Decreases repetition of token sequences
        presence_penalty: Increases likelihood of new topics

    Returns:
        The generated text response
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    
    return response.choices[0].message.content


def example_basic_decorator() -> None:
    """
    Example of using a single decorator with OpenAI.
    """
    print("\n==== Basic Decorator Example ====")
    
    # Create a prompt
    original_prompt = "Explain quantum computing"
    
    # Create a decorator instance
    concise = Concise(max_words=100)
    
    # Apply the decorator to the prompt
    decorated_prompt = concise.apply(original_prompt)
    
    print(f"Original prompt: {original_prompt}")
    print(f"Decorated prompt: {decorated_prompt}")
    
    # Send to OpenAI
    response = send_to_openai(decorated_prompt)
    
    print("\nResponse:")
    print(response)


def example_multiple_decorators() -> None:
    """
    Example of combining multiple decorators with OpenAI.
    """
    print("\n==== Multiple Decorators Example ====")
    
    # Create a prompt
    original_prompt = "Explain the benefits and risks of artificial intelligence"
    
    # Create decorator instances
    reasoning = Reasoning(depth="moderate")
    professional = Professional()
    step_by_step = StepByStep(numbered=True)
    
    # Apply decorators in sequence (order matters!)
    decorated_prompt = original_prompt
    decorated_prompt = reasoning.apply(decorated_prompt)
    decorated_prompt = professional.apply(decorated_prompt)
    decorated_prompt = step_by_step.apply(decorated_prompt)
    
    print(f"Original prompt: {original_prompt}")
    print(f"Decorated prompt: {decorated_prompt}")
    
    # Send to OpenAI
    response = send_to_openai(decorated_prompt)
    
    print("\nResponse:")
    print(response)


def example_using_request_class() -> None:
    """
    Example of using the DecoratedRequest class with OpenAI.
    """
    print("\n==== DecoratedRequest Example ====")
    
    # Create a prompt
    original_prompt = "Create a one-week meal plan for a vegetarian diet"
    
    # Create decorator instances
    step_by_step = StepByStep(numbered=True)
    output_format = OutputFormat(format_type="markdown")
    
    # Create a decorated request
    request = DecoratedRequest(
        prompt=original_prompt,
        decorators=[step_by_step, output_format],
        model="gpt-4",
        api_params={"temperature": 0.8, "max_tokens": 1200}
    )
    
    # Apply all decorators
    decorated_prompt = request.apply_decorators()
    
    print(f"Original prompt: {original_prompt}")
    print(f"Decorated prompt: {decorated_prompt}")
    
    # Access model and parameters from request
    model = request.model
    params = request.api_params
    
    # Send to OpenAI (using parameters from request)
    response = send_to_openai(
        decorated_prompt,
        model=model,
        temperature=params.get("temperature", 0.7),
        max_tokens=params.get("max_tokens", 1000)
    )
    
    print("\nResponse:")
    print(response)


def example_registry_discovery() -> None:
    """
    Example of using the decorator registry with OpenAI.
    """
    print("\n==== Registry Discovery Example ====")
    
    # Get the registry instance
    registry = DecoratorRegistry()
    
    # Find available decorators
    reasoning_decorators = registry.find_decorators_by_category("reasoning")
    
    print(f"Available reasoning decorators: {[d.__name__ for d in reasoning_decorators]}")
    
    # Get a decorator by name
    eli5_class = registry.get_decorator("ELI5")
    
    # Create an instance
    eli5 = eli5_class()
    
    # Apply to a prompt
    original_prompt = "Explain how blockchain technology works"
    decorated_prompt = eli5.apply(original_prompt)
    
    print(f"Original prompt: {original_prompt}")
    print(f"Decorated prompt: {decorated_prompt}")
    
    # Send to OpenAI
    response = send_to_openai(decorated_prompt)
    
    print("\nResponse:")
    print(response)


def example_model_specific_usage() -> None:
    """
    Example of adapting decorators based on OpenAI model capabilities.
    """
    print("\n==== Model-Specific Usage Example ====")
    
    # Define model capabilities (simplified version)
    model_capabilities = {
        "gpt-4": {
            "supports_json": True,
            "supports_reasoning": True,
            "token_limit": 8000
        },
        "gpt-3.5-turbo": {
            "supports_json": True,
            "supports_reasoning": True,
            "token_limit": 4000
        }
    }
    
    # Select model
    model = "gpt-3.5-turbo"
    
    # Create a prompt
    original_prompt = "Compare and contrast machine learning and deep learning"
    
    # Choose decorators based on model capabilities
    decorators = []
    
    if model_capabilities[model]["supports_reasoning"]:
        decorators.append(Reasoning(depth="moderate"))
    
    if model_capabilities[model]["supports_json"]:
        decorators.append(OutputFormat(format_type="json"))
    
    # Apply decorators
    decorated_prompt = original_prompt
    for decorator in decorators:
        decorated_prompt = decorator.apply(decorated_prompt)
    
    print(f"Model: {model}")
    print(f"Original prompt: {original_prompt}")
    print(f"Decorated prompt: {decorated_prompt}")
    
    # Send to OpenAI
    response = send_to_openai(decorated_prompt, model=model)
    
    print("\nResponse:")
    print(response)


if __name__ == "__main__":
    print("======= Prompt Decorators with OpenAI Examples =======")
    
    # Run examples
    example_basic_decorator()
    example_multiple_decorators()
    example_using_request_class()
    example_registry_discovery()
    example_model_specific_usage()
    
    print("\n======= Examples Complete =======") 