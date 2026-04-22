"""Schema definitions for prompt decorators.

This package contains schema definitions for validating decorator definitions
and parameters.
"""

from prompt_decorators.schemas.decorator_schema import DecoratorSchema, ParameterSchema

__all__ = [
    "DecoratorSchema",
    "ParameterSchema",
]
