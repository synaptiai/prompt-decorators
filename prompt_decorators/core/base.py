"""
Base classes for prompt decorators.

This module contains the foundational classes used throughout the prompt decorators system,
including BaseDecorator, Parameter, and ValidationError.
"""

from enum import Enum
from typing import Any, Dict, List, Optional, Set, Union

from pydantic import BaseModel, Field


class ValidationError(Exception):
    """Exception raised when decorator validation fails."""

    def __init__(self, message: str, decorator_name: Optional[str] = None):
        """
        Initialize ValidationError.

        Args:
            message: The error message
            decorator_name: Optional name of the decorator where validation failed
        """
        prefix = f"[{decorator_name}] " if decorator_name else ""
        super().__init__(f"{prefix}{message}")
        self.decorator_name = decorator_name


class ParameterType(str, Enum):
    """Types of parameters supported in decorators."""

    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    ENUM = "enum"
    ARRAY = "array"
    OBJECT = "object"


class Parameter(BaseModel):
    """
    Represents a parameter for a decorator.

    This class defines the metadata for a parameter, including its name, type,
    description, default value, and constraints.
    """

    name: str = Field(..., description="The name of the parameter")
    type: ParameterType = Field(..., description="The type of the parameter")
    description: str = Field(..., description="Description of the parameter")
    required: bool = Field(False, description="Whether the parameter is required")
    default: Optional[Any] = Field(None, description="Default value for the parameter")
    enum_values: Optional[List[str]] = Field(
        None, description="Possible values for enum type"
    )
    min_value: Optional[Union[int, float]] = Field(
        None, description="Minimum value for numeric types"
    )
    max_value: Optional[Union[int, float]] = Field(
        None, description="Maximum value for numeric types"
    )

    def validate_value(self, value: Any) -> Any:
        """
        Validate that the given value meets the parameter constraints.

        Args:
            value: The value to validate

        Returns:
            The validated value (possibly converted to the correct type)

        Raises:
            ValidationError: If the value is invalid for this parameter
        """
        # Type validation
        if value is None:
            if self.required:
                raise ValidationError(f"Parameter '{self.name}' is required")
            return self.default

        # Type-specific validation
        if self.type == ParameterType.STRING:
            if not isinstance(value, str):
                raise ValidationError(f"Parameter '{self.name}' must be a string")

        elif self.type == ParameterType.INTEGER:
            if not isinstance(value, int) or isinstance(value, bool):
                raise ValidationError(f"Parameter '{self.name}' must be an integer")

            if self.min_value is not None and value < self.min_value:
                raise ValidationError(
                    f"Parameter '{self.name}' must be >= {self.min_value}"
                )

            if self.max_value is not None and value > self.max_value:
                raise ValidationError(
                    f"Parameter '{self.name}' must be <= {self.max_value}"
                )

        elif self.type == ParameterType.FLOAT:
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise ValidationError(f"Parameter '{self.name}' must be a number")

            if self.min_value is not None and value < self.min_value:
                raise ValidationError(
                    f"Parameter '{self.name}' must be >= {self.min_value}"
                )

            if self.max_value is not None and value > self.max_value:
                raise ValidationError(
                    f"Parameter '{self.name}' must be <= {self.max_value}"
                )

        elif self.type == ParameterType.BOOLEAN:
            if not isinstance(value, bool):
                raise ValidationError(f"Parameter '{self.name}' must be a boolean")

        elif self.type == ParameterType.ENUM:
            if not isinstance(value, str):
                raise ValidationError(f"Parameter '{self.name}' must be a string")

            if self.enum_values and value not in self.enum_values:
                raise ValidationError(
                    f"Parameter '{self.name}' must be one of: {', '.join(self.enum_values)}"
                )

        return value


class BaseDecorator:
    """
    Base class for all prompt decorators.

    This class defines the common interface and behavior for all decorators.
    Subclasses should implement the apply_to_prompt and transform_response methods.
    """

    name: str = "BaseDecorator"
    description: str = "Base decorator class"
    parameters: Dict[str, Parameter] = {}
    conflicts_with: Set[str] = set()

    def __init__(self, **kwargs):
        """
        Initialize the decorator with parameter values.

        Args:
            **kwargs: Parameter values for this decorator instance

        Raises:
            ValidationError: If any parameter values are invalid
        """
        self.values = {}

        # Validate and store parameter values
        for name, param in self.parameters.items():
            if name in kwargs:
                value = kwargs.pop(name)
                validated_value = param.validate_value(value)
                self.values[name] = validated_value
            elif param.default is not None:
                self.values[name] = param.default
            elif param.required:
                raise ValidationError(f"Missing required parameter: {name}", self.name)

        # Check for unexpected parameters
        if kwargs:
            raise ValidationError(
                f"Unexpected parameters: {', '.join(kwargs.keys())}", self.name
            )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseDecorator":
        """
        Create a decorator instance from a dictionary representation.

        Args:
            data: Dictionary representation of the decorator

        Returns:
            A new decorator instance

        Raises:
            ValidationError: If the dictionary is invalid
        """
        if "name" not in data:
            raise ValidationError("Missing 'name' field in decorator data")
        
        if "parameters" not in data:
            raise ValidationError("Missing 'parameters' field in decorator data")
            
        return cls(**data.get("parameters", {}))

    def apply_to_prompt(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt string.

        Args:
            prompt: The original prompt string

        Returns:
            The modified prompt string

        Note:
            This method should be overridden by subclasses.
        """
        return prompt

    def transform_response(self, response: str) -> str:
        """
        Transform the response from an LLM.

        Args:
            response: The original response string

        Returns:
            The transformed response string

        Note:
            This method should be overridden by subclasses.
        """
        return response

    def __str__(self) -> str:
        """Return a string representation of the decorator."""
        params = ", ".join(f"{k}={repr(v)}" for k, v in self.values.items())
        return f"{self.name}({params})"
