"""Parameter Validation Module.

This module provides utilities for validating decorator parameters.
"""
import re
from enum import Enum
from typing import Any, Dict, List, Optional, Pattern, Type, TypeVar, Union, cast

from .base import ValidationError

T = TypeVar("T")


class Validator:
    """Base class for parameter validators."""

    def validate(self, decorator_name: str, param_name: str, value: Any) -> Any:
        """Validate a parameter value.

        Args:
            decorator_name: Name of the decorator
            param_name: Name of the parameter
            value: Parameter value to validate

        Returns:
            Validated parameter value (possibly converted)

        Raises:
            ValidationError: If validation fails
        """
        raise NotImplementedError("Subclasses must implement validate()")


class TypeValidator(Validator):
    """Validator for parameter types."""

    def __init__(self, expected_type: Type[T], allow_none: bool = False):
        """Initialize a type validator.

        Args:
            expected_type: Expected type for the parameter
            allow_none: Whether None is allowed
        """
        self.expected_type = expected_type
        self.allow_none = allow_none

    def validate(self, decorator_name: str, param_name: str, value: Any) -> Optional[T]:
        """Validate a parameter value against the expected type.

        Args:
            decorator_name: Name of the decorator
            param_name: Name of the parameter
            value: Parameter value to validate

        Returns:
            Validated parameter value

        Raises:
            ValidationError: If validation fails
        """  # Handle None case
        if value is None:
            if self.allow_none:
                return None
            raise ValidationError(
                decorator_name, param_name, "Parameter cannot be None"
            )

        # Check if the value is an instance of the expected type
        if not isinstance(value, self.expected_type):
            # Special handling for enum values
            if issubclass(self.expected_type, Enum) and isinstance(value, str):
                try:
                    # Try to convert string to enum
                    for member in self.expected_type:
                        if member.value == value:
                            return cast(T, member)
                    # No matching enum value
                    valid_values = [member.value for member in self.expected_type]
                    raise ValidationError(
                        decorator_name,
                        param_name,
                        f"Invalid value '{value}'. Must be one of: {', '.join(repr(v) for v in valid_values)}",
                    )
                except Exception as e:
                    if isinstance(e, ValidationError):
                        raise
                    raise ValidationError(
                        decorator_name,
                        param_name,
                        f"Cannot convert '{value}' to {self.expected_type.__name__}",
                    )

            raise ValidationError(
                decorator_name,
                param_name,
                f"Expected {self.expected_type.__name__}, got {type(value).__name__}",
            )

        return cast(T, value)


class RangeValidator(Validator):
    """Validator for numeric ranges."""

    def __init__(
        self,
        minimum: Optional[Union[int, float]] = None,
        maximum: Optional[Union[int, float]] = None,
        allow_none: bool = False,
    ):
        """Initialize a range validator.

        Args:
            minimum: Optional minimum value (inclusive)
            maximum: Optional maximum value (inclusive)
            allow_none: Whether None is allowed
        """
        self.minimum = minimum
        self.maximum = maximum
        self.allow_none = allow_none

    def validate(
        self, decorator_name: str, param_name: str, value: Any
    ) -> Optional[Union[int, float]]:
        """Validate a numeric parameter value against the range constraints.

        Args:
            decorator_name: Name of the decorator
            param_name: Name of the parameter
            value: Parameter value to validate

        Returns:
            Validated parameter value

        Raises:
            ValidationError: If validation fails
        """
        # Handle None case
        if value is None:
            if self.allow_none:
                return None
            raise ValidationError(
                decorator_name, param_name, "Parameter cannot be None"
            )

        # Check type first
        if not isinstance(value, (int, float)):
            raise ValidationError(
                decorator_name,
                param_name,
                f"Expected number, got {type(value).__name__}",
            )

        # Check range
        if self.minimum is not None and value < self.minimum:
            raise ValidationError(
                decorator_name,
                param_name,
                f"Value {value} is below minimum {self.minimum}",
            )
        if self.maximum is not None and value > self.maximum:
            raise ValidationError(
                decorator_name,
                param_name,
                f"Value {value} is above maximum {self.maximum}",
            )

        return value


