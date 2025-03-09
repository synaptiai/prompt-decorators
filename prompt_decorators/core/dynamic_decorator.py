"""Dynamic decorator functionality for prompt transformations.

This module provides a dynamic approach to loading and applying prompt decorators
from registry definitions. Instead of generating individual decorator classes for each
decorator in the registry, this module loads decorator definitions at runtime directly
from the JSON files in the registry.

Typical usage:
    >>> from prompt_decorators.core.dynamic_decorator import DynamicDecorator, transform_prompt
    >>> result = transform_prompt("What is quantum computing?", ["+++StepByStep(numbered=true)"])
    >>> decorated = DynamicDecorator("StepByStep", numbered=True)
    >>> result = decorated("What is quantum computing?")
"""

import json
import logging
import os
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union, cast

from prompt_decorators.schemas.decorator_schema import DecoratorSchema, ParameterSchema

# Constants
DEFAULT_REGISTRY_DIR = "registry"
REGISTRY_ENV_VAR = "DECORATOR_REGISTRY_DIR"
DECORATOR_PREFIX = "+++"
PARAMETER_PATTERN = r'([a-zA-Z0-9_]+)=("(?:[^"\\]|\\.)*"|[^,)]+)'
DECORATOR_PATTERN = (
    r"\+\+\+([A-Za-z][A-Za-z0-9]*(?::v[0-9]+(?:\.[0-9]+(?:\.[0-9]+)?)?)?)"
    r"(?:\(([^)]*)\))?"
)

logger = logging.getLogger(__name__)


class DecoratorParameter:
    """Class representing a validated decorator parameter."""

    def __init__(
        self,
        name: str,
        value: Any,
        param_type: str,
        validation: Optional[Dict[str, Any]] = None,
        enum_values: Optional[List[str]] = None,
    ) -> None:
        """Initialize a decorator parameter.

        Args:
            name: Name of the parameter
            value: Value of the parameter
            param_type: Type of the parameter (string, number, boolean, array, enum)
            validation: Optional validation rules
            enum_values: Optional list of allowed enum values

        Returns:
            None
        """
        self.name = name
        self.value = value
        self.type = param_type
        self.validation = validation or {}
        self.enum_values = enum_values or []

        # Validate the parameter
        self._validate()

    def _validate(self) -> None:
        """Validate the parameter according to its type and validation rules."""
        # Check type
        if self.type == "string" and not isinstance(self.value, str):
            raise ValueError(f"Parameter '{self.name}' must be a string")
        elif self.type == "number" and not isinstance(self.value, (int, float)):
            raise ValueError(f"Parameter '{self.name}' must be a number")
        elif self.type == "boolean" and not isinstance(self.value, bool):
            raise ValueError(f"Parameter '{self.name}' must be a boolean")
        elif self.type == "array" and not isinstance(self.value, list):
            raise ValueError(f"Parameter '{self.name}' must be an array")
        elif self.type == "enum" and self.value not in self.enum_values:
            allowed = ", ".join(f"'{v}'" for v in self.enum_values)
            raise ValueError(f"Parameter '{self.name}' must be one of: {allowed}")

        # Apply validation rules
        if self.type == "string":
            if (
                "minLength" in self.validation
                and len(self.value) < self.validation["minLength"]
            ):
                raise ValueError(
                    f"Parameter '{self.name}' must be at least "
                    f"{self.validation['minLength']} characters"
                )
            if (
                "maxLength" in self.validation
                and len(self.value) > self.validation["maxLength"]
            ):
                raise ValueError(
                    f"Parameter '{self.name}' must be at most "
                    f"{self.validation['maxLength']} characters"
                )
            if "pattern" in self.validation and not re.match(
                self.validation["pattern"], self.value
            ):
                raise ValueError(
                    f"Parameter '{self.name}' doesn't match required pattern"
                )
        elif self.type == "number":
            if "minimum" in self.validation and self.value < self.validation["minimum"]:
                raise ValueError(
                    f"Parameter '{self.name}' must be at least {self.validation['minimum']}"
                )
            if "maximum" in self.validation and self.value > self.validation["maximum"]:
                raise ValueError(
                    f"Parameter '{self.name}' must be at most {self.validation['maximum']}"
                )

    def __str__(self) -> str:
        """Return a string representation of the parameter."""
        if isinstance(self.value, str):
            return f"{self.name}='{self.value}'"
        return f"{self.name}={self.value}"


