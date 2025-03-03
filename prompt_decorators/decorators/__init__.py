"""
Decorators package for prompt decorators.

This package provides the decorator implementations for the prompt decorators framework.
"""

__all__ = ["Reasoning"]

__version__ = "0.1.0"

# Import the Reasoning class
from .reasoning import Reasoning

# Import generated decorators
try:
    # Try to import all generated decorators
    # Get all exported decorators from the generated package
    from .generated.decorators import *
    from .generated.decorators import __all__ as generated_all

    # Add to our __all__
    __all__ = ["Reasoning"]

    # Extend with generated decorators
    __all__.extend(generated_all)

except ImportError as e:
    # If generated decorators are not available, report the error
    import logging
    logging.warning(f"Failed to import generated decorators: {e}")
    __all__ = ["Reasoning"]
