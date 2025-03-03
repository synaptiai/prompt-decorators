"""Implementation of the StressTest decorator.

This module provides the StressTest decorator class for use in prompt engineering.

Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    StressTestSeverityEnum,
)


class StressTest(BaseDecorator):
    """Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances.

    Attributes:
        scenarios: Number of stress test scenarios to apply. (Any)
        severity: The intensity level of the stress conditions. (Literal["moderate", "severe", "extreme"])
        domain: Optional specific domain or dimension to stress test (e.g., financial, ethical, scalability). (str)
    """

    decorator_name = "stress_test"
    version = "1.0.0"  # Initial version

    @property
    def name(self) -> str:
        """Get the name of the decorator.

        Returns:
            The name of the decorator

        """
        return self.decorator_name

    def __init__(
        self,
        scenarios: Any = 3,
        severity: Literal["moderate", "severe", "extreme"] = "severe",
        domain: str = None,
    ) -> None:
        """Initialize the StressTest decorator.

        Args:
            scenarios: Number of stress test scenarios to apply
            severity: The intensity level of the stress conditions
            domain: Optional specific domain or dimension to stress test (e.g., financial, ethical, scalability)

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._scenarios = scenarios
        self._severity = severity
        self._domain = domain

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._scenarios = scenarios
        self._severity = severity
        self._domain = domain

        # Validate parameters
        if self._scenarios is not None:
            if not isinstance(self._scenarios, (int, float)):
                raise ValidationError(
                    "The parameter 'scenarios' must be a numeric type value."
                )
            if self._scenarios < 1:
                raise ValidationError(
                    "The parameter 'scenarios' must be greater than or equal to 1."
                )
            if self._scenarios > 5:
                raise ValidationError(
                    "The parameter 'scenarios' must be less than or equal to 5."
                )
        if self._severity is not None:
            if not isinstance(self._severity, str):
                raise ValidationError(
                    "The parameter 'severity' must be a string type value."
                )
            if self._severity not in ["moderate", "severe", "extreme"]:
                raise ValidationError(
                    f"The parameter 'severity' must be one of the allowed enum values: ['moderate', 'severe', 'extreme']. Got {self._severity}"
                )
        if self._domain is not None:
            if not isinstance(self._domain, str):
                raise ValidationError(
                    "The parameter 'domain' must be a string type value."
                )

    @property
    def scenarios(self) -> Any:
        """Get the scenarios parameter value.

        Args:
            self: The decorator instance

        Returns:
            The scenarios parameter value
        """
        return self._scenarios

    @property
    def severity(self) -> Literal["moderate", "severe", "extreme"]:
        """Get the severity parameter value.

        Args:
            self: The decorator instance

        Returns:
            The severity parameter value
        """
        return self._severity

    @property
    def domain(self) -> str:
        """Get the domain parameter value.

        Args:
            self: The decorator instance

        Returns:
            The domain parameter value
        """
        return self._domain

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "stress_test",
            "parameters": {
                "scenarios": self.scenarios,
                "severity": self.severity,
                "domain": self.domain,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.scenarios is not None:
            params.append(f"scenarios={self.scenarios}")
        if self.severity is not None:
            params.append(f"severity={self.severity}")
        if self.domain is not None:
            params.append(f"domain={self.domain}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"

    def apply(self, prompt: str) -> str:
        """Apply the decorator to a prompt string.

        Args:
            prompt: The prompt to apply the decorator to


        Returns:
            The modified prompt

        """
        # Subclasses should override this method with specific behavior
        return prompt

    @classmethod
    def is_compatible_with_version(cls, version: str) -> bool:
        """Check if the decorator is compatible with a specific version.

        Args:
            version: The version to check compatibility with.


        Returns:
            True if compatible, False otherwise.


        Raises:
            IncompatibleVersionError: If the version is incompatible.

        """
        # Check version compatibility
        if version > cls.version:
            raise IncompatibleVersionError(
                f"Version {version} is not compatible with {cls.__name__}. "
                f"Maximum compatible version is {cls.version}."
            )
        # For testing purposes, also raise for very old versions
        if version < "0.1.0":
            raise IncompatibleVersionError(
                f"Version {version} is too old for {cls.__name__}. "
                f"Minimum compatible version is 0.1.0."
            )
        return True

    @classmethod
    def get_metadata(cls) -> Dict[str, Any]:
        """Get metadata about the decorator.

        Returns:
            Dictionary containing metadata about the decorator

        """
        return {
            "name": cls.__name__,
            "description": """Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances.""",
            "category": "general",
            "version": cls.version,
        }
