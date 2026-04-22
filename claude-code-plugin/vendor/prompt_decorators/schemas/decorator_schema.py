"""Schema definitions for prompt decorators.

This module defines the schema classes used for validating decorator definitions
and parameters.
"""

from typing import Any, Dict, List, Optional, Union


class ParameterSchema:
    """Schema for decorator parameters."""

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
        """Initialize a parameter schema.

        Args:
            name: Name of the parameter
            description: Description of the parameter
            type_: Type of the parameter (string, integer, float, boolean, enum)
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

    def to_dict(self) -> Dict[str, Any]:
        """Convert the schema to a dictionary."""
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
    def from_dict(cls, data: Dict[str, Any]) -> "ParameterSchema":
        """Create a parameter schema from a dictionary."""
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


class DecoratorSchema:
    """Schema for decorator definitions."""

    def __init__(
        self,
        name: str,
        description: str,
        category: str,
        parameters: List[ParameterSchema],
        transform_function: str,
        version: str = "1.0.0",
    ):
        """Initialize a decorator schema.

        Args:
            name: Name of the decorator
            description: Description of the decorator
            category: Category of the decorator
            parameters: List of parameter schemas
            transform_function: JavaScript function for transforming prompts
            version: Version of the decorator
        """
        self.name = name
        self.description = description
        self.category = category
        self.parameters = parameters
        self.transform_function = transform_function
        self.version = version

    def to_dict(self) -> Dict[str, Any]:
        """Convert the schema to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "parameters": [param.to_dict() for param in self.parameters],
            "transform_function": self.transform_function,
            "version": self.version,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DecoratorSchema":
        """Create a decorator schema from a dictionary."""
        parameters = [
            ParameterSchema.from_dict(param) for param in data.get("parameters", [])
        ]
        return cls(
            name=data["name"],
            description=data["description"],
            category=data.get("category", "General"),
            parameters=parameters,
            transform_function=data["transform_function"],
            version=data.get("version", "1.0.0"),
        )
