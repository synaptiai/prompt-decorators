"""
API Request Handling Module

This module provides utilities for handling API requests with decorators.
"""

import json
from typing import Any, Dict, List, Optional, Set, Type, Union

from .base import BaseDecorator


class DecoratedRequest:
    """Class representing a request decorated with prompt decorators."""
    
    def __init__(
        self,
        prompt: str,
        decorators: Optional[List[BaseDecorator]] = None,
        model: Optional[str] = None,
        api_params: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize a decorated request.
        
        Args:
            prompt: The base prompt text
            decorators: Optional list of decorators to apply
            model: Optional model identifier
            api_params: Optional additional API parameters
        """
        self.prompt = prompt
        self.decorators = decorators or []
        self.model = model
        self.api_params = api_params or {}
        
        # Validate decorator compatibility
        self._validate_decorators()
    
    def _validate_decorators(self) -> None:
        """
        Validate that the decorators are compatible with each other.
        
        Raises:
            ValueError: If incompatible decorators are found
        """
        # This is a placeholder for more complex compatibility checking
        # In a real implementation, this would check for conflicting decorators
        decorator_names = set()
        
        for decorator in self.decorators:
            if decorator.name in decorator_names:
                raise ValueError(f"Duplicate decorator: {decorator.name}")
            decorator_names.add(decorator.name)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the request to a dictionary representation.
        
        Returns:
            Dictionary representation of the request
        """
        result = {
            "prompt": self.prompt,
            "decorators": [decorator.to_dict() for decorator in self.decorators]
        }
        
        if self.model:
            result["model"] = self.model
        
        if self.api_params:
            result["api_params"] = self.api_params
        
        return result
    
    def to_json(self, indent: Optional[int] = None) -> str:
        """
        Convert the request to a JSON string.
        
        Args:
            indent: Optional indentation for pretty-printing
            
        Returns:
            JSON string representation of the request
        """
        return json.dumps(self.to_dict(), indent=indent)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DecoratedRequest':
        """
        Create a request from a dictionary.
        
        Args:
            data: Dictionary representation of a request
            
        Returns:
            New request instance
            
        Raises:
            ValueError: If the data is invalid
        """
        if "prompt" not in data:
            raise ValueError("Missing required field 'prompt'")
        
        # Deserialize decorators from the dictionary
        # In a production implementation, we would import all available decorator classes
        # or use a decorator registry to dynamically load the correct classes
        from ..decorators import Reasoning, OutputFormat
        
        decorator_classes = {
            "Reasoning": Reasoning,
            "OutputFormat": OutputFormat,
            # Add more decorator classes as they become available
        }
        
        decorators = []
        for decorator_data in data.get("decorators", []):
            if "name" not in decorator_data:
                raise ValueError("Decorator missing 'name' field")
            
            decorator_name = decorator_data["name"]
            if decorator_name in decorator_classes:
                # Create a decorator instance of the appropriate class
                decorators.append(
                    decorator_classes[decorator_name].from_dict(decorator_data)
                )
            else:
                raise ValueError(f"Unknown decorator type: {decorator_name}")
        
        return cls(
            prompt=data["prompt"],
            decorators=decorators,
            model=data.get("model"),
            api_params=data.get("api_params", {})
        )
    
    @classmethod
    def from_json(cls, json_str: str) -> 'DecoratedRequest':
        """
        Create a request from a JSON string.
        
        Args:
            json_str: JSON string representation of a request
            
        Returns:
            New request instance
            
        Raises:
            ValueError: If the JSON is invalid
            json.JSONDecodeError: If the JSON is malformed
        """
        data = json.loads(json_str)
        return cls.from_dict(data)
    
    def add_decorator(self, decorator: BaseDecorator) -> 'DecoratedRequest':
        """
        Add a decorator to the request.
        
        Args:
            decorator: Decorator to add
            
        Returns:
            Self for method chaining
            
        Raises:
            ValueError: If adding the decorator would create incompatibility
        """
        # Check for duplicates
        if any(d.name == decorator.name for d in self.decorators):
            raise ValueError(f"Duplicate decorator: {decorator.name}")
        
        # Add the decorator
        self.decorators.append(decorator)
        
        # Re-validate compatibility
        self._validate_decorators()
        
        return self
    
    def get_decorator(self, decorator_name: str) -> Optional[BaseDecorator]:
        """
        Get a decorator by name.
        
        Args:
            decorator_name: Name of the decorator to find
            
        Returns:
            The decorator if found, None otherwise
        """
        for decorator in self.decorators:
            if decorator.name == decorator_name:
                return decorator
        return None
    
    def remove_decorator(self, decorator_name: str) -> bool:
        """
        Remove a decorator by name.
        
        Args:
            decorator_name: Name of the decorator to remove
            
        Returns:
            True if a decorator was removed, False otherwise
        """
        initial_count = len(self.decorators)
        self.decorators = [d for d in self.decorators if d.name != decorator_name]
        return len(self.decorators) < initial_count
    
    def apply_decorators(self) -> str:
        """
        Apply all decorators to the prompt.
        
        Returns:
            The decorated prompt text
        """
        # Apply each decorator to the prompt in sequence
        decorated_prompt = self.prompt
        
        for decorator in self.decorators:
            decorated_prompt = decorator.apply(decorated_prompt)
        
        return decorated_prompt
    
    def __str__(self) -> str:
        """
        Get string representation of the request.
        
        Returns:
            String representation
        """
        decorator_str = ', '.join(str(d) for d in self.decorators)
        return f"DecoratedRequest(prompt='{self.prompt[:50]}...', decorators=[{decorator_str}])" 