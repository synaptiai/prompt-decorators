"""
Implementation of the Version decorator.

This module provides the Version decorator class for use in prompt engineering.

Specifies the version of the Prompt Decorators standard to use. This decorator must be the first in any sequence when used, ensuring proper interpretation of decorators according to the specified standard version.
"""

import re
from typing import Any, Dict, List, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError


class Version(BaseDecorator):
    """
    Specifies the version of the Prompt Decorators standard to use. This
    decorator must be the first in any sequence when used, ensuring proper
    interpretation of decorators according to the specified standard
    version.

    Attributes:
        standard: The semantic version of the Prompt Decorators standard to use
    """

    decorator_name = "version"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        standard: str,
    ) -> None:
        """
        Initialize the Version decorator.

        Args:
            standard: The semantic version of the Prompt Decorators standard to
                use

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._standard = standard

        # Validate parameters
        if self._standard is None:
            raise ValidationError("The parameter 'standard' is required for Version decorator.")

        if self._standard is not None:
            if not isinstance(self._standard, str):
                raise ValidationError("The parameter 'standard' must be a string value.")
            import re
            if not re.match(r"^\d+\.\d+\.\d+$", self._standard):
                raise ValidationError("The parameter 'standard' value '" + str(self._standard) + "' does not match the required pattern.")


    @property
    def standard(self) -> str:
        """
        Get the standard parameter value.

        Args:
            self: The decorator instance

        Returns:
            The standard parameter value
        """
        return self._standard

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "version",
            "standard": self.standard,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.standard is not None:
            params.append(f"standard={self.standard}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"