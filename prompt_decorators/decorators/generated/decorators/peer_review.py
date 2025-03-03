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

    @property
    def name(self) -> str:
        """Get the name of the decorator.

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

        """
        return {
            "name": cls.__name__,
            "description": """Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.""",
            "category": "general",
            "version": cls.version,
        }
