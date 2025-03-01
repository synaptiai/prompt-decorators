#!/usr/bin/env python
"""
Telemetry System Demonstration

This script demonstrates how to use the telemetry system for tracking decorator usage.
"""

import os
import sys
import json
import time
from pathlib import Path
import argparse
import random

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from prompt_decorators.utils import get_telemetry_manager, get_registry
from prompt_decorators.core import BaseDecorator


class SampleDecorator(BaseDecorator):
    """Sample decorator for telemetry demonstration."""
    
    name = "Sample"
    version = "1.0.0"
    category = "demo"
    
    def __init__(self, factor: int = 1):
        """Initialize the sample decorator."""
        super().__init__()
        self.factor = factor
    
    def apply(self, prompt: str) -> str:
        """Apply the decorator to a prompt."""
        # Simulate processing time for performance tracking
        time.sleep(0.02 * self.factor)
        return f"Sample decorator applied (factor: {self.factor}).\n\n{prompt}"


def demonstrate_telemetry_basics():
    """Demonstrate basic telemetry functionality."""
    print("\n=== Telemetry Basics ===")
    
    # Get the telemetry manager
    telemetry = get_telemetry_manager()
    
    # Check if telemetry is enabled
    print(f"Telemetry is currently {'enabled' if telemetry.is_enabled() else 'disabled'}")
    
    # Enable telemetry
    print("Enabling telemetry...")
    telemetry.enable()
    print(f"Telemetry is now {'enabled' if telemetry.is_enabled() else 'disabled'}")
    
    # Track decorator usage
    print("\nTracking decorator usage...")
    telemetry.track_decorator_usage(
        decorator_name="Concise",
        version="1.0.0",
        parameters={"level": 2, "bulletPoints": True},
        metadata={"source": "API"}
    )
    
    # Show config location
    config_dir = os.environ.get(
        "PROMPT_DECORATORS_CONFIG_DIR",
        os.path.expanduser("~/.prompt_decorators")
    )
    print(f"\nTelemetry data is stored in: {config_dir}/telemetry_data")
    print(f"Telemetry configuration is stored in: {config_dir}/telemetry.json")


def demonstrate_tracking_performance():
    """Demonstrate tracking decorator performance."""
    print("\n=== Tracking Performance ===")
    
    # Get the telemetry manager
    telemetry = get_telemetry_manager()
    
    # Create sample decorators with different factors
    decorators = [
        SampleDecorator(factor=1),
        SampleDecorator(factor=2),
        SampleDecorator(factor=3)
    ]
    
    # Apply decorators and track performance
    prompt = "This is a sample prompt."
    
    for decorator in decorators:
        print(f"Applying {decorator.name} decorator with factor {decorator.factor}...")
        
        # Measure execution time
        start_time = time.time()
        decorated_prompt = decorator.apply(prompt)
        execution_time = time.time() - start_time
        
        # Track performance
        telemetry.track_performance(
            decorator_name=decorator.name,
            version=decorator.version,
            execution_time=execution_time,
            metadata={"factor": decorator.factor}
        )
        
        print(f"  Execution time: {execution_time:.4f} seconds")


def demonstrate_tracking_combinations():
    """Demonstrate tracking decorator combinations."""
    print("\n=== Tracking Decorator Combinations ===")
    
    # Get the telemetry manager
    telemetry = get_telemetry_manager()
    
    # Define some decorator examples
    decorators = [
        {"name": "Concise", "version": "1.0.0", "parameters": {"level": 2}},
        {"name": "Professional", "version": "1.0.0", "parameters": {}},
        {"name": "ELI5", "version": "1.0.0", "parameters": {"age": 10}},
        {"name": "Creative", "version": "1.0.0", "parameters": {"level": 3}},
        {"name": "StepByStep", "version": "1.0.0", "parameters": {"steps": 5}},
    ]
    
    # Track some random combinations
    for _ in range(3):
        # Pick a random number of decorators (1-3)
        num_decorators = random.randint(1, 3)
        
        # Select random decorators
        selected = random.sample(decorators, num_decorators)
        
        # Track the combination
        print(f"Tracking combination of {num_decorators} decorators:")
        for decorator in selected:
            print(f"  - {decorator['name']} (v{decorator['version']})")
            
        telemetry.track_decorator_combination(
            decorators=selected,
            prompt_length=random.randint(50, 500),
            metadata={"source": "demo"}
        )


def demonstrate_callbacks():
    """Demonstrate telemetry callbacks."""
    print("\n=== Telemetry Callbacks ===")
    
    # Get the telemetry manager
    telemetry = get_telemetry_manager()
    
    # Define a callback function
    def usage_callback(event):
        decorator = event.get("decorator", {})
        print(f"Callback received: {decorator.get('name')} used with parameters: {decorator.get('parameters')}")
    
    # Register the callback
    telemetry.register_callback("decorator_usage", usage_callback)
    print("Registered callback for decorator_usage events")
    
    # Track usage to trigger callback
    print("\nTracking usage to trigger callback...")
    telemetry.track_decorator_usage(
        decorator_name="ELI5",
        version="1.0.0",
        parameters={"age": 8}
    )
    
    # Unregister the callback
    telemetry.unregister_callback("decorator_usage", usage_callback)
    print("Unregistered callback")


def demonstrate_disable_telemetry():
    """Demonstrate disabling telemetry."""
    print("\n=== Disabling Telemetry ===")
    
    # Get the telemetry manager
    telemetry = get_telemetry_manager()
    
    # Ensure telemetry is enabled
    if not telemetry.is_enabled():
        telemetry.enable()
    
    print(f"Telemetry is currently {'enabled' if telemetry.is_enabled() else 'disabled'}")
    
    # Track usage with telemetry enabled
    telemetry.track_decorator_usage(
        decorator_name="Test",
        version="1.0.0"
    )
    print("Tracked usage with telemetry enabled")
    
    # Disable telemetry
    print("\nDisabling telemetry...")
    telemetry.disable()
    print(f"Telemetry is now {'enabled' if telemetry.is_enabled() else 'disabled'}")
    
    # Try to track usage with telemetry disabled
    telemetry.track_decorator_usage(
        decorator_name="Test",
        version="1.0.0"
    )
    print("Attempted to track usage with telemetry disabled (should be ignored)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demonstrate the telemetry system")
    parser.add_argument(
        "--basics", "-b",
        action="store_true",
        help="Run basic telemetry demonstration"
    )
    parser.add_argument(
        "--performance", "-p",
        action="store_true",
        help="Run performance tracking demonstration"
    )
    parser.add_argument(
        "--combinations", "-c",
        action="store_true",
        help="Run decorator combinations demonstration"
    )
    parser.add_argument(
        "--callbacks", "-a",
        action="store_true",
        help="Run callbacks demonstration"
    )
    parser.add_argument(
        "--disable", "-d",
        action="store_true",
        help="Run disable telemetry demonstration"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all demonstrations"
    )
    
    args = parser.parse_args()
    
    # If no specific demonstrations were requested, run everything
    if not (args.basics or args.performance or args.combinations or args.callbacks or args.disable) or args.all:
        demonstrate_telemetry_basics()
        demonstrate_tracking_performance()
        demonstrate_tracking_combinations()
        demonstrate_callbacks()
        demonstrate_disable_telemetry()
    else:
        if args.basics:
            demonstrate_telemetry_basics()
        if args.performance:
            demonstrate_tracking_performance()
        if args.combinations:
            demonstrate_tracking_combinations()
        if args.callbacks:
            demonstrate_callbacks()
        if args.disable:
            demonstrate_disable_telemetry() 