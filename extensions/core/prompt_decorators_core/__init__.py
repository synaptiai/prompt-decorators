"""
Prompt Decorators Core extension package.

This package provides a Python implementation of the Prompt Decorators Core extension,
which includes decorators for reasoning, step-by-step instructions, output formatting,
tone adjustment, and version specification.
"""

# Version
__version__ = "1.0.0"

# Import decorators
from .decorators import (
    BaseDecorator,
    Reasoning,
    ReasoningDepth,
    StepByStep,
    OutputFormat,
    OutputFormatType,
    Tone,
    ToneStyle,
    Version,
)

# Import API request
from .api import APIRequest

# Import utilities
from .utils import (
    format_parameter_value,
    parse_decorated_prompt,
    generate_system_instructions,
)

# Import CLI
from .cli import main as cli_main

# Define public API
__all__ = [
    # Version
    "__version__",
    
    # Decorators
    "BaseDecorator",
    "Reasoning",
    "ReasoningDepth",
    "StepByStep",
    "OutputFormat",
    "OutputFormatType",
    "Tone",
    "ToneStyle",
    "Version",
    
    # API
    "APIRequest",
    
    # Utilities
    "format_parameter_value",
    "parse_decorated_prompt",
    "generate_system_instructions",
    
    # CLI
    "cli_main",
] 