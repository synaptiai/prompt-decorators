"""
Base Decorator Class

This module provides the base class for all prompt decorators.
"""

import re
import json
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Optional, Any, Union, Set, Type, TypeVar, Generic, cast, ClassVar, Tuple
from functools import total_ordering


class ValidationError(Exception):
    """Exception raised for parameter validation errors."""
    
    def __init__(self, decorator_name: str, param_name: str, message: str):
        """
        Initialize a validation error.
        
        Args:
            decorator_name: Name of the decorator with the validation error
            param_name: Name of the parameter that failed validation
            message: Error message
        """
        self.decorator_name = decorator_name
        self.param_name = param_name
        super().__init__(f"{decorator_name}.{param_name}: {message}")


class IncompatibleVersionError(Exception):
    """Exception raised for incompatible decorator versions."""
    
    def __init__(self, decorator_name: str, requested_version: str, available_version: str):
        """
        Initialize an incompatible version error.
        
        Args:
            decorator_name: Name of the decorator
            requested_version: Requested version
            available_version: Available version
        """
        self.decorator_name = decorator_name
        self.requested_version = requested_version
        self.available_version = available_version
        super().__init__(
            f"Decorator {decorator_name} version {requested_version} is not compatible with available version {available_version}"
        )


@total_ordering
class Version:
    """Class representing a semantic version."""
    
    def __init__(self, version_str: str):
        """
        Initialize a version from a string.
        
        Args:
            version_str: Semantic version string (e.g., "1.2.3")
            
        Raises:
            ValueError: If the version string is invalid
        """
        # Check if the version string is valid
        pattern = r"^(\d+)\.(\d+)\.(\d+)(?:-([a-zA-Z0-9.-]+))?(?:\+([a-zA-Z0-9.-]+))?$"
        match = re.match(pattern, version_str)
        if not match:
            raise ValueError(f"Invalid semantic version string: {version_str}")
        
        # Extract components
        self.major = int(match.group(1))
        self.minor = int(match.group(2))
        self.patch = int(match.group(3))
        self.prerelease = match.group(4) or ""
        self.build = match.group(5) or ""
        self.version_str = version_str
    
    def is_compatible_with(self, other: 'Version') -> bool:
        """
        Check if this version is compatible with another version.
        
        For compatibility, major versions must match and this version's
        minor and patch must be greater than or equal to the other version's.
        
        Args:
            other: Version to compare with
            
        Returns:
            True if compatible, False otherwise
        """
        if self.major != other.major:
            return False
        
        if self.minor < other.minor:
            return False
        
        if self.minor == other.minor and self.patch < other.patch:
            return False
        
        return True
    
    def __eq__(self, other: object) -> bool:
        """Check if this version is equal to another version."""
        if not isinstance(other, Version):
            return NotImplemented
        
        return (
            self.major == other.major and
            self.minor == other.minor and
            self.patch == other.patch and
            self.prerelease == other.prerelease
        )
    
    def __lt__(self, other: object) -> bool:
        """Check if this version is less than another version."""
        if not isinstance(other, Version):
            return NotImplemented
        
        # Compare major, minor, patch
        if self.major != other.major:
            return self.major < other.major
        if self.minor != other.minor:
            return self.minor < other.minor
        if self.patch != other.patch:
            return self.patch < other.patch
        
        # If all components are equal, check prerelease
        if self.prerelease and not other.prerelease:
            return True  # Prerelease version is less than release version
        if not self.prerelease and other.prerelease:
            return False  # Release version is greater than prerelease version
        
        # Both have prerelease or both don't
        return self.prerelease < other.prerelease
    
    def __str__(self) -> str:
        """Get string representation of the version."""
        return self.version_str


T = TypeVar('T')


