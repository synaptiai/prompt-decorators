"""
StressTest Decorator

Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from ....core.base import BaseDecorator
from .enums import StressTestSeverityEnum


class StressTest(BaseDecorator):
    """Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances."""

    def __init__(
        self,
        scenarios: Optional[float] = 3,
        severity: Optional[StressTestSeverityEnum] = StressTestSeverityEnum.SEVERE,
        domain: Optional[str] = None,
    ):
        """
        Initialize StressTest decorator.

        Args:
            scenarios: Number of stress test scenarios to apply
            severity: The intensity level of the stress conditions
            domain: Optional specific domain or dimension to stress test (e.g., financial, ethical, scalability)
        """
        super().__init__(
            name="StressTest",
            version="1.0.0",
            parameters={
                "scenarios": scenarios,
                "severity": severity,
                "domain": domain,
            },
            metadata={
                "description": "Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances.",
                "author": "Prompt Decorators Working Group",
                "category": "verification",
            },
        )

    @property
    def scenarios(self) -> float:
        """Number of stress test scenarios to apply"""
        return self.parameters.get("scenarios")

    @property
    def severity(self) -> StressTestSeverityEnum:
        """The intensity level of the stress conditions"""
        return self.parameters.get("severity")

    @property
    def domain(self) -> str:
        """Optional specific domain or dimension to stress test (e.g., financial, ethical, scalability)"""
        return self.parameters.get("domain")

    def validate(self) -> None:
        """Validate decorator parameters."""
        super().validate()

        if self.scenarios is not None and self.scenarios < 1:
            raise ValueError(f"scenarios must be at least 1, got {self.scenarios}")
        if self.scenarios is not None and self.scenarios > 5:
            raise ValueError(f"scenarios must be at most 5, got {self.scenarios}")

    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The modified prompt with the decorator applied
        """
        # Apply the decorator: Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios
        instruction = f"Instructions for {self.name} decorator: "
        if self.scenarios is not None:
            instruction += f"scenarios={self.scenarios}, "
        if self.severity is not None:
            instruction += f"severity={self.severity}, "
        if self.domain is not None:
            instruction += f"domain={self.domain}, "
        # Combine with original prompt
        return f"{instruction}\n\n{prompt}"