"""
Implementation of the Reasoning decorator.

This module provides the Reasoning decorator class for use in prompt engineering.
"""

from typing import Any, Dict

from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Reasoning(BaseDecorator):
    """
    A decorator that encourages the model to provide reasoning for its responses.

    This decorator instructs the model to explain its thought process and provide
    justification for its answers.
    """

    decorator_name = "reasoning"
    name = "Reasoning"
    version = "1.0.0"
    min_compatible_version = "0.5.0"
    category = "cognitive"

    def __init__(self, depth: str = "medium") -> None:
        """
        Initialize the Reasoning decorator.

        Args:
            depth: The depth of reasoning to provide (shallow, medium, deep)

        Returns:
            None
        """
        super().__init__()
        self._depth = depth

    @property
    def depth(self) -> str:
        """Get the depth of reasoning."""
        return self._depth

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {"name": self.name, "parameters": {"depth": self.depth}}

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        return f"@{self.decorator_name}(depth={self.depth})"

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.

        Args:
            prompt: The prompt to apply the decorator to

        Returns:
            The modified prompt
        """
        depth_instructions = {
            "shallow": "Briefly explain your reasoning.",
            "medium": "Explain your reasoning step by step.",
            "deep": "Provide detailed reasoning for each step of your thought process.",
        }

        instruction = depth_instructions.get(self.depth, depth_instructions["medium"])
        return f"{prompt}\n\n{instruction}"

    @classmethod
    def is_compatible_with_version(cls, version: str) -> bool:
        """
        Check if the decorator is compatible with a specific version.

        Args:
            version: The version to check compatibility with

        Returns:
            True if compatible, False otherwise

        Raises:
            IncompatibleVersionError: If the version is incompatible
        """
        if version < cls.min_compatible_version:
            raise IncompatibleVersionError(
                f"Version {version} is not compatible with {cls.name}. "
                f"Minimum compatible version is {cls.min_compatible_version}."
            )
        return True

    @classmethod
    def get_metadata(cls) -> Dict[str, Any]:
        """
        Get metadata about the decorator.

        Returns:
            Dictionary containing metadata about the decorator
        """
        return {
            "name": cls.name,
            "description": "A decorator that encourages the model to provide reasoning for its responses.",
            "category": cls.category,
            "version": cls.version,
            "parameters": {
                "depth": {
                    "description": "The depth of reasoning to provide",
                    "type": "string",
                    "enum": ["shallow", "medium", "deep"],
                    "required": False,
                    "default": "medium",
                }
            },
        }
