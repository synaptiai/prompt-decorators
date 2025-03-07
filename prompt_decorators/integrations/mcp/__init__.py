"""
Model Context Protocol (MCP) integration for Prompt Decorators.

This module provides integration between Prompt Decorators and the Model Context Protocol (MCP),
allowing users to apply decorators through MCP tools.
"""

from typing import Any, Dict, Type

# Re-export functions from mcp_dynamic.py
from prompt_decorators.integrations.mcp_dynamic import (
    MCP_AVAILABLE,
    DecoratorInfo,
    TemplateInfo,
    create_default_templates,
    create_mcp_server,
)

# For backward compatibility
DecoratorTemplate = TemplateInfo


# For backward compatibility
def load_decorator_classes() -> Dict[str, Type[Any]]:
    """
    Dummy function for backward compatibility.

    This function is no longer used in the dynamic decorator implementation.
    It's provided here for backward compatibility with existing tests.

    Returns:
        An empty dictionary
    """
    from prompt_decorators.core import DecoratorBase

    return {"DummyDecorator": DecoratorBase}


__all__ = [
    "MCP_AVAILABLE",
    "create_mcp_server",
    "create_default_templates",
    "load_decorator_classes",
    "DecoratorInfo",
    "TemplateInfo",
    "DecoratorTemplate",
]
