# Generated file - DO NOT EDIT BY HAND

import pytest
from prompt_decorators.decorators import *


@pytest.fixture
def decorator_registry():
    """Fixture providing access to all registered decorators."""
    from prompt_decorators.core.registry import get_registry
    return get_registry()
