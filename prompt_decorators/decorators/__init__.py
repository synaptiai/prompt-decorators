"""
Decorators package for prompt decorators.

This package provides the decorator implementations for the prompt decorators framework.
"""

__all__ = []

__version__ = "0.1.0"

# Import manually implemented decorators
from .reasoning import Reasoning
from .format import OutputFormat

# Import generated decorators
# This will be updated when decorators are generated
try:
    # Try to import all generated decorators
    from .generated.decorators import *
    
    # Get all exported decorators from the generated package
    from .generated.decorators import __all__ as generated_all
    
    # Add to our __all__
    __all__ = [
        # Manually implemented decorators
        'Reasoning',
        'OutputFormat',
    ]
    
    # Extend with generated decorators
    __all__.extend(generated_all)
    
except ImportError:
    # If generated decorators are not available, just export manually implemented ones
    __all__ = [
        'Reasoning',
        'OutputFormat',
    ] 