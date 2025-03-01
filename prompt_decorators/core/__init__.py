"""
Core package for prompt decorators.

This package provides the core classes and functionality for the prompt decorators framework.
"""

__version__ = "0.1.0"

from .base import BaseDecorator
from .model_specific import ModelSpecificDecorator, ModelSpecificDecoratorFactory

__all__ = [
    'BaseDecorator',
    'ModelSpecificDecorator',
    'ModelSpecificDecoratorFactory'
] 