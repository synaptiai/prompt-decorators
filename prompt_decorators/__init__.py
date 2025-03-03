"""Prompt Decorators Framework.

A Python framework for defining, managing, and applying prompt decorators to enhance interactions with Large Language Models (LLMs).
"""

__version__ = "0.1.0"

from prompt_decorators.core import BaseDecorator
from prompt_decorators.utils import DecoratorRegistry

__all__ = ["BaseDecorator", "DecoratorRegistry"]