class PatternValidator(Validator):
    """Validator for string patterns."""

    def __init__(self, pattern: Union[str, Pattern], allow_none: bool = False):
        """Initialize a pattern validator.

        Args:
            pattern: Regex pattern to match
            allow_none: Whether None is allowed
        """
        self.pattern = re.compile(pattern) if isinstance(pattern, str) else pattern
        self.allow_none = allow_none

    def validate(
        self, decorator_name: str, param_name: str, value: Any
    ) -> Optional[str]:
        """Validate a string parameter value against the pattern.

        Args:
            decorator_name: Name of the decorator
            param_name: Name of the parameter
            value: Parameter value to validate

        Returns:
            Validated parameter value

        Raises:
            ValidationError: If validation fails
        """  # Handle None case
        if value is None:
            if self.allow_none:
                return None
            raise ValidationError(
                decorator_name, param_name, "Parameter cannot be None"
            )

        # Check type first
        if not isinstance(value, str):
            raise ValidationError(
                decorator_name,
                param_name,
                f"Expected string, got {type(value).__name__}",
            )

        # Check pattern
        if not self.pattern.match(value):
            raise ValidationError(
                decorator_name,
                param_name,
                f"Value '{value}' does not match pattern '{self.pattern.pattern}'",
            )

        return value


class EnumValidator(Validator):
    """Validator for enum values."""

    def __init__(self, enum_class: Type[Enum], allow_none: bool = False):
        """Initialize an enum validator.

        Args:
            enum_class: Enum class to validate against
            allow_none: Whether None is allowed
        """
        self.enum_class = enum_class
        self.allow_none = allow_none

    def validate(
        self, decorator_name: str, param_name: str, value: Any
    ) -> Optional[Enum]:
        """Validate an enum parameter value.

        Args:
            decorator_name: Name of the decorator
            param_name: Name of the parameter
            value: Parameter value to validate

        Returns:
            Validated parameter value (as Enum member)

        Raises:
            ValidationError: If validation fails
        """  # Handle None case
        if value is None:
            if self.allow_none:
                return None
            raise ValidationError(
                decorator_name, param_name, "Parameter cannot be None"
            )

        # If already an enum instance, verify it's the right type
        if isinstance(value, Enum):
            if not isinstance(value, self.enum_class):
                raise ValidationError(
                    decorator_name,
                    param_name,
                    f"Expected {self.enum_class.__name__}, got {type(value).__name__}",
                )
            return value

        # Try to convert string to enum
        if isinstance(value, str):
            for member in self.enum_class:
                if member.value == value:
                    return member

            # No matching enum value
            valid_values = [member.value for member in self.enum_class]
            raise ValidationError(
                decorator_name,
                param_name,
                f"Invalid value '{value}'. Must be one of: {', '.join(repr(v) for v in valid_values)}",
            )

        raise ValidationError(
            decorator_name,
            param_name,
            f"Expected {self.enum_class.__name__} or string, got {type(value).__name__}",
        )


class ListValidator(Validator):
    """Validator for list parameters."""

    def __init__(
        self,
        item_validator: Optional[Validator] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        allow_none: bool = False,
    ):
        """Initialize a list validator.

        Args:
            item_validator: Optional validator for list items
            min_length: Optional minimum list length
            max_length: Optional maximum list length
            allow_none: Whether None is allowed
        """
        self.item_validator = item_validator
        self.min_length = min_length
        self.max_length = max_length
        self.allow_none = allow_none

    def validate(
        self, decorator_name: str, param_name: str, value: Any
    ) -> Optional[List[Any]]:
        """Validate a list parameter value.

        Args:
            decorator_name: Name of the decorator
            param_name: Name of the parameter
            value: Parameter value to validate

        Returns:
            Validated parameter value

        Raises:
            ValidationError: If validation fails
        """  # Handle None case
        if value is None:
            if self.allow_none:
                return None
            raise ValidationError(
                decorator_name, param_name, "Parameter cannot be None"
            )

        # Check type first
        if not isinstance(value, list):
            raise ValidationError(
                decorator_name, param_name, f"Expected list, got {type(value).__name__}"
            )

        # Check length constraints
        if self.min_length is not None and len(value) < self.min_length:
            raise ValidationError(
                decorator_name,
                param_name,
                f"List length {len(value)} is below minimum {self.min_length}",
            )
        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(
                decorator_name,
                param_name,
                f"List length {len(value)} is above maximum {self.max_length}",
            )

        # Validate items if item_validator is specified
        if self.item_validator:
            validated_list = []
            for i, item in enumerate(value):
                try:
                    validated_item = self.item_validator.validate(
                        decorator_name, f"{param_name}[{i}]", item
                    )
                    validated_list.append(validated_item)
                except ValidationError as e:
                    # Re-raise with original parameter name
                    raise ValidationError(
                        decorator_name,
                        param_name,
                        f"Item at index {i} is invalid: {e.args[0].split(':', 1)[1].strip()}",
                    )
            return validated_list

        return value


