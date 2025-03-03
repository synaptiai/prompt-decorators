"""
Implementation of the Contrarian decorator.

This module provides the Contrarian decorator class for use in prompt engineering.

Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    ContrarianApproachEnum,
)


class Contrarian(BaseDecorator):
    """
    Generates responses that deliberately challenge conventional wisdom or
    mainstream perspectives. This decorator encourages critical thinking
    by presenting counterarguments, alternative interpretations, or
    challenging established positions on a topic.

    Attributes:
        approach: The specific contrarian approach to take
        maintain: Whether to maintain contrarian stance throughout (true) or provide balanced view at the end (false)
        focus: Optional specific aspect of the topic to focus contrarian analysis on
    """

    decorator_name = "contrarian"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        approach: Literal["outsider", "skeptic", "devil's-advocate"] = "devil's-advocate",
        maintain: bool = False,
        focus: str = None,
    ) -> None:
        """
        Initialize the Contrarian decorator.

        Args:
            approach: The specific contrarian approach to take
            maintain: Whether to maintain contrarian stance throughout (true) or
                provide balanced view at the end (false)
            focus: Optional specific aspect of the topic to focus contrarian
                analysis on

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._approach = approach
        self._maintain = maintain
        self._focus = focus

        # Validate parameters
        if self._approach is not None:
            valid_values = ["outsider", "skeptic", "devil's-advocate"]
            if self._approach not in valid_values:
                raise ValidationError("The parameter 'approach' must be one of the following values: " + ", ".join(valid_values))

        if self._maintain is not None:
            if not isinstance(self._maintain, bool):
                raise ValidationError("The parameter 'maintain' must be a boolean value.")

        if self._focus is not None:
            if not isinstance(self._focus, str):
                raise ValidationError("The parameter 'focus' must be a string value.")


    @property
    def approach(self) -> Literal["outsider", "skeptic", "devil's-advocate"]:
        """
        Get the approach parameter value.

        Args:
            self: The decorator instance

        Returns:
            The approach parameter value
        """
        return self._approach

    @property
    def maintain(self) -> bool:
        """
        Get the maintain parameter value.

        Args:
            self: The decorator instance

        Returns:
            The maintain parameter value
        """
        return self._maintain

    @property
    def focus(self) -> str:
        """
        Get the focus parameter value.

        Args:
            self: The decorator instance

        Returns:
            The focus parameter value
        """
        return self._focus

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "contrarian",
            "approach": self.approach,
            "maintain": self.maintain,
            "focus": self.focus,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.approach is not None:
            params.append(f"approach={self.approach}")
        if self.maintain is not None:
            params.append(f"maintain={self.maintain}")
        if self.focus is not None:
            params.append(f"focus={self.focus}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"