class DynamicDecorator:
    """Dynamic decorator class for prompt transformations.

    This class provides a dynamic approach to loading and applying prompt decorators
    from registry definitions. Instead of generating individual decorator classes for each
    decorator in the registry, this class loads decorator definitions at runtime directly
    from the JSON files in the registry.
    """

    # Class-level registry of decorator definitions
    _registry: Dict[str, Dict[str, Any]] = {}
    _loaded = False

    def __init__(self, name: str, **kwargs: Any) -> None:
        """Initialize a dynamic decorator.

        Args:
            name: Name of the decorator to load
            **kwargs: Parameters for the decorator

        Raises:
            ValueError: If the decorator is not found in the registry

        Returns:
            None
        """
        # Load the registry if not already loaded
        if not DynamicDecorator._loaded:
            DynamicDecorator.load_registry()

        # Get the decorator definition from the registry
        if name not in DynamicDecorator._registry:
            raise ValueError(f"Decorator '{name}' not found in registry")

        self.name = name
        self.definition = DynamicDecorator._registry[name]
        self.parameters: Dict[str, DecoratorParameter] = {}

        # Set up parameters
        self._validate_parameters(kwargs)

    def _validate_parameters(self, params: Dict[str, Any]) -> None:
        """Validate and store parameters.

        Args:
            params: Parameters to validate

        Raises:
            ValueError: If a required parameter is missing or a parameter is invalid

        Returns:
            None
        """
        # Get parameter definitions from the registry
        param_defs = self.definition.get("parameters", [])

        # Create a dictionary of parameter definitions by name
        param_dict = {p["name"]: p for p in param_defs}

        # Check for required parameters
        for param_name, param_def in param_dict.items():
            if param_def.get("required", False) and param_name not in params:
                raise ValueError(f"Required parameter '{param_name}' is missing")

        # Process provided parameters
        for param_name, param_value in params.items():
            if param_name not in param_dict:
                raise ValueError(f"Unknown parameter '{param_name}'")

            param_def = param_dict[param_name]
            param_type = param_def.get("type", "string")

            # Validate parameter value
            self._validate_parameter_value(param_name, param_value, param_def)

            # Store the parameter
            self.parameters[param_name] = DecoratorParameter(
                name=param_name,
                value=param_value,
                param_type=param_type,
                validation=param_def.get("validation", {}),
                enum_values=param_def.get("enum_values", []),
            )

        # Set default values for missing parameters
        for param_name, param_def in param_dict.items():
            if param_name not in params and "default" in param_def:
                default_value = param_def["default"]
                param_type = param_def.get("type", "string")
                self.parameters[param_name] = DecoratorParameter(
                    name=param_name,
                    value=default_value,
                    param_type=param_type,
                    validation=param_def.get("validation", {}),
                    enum_values=param_def.get("enum_values", []),
                )

    def _validate_parameter_value(
        self, name: str, value: Any, param_def: Dict[str, Any]
    ) -> None:
        """Validate a parameter value against its definition.

        Args:
            name: Name of the parameter
            value: Value to validate
            param_def: Parameter definition

        Raises:
            ValueError: If the parameter value is invalid

        Returns:
            None
        """
        param_type = param_def.get("type", "string")

        # Type validation
        if param_type == "string":
            if not isinstance(value, str):
                raise ValueError(
                    f"Parameter '{name}' must be a string, got {type(value).__name__}"
                )
        elif param_type == "integer":
            if not isinstance(value, int) or isinstance(value, bool):
                raise ValueError(
                    f"Parameter '{name}' must be an integer, got {type(value).__name__}"
                )
        elif param_type == "number":
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise ValueError(
                    f"Parameter '{name}' must be a number, got {type(value).__name__}"
                )
        elif param_type == "boolean":
            if not isinstance(value, bool):
                raise ValueError(
                    f"Parameter '{name}' must be a boolean, got {type(value).__name__}"
                )
        elif param_type == "enum":
            enum_values = param_def.get("enum_values", [])
            if not enum_values:
                raise ValueError(f"No enum values defined for parameter '{name}'")
            if value not in enum_values:
                raise ValueError(
                    f"Parameter '{name}' must be one of {enum_values}, got '{value}'"
                )

        # Additional validation
        validation = param_def.get("validation", {})

        # Check min_value and max_value for numeric types
        if param_type in ("integer", "number"):
            # Check min_value
            min_value = validation.get("min") or param_def.get("min_value")
            if min_value is not None and value < min_value:
                raise ValueError(
                    f"Parameter '{name}' must be at least {min_value}, got {value}"
                )

            # Check max_value
            max_value = validation.get("max") or param_def.get("max_value")
            if max_value is not None and value > max_value:
                raise ValueError(
                    f"Parameter '{name}' must be at most {max_value}, got {value}"
                )

        # Check string validations
        elif param_type == "string":
            min_length = validation.get("min_length") or param_def.get("min_length")
            max_length = validation.get("max_length") or param_def.get("max_length")
            pattern = validation.get("pattern") or param_def.get("pattern")

            if min_length is not None and len(value) < min_length:
                raise ValueError(
                    f"Parameter '{name}' must be at least {min_length} characters, got {len(value)}"
                )
            if max_length is not None and len(value) > max_length:
                raise ValueError(
                    f"Parameter '{name}' must be at most {max_length} characters, got {len(value)}"
                )
            if pattern is not None:
                import re

                if not re.match(pattern, value):
                    raise ValueError(
                        f"Parameter '{name}' must match pattern '{pattern}', got '{value}'"
                    )

    def __call__(self, text_or_func: Union[str, Callable]) -> Union[str, Callable]:
        """Apply the decorator to a text or function.

        Args:
            text_or_func: Text to transform or function to decorate

        Returns:
            Transformed text or decorated function
        """
        # If text_or_func is a function, return a wrapper function
        if callable(text_or_func):
            # Define a wrapper function that applies the decorator to the result of the original function
            def wrapper(*args: Any, **kwargs: Any) -> str:
                """Apply the decorator to the result of the decorated function.

                This wrapper function captures the result of the original function
                and applies the decorator's transformation to it.

                Args:
                    *args: Positional arguments to pass to the original function.
                    **kwargs: Keyword arguments to pass to the original function.

                Returns:
                    str: The transformed result after applying the decorator.
                """
                result = text_or_func(*args, **kwargs)
                return self.apply(result)

            # Return the wrapper function
            return wrapper

        # Otherwise, apply the decorator to the text
        return self.apply(text_or_func)

    def apply(self, text: str) -> str:
        """Apply the decorator to a text.

        Args:
            text: Text to transform

        Returns:
            Transformed text
        """
        # Get the transform function from the definition
        transform_function = self.definition.get("transform_function", "")
        if not transform_function:
            return text

        # Create a JavaScript-like environment for the transform function
        # This is a simplified approach and may not handle all JS features
        js_env = {
            "text": text,
            "console": {"log": print},
            "return": None,
        }

        # Add parameters to the environment
        for name, param in self.parameters.items():
            js_env[name] = param.value

        # Execute the transform function
        try:
            # Add a return statement if not present
            if "return" not in transform_function:
                transform_function = f"return {transform_function}"

            # Create a Python function from the JavaScript-like code
            transform_code = f"def transform(text, **kwargs):\n"
            for line in transform_function.split("\n"):
                transform_code += f"    {line}\n"

            # Compile and execute the function
            namespace: Dict[str, Any] = {}
            exec(transform_code, namespace)
            # Use a more generic type annotation that allows for kwargs
            transform = namespace["transform"]  # type: ignore

            # Call the function with the text and parameters as kwargs
            param_dict = {k: v.value for k, v in self.parameters.items()}
            result = transform(text, **param_dict)

            # Ensure the result is a string
            if not isinstance(result, str):
                result = str(result)

            return cast(str, result)
        except Exception as e:
            logger.error(f"Error applying decorator '{self.name}': {e}")
            return text

    def __str__(self) -> str:
        """Return a string representation of the decorator."""
        params_str = ", ".join(str(p) for p in self.parameters.values())
        return f"{self.name}({params_str})"

    @classmethod
    def load_registry(cls) -> None:
        """Load decorator definitions from the registry directory.

        This method scans the registry directory for JSON files containing
        decorator definitions and loads them into the class-level registry.

        Args:
            cls: The class object

        Returns:
            None
        """
        # Get the registry directory from environment variable or use default
        registry_dir_str = os.environ.get(REGISTRY_ENV_VAR, DEFAULT_REGISTRY_DIR)

        # Determine the absolute path to the registry directory
        if not os.path.isabs(registry_dir_str):
            # Try to find the registry relative to the current directory
            if os.path.exists(registry_dir_str):
                registry_dir_str = os.path.abspath(registry_dir_str)
            else:
                # Try to find the registry relative to the module directory
                module_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                registry_path_str = os.path.join(module_dir, registry_dir_str)
                if os.path.exists(registry_path_str):
                    registry_dir_str = registry_path_str
                else:
                    # Try one level up
                    parent_dir = os.path.dirname(module_dir)
                    registry_path_str = os.path.join(parent_dir, registry_dir_str)
                    if os.path.exists(registry_path_str):
                        registry_dir_str = registry_path_str

        logger.debug(f"Loading registry from {registry_dir_str}")

        # Clear the registry
        cls._registry.clear()

        # Check if the registry directory exists
        if not os.path.exists(registry_dir_str):
            logger.warning(f"Registry directory not found: {registry_dir_str}")
            cls._loaded = True
            return

        # Scan the registry directory for JSON files
        registry_path = Path(registry_dir_str)
        for subdir in ["core", "extensions", "simplified_decorators"]:
            subdir_path = registry_path / subdir
            if not subdir_path.exists():
                continue

            for json_file in subdir_path.glob("**/*.json"):
                try:
                    with open(json_file, "r") as f:
                        data = json.load(f)

                    # Check if this is a decorator definition
                    if "decoratorName" in data:
                        name = data["decoratorName"]
                        cls._registry[name] = {
                            "name": name,
                            "description": data.get("description", ""),
                            "category": data.get("category", "General"),
                            "parameters": data.get("parameters", []),
                            "transform_function": data.get(
                                "transform_function", data.get("transformFunction", "")
                            ),
                            "version": data.get("version", "1.0.0"),
                        }
                        logger.debug(f"Loaded decorator: {name}")
                except Exception as e:
                    logger.error(f"Error loading decorator from {json_file}: {e}")

        cls._loaded = True
        logger.info(f"Loaded {len(cls._registry)} decorators from registry")

    @classmethod
    def from_definition(cls, definition: Any) -> type:
        """Create a decorator class from a definition.

        Args:
            definition: Decorator definition

        Returns:
            A decorator class
        """
        # Convert the definition to a dictionary if it's not already
        if hasattr(definition, "to_dict"):
            definition_dict = definition.to_dict()
        else:
            definition_dict = definition

        # Create a new class for the decorator
        name = definition_dict["name"]
        decorator_class = type(
            name,
            (cls,),
            {
                "__init__": lambda self, **kwargs: cls.__init__(self, name, **kwargs),
                "__doc__": definition_dict.get("description", ""),
            },
        )

        # Register the decorator
        cls._registry[name] = definition_dict

        return decorator_class

    @classmethod
    def register_decorator(cls, decorator_def: Dict[str, Any]) -> None:
        """Register a decorator directly from a dictionary definition.

        This is particularly useful for testing, where you might want to
        register decorators without loading them from files.

        Args:
            decorator_def: Dictionary containing the decorator definition

        Returns:
            None
        """
        if not cls._loaded:
            cls._registry.clear()
            cls._loaded = True

        name = decorator_def.get("decoratorName")
        if not name:
            raise ValueError("Decorator definition must include 'decoratorName'")

        cls._registry[name] = {
            "name": name,
            "description": decorator_def.get("description", ""),
            "category": decorator_def.get("category", "General"),
            "parameters": decorator_def.get("parameters", []),
            "transform_function": decorator_def.get(
                "transform_function", decorator_def.get("transformFunction", "")
            ),
            "version": decorator_def.get("version", "1.0.0"),
        }
        logger.debug(f"Registered decorator: {name}")

    @classmethod
    def get_available_decorators(cls) -> List[Any]:
        """Get a list of all available decorators.

        Args:
            cls: The class object

        Returns:
            List of decorator definitions
        """
        # Load the registry if not already loaded
        if not cls._loaded:
            cls.load_registry()

        # Convert registry entries to DecoratorSchema objects
        result = []
        for name, definition in cls._registry.items():
            # Create parameter schemas
            parameters = []
            for param_def in definition.get("parameters", []):
                param_schema = ParameterSchema(
                    name=param_def["name"],
                    description=param_def.get("description", ""),
                    type_=param_def.get("type", "string"),
                    required=param_def.get("required", False),
                    default=param_def.get("default"),
                    enum_values=param_def.get("enum_values"),
                    min_value=param_def.get("min_value"),
                    max_value=param_def.get("max_value"),
                    min_length=param_def.get("min_length"),
                    max_length=param_def.get("max_length"),
                    pattern=param_def.get("pattern"),
                )
                parameters.append(param_schema)

            # Create decorator schema
            decorator_schema = DecoratorSchema(
                name=name,
                description=definition.get("description", ""),
                category=definition.get("category", "General"),
                parameters=parameters,
                transform_function=definition.get("transform_function", ""),
                version=definition.get("version", "1.0.0"),
            )
            result.append(decorator_schema)

        return result


