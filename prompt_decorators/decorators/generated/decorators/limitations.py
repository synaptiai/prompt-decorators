"""Implementation of the Limitations decorator.

This module provides the Limitations decorator class for use in prompt engineering.

Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    LimitationsDetailEnum,
    LimitationsFocusEnum,
    LimitationsPositionEnum,
)


class Limitations(BaseDecorator):
    """Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.

    Attributes:
        detail: The level of detail in the limitations statement. (Literal["brief", "moderate", "comprehensive"])
        position: Where to place the limitations statement in the response. (Literal["beginning", "end"])
        focus: The primary aspect to focus on in the limitations. (Literal["knowledge", "methodology", "context", "biases", "all"])
    """

    name = "limitations"  # Class-level name for serialization
    decorator_name = "limitations"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please include an explicit statement of limitations, caveats, or"
        "uncertainties related to the information in your response.",
        "parameterMapping": {
            "detail": {
                "valueMap": {
                    "brief": "Add a concise, focused statement highlighting only the most critical limitations.",
                    "moderate": "Provide a balanced discussion of several important limitations with some supporting context.",
                    "comprehensive": "Include a thorough examination of all significant limitations with detailed explanations and implications.",
                },
            },
            "position": {
                "valueMap": {
                    "beginning": "Place the limitations statement at the beginning of your response, before presenting the main information.",
                    "end": "Place the limitations statement at the end of your response, after presenting the main information.",
                },
            },
            "focus": {
                "valueMap": {
                    "knowledge": "Focus primarily on limitations related to the current state of knowledge or understanding in this field.",
                    "methodology": "Focus primarily on limitations in the methodology, research approaches, or analytical techniques used in this area.",
                    "context": "Focus primarily on contextual limitations such as time period, geographical scope, or situational constraints.",
                    "biases": "Focus primarily on potential biases, including research biases, sampling biases, or perspective biases.",
                    "all": "Address a balanced mix of limitations across knowledge gaps, methodological issues, contextual constraints, and potential biases.",
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
        detail: Literal["brief", "moderate", "comprehensive"] = "moderate",
        position: Literal["beginning", "end"] = "end",
        focus: Literal["knowledge", "methodology", "context", "biases", "all"] = "all",
    ) -> None:
        """Initialize the Limitations decorator.

        Args:
            detail: The level of detail in the limitations statement
            position: Where to place the limitations statement in the response
            focus: The primary aspect to focus on in the limitations


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._detail = detail
        self._position = position
        self._focus = focus

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._detail = detail
        self._position = position
        self._focus = focus

        # Validate parameters
        if self._detail is not None:
            if not isinstance(self._detail, str):
                raise ValidationError(
                    "The parameter 'detail' must be a string type value."
                )
            if self._detail not in ["brief", "moderate", "comprehensive"]:
                raise ValidationError(
                    f"The parameter 'detail' must be one of the allowed enum values: ['brief', 'moderate', 'comprehensive']. Got {self._detail}"
                )
        if self._position is not None:
            if not isinstance(self._position, str):
                raise ValidationError(
                    "The parameter 'position' must be a string type value."
                )
            if self._position not in ["beginning", "end"]:
                raise ValidationError(
                    f"The parameter 'position' must be one of the allowed enum values: ['beginning', 'end']. Got {self._position}"
                )
        if self._focus is not None:
            if not isinstance(self._focus, str):
                raise ValidationError(
                    "The parameter 'focus' must be a string type value."
                )
            if self._focus not in [
                "knowledge",
                "methodology",
                "context",
                "biases",
                "all",
            ]:
                raise ValidationError(
                    f"The parameter 'focus' must be one of the allowed enum values: ['knowledge', 'methodology', 'context', 'biases', 'all']. Got {self._focus}"
                )

    @property
    def detail(self) -> Literal["brief", "moderate", "comprehensive"]:
        """Get the detail parameter value.

        Args:
            self: The decorator instance

        Returns:
            The detail parameter value
        """
        return self._detail

    @property
    def position(self) -> Literal["beginning", "end"]:
        """Get the position parameter value.

        Args:
            self: The decorator instance

        Returns:
            The position parameter value
        """
        return self._position

    @property
    def focus(self) -> Literal["knowledge", "methodology", "context", "biases", "all"]:
        """Get the focus parameter value.

        Args:
            self: The decorator instance

        Returns:
            The focus parameter value
        """
        return self._focus

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "limitations",
            "parameters": {
                "detail": self.detail,
                "position": self.position,
                "focus": self.focus,
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
        if self.detail is not None:
            params.append(f"detail={self.detail}")
        if self.position is not None:
            params.append(f"position={self.position}")
        if self.focus is not None:
            params.append(f"focus={self.focus}")

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
            "description": """Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.""",
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
