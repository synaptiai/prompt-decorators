"""
Context Decorator

A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import ContextScopeEnum, ContextLevelEnum


class Context(BaseDecorator):
    """A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements."""

    def __init__(
        self,
        domain: str,
        scope: Optional[ContextScopeEnum] = ContextScopeEnum.ALL,
        level: Optional[ContextLevelEnum] = ContextLevelEnum.MIXED,
    ):
        """
        Initialize Context decorator.

        Args:
            domain: The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education')
            scope: Which aspects of decorators to contextualize
            level: The expertise level to target within the domain
        """
        super().__init__(
            name="Context",
            version="1.0.0",
            parameters={
                "domain": domain,
                "scope": scope,
                "level": level,
            },
            metadata={
                "description": "A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.",
                "author": "Prompt Decorators Working Group",
                "category": "meta",
            },
        )

    @property
    def domain(self) -> str:
        """The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education')"""
        return self.parameters.get("domain")

    @property
    def scope(self) -> ContextScopeEnum:
        """Which aspects of decorators to contextualize"""
        return self.parameters.get("scope")

    @property
    def level(self) -> ContextLevelEnum:
        """The expertise level to target within the domain"""
        return self.parameters.get("level")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: A meta-decorator that adapts standard decorators for domain-specific contexts
        instruction = f"Instructions for {self.name} decorator: "
        if self.domain is not None:
            instruction += f"domain={self.domain}, "
        if self.scope is not None:
            instruction += f"scope={self.scope}, "
        if self.level is not None:
            instruction += f"level={self.level}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"