def parse_decorator(decorator_text: str) -> Tuple[str, Dict[str, Any]]:
    """Parse a decorator string into name and parameters.

    Args:
        decorator_text: Text containing a decorator definition

    Returns:
        Tuple of (name, parameters)
    """
    # Extract decorator name and parameters
    match = re.match(DECORATOR_PATTERN, decorator_text)
    if not match:
        raise ValueError(f"Invalid decorator syntax: {decorator_text}")

    name = match.group(1)
    params_str = match.group(2) or ""

    # Parse parameters
    params = {}
    if params_str:
        for param_match in re.finditer(PARAMETER_PATTERN, params_str):
            param_name = param_match.group(1)
            param_value = param_match.group(2)

            # Remove quotes from string values
            if param_value.startswith('"') and param_value.endswith('"'):
                param_value = param_value[1:-1]

            # Convert to appropriate type
            if param_value.lower() == "true":
                param_value = True
            elif param_value.lower() == "false":
                param_value = False
            elif param_value.isdigit():
                param_value = int(param_value)
            elif (
                param_value.replace(".", "", 1).isdigit()
                and param_value.count(".") == 1
            ):
                param_value = float(param_value)

            params[param_name] = param_value

    return name, params


def extract_decorators(text: str) -> Tuple[List[DynamicDecorator], str]:
    """Extract decorators from text.

    Args:
        text: Text containing decorator definitions

    Returns:
        Tuple of (decorators, clean_text)
    """
    # Find all decorator annotations
    matches = re.finditer(DECORATOR_PATTERN, text, re.MULTILINE)
    decorators = []
    clean_text = text

    # Process each match
    for match in matches:
        # Get the full decorator text
        decorator_text = match.group(0)

        try:
            # Parse the decorator
            name, params = parse_decorator(decorator_text)

            # Create the decorator
            decorator = DynamicDecorator(name, **params)
            decorators.append(decorator)
        except Exception as e:
            logger.error(f"Error creating decorator from '{decorator_text}': {e}")

        # Remove the decorator from the text
        clean_text = clean_text.replace(decorator_text, "", 1)

    # Clean up any extra whitespace
    clean_text = clean_text.strip()

    return decorators, clean_text


def transform_prompt(prompt: str, decorators: List[str]) -> str:
    """Transform a prompt using a list of decorator strings.

    Args:
        prompt: The prompt to transform
        decorators: List of decorator strings

    Returns:
        The transformed prompt
    """
    result = prompt

    # Apply each decorator in order
    for decorator_str in decorators:
        try:
            # Parse the decorator
            name, params = parse_decorator(decorator_str)

            # Create and apply the decorator
            decorator = DynamicDecorator(name, **params)
            transformed = decorator(result)
            if isinstance(transformed, str):
                result = transformed
            else:
                # This should not happen in normal usage, but handle it just in case
                result = str(transformed)
        except Exception as e:
            logger.error(f"Error applying decorator '{decorator_str}': {e}")

    return result
