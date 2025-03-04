"""Finance domain-specific decorators for Prompt Decorators.

This package provides decorators tailored for financial applications,
including risk assessment, financial analysis, and regulatory compliance.
"""

import json
import os

from prompt_decorators.utils.discovery import DecoratorRegistry

from .decorators import FinancialAnalysis, RiskDisclosure


def register_extensions(registry: DecoratorRegistry) -> None:
    """Register finance domain-specific extensions with the decorator registry.

    Args:
        registry: The decorator registry to register with
    """
    # Register decorator classes
    registry.register_decorator(RiskDisclosure)
    registry.register_decorator(FinancialAnalysis)

    # Note: The registry doesn't currently support updating metadata directly
    # The metadata is in registry_extensions/finance_decorators.json for reference

    print(f"Registered finance domain-specific decorators with the registry")
