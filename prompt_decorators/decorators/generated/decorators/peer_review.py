"""Implementation of the PeerReview decorator.

This module provides the PeerReview decorator class for use in prompt engineering.

Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.core.exceptions import IncompatibleVersionError
from prompt_decorators.decorators.generated.decorators.enums import (
    PeerReviewCriteriaEnum,
    PeerReviewPositionEnum,
    PeerReviewStyleEnum,
)


class PeerReview(BaseDecorator):
    """Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.

    Attributes:
        criteria: Primary criteria to focus on in the review. (Literal["accuracy", "methodology", "limitations", "completeness", "all"])
        style: The tone and approach of the peer review. (Literal["constructive", "critical", "balanced"])
        position: Where to place the peer review relative to the main content. (Literal["after", "before", "alongside"])
    """

    name = "peer_review"  # Class-level name for serialization
    decorator_name = "peer_review"
    version = "1.0.0"  # Initial version

    # Transformation template for prompt modification
    transformation_template = {
        "instruction": "Please include a simulated peer review of your response, evaluating"
        "the content as an academic reviewer would.",
        "parameterMapping": {
            "criteria": {
                "valueMap": {
                    "accuracy": "Focus the peer review primarily on the factual accuracy and precision of the information presented.",
                    "methodology": "Focus the peer review primarily on the methodological approach, analytical framework, or reasoning process used.",
                    "limitations": "Focus the peer review primarily on identifying limitations, gaps, or unaddressed aspects in the analysis.",
                    "completeness": "Focus the peer review primarily on how thoroughly the topic is covered and whether key elements are missing.",
                    "all": "Include a comprehensive peer review addressing accuracy, methodology, limitations, and completeness of the content.",
                },
            },
            "style": {
                "valueMap": {
                    "constructive": "Maintain a supportive tone in the peer review, emphasizing positive aspects while gently suggesting improvements.",
                    "critical": "Adopt a rigorously critical stance in the peer review, thoroughly identifying weaknesses and challenging assumptions.",
                    "balanced": "Provide a balanced peer review that equally addresses strengths and weaknesses with a neutral academic tone.",
                },
            },
            "position": {
                "valueMap": {
                    "after": "Present the main content first, followed by the peer review section.",
                    "before": "Begin with the peer review section, then present the main content.",
                    "alongside": "Integrate the peer review comments throughout the content, marking them clearly as reviewer notes.",
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
        criteria: Literal[
            "accuracy", "methodology", "limitations", "completeness", "all"
        ] = "all",
        style: Literal["constructive", "critical", "balanced"] = "balanced",
        position: Literal["after", "before", "alongside"] = "after",
    ) -> None:
        """Initialize the PeerReview decorator.

        Args:
            criteria: Primary criteria to focus on in the review
            style: The tone and approach of the peer review
            position: Where to place the peer review relative to the main content


        Returns:
            None

        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._criteria = criteria
        self._style = style
        self._position = position

        # Validate parameters
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._criteria = criteria
        self._style = style
        self._position = position

        # Validate parameters
        if self._criteria is not None:
            if not isinstance(self._criteria, str):
                raise ValidationError(
                    "The parameter 'criteria' must be a string type value."
                )
            if self._criteria not in [
                "accuracy",
                "methodology",
                "limitations",
                "completeness",
                "all",
            ]:
                raise ValidationError(
                    f"The parameter 'criteria' must be one of the allowed enum values: ['accuracy', 'methodology', 'limitations', 'completeness', 'all']. Got {self._criteria}"
                )
        if self._style is not None:
            if not isinstance(self._style, str):
                raise ValidationError(
                    "The parameter 'style' must be a string type value."
                )
            if self._style not in ["constructive", "critical", "balanced"]:
                raise ValidationError(
                    f"The parameter 'style' must be one of the allowed enum values: ['constructive', 'critical', 'balanced']. Got {self._style}"
                )
        if self._position is not None:
            if not isinstance(self._position, str):
                raise ValidationError(
                    "The parameter 'position' must be a string type value."
                )
            if self._position not in ["after", "before", "alongside"]:
                raise ValidationError(
                    f"The parameter 'position' must be one of the allowed enum values: ['after', 'before', 'alongside']. Got {self._position}"
                )

    @property
    def criteria(
        self,
    ) -> Literal["accuracy", "methodology", "limitations", "completeness", "all"]:
        """Get the criteria parameter value.

        Args:
            self: The decorator instance

        Returns:
            The criteria parameter value
        """
        return self._criteria

    @property
    def style(self) -> Literal["constructive", "critical", "balanced"]:
        """Get the style parameter value.

        Args:
            self: The decorator instance

        Returns:
            The style parameter value
        """
        return self._style

    @property
    def position(self) -> Literal["after", "before", "alongside"]:
        """Get the position parameter value.

        Args:
            self: The decorator instance

        Returns:
            The position parameter value
        """
        return self._position

    def to_dict(self) -> Dict[str, Any]:
        """Convert the decorator to a dictionary.

        Args:
            self: The decorator instance

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "peer_review",
            "parameters": {
                "criteria": self.criteria,
                "style": self.style,
                "position": self.position,
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
        if self.style is not None:
            params.append(f"style={self.style}")
        if self.position is not None:
            params.append(f"position={self.position}")

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
            "description": """Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.""",
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
