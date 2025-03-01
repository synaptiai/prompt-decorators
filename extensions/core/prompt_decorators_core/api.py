"""
API request handling for the Prompt Decorators Core extension package.
"""

import json
from typing import Any, Dict, List, Optional, Union

from .decorators import BaseDecorator
from .utils import parse_decorated_prompt, generate_system_instructions


class APIRequest:
    """
    Class for handling API requests with prompt decorators.
    
    This class provides methods for creating API requests with decorators,
    parsing decorated prompts, and generating system instructions.
    """
    
    def __init__(
        self,
        model: str,
        prompt: str,
        decorators: Optional[List[BaseDecorator]] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ):
        """
        Initialize an API request.
        
        Args:
            model: The model to use for the request.
            prompt: The prompt text.
            decorators: Optional list of decorators to apply.
            temperature: The temperature for the request.
            max_tokens: The maximum number of tokens to generate.
        """
        self.model = model
        self.prompt = prompt
        self.decorators = decorators or []
        self.temperature = temperature
        self.max_tokens = max_tokens
    
    @classmethod
    def from_decorated_prompt(
        cls,
        model: str,
        decorated_prompt: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> "APIRequest":
        """
        Create an API request from a decorated prompt.
        
        Args:
            model: The model to use for the request.
            decorated_prompt: The decorated prompt text.
            temperature: The temperature for the request.
            max_tokens: The maximum number of tokens to generate.
            
        Returns:
            An APIRequest instance.
        """
        decorators_dict, prompt = parse_decorated_prompt(decorated_prompt)
        
        # We're not converting to decorator objects here since we already have the dicts
        return cls(
            model=model,
            prompt=prompt,
            decorators=[],  # Empty list since we'll use decorators_dict directly
            temperature=temperature,
            max_tokens=max_tokens,
            # Store the parsed decorators for later use
        )._with_parsed_decorators(decorators_dict)
    
    def _with_parsed_decorators(self, decorators_dict: List[Dict[str, Any]]) -> "APIRequest":
        """
        Store parsed decorators in the request.
        
        Args:
            decorators_dict: List of decorator dictionaries.
            
        Returns:
            The updated APIRequest instance.
        """
        self._parsed_decorators = decorators_dict
        return self
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the API request to a dictionary.
        
        Returns:
            A dictionary representation of the API request.
        """
        result = {
            "model": self.model,
            "prompt": self.prompt,
            "temperature": self.temperature
        }
        
        if self.max_tokens is not None:
            result["max_tokens"] = self.max_tokens
        
        # Use parsed decorators if available, otherwise convert decorator objects
        if hasattr(self, "_parsed_decorators"):
            result["decorators"] = self._parsed_decorators
        else:
            result["decorators"] = [decorator.to_dict() for decorator in self.decorators]
        
        return result
    
    def to_json(self) -> str:
        """
        Convert the API request to a JSON string.
        
        Returns:
            A JSON string representation of the API request.
        """
        return json.dumps(self.to_dict(), indent=2)
    
    def get_system_instructions(self) -> str:
        """
        Generate system instructions based on the decorators.
        
        Returns:
            A string containing system instructions.
        """
        # Use parsed decorators if available, otherwise convert decorator objects
        if hasattr(self, "_parsed_decorators"):
            return generate_system_instructions(self._parsed_decorators)
        else:
            return generate_system_instructions([decorator.to_dict() for decorator in self.decorators])
    
    def get_decorated_prompt(self) -> str:
        """
        Get the decorated prompt string.
        
        Returns:
            The decorated prompt string.
        """
        decorator_strings = []
        
        # Use decorator objects if available
        if not hasattr(self, "_parsed_decorators"):
            for decorator in self.decorators:
                decorator_strings.append(decorator.to_string())
        else:
            # Use parsed decorators
            from .utils import format_parameter_value
            for decorator in self._parsed_decorators:
                name = decorator["name"]
                params = decorator["parameters"]
                params_str = ", ".join(f"{k}={format_parameter_value(v)}" for k, v in params.items())
                decorator_strings.append(f"+++{name}({params_str})")
        
        return "".join(decorator_strings) + self.prompt 