class DictValidator(Validator):
    """Validator for dictionary parameters."""

    def __init__(
        self,
        key_validator: Optional[Validator] = None,
        value_validator: Optional[Validator] = None,
        required_keys: Optional[List[str]] = None,
        allow_extra_keys: bool = True,
        allow_none: bool = False,
    ):
        """Initialize a dictionary validator.

        Args:
            key_validator: Optional validator for dictionary keys
            value_validator: Optional validator for dictionary values
            required_keys: Optional list of required keys
            allow_extra_keys: Whether to allow keys not in required_keys
            allow_none: Whether None is allowed
        """
        self.key_validator = key_validator
        self.value_validator = value_validator
        self.required_keys = required_keys or []
        self.allow_extra_keys = allow_extra_keys
        self.allow_none = allow_none

    def validate(
        self, decorator_name: str, param_name: str, value: Any
    ) -> Optional[Dict[Any, Any]]:
        """Validate a dictionary parameter value.

        Args:
            decorator_name: Name of the decorator
            param_name: Name of the parameter
            value: Parameter value to validate

        Returns:
            Validated parameter value

        Raises:
            ValidationError: If validation fails
        """  # Handle None case
        if value is None:
            if self.allow_none:
                return None
            raise ValidationError(
                decorator_name, param_name, "Parameter cannot be None"
            )

        # Check type first
        if not isinstance(value, dict):
            raise ValidationError(
                decorator_name,
                param_name,
                f"Expected dictionary, got {type(value).__name__}",
            )

        # Check required keys
        for key in self.required_keys:
            if key not in value:
                raise ValidationError(
                    decorator_name, param_name, f"Missing required key '{key}'"
                )

        # Check for disallowed keys
        if not self.allow_extra_keys and self.required_keys:
            for key in value:
                if key not in self.required_keys:
                    raise ValidationError(
                        decorator_name, param_name, f"Extra key '{key}' is not allowed"
                    )

        # Validate keys and values
        validated_dict = {}
        for key, val in value.items():
            # Validate key
            validated_key = key
            if self.key_validator:
                try:
                    validated_key = self.key_validator.validate(
                        decorator_name, f"{param_name} key", key
                    )
                except ValidationError as e:
                    raise ValidationError(
                        decorator_name,
                        param_name,
                        f"Key '{key}' is invalid: {e.args[0].split(':', 1)[1].strip()}",
                    )

            # Validate value
            validated_value = val
            if self.value_validator:
                try:
                    validated_value = self.value_validator.validate(
                        decorator_name, f"{param_name}['{key}']", val
                    )
                except ValidationError as e:
                    raise ValidationError(
                        decorator_name,
                        param_name,
                        f"Value for key '{key}' is invalid: {e.args[0].split(':', 1)[1].strip()}",
                    )

            validated_dict[validated_key] = validated_value

        return validated_dict


class ValidationPipeline:
    """Pipeline for validating multiple parameters."""

    def __init__(self, validators: Dict[str, Validator]):
        """Initialize a validation pipeline.

        Args:
            validators: Dictionary mapping parameter names to validators
        """
        self.validators = validators

    def validate(
        self, decorator_name: str, parameters: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Validate multiple parameters.

        Args:
            decorator_name: Name of the decorator
            parameters: Dictionary of parameter values

        Returns:
            Dictionary of validated parameter values

        Raises:
            ValidationError: If any parameter fails validation
        """
        validated_params = {}

        for param_name, validator in self.validators.items():
            if param_name in parameters:
                validated_params[param_name] = validator.validate(
                    decorator_name, param_name, parameters[param_name]
                )

        return validated_params
