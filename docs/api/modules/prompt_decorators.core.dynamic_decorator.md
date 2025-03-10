# dynamic_decorator

Dynamic decorator functionality for prompt transformations.

This module provides a dynamic approach to loading and applying prompt decorators
from registry definitions. Instead of generating individual decorator classes for each
decorator in the registry, this module loads decorator definitions at runtime directly
from the JSON files in the registry.

Typical usage:
    >>> from prompt_decorators.core.dynamic_decorator import DynamicDecorator, transform_prompt
    >>> result = transform_prompt("What is quantum computing?", ["+++StepByStep(numbered=true)"])
    >>> decorated = DynamicDecorator("StepByStep", numbered=True)
    >>> result = decorated("What is quantum computing?")

## Module Variables

### `DECORATOR_PATTERN`

Type: `str`

Value: `'\\+\\+\\+([A-Za-z][A-Za-z0-9]*(?::v[0-9]+(?:\\.[0-9]+(?:\\.[0-9]+)?)?)?)(?:\\(([^)]*)\\))?'`

### `DECORATOR_PREFIX`

Type: `str`

Value: `'+++'`

### `DEFAULT_REGISTRY_DIR`

Type: `str`

Value: `'registry'`

### `PARAMETER_PATTERN`

Type: `str`

Value: `'([a-zA-Z0-9_]+)=("(?:[^"\\\\]|\\\\.)*"|[^,)]+)'`

### `REGISTRY_ENV_VAR`

Type: `str`

Value: `'DECORATOR_REGISTRY_DIR'`

### `logger`

Type: `Logger`

Value: `<Logger prompt_decorators.core.dynamic_decorator (INFO)>`

## Classes

### `DecoratorParameter`

Class representing a validated decorator parameter.

#### Methods

##### `__init__`

Initialize a decorator parameter.

Args:
    name: Name of the parameter
    value: Value of the parameter
    param_type: Type of the parameter (string, number, boolean, array, enum)
    validation: Optional validation rules
    enum_values: Optional list of allowed enum values

Returns:
    None

**Signature:** `__init__(self, name: str, value: Any, param_type: str, validation: Optional[Dict[str, Any]] = None, enum_values: Optional[List[str]] = None) -> None`

**Parameters:**

- `name`: `str`
- `value`: `Any`
- `param_type`: `str`
- `validation`: `Optional` (default: `None`)
- `enum_values`: `Optional` (default: `None`)

### `DynamicDecorator`

Dynamic decorator class for prompt transformations.

This class provides a dynamic approach to loading and applying prompt decorators
from registry definitions. Instead of generating individual decorator classes for each
decorator in the registry, this class loads decorator definitions at runtime directly
from the JSON files in the registry.

#### Attributes

- `from_definition`: `classmethod` = `<classmethod(<function DynamicDecorator.from_definition at 0x1064c5080>)>`
- `get_available_decorators`: `classmethod` = `<classmethod(<function DynamicDecorator.get_available_decorators at 0x1064c51c0>)>`
- `load_registry`: `classmethod` = `<classmethod(<function DynamicDecorator.load_registry at 0x1064c4fe0>)>`
- `register_decorator`: `classmethod` = `<classmethod(<function DynamicDecorator.register_decorator at 0x1064c5120>)>`

#### Methods

##### `__init__`

Initialize a dynamic decorator.

Args:
    name: Name of the decorator to load
    **kwargs: Parameters for the decorator

Raises:
    ValueError: If the decorator is not found in the registry

Returns:
    None

**Signature:** `__init__(self, name: str, **kwargs: Any) -> None`

**Parameters:**

- `name`: `str`
- `kwargs`: `Any`

##### `apply`

Apply the decorator to a text.

Args:
    text: Text to transform

Returns:
    Transformed text

**Signature:** `apply(self, text: str) -> str`

**Parameters:**

- `text`: `str`

**Returns:** `str`

## Functions

### `create_transform_function_from_template`

Convert a transformation template to an executable transform function.

Args:
    template: The transformation template definition

Returns:
    A string containing executable Python code for the transform function

**Signature:** `create_transform_function_from_template(template: Dict[str, Any]) -> str`

**Parameters:**

- `template`: `Dict`

**Returns:** `str`

### `extract_decorators`

Extract decorators from text.

Args:
    text: Text containing decorator definitions

Returns:
    Tuple of (decorators, clean_text)

**Signature:** `extract_decorators(text: str) -> Tuple[List[prompt_decorators.core.dynamic_decorator.DynamicDecorator], str]`

**Parameters:**

- `text`: `str`

**Returns:** `Tuple`

### `parse_decorator`

Parse a decorator string into name and parameters.

Args:
    decorator_text: Text containing a decorator definition

Returns:
    Tuple of (name, parameters)

**Signature:** `parse_decorator(decorator_text: str) -> Tuple[str, Dict[str, Any]]`

**Parameters:**

- `decorator_text`: `str`

**Returns:** `Tuple`

### `transform_prompt`

Transform a prompt using a list of decorator strings.

Args:
    prompt: The prompt to transform
    decorators: List of decorator strings

Returns:
    The transformed prompt

**Signature:** `transform_prompt(prompt: str, decorators: List[str]) -> str`

**Parameters:**

- `prompt`: `str`
- `decorators`: `List`

**Returns:** `str`
