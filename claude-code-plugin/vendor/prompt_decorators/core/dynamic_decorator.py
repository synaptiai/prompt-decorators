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
from importlib import resources
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
    cast,
)

if TYPE_CHECKING:
    from typing import Iterator, Protocol

    class HasGlob(Protocol):
        """Protocol for objects that support the glob method."""

        def glob(self, pattern: str) -> Iterator[Any]:
            """Find paths matching a pattern.

            Args:
                pattern: The pattern to match

            Returns:
                Iterator of matching paths
            """
            ...

    class HasSuffix(Protocol):
        """Protocol for objects that have a suffix property and file-like methods."""

        @property
        def suffix(self) -> str:
            """Get the file extension.

            Args:
                self: The object instance

            Returns:
                The file extension including the leading dot
            """
            ...

        def is_file(self) -> bool:
            """Check if the path is a file.

            Args:
                self: The object instance

            Returns:
                True if the path is a file, False otherwise
            """
            ...

        def open(self, mode: str) -> Any:
            """Open the file.

            Args:
                mode: The mode to open the file in

            Returns:
                A file-like object
            """
            ...


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


def create_transform_function_from_template(template: Dict[str, Any]) -> str:
    """Convert a transformation template to an executable transform function.

    Args:
        template: The transformation template definition

    Returns:
        A string containing executable Python code for the transform function
    """
    instruction = template.get("instruction", "")
    parameter_mapping = template.get("parameterMapping", {})
    placement = template.get("placement", "prepend")

    # Create a Python function string from the template
    function_str = """
def transform(text, **kwargs):
    result = '''{}'''
    """.format(
        instruction
    )

    # Add parameter mapping logic
    for param_name, mapping in parameter_mapping.items():
        function_str += """
    if "{param}" in kwargs:
        param_value = kwargs["{param}"]
        """.format(
            param=param_name
        )

        # Handle value maps
        if "valueMap" in mapping:
            function_str += """
        param_value_str = str(param_value)
        value_map = {}
        if param_value_str in value_map:
            result += " " + value_map[param_value_str]
            """.format(
                repr(mapping["valueMap"])
            )

        # Handle format strings
        elif "format" in mapping:
            format_str = mapping["format"]
            function_str += """
        format_str = '''{}'''
        result += " " + format_str.format(value=param_value)
            """.format(
                format_str
            )

    # Add placement logic
    if placement == "prepend":
        function_str += """
    return result + "\\n\\n" + text
    """
    elif placement == "append":
        function_str += """
    return text + "\\n\\n" + result
    """
    elif placement == "replace":
        function_str += """
    return result
    """
    else:  # Default to append
        function_str += """
    return text + "\\n\\n" + result
    """

    return function_str


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
            name: Parameter name
            value: Parameter value
            param_def: Parameter definition

        Raises:
            ValueError: If the parameter value is invalid

        Returns:
            None
        """
        param_type = param_def.get("type", "string")

        # Skip validation for None values if the parameter is not required
        if value is None and not param_def.get("required", False):
            return

        # Validate based on type
        if param_type == "string":
            if not isinstance(value, str):
                raise ValueError(
                    f"Parameter '{name}' must be a string, got {type(value).__name__}"
                )
            min_length = param_def.get("min_length")
            max_length = param_def.get("max_length")
            if min_length is not None and len(value) < min_length:
                raise ValueError(
                    f"Parameter '{name}' must be at least {min_length} characters long"
                )
            if max_length is not None and len(value) > max_length:
                raise ValueError(
                    f"Parameter '{name}' must be at most {max_length} characters long"
                )
        elif param_type == "number":
            if not isinstance(value, (int, float)):
                raise ValueError(
                    f"Parameter '{name}' must be a number, got {type(value).__name__}"
                )
            min_value = param_def.get("min_value")
            max_value = param_def.get("max_value")
            if min_value is not None and value < min_value:
                raise ValueError(f"Parameter '{name}' must be at least {min_value}")
            if max_value is not None and value > max_value:
                raise ValueError(f"Parameter '{name}' must be at most {max_value}")
        elif param_type == "boolean":
            if not isinstance(value, bool):
                raise ValueError(
                    f"Parameter '{name}' must be a boolean, got {type(value).__name__}"
                )
        elif param_type == "enum":
            if not isinstance(value, str):
                raise ValueError(
                    f"Parameter '{name}' must be a string, got {type(value).__name__}"
                )
            # Check for enum values in either 'enum_values' or 'enum' field
            enum_values = param_def.get("enum_values", param_def.get("enum", []))
            if not enum_values:
                # Instead of raising an error, log a warning and continue
                logger.warning(f"No enum values defined for parameter '{name}'")
                return
            if value not in enum_values:
                raise ValueError(
                    f"Parameter '{name}' must be one of {enum_values}, got '{value}'"
                )
        else:
            # Unknown type, skip validation
            pass

    def __call__(self, text_or_func: Union[str, Callable]) -> Union[str, Callable]:
        """Apply the decorator to a text or function.

        Args:
            text_or_func: Text to transform or function to decorate

        Returns:
            Transformed text or decorated function
        """
        # If text_or_func is a function, return a wrapper function
        if callable(text_or_func):
            # Define a wrapper function that applies the decorator to the result of
            # the original function
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
            # If no transform function but we have a transformationTemplate, create one on the fly
            if "transformationTemplate" in self.definition:
                try:
                    transform_function = create_transform_function_from_template(
                        self.definition["transformationTemplate"]
                    )
                    logger.debug(
                        f"Created transform function from template for {self.name} on-demand"
                    )
                except Exception as e:
                    logger.error(
                        f"Error creating transform function from template for {self.name}: {e}"
                    )
                    return text
            else:
                return text

        # Add parameters to dictionary for function call
        param_dict = {k: v.value for k, v in self.parameters.items()}

        # Execute the transform function
        try:
            # Check if transform_function already looks like a complete Python function
            if transform_function.strip().startswith("def transform("):
                # If it's from our template generator, it's already a complete function
                transform_code = transform_function
            else:
                # For backward compatibility with inline code snippets
                # Add a return statement if not present
                if "return" not in transform_function:
                    transform_function = f"return {transform_function}"

                # Create a Python function from the code
                transform_code = "def transform(text, **kwargs):\n"
                for line in transform_function.split("\n"):
                    transform_code += f"    {line}\n"

            # Compile and execute the function
            namespace: Dict[str, Any] = {}
            exec(transform_code, namespace)
            transform = namespace["transform"]  # type: ignore

            # Call the function with the text and parameters as kwargs
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

        This method implements a comprehensive three-tier loading strategy:
        1. Package resources loading (preferred)
        2. Auto-repair if package registry is empty
        3. Enhanced filesystem fallback

        Args:
            cls: The class object

        Returns:
            None
        """
        # Clear the registry
        cls._registry.clear()

        # First try to load from package resources
        loaded_from_package = cls._load_from_package_resources()

        # If nothing was loaded from package resources, try auto-repair
        if not loaded_from_package:
            logger.debug("Package registry empty, attempting auto-repair...")
            try:
                # Import registry validator for auto-repair
                from prompt_decorators.utils.registry_validator import RegistryValidator

                # Attempt auto-repair
                success, message = RegistryValidator.auto_repair_registry()
                if success:
                    logger.info(f"Registry auto-repair successful: {message}")
                    # Retry loading from package resources after repair
                    loaded_from_package = cls._load_from_package_resources()
                else:
                    logger.warning(f"Registry auto-repair failed: {message}")
            except ImportError:
                logger.debug("Registry validator not available for auto-repair")
            except Exception as e:
                logger.warning(f"Auto-repair attempt failed: {e}")

        # If still nothing loaded, fall back to filesystem
        if not loaded_from_package:
            logger.debug("Falling back to filesystem loading...")
            cls._load_from_filesystem()

        cls._loaded = True
        decorator_count = len(cls._registry)
        logger.info(f"Loaded {decorator_count} decorators from registry")

        # Log loading strategy used for debugging
        if decorator_count > 0:
            if loaded_from_package:
                logger.debug("Successfully loaded decorators from package resources")
            else:
                logger.debug("Successfully loaded decorators from filesystem fallback")
        else:
            logger.warning("No decorators loaded - registry may be missing or empty")

    @classmethod
    def _load_from_package_resources(cls) -> bool:
        """Load decorator definitions from package resources.

        Args:
            cls: The class object

        Returns:
            bool: True if any decorators were loaded, False otherwise
        """
        try:
            # Try to import the registry package
            try:
                # For Python 3.9+
                from importlib.resources import files

                registry_exists = (
                    files("prompt_decorators").joinpath("registry").is_dir()
                )
            except (ImportError, AttributeError):
                # Fallback for Python 3.7-3.8
                registry_exists = resources.is_resource("prompt_decorators", "registry")

            if not registry_exists:
                logger.debug("Registry not found in package resources")
                return False

            # Process registry subdirectories
            subdirs = ["core", "extensions", "simplified_decorators"]
            decorators_loaded = 0

            for subdir in subdirs:
                try:
                    # Try to access the subdirectory
                    try:
                        # For Python 3.9+
                        subdir_path = files("prompt_decorators").joinpath(
                            f"registry/{subdir}"
                        )
                        if not subdir_path.is_dir():
                            continue

                        # Walk through the directory structure
                        # Use Path.glob for Python 3.9+ and manual iteration for older versions
                        try:
                            # Type ignore for mypy since it doesn't know the exact type
                            for json_file in subdir_path.glob("**/*.json"):  # type: ignore
                                with json_file.open("r") as f:  # type: ignore
                                    data = json.load(f)
                                    if cls._process_decorator_data(data):
                                        decorators_loaded += 1
                        except AttributeError:
                            # Fallback for older Python versions or different Path implementations
                            logger.debug(
                                "Using fallback method for traversing directory structure"
                            )
                            # This is a simplified approach that won't handle nested directories
                            # Type ignore for mypy since it doesn't know the exact type
                            json_files = [
                                p
                                for p in subdir_path.iterdir()  # type: ignore
                                if p.is_file()
                                and hasattr(p, "suffix")  # type: ignore
                                and getattr(  # Check if p has suffix attribute
                                    p, "suffix"
                                )
                                == ".json"  # Get suffix safely
                            ]
                            for json_file in json_files:
                                with json_file.open("r") as f:
                                    data = json.load(f)
                                    if cls._process_decorator_data(data):
                                        decorators_loaded += 1
                    except (ImportError, AttributeError):
                        # Fallback for Python 3.7-3.8
                        if not resources.is_resource(
                            "prompt_decorators.registry", subdir
                        ):
                            continue

                        # This is a simplified approach for older Python versions
                        # It won't handle nested directories well, but it's a fallback
                        for resource in resources.contents(
                            f"prompt_decorators.registry.{subdir}"
                        ):
                            if resource.endswith(".json"):
                                json_data = resources.read_text(
                                    f"prompt_decorators.registry.{subdir}", resource
                                )
                                data = json.loads(json_data)
                                if cls._process_decorator_data(data):
                                    decorators_loaded += 1
                except Exception as e:
                    logger.error(
                        f"Error loading decorators from package resources/{subdir}: {e}"
                    )

            return decorators_loaded > 0
        except Exception as e:
            logger.error(f"Error loading decorators from package resources: {e}")
            return False

    @classmethod
    def _process_decorator_data(cls, data: Dict[str, Any]) -> bool:
        """Process decorator data from JSON.

        Args:
            data: The decorator data loaded from JSON

        Returns:
            bool: True if the decorator was processed successfully, False otherwise
        """
        try:
            # Check if this is a decorator definition
            if "decoratorName" not in data:
                return False

            name = data["decoratorName"]

            # Get transform_function or create one from transformation template
            transform_function = data.get("transform_function") or data.get(
                "transformFunction", ""
            )

            # If no transform_function but there is a transformationTemplate, create one
            if not transform_function and "transformationTemplate" in data:
                try:
                    transform_function = create_transform_function_from_template(
                        data["transformationTemplate"]
                    )
                    logger.debug(f"Created transform function from template for {name}")
                except Exception as e:
                    logger.error(
                        f"Error creating transform function from template for {name}: {e}"
                    )

            # Process parameters - ensure enum values are properly set
            parameters = data.get("parameters", [])
            for param in parameters:
                # If param has 'enum' but not 'enum_values', copy enum to enum_values
                if (
                    param.get("type") == "enum"
                    and "enum" in param
                    and "enum_values" not in param
                ):
                    param["enum_values"] = param["enum"]
                    logger.debug(
                        f"Copied enum values to enum_values for {name}.{param.get('name')}"
                    )

            cls._registry[name] = {
                "name": name,
                "description": data.get("description", ""),
                "category": data.get("category", "General"),
                "parameters": parameters,
                "transform_function": transform_function,
                "transformationTemplate": data.get("transformationTemplate", {}),
                "version": data.get("version", "1.0.0"),
            }
            logger.debug(f"Loaded decorator: {name}")
            return True
        except Exception as e:
            logger.error(f"Error processing decorator data: {e}")
            return False

    @classmethod
    def _load_from_filesystem(cls) -> None:
        """Load decorator definitions from the filesystem for backward compatibility."""
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

        logger.debug(f"Loading registry from filesystem: {registry_dir_str}")

        # Check if the registry directory exists
        if not os.path.exists(registry_dir_str):
            logger.warning(f"Registry directory not found: {registry_dir_str}")
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
                    cls._process_decorator_data(data)
                except Exception as e:
                    logger.error(f"Error loading decorator from {json_file}: {e}")

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
        """Register a decorator with the registry.

        Args:
            decorator_def: Decorator definition dictionary from JSON

        Raises:
            ValueError: If the decorator definition is invalid

        Returns:
            None
        """
        if not isinstance(decorator_def, dict):
            raise ValueError("Decorator definition must be a dictionary")

        name = decorator_def.get("decoratorName")
        if not name:
            raise ValueError("Decorator definition must include 'decoratorName'")

        # Get transform_function or create one from transformation template
        transform_function = decorator_def.get(
            "transform_function"
        ) or decorator_def.get("transformFunction", "")

        # If no transform_function but there is a transformationTemplate, create one
        if not transform_function and "transformationTemplate" in decorator_def:
            try:
                transform_function = create_transform_function_from_template(
                    decorator_def["transformationTemplate"]
                )
                logger.debug(f"Created transform function from template for {name}")
            except Exception as e:
                logger.error(
                    f"Error creating transform function from template for {name}: {e}"
                )

        # Process parameters - ensure enum values are properly set
        parameters = decorator_def.get("parameters", [])
        for param in parameters:
            # If param has 'enum' but not 'enum_values', copy enum to enum_values
            if (
                param.get("type") == "enum"
                and "enum" in param
                and "enum_values" not in param
            ):
                param["enum_values"] = param["enum"]
                logger.debug(
                    f"Copied enum values to enum_values for {name}.{param.get('name')}"
                )

        cls._registry[name] = {
            "name": name,
            "description": decorator_def.get("description", ""),
            "category": decorator_def.get("category", "General"),
            "parameters": parameters,
            "transform_function": transform_function,
            "transformationTemplate": decorator_def.get("transformationTemplate", {}),
            "version": decorator_def.get("version", "1.0.0"),
        }
        logger.debug(f"Registered decorator: {name}")
        cls._loaded = True  # Mark registry as loaded after successful registration

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
