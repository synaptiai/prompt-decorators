"""Request handling for prompt decorators.

This module provides the DecoratedRequest class for managing decorated prompts.
"""

import json
from typing import Any, Dict, List, Optional, Type, Union

from prompt_decorators.core.base import BaseDecorator


class DecoratedRequest:
    """Class representing a request decorated with prompt decorators."""

    def __init__(
        self,
        prompt: str,
        decorators: Optional[List[BaseDecorator]] = None,
        model: Optional[str] = None,
        api_params: Optional[Dict[str, Any]] = None,
    ):
        """Initialize a decorated request.

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
        """Validate that the decorators are compatible with each other.

        Args:
            self: The request instance

        Returns:
            None

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
        """Convert the request to a dictionary representation.

        Args:
            self: The request instance

        Returns:
            Dictionary representation of the request
        """
        result = {
            "prompt": self.prompt,
            "decorators": [decorator.to_dict() for decorator in self.decorators],
        }

        if self.model:
            result["model"] = self.model

        if self.api_params:
            result["api_params"] = self.api_params

        return result

    def to_json(self, indent: Optional[int] = None) -> str:
        """Convert the request to a JSON string.

        Args:
            indent: Optional indentation for pretty-printing

        Returns:
            JSON string representation of the request
        """
        return json.dumps(self.to_dict(), indent=indent)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DecoratedRequest":
        """Create a request from a dictionary.

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
        from ..decorators import OutputFormat, Reasoning

        decorator_classes = {
            "Reasoning": Reasoning,
            "OutputFormat": OutputFormat,
            # Add more decorator classes as they become available
        }

        decorators = []
        if "decorators" in data:
            for decorator_data in data["decorators"]:
                if "type" not in decorator_data:
                    raise ValueError("Decorator missing 'type' field")

                decorator_type = decorator_data["type"]
                if decorator_type not in decorator_classes:
                    raise ValueError(f"Unknown decorator type: {decorator_type}")

                decorator_class = decorator_classes[decorator_type]
                decorator = decorator_class.from_dict(decorator_data)
                decorators.append(decorator)

        return cls(
            prompt=data["prompt"],
            decorators=decorators,
            model=data.get("model"),
            api_params=data.get("api_params", {}),
        )

    @classmethod
    def from_json(cls, json_str: str) -> "DecoratedRequest":
        """Create a request from a JSON string.

        Args:
            json_str: JSON string representation of a request

        Returns:
            New request instance

        Raises:
            ValueError: If the JSON is invalid
        """
        try:
            data = json.loads(json_str)
            return cls.from_dict(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")

    def add_decorator(self, decorator: BaseDecorator) -> "DecoratedRequest":
        """Add a decorator to the request.

        Args:
            decorator: The decorator to add

        Returns:
            Self for method chaining

        Raises:
            ValueError: If a decorator with the same name already exists
        """
        # Check if a decorator with the same name already exists
        for existing in self.decorators:
            if existing.name == decorator.name:
                raise ValueError(
                    f"Decorator with name '{decorator.name}' already exists"
                )

        self.decorators.append(decorator)
        return self

    def get_decorator(self, decorator_name: str) -> Optional[BaseDecorator]:
        """Get a decorator by name.

        Args:
            decorator_name: Name of the decorator to retrieve

        Returns:
            The decorator if found, None otherwise
        """
        for decorator in self.decorators:
            if decorator.name == decorator_name:
                return decorator
        return None

    def remove_decorator(self, decorator_name: str) -> bool:
        """Remove a decorator by name.

        Args:
            decorator_name: Name of the decorator to remove

        Returns:
            True if the decorator was removed, False if not found
        """
        for i, decorator in enumerate(self.decorators):
            if decorator.name == decorator_name:
                self.decorators.pop(i)
                return True
        return False

    def apply_decorators(self) -> str:
        """Apply all decorators to the prompt.

        Args:
            self: The request instance

        Returns:
            The decorated prompt text

        Note:
            Decorators are applied in the order they were added.
            This allows for composing decorators in a specific sequence.
        """
        decorated_prompt = self.prompt

        for decorator in self.decorators:
            decorated_prompt = decorator.apply_to_prompt(decorated_prompt)

        return decorated_prompt

    def __str__(self) -> str:
        """Get a string representation of the request.

        Returns:
            String representation showing the prompt and decorators
        """
        decorator_str = ", ".join(d.name for d in self.decorators)
        return f"DecoratedRequest(prompt='{self.prompt[:50]}...', decorators=[{decorator_str}])"
