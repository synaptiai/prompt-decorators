"""Implementation of the Prioritize decorator.

This module provides the Prioritize decorator class for use in prompt engineering.

Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Prioritize(BaseDecorator):
    """Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.

    Attributes:
        criteria: The specific criterion to use for prioritization (e.g., importance, urgency, ROI). (str)
        count: Number of prioritized items to include. (Any)
        showRationale: Whether to explain the reasoning behind each priority ranking. (bool)
    """

    name = "prioritize"  # Class-level name for serialization
    decorator_name = "prioritize"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please prioritize the information in your response by ranking it"
        "according to specific criteria. Organize the content hierarchically"
        "from most to least critical, clearly distinguishing different levels"
        "of priority.",
        "parameterMapping": {
            "criteria": {
                "format": "Rank the information based specifically on {value}, with the highest {value} items appearing first and lowest appearing last.",
            },
            "count": {
                "format": "Include exactly {value} prioritized items in your response, focusing on those with the highest priority according to the specified criteria.",
            },
            "showRationale": {
                "valueMap": {
                    "true": "For each prioritized item, provide a clear explanation of the reasoning behind its ranking position.",
                    "false": "Focus on presenting the prioritized items in order without explaining the rationale for each ranking position.",
                },
            },
        },
        "placement": "prepend",
        "compositionBehavior": "accumulate",
    }

    @property
    def name(self) -> str:
        """Get the name of the decorator.

        Args:
            self: The decorator instance


        Returns:
            The name of the decorator

        """
        return self.decorator_name

    def __init__(
        self,
        criteria: str = "importance",
        count: Any = 5,
        showRationale: bool = False,
    ) -> None:
        """Initialize the Prioritize decorator.

        Args:
            criteria: The specific criterion to use for prioritization (e.g., importance, urgency, ROI)
            count: Number of prioritized items to include
            showRationale: Whether to explain the reasoning behind each priority ranking


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._criteria = criteria
        self._count = count
        self._showRationale = showRationale

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._criteria = criteria
        self._count = count
        self._showRationale = showRationale

        # Validate parameters
        if self._criteria is not None:
            if not isinstance(self._criteria, str):
                raise ValidationError(
                    "The parameter 'criteria' must be a string type value."
                )
        if self._count is not None:
            if not isinstance(self._count, (int, float)):
                raise ValidationError(
                    "The parameter 'count' must be a numeric type value."
                )
            if self._count < 1:
                raise ValidationError(
                    "The parameter 'count' must be greater than or equal to 1."
                )
            if self._count > 10:
                raise ValidationError(
                    "The parameter 'count' must be less than or equal to 10."
                )
        if self._showRationale is not None:
            if not isinstance(self._showRationale, bool):
                raise ValidationError(
                    "The parameter 'showRationale' must be a boolean type value."
                )

    @property
    def criteria(self) -> str:
        """Get the criteria parameter value.

        Args:
            self: The decorator instance

        Returns:
            The criteria parameter value
        """
        return self._criteria

    @property
    def count(self) -> Any:
        """Get the count parameter value.

        Args:
            self: The decorator instance

        Returns:
            The count parameter value
        """
        return self._count

    @property
    def showRationale(self) -> bool:
        """Get the showRationale parameter value.

        Args:
            self: The decorator instance

        Returns:
            The showRationale parameter value
        """
        return self._showRationale

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "prioritize",
            "parameters": {
                "criteria": self.criteria,
                "count": self.count,
                "showRationale": self.showRationale,
            },
        }

    def to_string(self) -> str:
        """Convert the decorator to a string.

        Args:
            self: The decorator instance

        Returns:
            String representation of the decorator
        """
        params = []
        if self.criteria is not None:
            params.append(f"criteria={self.criteria}")
        if self.count is not None:
            params.append(f"count={self.count}")
        if self.showRationale is not None:
            params.append(f"showRationale={self.showRationale}")

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


        Args:
            cls: The decorator class

        """
        return {
            "name": cls.__name__,
            "description": """Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.""",
            "category": "general",
            "version": cls.version,
        }

    def apply_to_prompt(self, prompt: str) -> str:
        """Apply the decorator to a prompt.

        This method transforms the prompt using the transformation template.

        Args:
            prompt: The prompt to decorate

        Returns:
            The decorated prompt

        """
        # Use the apply_to_prompt implementation from BaseDecorator
        return super().apply_to_prompt(prompt)
