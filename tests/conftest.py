"""Pytest configuration for decorator tests."""

import importlib
from typing import Optional, Type

import pytest

from prompt_decorators.core.base import DecoratorBase


@pytest.fixture
def load_decorator():
    """Fixture to load a decorator class by name."""

    def _load_decorator(decorator_name: str) -> Optional[Type[DecoratorBase]]:
        try:
            # First try to load from core decorators
            module = importlib.import_module(
                f"prompt_decorators.decorators.core.{decorator_name.lower()}"
            )
            return getattr(module, decorator_name)
        except (ImportError, AttributeError):
            try:
                # If not found in core, try to load from extension decorators
                module = importlib.import_module(
                    f"prompt_decorators.decorators.extensions.{decorator_name.lower()}"
                )
                return getattr(module, decorator_name)
            except (ImportError, AttributeError):
                return None

    return _load_decorator
