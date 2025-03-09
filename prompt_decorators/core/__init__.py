"""Core components of the prompt decorators system.

This package contains the core components and functionality that power the
prompt decorators system, including the base decorator classes, validation logic,
request handling, and model-specific adaptations.
"""
from prompt_decorators.core.base import (
    DecoratorBase,
    DecoratorParameter,
    Parameter,
    ParameterType,
    ValidationError,
)
from prompt_decorators.core.parser import DecoratorParser
from prompt_decorators.core.registry import DecoratorRegistry

# Add an alias for backward compatibility
BaseDecorator = DecoratorBase

__all__ = [
    "DecoratorBase",
    "BaseDecorator",  # Include the alias in __all__
    "DecoratorParameter",
    "Parameter",
    "ValidationError",
    "ParameterType",
    "DecoratorParser",
    "DecoratorRegistry",
]
