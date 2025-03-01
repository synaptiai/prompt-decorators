#!/usr/bin/env python3
"""
Example implementation of a Debate decorator.

This example shows how to implement a new decorator that formats responses
as a debate between multiple perspectives.
"""

from typing import Dict, List, Optional, Union, Any
import json
import sys
from pathlib import Path

# Import the base decorator class (if you're integrating with an existing framework)
# Otherwise, you can define your own base class
try:
    # Assuming you have the prompt-decorators-core package installed
    from prompt_decorators_core import BaseDecorator, APIRequest
except ImportError:
    # If not installed, provide a simple implementation
    class BaseDecorator:
        """Base class for all prompt decorators."""
        
        def __init__(self, name: str, version: str = "1.0.0"):
            """Initialize the decorator with a name and version.
            
            Args:
                name: The name of the decorator
                version: The semantic version of the decorator implementation
            """
            self.name = name
            self.version = version
            self.parameters: Dict[str, Any] = {}
            
        def to_system_instructions(self) -> str:
            """Convert decorator to system instructions for the AI.
            
            Returns:
                A string containing system instructions
            """
            raise NotImplementedError("Subclasses must implement this method")
            
        def to_dict(self) -> Dict[str, Any]:
            """Convert decorator to a dictionary representation.
            
            Returns:
                Dictionary representation of the decorator
            """
            return {
                "name": self.name,
                "version": self.version,
                "parameters": self.parameters
            }
            
    class APIRequest:
        """Simple API request class."""
        
        def __init__(self, prompt: str, decorators: Optional[List[BaseDecorator]] = None):
            """Initialize with prompt and decorators.
            
            Args:
                prompt: The user's prompt
                decorators: List of decorators to apply
            """
            self.prompt = prompt
            self.decorators = decorators or []


class DebateDecorator(BaseDecorator):
    """Decorator that structures responses as a debate between multiple perspectives."""
    
    def __init__(self, perspectives: int = 2, balanced: bool = True):
        """Initialize the Debate decorator.
        
        Args:
            perspectives: Number of different perspectives to include (2-5)
            balanced: Whether to ensure equal representation of each perspective
        """
        super().__init__(name="Debate", version="1.0.0")
        
        # Validate parameters
        if not isinstance(perspectives, int) or perspectives < 2 or perspectives > 5:
            raise ValueError("perspectives must be an integer between 2 and 5")
            
        self.parameters = {
            "perspectives": perspectives,
            "balanced": balanced
        }
    
    def to_system_instructions(self) -> str:
        """Convert decorator to system instructions for the AI.
        
        Returns:
            A string containing system instructions
        """
        perspectives = self.parameters.get("perspectives", 2)
        balanced = self.parameters.get("balanced", True)
        
        instructions = [
            f"Structure your response as a debate between {perspectives} different perspectives on the topic.",
            "For each perspective:",
            "1. Clearly label it (e.g., 'Perspective 1: Economic View')",
            "2. Present the strongest possible arguments for that position",
            "3. Include potential counterarguments or limitations of this perspective"
        ]
        
        if balanced:
            instructions.append("Ensure equal representation and strength of arguments for each perspective.")
        
        instructions.append(f"After presenting all {perspectives} perspectives, provide a brief synthesis that acknowledges the complexity of the issue.")
        
        return "\n".join(instructions)


def validate_decorator_against_schema(decorator: BaseDecorator, schema_path: Optional[str] = None) -> bool:
    """Validate a decorator against the schema.
    
    This is a simplified validation function. In a real implementation,
    you would use a more robust validation approach.
    
    Args:
        decorator: The decorator to validate
        schema_path: Path to the schema file
        
    Returns:
        True if valid, False otherwise
    """
    try:
        # For this example, we'll just do some basic validation
        required_fields = {"name", "version", "parameters"}
        decorator_dict = decorator.to_dict()
        
        for field in required_fields:
            if field not in decorator_dict:
                print(f"Missing required field: {field}")
                return False
                
        # In a real implementation, you would validate against the JSON schema
        if schema_path:
            try:
                import jsonschema
                
                with open(schema_path, "r") as f:
                    schema = json.load(f)
                    
                jsonschema.validate(instance=decorator_dict, schema=schema)
            except ImportError:
                print("jsonschema package not installed, skipping schema validation")
            except Exception as e:
                print(f"Validation error: {e}")
                return False
                
        return True
    except Exception as e:
        print(f"Validation error: {e}")
        return False


def create_registry_entry() -> Dict[str, Any]:
    """Create a registry entry for the Debate decorator.
    
    Returns:
        Dictionary containing the registry entry
    """
    return {
        "decoratorName": "Debate",
        "version": "1.0.0",
        "description": "Structures the response as a debate between multiple perspectives on a topic",
        "author": {
            "name": "Dialectic AI",
            "email": "contact@example.org",
            "url": "https://example.org"
        },
        "parameters": [
            {
                "name": "perspectives",
                "type": "number",
                "description": "Number of different perspectives to include",
                "default": 2,
                "required": False,
                "validation": {
                    "minimum": 2,
                    "maximum": 5
                }
            },
            {
                "name": "balanced",
                "type": "boolean",
                "description": "Whether to ensure equal representation of each perspective",
                "default": True,
                "required": False
            }
        ],
        "examples": [
            {
                "description": "Three-perspective debate on a policy issue",
                "usage": "+++Debate(perspectives=3, balanced=true)\nShould universal basic income be implemented nationally?",
                "result": "Presents three balanced perspectives on UBI in a debate format"
            }
        ],
        "compatibility": {
            "requires": [],
            "conflicts": ["OutputFormat"],
            "minStandardVersion": "1.0.0",
            "maxStandardVersion": "2.0.0",
            "models": [
                "gpt-4"
            ]
        }
    }


def main():
    """Example usage of the Debate decorator."""
    # Create an instance of the Debate decorator
    debate = DebateDecorator(perspectives=3, balanced=True)
    
    # Validate the decorator
    print("Validating decorator...")
    is_valid = validate_decorator_against_schema(debate)
    print(f"Decorator is {'valid' if is_valid else 'invalid'}\n")
    
    # Display the system instructions
    print("System instructions:")
    print("-" * 50)
    print(debate.to_system_instructions())
    print("-" * 50 + "\n")
    
    # Create an API request with the decorator
    prompt = "Should universal basic income be implemented nationally?"
    request = APIRequest(prompt=prompt, decorators=[debate])
    
    # Display the request
    print("Example API request:")
    print("-" * 50)
    print(f"Prompt: {request.prompt}")
    print("Decorators:")
    for d in request.decorators:
        print(f"  - {d.name} (version {d.version})")
        for key, value in d.parameters.items():
            print(f"    - {key}: {value}")
    print("-" * 50 + "\n")
    
    # Display the registry entry
    print("Registry entry:")
    print("-" * 50)
    registry_entry = create_registry_entry()
    print(json.dumps(registry_entry, indent=2))
    print("-" * 50)
    
    # In a real implementation, you would save the registry entry to a file
    # and validate it against the registry-entry schema
    # For example:
    # with open("registry/extensions/debate.json", "w") as f:
    #     json.dump(registry_entry, f, indent=2)


if __name__ == "__main__":
    main() 