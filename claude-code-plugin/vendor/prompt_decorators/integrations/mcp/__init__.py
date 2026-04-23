"""Model Context Protocol (MCP) integration for Prompt Decorators.

This module provides integration between Prompt Decorators and the Model Context Protocol (MCP),
allowing users to apply decorators through MCP tools.
"""

import logging
import sys
from typing import Any, Callable, Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger("prompt-decorators-mcp")

# For compatibility with dynamic_decorators_module
from prompt_decorators.dynamic_decorators_module import (
    apply_dynamic_decorators,
    get_available_decorators,
)

# Core exports
from prompt_decorators.integrations.mcp.server import (
    apply_decorators,
    create_decorated_prompt,
    get_decorator_details,
    list_decorators,
    mcp,
    run_server,
)

__all__ = [
    # Core functions
    "mcp",
    "run_server",
    # MCP tools
    "list_decorators",
    "get_decorator_details",
    "apply_decorators",
    "create_decorated_prompt",
    # For backward compatibility
    "get_available_decorators",
    "apply_dynamic_decorators",
]
