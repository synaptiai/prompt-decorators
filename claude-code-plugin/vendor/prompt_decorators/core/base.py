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


class DecoratorParameter:
    """Represents a parameter for a decorator.

    This class is used by dynamic decorators to define parameters and validate values.
    """

    def __init__(
        self,
        name: str,
        description: str,
        type_: str = "string",
        required: bool = False,
        default: Any = None,
        enum_values: Optional[List[str]] = None,
        min_value: Optional[Union[int, float]] = None,
        max_value: Optional[Union[int, float]] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
    ):
        """Initialize a decorator parameter.

        Args:
            name: The name of the parameter
            description: A description of the parameter
            type_: The type of the parameter (string, integer, float, boolean, enum)
            required: Whether the parameter is required
            default: Default value for the parameter
            enum_values: Possible values for enum type
            min_value: Minimum value for numeric types
            max_value: Maximum value for numeric types
            min_length: Minimum length for string or array types
            max_length: Maximum length for string or array types
            pattern: Regex pattern for string validation
        """
        self.name = name
        self.description = description
        self.type = type_
        self.required = required
        self.default = default
        self.enum_values = enum_values or []
        self.min_value = min_value
        self.max_value = max_value
        self.min_length = min_length
        self.max_length = max_length
        self.pattern = pattern

    def validate(self, value: Any) -> Any:
        """Validate a parameter value against constraints.

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

        # Type validation and conversion
        if self.type == "string":
            if not isinstance(value, str):
                try:
                    value = str(value)
                except:
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

        elif self.type == "integer":
            try:
                value = int(value)
            except (ValueError, TypeError):
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

        elif self.type == "float":
            try:
                value = float(value)
            except (ValueError, TypeError):
                raise ValidationError(
                    f"Parameter '{self.name}' must be a float, got {type(value).__name__}"
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

        elif self.type == "boolean":
            if isinstance(value, str):
                if value.lower() in ("true", "yes", "1"):
                    value = True
                elif value.lower() in ("false", "no", "0"):
                    value = False
                else:
                    raise ValidationError(
                        f"Parameter '{self.name}' must be a boolean, got '{value}'"
                    )
            else:
                try:
                    value = bool(value)
                except (ValueError, TypeError):
                    raise ValidationError(
                        f"Parameter '{self.name}' must be a boolean, got {type(value).__name__}"
                    )

        elif self.type == "enum":
            if not self.enum_values:
                raise ValidationError(
                    f"No enum values defined for parameter '{self.name}'"
                )

            if value not in self.enum_values:
                raise ValidationError(
                    f"Parameter '{self.name}' must be one of {self.enum_values}, got '{value}'"
                )

        return value

    def to_dict(self) -> Dict[str, Any]:
        """Convert the parameter to a dictionary representation."""
        result = {
            "name": self.name,
            "description": self.description,
            "type": self.type,
            "required": self.required,
        }

        if self.default is not None:
            result["default"] = self.default

        if self.enum_values:
            result["enum_values"] = self.enum_values

        if self.min_value is not None:
            result["min_value"] = self.min_value

        if self.max_value is not None:
            result["max_value"] = self.max_value

        if self.min_length is not None:
            result["min_length"] = self.min_length

        if self.max_length is not None:
            result["max_length"] = self.max_length

        if self.pattern is not None:
            result["pattern"] = self.pattern

        return result

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DecoratorParameter":
        """Create a parameter from a dictionary representation."""
        return cls(
            name=data["name"],
            description=data["description"],
            type_=data.get("type", "string"),
            required=data.get("required", False),
            default=data.get("default"),
            enum_values=data.get("enum_values"),
            min_value=data.get("min_value"),
            max_value=data.get("max_value"),
            min_length=data.get("min_length"),
            max_length=data.get("max_length"),
            pattern=data.get("pattern"),
        )


class DecoratorBase:
    """Base class for all prompt decorators.

    This class defines the common interface and behavior for all decorators.
    Subclasses should implement the apply_to_prompt and transform_response methods.
    """

    name: str = "DecoratorBase"
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
    def from_dict(cls, data: Dict[str, Any]) -> "DecoratorBase":
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
            value = getattr(self, f"_{param_name}")
            if value is None:
                # Skip None values
                continue

            # Apply the mapping
            if "valueMapping" in mapping:
                # Apply value mapping if defined
                value_mapping = mapping["valueMapping"]
                if str(value) in value_mapping:
                    instruction = instruction.replace(
                        f"{{{param_name}}}", str(value_mapping[str(value)])
                    )
                else:
                    instruction = instruction.replace(f"{{{param_name}}}", str(value))
            else:
                # Simple replacement
                instruction = instruction.replace(f"{{{param_name}}}", str(value))

        # Apply the instruction to the prompt based on placement
        placement = self.transformation_template.get("placement", "prepend")
        if placement == "prepend":
            return f"{instruction}\n{prompt}"
        elif placement == "append":
            return f"{prompt}\n{instruction}"
        elif placement == "replace":
            return instruction
        else:
            # Default to prepend
            return f"{instruction}\n{prompt}"

    def transform_response(self, response: str) -> str:
        """Transform the LLM response according to the decorator's behavior.

        The base implementation returns the response unchanged. Subclasses
        should override this method if they need to modify the response.

        Args:
            response: The LLM response to transform

        Returns:
            The transformed response
        """
        return response

    def __str__(self) -> str:
        """Return a string representation of the decorator."""
        params = []
        for name in self.parameters:
            value = getattr(self, f"_{name}")
            if value is not None:
                if isinstance(value, str):
                    params.append(f"{name}='{value}'")
                else:
                    params.append(f"{name}={value}")
        return f"{self.name}({', '.join(params)})"

    def __call__(self, prompt: str) -> str:
        """Apply the decorator to a prompt.

        This method is a convenience wrapper around apply_to_prompt.

        Args:
            prompt: The prompt to decorate

        Returns:
            The decorated prompt
        """
        return self.apply_to_prompt(prompt)


# Alias DecoratorBase as BaseDecorator for backward compatibility
BaseDecorator = DecoratorBase