class BaseDecorator(ABC):
    """
    Base class for all prompt decorators.
    
    All prompt decorators must inherit from this class and implement the
    apply method.
    """
    
    # Class variables
    name: ClassVar[str] = "BaseDecorator"
    description: ClassVar[str] = ""
    category: ClassVar[str] = "uncategorized"
    version: ClassVar[str] = "1.0.0"
    min_compatible_version: ClassVar[str] = "1.0.0"
    
    @classmethod
    def get_version(cls) -> Version:
        """
        Get the decorator version.
        
        Returns:
            Version object for the decorator
        """
        return Version(cls.version)
    
    @classmethod
    def is_compatible_with_version(cls, version_str: str) -> bool:
        """
        Check if this decorator is compatible with the specified version.
        
        Args:
            version_str: Version string to check compatibility with
            
        Returns:
            True if compatible, False otherwise
        """
        try:
            requested_version = Version(version_str)
            current_version = Version(cls.version)
            min_version = Version(cls.min_compatible_version)
            
            # The requested version must be greater than or equal to the
            # minimum compatible version and less than or equal to the current version
            return (
                requested_version >= min_version and
                current_version >= requested_version
            )
        except ValueError:
            return False
    
    def __init__(
        self,
        name: Optional[str] = None,
        version: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize a decorator.
        
        Args:
            name: Decorator name (defaults to class name)
            version: Decorator version (defaults to class version)
            parameters: Dictionary of parameter values
            metadata: Optional metadata dictionary
        """
        self.name = name or self.__class__.name or self.__class__.__name__
        self.version = version or self.__class__.version
        self.parameters = parameters or {}
        self.metadata = metadata or {}
        
        # Validate version compatibility
        if version and not self.__class__.is_compatible_with_version(version):
            raise IncompatibleVersionError(
                self.name, 
                version, 
                self.__class__.version
            )
        
        # Perform validation
        self.validate()
    
    def validate(self) -> None:
        """
        Validate decorator parameters.
        
        This base implementation does basic type checking.
        Subclasses should override for specific validation.
        
        Raises:
            ValidationError: If any parameter fails validation
        """
        pass
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert decorator to a dictionary representation.
        
        Returns:
            Dictionary representation of the decorator
        """
        return {
            "name": self.name,
            "version": self.version,
            "parameters": self.parameters,
            "metadata": self.metadata
        }
    
    def to_json(self, indent: Optional[int] = None) -> str:
        """
        Convert decorator to a JSON string.
        
        Args:
            indent: Optional indentation for pretty-printing
            
        Returns:
            JSON string representation of the decorator
        """
        return json.dumps(self.to_dict(), indent=indent)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseDecorator':
        """
        Create a decorator from a dictionary.
        
        Args:
            data: Dictionary representation of a decorator
            
        Returns:
            New decorator instance
            
        Raises:
            ValueError: If the data is invalid or incompatible with this class
            IncompatibleVersionError: If the version is incompatible
        """
        name = data.get("name")
        if name and cls.__name__ != name and cls.name != name:
            raise ValueError(f"Expected decorator name {cls.__name__}, got {name}")
        
        version = data.get("version")
        if version and not cls.is_compatible_with_version(version):
            raise IncompatibleVersionError(
                cls.__name__, 
                version, 
                cls.version
            )
        
        return cls(
            name=name,
            version=version,
            parameters=data.get("parameters", {}),
            metadata=data.get("metadata", {})
        )
    
    @classmethod
    def from_json(cls, json_str: str) -> 'BaseDecorator':
        """
        Create a decorator from a JSON string.
        
        Args:
            json_str: JSON string representation of a decorator
            
        Returns:
            New decorator instance
            
        Raises:
            ValueError: If the JSON is invalid or incompatible with this class
            json.JSONDecodeError: If the JSON is malformed
            IncompatibleVersionError: If the version is incompatible
        """
        data = json.loads(json_str)
        return cls.from_dict(data)
    
    def _validate_type(self, param_name: str, expected_type: Type[T], allow_none: bool = False) -> Optional[T]:
        """
        Validate parameter type.
        
        Args:
            param_name: Name of the parameter to validate
            expected_type: Expected parameter type
            allow_none: Whether None is allowed
            
        Returns:
            The parameter value if valid
            
        Raises:
            ValidationError: If the parameter type is invalid
        """
        value = self.parameters.get(param_name)
        
        # Handle None case
        if value is None:
            if allow_none:
                return None
            raise ValidationError(
                self.name, param_name, f"Parameter cannot be None"
            )
        
        # Check if the value is an instance of the expected type
        if not isinstance(value, expected_type):
            # Special handling for enum values
            if issubclass(expected_type, Enum) and isinstance(value, str):
                try:
                    # Try to convert string to enum
                    for member in expected_type:
                        if member.value == value:
                            return cast(T, member)
                    # No matching enum value
                    valid_values = [member.value for member in expected_type]
                    raise ValidationError(
                        self.name, param_name, 
                        f"Invalid value '{value}'. Must be one of: {', '.join(repr(v) for v in valid_values)}"
                    )
                except Exception as e:
                    if isinstance(e, ValidationError):
                        raise
                    raise ValidationError(
                        self.name, param_name, f"Cannot convert '{value}' to {expected_type.__name__}"
                    )
            
            raise ValidationError(
                self.name, param_name, 
                f"Expected {expected_type.__name__}, got {type(value).__name__}"
            )
        
        return cast(T, value)
    
    def _validate_range(
        self, 
        param_name: str, 
        minimum: Optional[Union[int, float]] = None, 
        maximum: Optional[Union[int, float]] = None,
        allow_none: bool = False
    ) -> Optional[Union[int, float]]:
        """
        Validate numeric parameter range.
        
        Args:
            param_name: Name of the parameter to validate
            minimum: Optional minimum value (inclusive)
            maximum: Optional maximum value (inclusive)
            allow_none: Whether None is allowed
            
        Returns:
            The parameter value if valid
            
        Raises:
            ValidationError: If the parameter is out of range
        """
        value = self.parameters.get(param_name)
        
        # Handle None case
        if value is None:
            if allow_none:
                return None
            raise ValidationError(
                self.name, param_name, f"Parameter cannot be None"
            )
        
        # Check type first
        if not isinstance(value, (int, float)):
            raise ValidationError(
                self.name, param_name, f"Expected number, got {type(value).__name__}"
            )
        
        # Check range
        if minimum is not None and value < minimum:
            raise ValidationError(
                self.name, param_name, f"Value {value} is below minimum {minimum}"
            )
        if maximum is not None and value > maximum:
            raise ValidationError(
                self.name, param_name, f"Value {value} is above maximum {maximum}"
            )
        
        return value
    
    def _validate_pattern(
        self, 
        param_name: str, 
        pattern: str,
        allow_none: bool = False
    ) -> Optional[str]:
        """
        Validate string parameter against a regex pattern.
        
        Args:
            param_name: Name of the parameter to validate
            pattern: Regex pattern to match
            allow_none: Whether None is allowed
            
        Returns:
            The parameter value if valid
            
        Raises:
            ValidationError: If the parameter doesn't match the pattern
        """
        value = self.parameters.get(param_name)
        
        # Handle None case
        if value is None:
            if allow_none:
                return None
            raise ValidationError(
                self.name, param_name, f"Parameter cannot be None"
            )
        
        # Check type first
        if not isinstance(value, str):
            raise ValidationError(
                self.name, param_name, f"Expected string, got {type(value).__name__}"
            )
        
        # Check pattern
        if not re.match(pattern, value):
            raise ValidationError(
                self.name, param_name, f"Value '{value}' does not match pattern '{pattern}'"
            )
        
        return value
    
    def _validate_enum(
        self,
        param_name: str,
        enum_class: Type[Enum],
        allow_none: bool = False
    ) -> Optional[Enum]:
        """
        Validate enum parameter.
        
        Args:
            param_name: Name of the parameter to validate
            enum_class: Enum class to validate against
            allow_none: Whether None is allowed
            
        Returns:
            The parameter value if valid
            
        Raises:
            ValidationError: If the parameter is not a valid enum value
        """
        value = self.parameters.get(param_name)
        
        # Handle None case
        if value is None:
            if allow_none:
                return None
            raise ValidationError(
                self.name, param_name, f"Parameter cannot be None"
            )
        
        # If already an enum instance, verify it's the right type
        if isinstance(value, Enum):
            if not isinstance(value, enum_class):
                raise ValidationError(
                    self.name, param_name, 
                    f"Expected {enum_class.__name__}, got {type(value).__name__}"
                )
            return value
        
        # Try to convert string to enum
        if isinstance(value, str):
            for member in enum_class:
                if member.value == value:
                    return member
            
            # No matching enum value
            valid_values = [member.value for member in enum_class]
            raise ValidationError(
                self.name, param_name, 
                f"Invalid value '{value}'. Must be one of: {', '.join(repr(v) for v in valid_values)}"
            )
        
        raise ValidationError(
            self.name, param_name, 
            f"Expected {enum_class.__name__} or string, got {type(value).__name__}"
        )
    
    def _validate_list(
        self,
        param_name: str,
        item_type: Optional[Type[T]] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        allow_none: bool = False
    ) -> Optional[List[T]]:
        """
        Validate list parameter.
        
        Args:
            param_name: Name of the parameter to validate
            item_type: Optional type for list items
            min_length: Optional minimum list length
            max_length: Optional maximum list length
            allow_none: Whether None is allowed
            
        Returns:
            The parameter value if valid
            
        Raises:
            ValidationError: If the parameter is not a valid list
        """
        value = self.parameters.get(param_name)
        
        # Handle None case
        if value is None:
            if allow_none:
                return None
            raise ValidationError(
                self.name, param_name, f"Parameter cannot be None"
            )
        
        # Check type first
        if not isinstance(value, list):
            raise ValidationError(
                self.name, param_name, f"Expected list, got {type(value).__name__}"
            )
        
        # Check length constraints
        if min_length is not None and len(value) < min_length:
            raise ValidationError(
                self.name, param_name, f"List length {len(value)} is below minimum {min_length}"
            )
        if max_length is not None and len(value) > max_length:
            raise ValidationError(
                self.name, param_name, f"List length {len(value)} is above maximum {max_length}"
            )
        
        # Check item types if specified
        if item_type is not None:
            for i, item in enumerate(value):
                if not isinstance(item, item_type):
                    raise ValidationError(
                        self.name, param_name, 
                        f"Item at index {i} has invalid type: expected {item_type.__name__}, got {type(item).__name__}"
                    )
        
        return cast(List[T], value)
    
    @classmethod
    def get_metadata(cls) -> Dict[str, Any]:
        """
        Get metadata about this decorator class.
        
        Returns:
            Dictionary with decorator metadata
        """
        return {
            "name": cls.name or cls.__name__,
            "description": cls.description,
            "category": cls.category,
            "version": cls.version,
            "min_compatible_version": cls.min_compatible_version
        }
        
    def __repr__(self) -> str:
        """
        Get string representation of the decorator.
        
        Returns:
            String representation
        """
        return f"{self.name}(version={self.version}, parameters={self.parameters})"

    @abstractmethod
    def apply(self, prompt: str) -> str:
        """
        Apply the decorator to a prompt.
        
        Args:
            prompt: The original prompt to decorate
            
        Returns:
            The decorated prompt
        """
        raise NotImplementedError("Subclasses must implement apply()") 