"""Prompt Decorators - A framework for dynamic prompt modification.

This module provides decorators that can be applied to prompts
to enhance, modify, or transform them before they are sent to LLMs.
"""

import logging
from typing import Any, Dict, List, Optional, Tuple, Union

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import the core elements
from prompt_decorators.core.base import DecoratorBase, DecoratorParameter
from prompt_decorators.core.dynamic_decorator import DynamicDecorator

# Import the dynamic decorators module (replacing the generated decorators)
from prompt_decorators.dynamic_decorators_module import (
    DecoratorDefinition,
    apply_decorator,
    apply_dynamic_decorators,
    create_decorator_class,
    create_decorator_instance,
    extract_decorator_name,
    get_available_decorators,
    load_decorator_definitions,
    parse_decorator_text,
    register_decorator,
)

# Import schemas
from prompt_decorators.schemas.decorator_schema import DecoratorSchema, ParameterSchema

# Import utilities
from prompt_decorators.utils.string_utils import (
    extract_decorators_from_text,
    replace_decorators_in_text,
)

# Version information
__version__ = "0.3.1"

# Public API
__all__ = [
    # Core classes
    "DecoratorBase",
    "DecoratorParameter",
    "DynamicDecorator",
    # Dynamic decorator module functions
    "load_decorator_definitions",
    "get_available_decorators",
    "create_decorator_instance",
    "create_decorator_class",
    "apply_dynamic_decorators",
    "apply_decorator",
    "register_decorator",
    "extract_decorator_name",
    "parse_decorator_text",
    "DecoratorDefinition",
    # Schemas
    "DecoratorSchema",
    "ParameterSchema",
    # Utilities
    "extract_decorators_from_text",
    "replace_decorators_in_text",
]
