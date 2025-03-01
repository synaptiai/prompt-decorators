"""
Extension Decorator

A meta-decorator that enables loading of community-defined decorators from external sources. This facilitates the use of specialized decorator packages, domain-specific extensions, or custom decorator libraries maintained by communities or organizations.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator


class Extension(BaseDecorator):
    """A meta-decorator that enables loading of community-defined decorators from external sources. This facilitates the use of specialized decorator packages, domain-specific extensions, or custom decorator libraries maintained by communities or organizations."""

    def __init__(
        self,
        source: str,
        version: Optional[str] = None,
        decorators: Optional[List[Any]] = None,
    ):
        """
        Initialize Extension decorator.

        Args:
            source: URI or identifier for the extension package (e.g., URL, namespace, or registry identifier)
            version: Specific version of the extension package to use
            decorators: Specific decorators to load from the extension (if empty, loads all decorators from the package)
        """
        super().__init__(
            name="Extension",
            version="1.0.0",
            parameters={
                "source": source,
                "version": version,
                "decorators": decorators,
            },
            metadata={
                "description": "A meta-decorator that enables loading of community-defined decorators from external sources. This facilitates the use of specialized decorator packages, domain-specific extensions, or custom decorator libraries maintained by communities or organizations.",
                "author": "Prompt Decorators Working Group",
                "category": "meta",
            },
        )

    @property
    def source(self) -> str:
        """URI or identifier for the extension package (e.g., URL, namespace, or registry identifier)"""
        return self.parameters.get("source")

    @property
    def version(self) -> str:
        """Specific version of the extension package to use"""
        return self.parameters.get("version")

    @property
    def decorators(self) -> List[Any]:
        """Specific decorators to load from the extension (if empty, loads all decorators from the package)"""
        return self.parameters.get("decorators")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: A meta-decorator that enables loading of community-defined decorators from external sources
        instruction = f"Instructions for {self.name} decorator: "
        if self.source is not None:
            instruction += f"source={self.source}, "
        if self.version is not None:
            instruction += f"version={self.version}, "
        if self.decorators is not None:
            instruction += f"decorators={self.decorators}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"