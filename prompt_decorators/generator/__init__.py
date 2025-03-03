"""
Generator package for prompt decorators.

This package contains the code generators and registry scanners for prompt decorators.
It allows for automatic generation of decorator code and tests from registry definitions.
"""

from .code_gen import CodeGenerator
from .registry import RegistryScanner
from .test_gen import TestGenerator

__all__ = ["RegistryScanner", "CodeGenerator", "TestGenerator"]

__version__ = "0.1.0"
