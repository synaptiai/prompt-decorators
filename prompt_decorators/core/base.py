"""Base classes for prompt decorators.

This module provides the base classes and utilities for creating and using
prompt decorators.
"""
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Union

from pydantic import BaseModel, Field


class ValidationError(Exception):
    """Exception raised when decorator validation fails."""

    def __init__(self, message: str, decorator_name: Optional[str] = None):
        """Initialize ValidationError.

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
    """Represents a parameter for a decorator.

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
    min_length: Optional[int] = Field(
        None, description="Minimum length for string or array types"
    )
    max_length: Optional[int] = Field(
        None, description="Maximum length for string or array types"
    )
    pattern: Optional[str] = Field(
        None, description="Regex pattern for string validation"
    )

    def validate_value(self, value: Any) -> Any:
        """Validate a parameter value against the parameter's constraints.

        Args:
            value: The value to validate

        Returns:
            The validated value (possibly converted to the correct type)

        Raises:
            ValidationError: If the value is invalid
        """
        # Handle None for non-required parameters
        if value is None:
            if self.required:
                raise ValidationError(f"Parameter '{self.name}' is required")
            return self.default

        # Type validation
        if self.type == ParameterType.STRING:
            if not isinstance(value, str):
                raise ValidationError(
                    f"Parameter '{self.name}' must be a string, got {type(value).__name__}"
                )
            # Length validation
            if self.min_length is not None and len(value) < self.min_length:
                raise ValidationError(
                    f"Parameter '{self.name}' must be at least {self.min_length} characters"
                )
            if self.max_length is not None and len(value) > self.max_length:
                raise ValidationError(
                    f"Parameter '{self.name}' must be at most {self.max_length} characters"
                )
            # Pattern validation
            if self.pattern is not None:
                import re

                if not re.match(self.pattern, value):
                    raise ValidationError(
                        f"Parameter '{self.name}' must match pattern '{self.pattern}'"
                    )
        elif self.type == ParameterType.INTEGER:
            if not isinstance(value, int) or isinstance(value, bool):
                raise ValidationError(
                    f"Parameter '{self.name}' must be an integer, got {type(value).__name__}"
                )
            # Range validation
            if self.min_value is not None and value < self.min_value:
                raise ValidationError(
                    f"Parameter '{self.name}' must be at least {self.min_value}"
                )
            if self.max_value is not None and value > self.max_value:
                raise ValidationError(
                    f"Parameter '{self.name}' must be at most {self.max_value}"
                )
        # Add validation for other types as needed

        return value


class BaseDecorator:
    """Base class for all prompt decorators.

    This class defines the common interface and behavior for all decorators.
    Subclasses should implement the apply_to_prompt and transform_response methods.
    """

    name: str = "BaseDecorator"
    description: str = "Base decorator class"
    parameters: Dict[str, Parameter] = {}
    conflicts_with: Set[str] = set()

    # Transformation template support
    transformation_template: Dict[str, Any] = {
        "instruction": "",
        "parameterMapping": {},
        "placement": "prepend",
        "compositionBehavior": "accumulate",
    }

    def __init__(self, **kwargs):
        """Initialize a decorator with parameter values.

        Args:
            **kwargs: Parameter values for the decorator

        Raises:
            ValidationError: If any parameter values are invalid
        """
        # Store parameter values
        for name, value in kwargs.items():
            if name in self.parameters:
                # Validate the parameter value
                validated_value = self.parameters[name].validate_value(value)
                setattr(self, f"_{name}", validated_value)
            else:
                raise ValidationError(f"Unknown parameter: {name}", self.name)

        # Set default values for missing parameters
        for name, param in self.parameters.items():
            if name not in kwargs:
                if param.required:
                    raise ValidationError(
                        f"Missing required parameter: {name}", self.name
                    )
                setattr(self, f"_{name}", param.default)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseDecorator":
        """Create a decorator instance from a dictionary representation.

        Args:
            data: Dictionary representation of the decorator

        Returns:
            A new decorator instance

        Raises:
            ValidationError: If the dictionary is invalid
        """
        if "name" not in data:
            raise ValidationError("Missing required field: name")

        decorator_name = data["name"]

        # Get the expected name from the decorator_name class attribute
        # This is more reliable than trying to access the name property on the class
        expected_name = getattr(cls, "decorator_name", cls.__name__.lower())

        if decorator_name != expected_name:
            raise ValidationError(
                f"Expected decorator name '{expected_name}', got '{decorator_name}'"
            )

        # Extract parameter values
        params = {}
        if "parameters" in data:
            parameters = data["parameters"]
            # Handle parameters as a dictionary (name: value)
            if isinstance(parameters, dict):
                for name, value in parameters.items():
                    params[name] = value
            # Handle parameters as a list of dictionaries (name, value)
            elif isinstance(parameters, list):
                for param_data in parameters:
                    if "name" not in param_data or "value" not in param_data:
                        raise ValidationError(
                            "Parameter must have name and value fields"
                        )
                    params[param_data["name"]] = param_data["value"]
            else:
                raise ValidationError("Parameters must be a dictionary or a list")

        # Create the decorator instance
        return cls(**params)

    def apply_to_prompt(self, prompt: str) -> str:
        """Apply the decorator to a prompt.

        This method uses the transformation_template to transform the prompt
        according to the decorator's intended behavior.

        Args:
            prompt: The prompt to decorate

        Returns:
            The decorated prompt
        """
        if not self.transformation_template or not self.transformation_template.get(
            "instruction"
        ):
            # Base implementation if no transformation template is defined
            return prompt

        # Get the base instruction from the template
        instruction = self.transformation_template.get("instruction", "")

        # Apply parameter-specific modifications
        param_mapping = self.transformation_template.get("parameterMapping", {})
        for param_name, mapping in param_mapping.items():
            # Get the parameter value using the property getter
            value = getattr(self, param_name, None)
            if value is not None and "valueMap" in mapping:
                # Convert value to string for lookup
                value_str = str(value).lower()
                if value_str in mapping["valueMap"]:
                    # Append the parameter-specific instruction
                    instruction += f" {mapping['valueMap'][value_str]}"

        # Apply the transformation according to placement strategy
        placement = self.transformation_template.get("placement", "append")
        if placement == "prepend":
            # Instructions before prompt
            return f"{instruction}\n\n{prompt}"
        elif placement == "append":
            # Instructions after prompt
            return f"{prompt}\n\n{instruction}"
        elif placement == "replace":
            return instruction
        elif placement == "wrap":
            # Instructions before and after prompt
            return f"{instruction}\n\n{prompt}\n\n{instruction}"
        else:
            # Default to append if placement strategy is not recognized
            return f"{prompt}\n\n{instruction}"

    def transform_response(self, response: str) -> str:
        """Transform the response from the model.

        Args:
            response: The response to transform

        Returns:
            The transformed response
        """
        # Base implementation does nothing
        return response

    def __str__(self) -> str:
        """Return a string representation of the decorator.

        Returns:
            A string representation
        """
        return f"{self.name}()"
