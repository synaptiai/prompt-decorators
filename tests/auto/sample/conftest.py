#!/usr/bin/env python
"""
Pytest fixtures for decorator tests.
"""

import pytest
from typing import Dict, Any, Optional, Type
import importlib
import inspect
from pathlib import Path

from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.utils.discovery import DecoratorRegistry

@pytest.fixture
def registry():
    """Fixture for a clean decorator registry"""
    registry = DecoratorRegistry()
    registry.clear()
    return registry

@pytest.fixture
def sample_prompt():
    """Fixture for a sample prompt to test decorators"""
    return "Explain quantum computing in simple terms."

@pytest.fixture
def load_decorator():
    """Fixture for dynamically loading a decorator class"""
    def _load_decorator(decorator_name: str) -> Optional[Type[BaseDecorator]]:
        try:
            module_name = f"prompt_decorators.decorators.generated.decorators.{decorator_name.lower()}"
            module = importlib.import_module(module_name)
            
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and 
                    issubclass(obj, BaseDecorator) and 
                    obj != BaseDecorator and
                    getattr(obj, "name", "") == decorator_name):
                    return obj
            return None
        except ImportError:
            return None
    
    return _load_decorator

@pytest.fixture
def create_decorator():
    """Fixture for creating a decorator instance with parameters"""
    def _create_decorator(decorator_class: Type[BaseDecorator], params: Dict[str, Any]):
        try:
            return decorator_class(**params)
        except Exception as e:
            return None
    
    return _create_decorator
