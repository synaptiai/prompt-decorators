"""Pytest configuration for decorator tests."""

import pytest
import importlib
from typing import Optional, Type

from prompt_decorators.core.base import BaseDecorator

@pytest.fixture
def load_decorator():
    """Fixture to load a decorator class by name."""
    def _load_decorator(decorator_name: str) -> Optional[Type[BaseDecorator]]:
        try:
            module = importlib.import_module(f'prompt_decorators.decorators.generated.decorators.{decorator_name.lower()}')
            return getattr(module, decorator_name)
        except (ImportError, AttributeError):
            return None
    return _load_decorator
