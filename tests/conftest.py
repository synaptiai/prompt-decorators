"""Custom fixtures for prompt-decorators tests.

This file supplements the auto-generated fixtures in tests/auto/conftest.py.
"""

import importlib
import sys
from typing import Callable, Type

import pytest

from prompt_decorators.core.base import BaseDecorator


@pytest.fixture
def load_decorator() -> Callable[[str], Type[BaseDecorator]]:
    """Load a decorator class by name.

    Args:
        name: The name of the decorator class to load

    Returns:
        The decorator class
    """

    def _load(name: str) -> Type[BaseDecorator]:
        # First try to import from the generated module
        try:
            module = importlib.import_module(
                f"prompt_decorators.decorators.generated.decorators.{name.lower()}"
            )
            return getattr(module, name)
        except (ImportError, AttributeError):
            pass

        # Then try from the main decorators package
        try:
            # Import the decorators module and check for the class
            import prompt_decorators.decorators as decorators_module

            if hasattr(decorators_module, name):
                return getattr(decorators_module, name)
        except (ImportError, AttributeError):
            pass

        # As a last resort, try to find the decorator class in any loaded module
        for module_name, module in sys.modules.items():
            if module_name.startswith("prompt_decorators"):
                try:
                    decorator_class = getattr(module, name, None)
                    if decorator_class and issubclass(decorator_class, BaseDecorator):
                        return decorator_class
                except (AttributeError, TypeError):
                    pass

        raise ValueError(f"Could not find decorator class: {name}")

    return _load


@pytest.fixture
def sample_prompt() -> str:
    """Provide a sample prompt for testing decorator application.

    Returns:
        A sample prompt string
    """
    return "Write a function to calculate the Fibonacci sequence."
