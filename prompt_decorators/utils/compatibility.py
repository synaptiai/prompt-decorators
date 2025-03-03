"""Decorator Compatibility Module.

This module provides utilities for checking compatibility between decorators.
"""
import logging
from typing import Any, Dict, List, Optional, Set, Union

from ..core.base import BaseDecorator

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class CompatibilityIssue:
    """Class representing a compatibility issue between decorators."""

    SEVERITY_INFO = "info"
    SEVERITY_WARNING = "warning"
    SEVERITY_ERROR = "error"

    def __init__(
        self,
        message: str,
        decorator1: Union[str, BaseDecorator],
        decorator2: Union[str, BaseDecorator],
        severity: str = SEVERITY_WARNING,
    ):
        """Initialize a compatibility issue.

        Args:
            message: Description of the issue
            decorator1: First decorator involved
            decorator2: Second decorator involved
            severity: Issue severity (info, warning, error)
        """
        self.message = message
        self.decorator1 = (
            decorator1.name if isinstance(decorator1, BaseDecorator) else decorator1
        )
        self.decorator2 = (
            decorator2.name if isinstance(decorator2, BaseDecorator) else decorator2
        )
        self.severity = severity

    def __str__(self) -> str:
        """Get string representation of the issue.

        Returns:
            String representation
        """
        return f"{self.severity.upper()}: {self.message} (between {self.decorator1} and {self.decorator2})"


class CompatibilityChecker:
    """Checker for decorator compatibility."""

    def __init__(self):
        """Initialize a compatibility checker."""
        # Dictionary mapping decorator pairs to compatibility rules
        self._compatibility_rules: Dict[tuple, List[Dict[str, Any]]] = {}

        # Sets of explicitly incompatible decorator pairs
        self._incompatible_pairs: Set[tuple] = set()

    def add_rule(self, decorator1: str, decorator2: str, rule: Dict[str, Any]) -> None:
        """Add a compatibility rule.

        Args:
            decorator1: Name of the first decorator
            decorator2: Name of the second decorator
            rule: Dictionary with rule parameters

        Returns:
            None
        """
        # Ensure consistent ordering of decorator names
        pair = tuple(sorted([decorator1, decorator2]))

        if pair not in self._compatibility_rules:
            self._compatibility_rules[pair] = []

        self._compatibility_rules[pair].append(rule)

        # If this is an incompatibility rule, add to incompatible pairs
        if rule.get("compatible", True) is False:
            self._incompatible_pairs.add(pair)

    def add_incompatible_pair(
        self, decorator1: str, decorator2: str, message: Optional[str] = None
    ) -> None:
        """Add a pair of incompatible decorators.

        Args:
            decorator1: Name of the first decorator
            decorator2: Name of the second decorator
            message: Optional message explaining the incompatibility

        Returns:
            None
        """
        pair = tuple(sorted([decorator1, decorator2]))
        self._incompatible_pairs.add(pair)

        # Add a rule for documentation
        self.add_rule(
            decorator1,
            decorator2,
            {
                "compatible": False,
                "message": message or f"{decorator1} is incompatible with {decorator2}",
                "severity": CompatibilityIssue.SEVERITY_ERROR,
            },
        )

    def check_compatibility(
        self,
        decorator1: Union[str, BaseDecorator],
        decorator2: Union[str, BaseDecorator],
    ) -> List[CompatibilityIssue]:
        """Check compatibility between two decorators.

        Args:
            decorator1: First decorator
            decorator2: Second decorator

        Returns:
            List of compatibility issues (empty if fully compatible)
        """
        # Extract names
        name1 = decorator1.name if isinstance(decorator1, BaseDecorator) else decorator1
        name2 = decorator2.name if isinstance(decorator2, BaseDecorator) else decorator2

        # Ensure consistent ordering
        pair = tuple(sorted([name1, name2]))

        issues = []

        # Check for explicit incompatibility
        if pair in self._incompatible_pairs:
            issues.append(
                CompatibilityIssue(
                    message=f"{name1} is incompatible with {name2}",
                    decorator1=decorator1,
                    decorator2=decorator2,
                    severity=CompatibilityIssue.SEVERITY_ERROR,
                )
            )

        # Check additional rules
        for rule in self._compatibility_rules.get(pair, []):
            if not rule.get("compatible", True):
                issues.append(
                    CompatibilityIssue(
                        message=rule.get(
                            "message", f"{name1} is incompatible with {name2}"
                        ),
                        decorator1=decorator1,
                        decorator2=decorator2,
                        severity=rule.get(
                            "severity", CompatibilityIssue.SEVERITY_ERROR
                        ),
                    )
                )
            elif "condition" in rule:
                # TODO: Implement condition evaluation
                # This would evaluate a condition involving the decorators' parameters
                pass

        return issues

    def check_compatibility_group(
        self, decorators: List[Union[str, BaseDecorator]]
    ) -> List[CompatibilityIssue]:
        """Check compatibility among a group of decorators.

        Args:
            decorators: List of decorators to check

        Returns:
            List of compatibility issues (empty if fully compatible)
        """
        issues = []

        # Check all pairs
        for i in range(len(decorators)):
            for j in range(i + 1, len(decorators)):
                issues.extend(self.check_compatibility(decorators[i], decorators[j]))

        return issues


# Create a global compatibility checker
compatibility_checker = CompatibilityChecker()


# Convenience function to get the global compatibility checker
def get_compatibility_checker() -> CompatibilityChecker:
    """Get the global compatibility checker.

    Returns:
        The global compatibility checker instance
    """
    return compatibility_checker


def setup_core_compatibility_rules() -> None:
    """Set up compatibility rules for core decorators."""
    checker = get_compatibility_checker()

    # Add incompatible pairs
    checker.add_incompatible_pair(
        "Reasoning",
        "Summary",
        "Reasoning and Summary decorators serve opposing purposes - one expands detail while the other condenses it",
    )

    # Add compatibility warnings
    checker.add_rule(
        "Reasoning",
        "OutputFormat",
        {
            "compatible": True,
            "message": "When using Reasoning with OutputFormat, 'markdown' format provides the best readability for step-by-step reasoning",
            "severity": CompatibilityIssue.SEVERITY_INFO,
        },
    )

    checker.add_rule(
        "StepByStep",
        "DetailLevel",
        {
            "compatible": True,
            "message": "StepByStep works best with DetailLevel set to 'detailed' or 'comprehensive'",
            "severity": CompatibilityIssue.SEVERITY_INFO,
        },
    )

    # Add parameter-specific rules (condition logic will be implemented in future updates)
    checker.add_rule(
        "OutputFormat",
        "CodeGeneration",
        {
            "compatible": True,
            "message": "When generating code, OutputFormat should use a format_type compatible with code display (markdown, text)",
            "severity": CompatibilityIssue.SEVERITY_WARNING,
            "condition": "OutputFormat.format_type not in ['markdown', 'text'] and CodeGeneration is present",
        },
    )


# Set up core compatibility rules
setup_core_compatibility_rules()
