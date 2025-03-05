"""Implementation of the Steelman decorator.

This module provides the Steelman decorator class for use in prompt engineering.

Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError


class Steelman(BaseDecorator):
    """Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.

    Attributes:
        sides: Number of different viewpoints to steel-man. (Any)
        critique: Whether to include critique after presenting the steel-manned arguments. (bool)
        separation: Whether to clearly separate the steel-manned presentations from any analysis. (bool)
    """

    name = "steelman"  # Class-level name for serialization
    decorator_name = "steelman"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please present the strongest possible version of each position or"
        "argument related to this topic, ensuring each viewpoint is represented"
        "in its most compelling and charitable form, even those you might not"
        "personally agree with.",
        "parameterMapping": {
            "sides": {
                "format": "Present the strongest possible version of {value} different viewpoints or positions on this topic.",
            },
            "critique": {
                "valueMap": {
                    "true": "After presenting each steel-manned position, provide a balanced critique that evaluates its strengths and weaknesses.",
                    "false": "Focus solely on presenting the strongest versions of each position without providing your own critique or evaluation.",
                },
            },
            "separation": {
                "valueMap": {
                    "true": "Clearly separate the presentation of steel-manned arguments from any subsequent analysis or critique using distinct sections.",
                    "false": "Integrate the presentation of steel-manned arguments with any analysis or critique in a more flowing format.",
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
        sides: Any = 2,
        critique: bool = False,
        separation: bool = True,
    ) -> None:
        """Initialize the Steelman decorator.

        Args:
            sides: Number of different viewpoints to steel-man
            critique: Whether to include critique after presenting the steel-manned arguments
            separation: Whether to clearly separate the steel-manned presentations from any analysis


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._sides = sides
        self._critique = critique
        self._separation = separation

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._sides = sides
        self._critique = critique
        self._separation = separation

        # Validate parameters
        if self._sides is not None:
            if not isinstance(self._sides, (int, float)):
                raise ValidationError(
                    "The parameter 'sides' must be a numeric type value."
                )
            if self._sides < 1:
                raise ValidationError(
                    "The parameter 'sides' must be greater than or equal to 1."
                )
            if self._sides > 5:
                raise ValidationError(
                    "The parameter 'sides' must be less than or equal to 5."
                )
        if self._critique is not None:
            if not isinstance(self._critique, bool):
                raise ValidationError(
                    "The parameter 'critique' must be a boolean type value."
                )
        if self._separation is not None:
            if not isinstance(self._separation, bool):
                raise ValidationError(
                    "The parameter 'separation' must be a boolean type value."
                )

    @property
    def sides(self) -> Any:
        """Get the sides parameter value.

        Args:
            self: The decorator instance

        Returns:
            The sides parameter value
        """
        return self._sides

    @property
    def critique(self) -> bool:
        """Get the critique parameter value.

        Args:
            self: The decorator instance

        Returns:
            The critique parameter value
        """
        return self._critique

    @property
    def separation(self) -> bool:
        """Get the separation parameter value.

        Args:
            self: The decorator instance

        Returns:
            The separation parameter value
        """
        return self._separation

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "steelman",
            "parameters": {
                "sides": self.sides,
                "critique": self.critique,
                "separation": self.separation,
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
        if self.sides is not None:
            params.append(f"sides={self.sides}")
        if self.critique is not None:
            params.append(f"critique={self.critique}")
        if self.separation is not None:
            params.append(f"separation={self.separation}")

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
            "description": """Presents the strongest possible version of an argument or position, even those the AI might not agree with. This decorator opposes strawman fallacies by ensuring each viewpoint is represented in its most compelling and charitable form.""",
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
