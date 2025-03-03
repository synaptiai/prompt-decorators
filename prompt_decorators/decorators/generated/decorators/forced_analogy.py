"""
Implementation of the ForcedAnalogy decorator.

This module provides the ForcedAnalogy decorator class for use in prompt engineering.

Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.
"""

import re
from typing import Any, Dict, List, Literal, Optional, Union, cast

from prompt_decorators.core.base import BaseDecorator, ValidationError
from prompt_decorators.decorators.generated.decorators.enums import (
    ForcedAnalogyComprehensivenessEnum,
)


class ForcedAnalogy(BaseDecorator):
    """
    Explains concepts by specifically comparing them to a particular
    domain or field. This decorator forces analogies from a specified
    source domain to make complex or unfamiliar topics more relatable and
    understandable.

    Attributes:
        source: The specific domain, field, or context to draw analogies from
        comprehensiveness: How comprehensively to map concepts between domains
        mappings: Number of distinct concept mappings to create between domains
    """

    decorator_name = "forced_analogy"
    version = "1.0.0"  # Initial version

    def __init__(
        self,
        source: str,
        comprehensiveness: Literal["basic", "comprehensive", "detailed"] = "comprehensive",
        mappings: Any = 3,
    ) -> None:
        """
        Initialize the ForcedAnalogy decorator.

        Args:
            source: The specific domain, field, or context to draw analogies
                from
            comprehensiveness: How comprehensively to map concepts between domains
            mappings: Number of distinct concept mappings to create between
                domains

        Returns:
            None
        """
        # Initialize with base values
        super().__init__()

        # Store parameters
        self._source = source
        self._comprehensiveness = comprehensiveness
        self._mappings = mappings

        # Validate parameters
        if self._source is None:
            raise ValidationError("The parameter 'source' is required for ForcedAnalogy decorator.")

        if self._source is not None:
            if not isinstance(self._source, str):
                raise ValidationError("The parameter 'source' must be a string value.")

        if self._comprehensiveness is not None:
            valid_values = ["basic", "comprehensive", "detailed"]
            if self._comprehensiveness not in valid_values:
                raise ValidationError("The parameter 'comprehensiveness' must be one of the following values: " + ", ".join(valid_values))

        if self._mappings is not None:
            if not isinstance(self._mappings, (int, float)) or isinstance(self._mappings, bool):
                raise ValidationError("The parameter 'mappings' must be a numeric value.")


    @property
    def source(self) -> str:
        """
        Get the source parameter value.

        Args:
            self: The decorator instance

        Returns:
            The source parameter value
        """
        return self._source

    @property
    def comprehensiveness(self) -> Literal["basic", "comprehensive", "detailed"]:
        """
        Get the comprehensiveness parameter value.

        Args:
            self: The decorator instance

        Returns:
            The comprehensiveness parameter value
        """
        return self._comprehensiveness

    @property
    def mappings(self) -> Any:
        """
        Get the mappings parameter value.

        Args:
            self: The decorator instance

        Returns:
            The mappings parameter value
        """
        return self._mappings

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the decorator to a dictionary.

        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": "forced_analogy",
            "source": self.source,
            "comprehensiveness": self.comprehensiveness,
            "mappings": self.mappings,
        }

    def to_string(self) -> str:
        """
        Convert the decorator to a string.

        Returns:
            String representation of the decorator
        """
        params = []
        if self.source is not None:
            params.append(f"source={self.source}")
        if self.comprehensiveness is not None:
            params.append(f"comprehensiveness={self.comprehensiveness}")
        if self.mappings is not None:
            params.append(f"mappings={self.mappings}")

        if params:
            return f"@{self.decorator_name}(" + ", ".join(params) + ")"
        else:
            return f"@{self.decorator_name}"