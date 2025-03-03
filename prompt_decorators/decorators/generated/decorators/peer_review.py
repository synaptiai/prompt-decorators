"""
Implementation of the PeerReview decorator.

This module provides the PeerReview decorator class for use in prompt engineering.

Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    PeerReviewCriteriaEnum,
    PeerReviewStyleEnum,
    PeerReviewPositionEnum,
)


class PeerReview(BaseDecorator):
    """
    Augments the response with a simulated peer review of the content.
    This decorator enhances critical thinking by evaluating the response's
    strengths, weaknesses, methodological soundness, and potential
    improvements as an academic reviewer would.

    Attributes:
        criteria: Primary criteria to focus on in the review
        style: The tone and approach of the peer review
        position: Where to place the peer review relative to the main content
    """

    decorator_name = "peer_review"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        criteria: Literal["accuracy", "methodology", "limitations", "completeness", "all"] = "all",
        style: Literal["constructive", "critical", "balanced"] = "balanced",
        position: Literal["after", "before", "alongside"] = "after",
    ) -> None:
        """
        Initialize the PeerReview decorator.

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
        if self._criteria is not None:
            valid_values = ["accuracy", "methodology", "limitations", "completeness", "all"]
            if self._criteria not in valid_values:
                raise ValidationError("The parameter 'criteria' must be one of the following values: " + ", ".join(valid_values))

        if self._style is not None:
            valid_values = ["constructive", "critical", "balanced"]
            if self._style not in valid_values:
                raise ValidationError("The parameter 'style' must be one of the following values: " + ", ".join(valid_values))

        if self._position is not None:
            valid_values = ["after", "before", "alongside"]
            if self._position not in valid_values:
                raise ValidationError("The parameter 'position' must be one of the following values: " + ", ".join(valid_values))


    @property
    def criteria(self) -> Literal["accuracy", "methodology", "limitations", "completeness", "all"]:
        """
        Get the criteria parameter value.

        Args:
            self: The decorator instance

        Returns:
            The criteria parameter value
        """
        return self._criteria

    @property
    def style(self) -> Literal["constructive", "critical", "balanced"]:
        """
        Get the style parameter value.

        Args:
            self: The decorator instance

        Returns:
            The style parameter value
        """
        return self._style

    @property
    def position(self) -> Literal["after", "before", "alongside"]:
        """
        Get the position parameter value.

        Args:
            self: The decorator instance

        Returns:
            The position parameter value
        """
        return self._position

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "peer_review",
            "criteria": self.criteria,
            "style": self.style,
            "position": self.position,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

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