"""
Implementation of the StressTest decorator.

This module provides the StressTest decorator class for use in prompt engineering.

Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances.
"""

from typing import Any, Dict, Literal

from prompt_decorators.core.base import BaseDecorator, ValidationError


class StressTest(BaseDecorator):
    """
    Tests the robustness of ideas, theories, plans, or systems by applying
    extreme conditions, edge cases, and unlikely scenarios. This decorator
    helps identify vulnerabilities, limitations, and breaking points that
    might not be apparent under normal circumstances.

    Attributes:
        scenarios: Number of stress test scenarios to apply
        severity: The intensity level of the stress conditions
        domain: Optional specific domain or dimension to stress test (e.g., financial, ethical, scalability)
    """

    decorator_name = "stress_test"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        scenarios: Any = 3,
        severity: Literal["moderate", "severe", "extreme"] = "severe",
        domain: str = None,
    ) -> None:
        """
        Initialize the StressTest decorator.

        Args:
            scenarios: Number of stress test scenarios to apply
            severity: The intensity level of the stress conditions
            domain: Optional specific domain or dimension to stress test (e.g.,
                financial, ethical, scalability)

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._scenarios = scenarios
        self._severity = severity
        self._domain = domain

        # Validate parameters
        if self._scenarios is not None:
            if not isinstance(self._scenarios, (int, float)) or isinstance(
                self._scenarios, bool
            ):
                raise ValidationError(
                    "The parameter 'scenarios' must be a numeric value."
                )

        if self._severity is not None:
            valid_values = ["moderate", "severe", "extreme"]
            if self._severity not in valid_values:
                raise ValidationError(
                    "The parameter 'severity' must be one of the following values: "
                    + ", ".join(valid_values)
                )

        if self._domain is not None:
            if not isinstance(self._domain, str):
                raise ValidationError("The parameter 'domain' must be a string value.")

    @property
    def scenarios(self) -> Any:
        """
        Get the scenarios parameter value.

        Args:
            self: The decorator instance

        Returns:
            The scenarios parameter value
        """
        return self._scenarios

    @property
    def severity(self) -> Literal["moderate", "severe", "extreme"]:
        """
        Get the severity parameter value.

        Args:
            self: The decorator instance

        Returns:
            The severity parameter value
        """
        return self._severity

    @property
    def domain(self) -> str:
        """
        Get the domain parameter value.

        Args:
            self: The decorator instance

        Returns:
            The domain parameter value
        """
        return self._domain

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "stress_test",
            "scenarios": self.scenarios,
            "severity": self.severity,
            "domain": self.domain,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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
