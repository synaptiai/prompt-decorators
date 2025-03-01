#!/usr/bin/env python
"""
Model Detection Example

This script demonstrates how to use the ModelDetector to detect and query model capabilities.
"""

import os
import sys
import json
from pathlib import Path
import argparse

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from prompt_decorators.utils import (
    ModelDetector, 
    ModelCapabilities, 
    get_model_detector
)
from prompt_decorators.utils.discovery import get_registry


def demonstrate_model_detection():
    """Demonstrate basic model detection functionality."""
    print("\n=== Model Detection ===")
    
    # Get the model detector
    detector = get_model_detector()
    
    # Get information about a specific model
    model_id = "gpt-4"
    model = detector.get_model_capabilities(model_id)
    
    if model:
        print(f"\nModel: {model.model_id} (Family: {model.model_family}, Version: {model.version})")
        print("Capabilities:")
        for key, value in model.capabilities.items():
            print(f"  - {key}: {value}")
    else:
        print(f"Model {model_id} not found.")
    
    # Show all available models
    models = detector.get_all_models()
    print(f"\nAll available models ({len(models)}):")
    for model in models:
        print(f"  - {model.model_id} (Family: {model.model_family})")
    
    # Show all model families
    families = detector.get_all_families()
    print(f"\nAll model families ({len(families)}):")
    for family in families:
        models_in_family = detector.get_models_by_family(family)
        print(f"  - {family} ({len(models_in_family)} models)")
        for model in models_in_family:
            print(f"    - {model.model_id} (v{model.version})")


def demonstrate_capabilities_check():
    """Demonstrate checking model capabilities for specific features."""
    print("\n=== Capabilities Check ===")
    
    # Get the model detector
    detector = get_model_detector()
    
    # Compare capabilities of different models
    models_to_check = ["gpt-4", "gpt-3.5-turbo", "claude-2", "llama-2-70b-chat"]
    features_to_check = [
        "reasoning", 
        "json_output", 
        "function_calling", 
        "multi_tool_use"
    ]
    
    print("\nFeature support by model:")
    print(f"{'Feature':<20} | " + " | ".join(f"{model:<12}" for model in models_to_check))
    print(f"{'-'*20} | " + " | ".join(f"{'-'*12}" for _ in models_to_check))
    
    for feature in features_to_check:
        support_indicators = []
        for model_id in models_to_check:
            model = detector.get_model_capabilities(model_id)
            if model and model.supports_feature(feature):
                support_indicators.append("✓")
            else:
                support_indicators.append("✗")
        
        print(f"{feature:<20} | " + " | ".join(f"{indicator:^12}" for indicator in support_indicators))


def demonstrate_decorator_compatibility():
    """Demonstrate checking which decorators are compatible with different models."""
    print("\n=== Decorator Compatibility ===")
    
    # Get the model detector
    detector = get_model_detector()
    
    # Check decorator compatibility for different models
    models_to_check = ["gpt-4", "gpt-3.5-turbo", "mistral-7b-instruct"]
    decorators_to_check = [
        "Reasoning",
        "StepByStep",
        "Socratic",
        "TreeOfThought",
        "CiteSources",
        "ELI5"
    ]
    
    print("\nDecorator support by model:")
    print(f"{'Decorator':<15} | " + " | ".join(f"{model:<12}" for model in models_to_check))
    print(f"{'-'*15} | " + " | ".join(f"{'-'*12}" for _ in models_to_check))
    
    for decorator in decorators_to_check:
        support_indicators = []
        for model_id in models_to_check:
            model = detector.get_model_capabilities(model_id)
            if model and "supported_decorators" in model.capabilities:
                if decorator in model.capabilities["supported_decorators"]:
                    support_indicators.append("✓")
                else:
                    support_indicators.append("✗")
            else:
                support_indicators.append("?")
        
        print(f"{decorator:<15} | " + " | ".join(f"{indicator:^12}" for indicator in support_indicators))


def demonstrate_model_adaptation():
    """Demonstrate how decorators can adapt to different models."""
    print("\n=== Model Adaptation ===")
    
    # Get the model detector
    detector = get_model_detector()
    
    # Get the registry
    registry = get_registry()
    
    # Define a prompt
    prompt = "Explain the concept of quantum computing."
    
    # Try to apply a decorator with different models
    decorator_name = "Reasoning"
    models_to_try = ["gpt-4", "gpt-3.5-turbo", "mistral-7b-instruct"]
    
    for model_id in models_to_try:
        print(f"\nApplying {decorator_name} decorator with model: {model_id}")
        
        # Get model capabilities
        model = detector.get_model_capabilities(model_id)
        
        if not model:
            print(f"  Model {model_id} not found.")
            continue
        
        # Check if the decorator is supported
        if (model and "supported_decorators" in model.capabilities and 
            decorator_name in model.capabilities["supported_decorators"]):
            
            # In a real implementation, we would adapt the decorator based on model capabilities
            # For this example, we'll just simulate different adaptations
            
            print(f"  Model {model_id} supports the {decorator_name} decorator.")
            
            if model.supports_feature("multi_tool_use"):
                print("  Using advanced reasoning capabilities...")
                adapted_prompt = f"Please use advanced reasoning with multiple tools to answer: {prompt}"
            elif model.supports_feature("reasoning"):
                print("  Using basic reasoning capabilities...")
                adapted_prompt = f"Please use step-by-step reasoning to answer: {prompt}"
            else:
                print("  Using fallback approach (no special reasoning capabilities)...")
                adapted_prompt = f"Please explain in detail: {prompt}"
                
            print(f"  Adapted prompt: {adapted_prompt}")
        else:
            print(f"  Model {model_id} does not support the {decorator_name} decorator.")
            print("  Using fallback approach...")
            adapted_prompt = f"Please explain clearly: {prompt}"
            print(f"  Adapted prompt: {adapted_prompt}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demonstrate model detection")
    parser.add_argument(
        "--basic", "-b",
        action="store_true",
        help="Run basic model detection demonstration"
    )
    parser.add_argument(
        "--capabilities", "-c",
        action="store_true",
        help="Run capabilities check demonstration"
    )
    parser.add_argument(
        "--compatibility", "-d",
        action="store_true",
        help="Run decorator compatibility demonstration"
    )
    parser.add_argument(
        "--adaptation", "-a",
        action="store_true",
        help="Run model adaptation demonstration"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all demonstrations"
    )
    
    args = parser.parse_args()
    
    # If no specific demonstrations were requested, run everything
    if not (args.basic or args.capabilities or args.compatibility or args.adaptation) or args.all:
        demonstrate_model_detection()
        demonstrate_capabilities_check()
        demonstrate_decorator_compatibility()
        demonstrate_model_adaptation()
    else:
        if args.basic:
            demonstrate_model_detection()
        if args.capabilities:
            demonstrate_capabilities_check()
        if args.compatibility:
            demonstrate_decorator_compatibility()
        if args.adaptation:
            demonstrate_model_adaptation() 