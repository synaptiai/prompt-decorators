# dynamic_decorators_module

Dynamic Prompt Decorators Module.

This module provides a unified interface for working with prompt decorators
without the need for code generation. It dynamically loads decorator definitions
from the registry at runtime, removing the need to generate Python classes for
each decorator.

Features:
- Dynamic loading of decorators from registry
- Prompt transformation with any decorator
- Parameter validation against schema
- Support for decorator composition

## Public API

This module exports the following components:

- `DynamicDecorator`: Class - Dynamic decorator class for prompt transformations
- `DecoratorDefinition`: Class - Class representing a decorator definition
- `load_decorator_definitions`: Function - Load decorator definitions from the registry
- `get_available_decorators`: Function - Get a list of all available decorators
- `create_decorator_instance`: Function - Create a decorator instance by name
- `create_decorator_class`: Function - Create a decorator class from a definition
- `apply_dynamic_decorators`: Function - Apply decorators to a prompt using the +++ syntax
- `apply_decorator`: Function - Apply a decorator to a prompt
- `register_decorator`: Function - Register a decorator definition
- `extract_decorator_name`: Function - Extract the decorator name from decorator text
- `parse_decorator_text`: Function - Parse decorator text into name and parameters
- `create_decorator`: Function - Create a decorator instance by name (alias for create_decorator_instance)
- `list_available_decorators`: Function - List all available decorator names
- `transform_prompt`: Function - Transform a prompt using a list of decorator strings

## Classes

### `DecoratorDefinition`

Class representing a decorator definition.

#### Methods

##### `__init__`

Initialize a decorator definition.

Args:
    name: Name of the decorator
    description: Description of the decorator
    category: Category of the decorator
    parameters: List of parameter definitions
    transform_function: JavaScript function for transforming prompts
    version: Version of the decorator

**Signature:** `__init__(self, name: str, description: str, category: str, parameters: List[Dict[str, Any]], transform_function: str, version: str = '1.0.0')`

**Parameters:**

- `name`: `str`
- `description`: `str`
- `category`: `str`
- `parameters`: `List`
- `transform_function`: `str`
- `version`: `str` (default: `1.0.0`)

##### `to_dict`

Convert the definition to a dictionary.

**Signature:** `to_dict(self) -> Dict[str, Any]`

**Parameters:**


**Returns:** `Dict`

### `DynamicDecorator`

*Imported from `prompt_decorators.core.dynamic_decorator`*

Dynamic decorator class for prompt transformations.

This class provides a dynamic approach to loading and applying prompt decorators
from registry definitions. Instead of generating individual decorator classes for each
decorator in the registry, this class loads decorator definitions at runtime directly
from the JSON files in the registry.

#### Attributes

- `from_definition`: `classmethod` = `<classmethod(<function DynamicDecorator.from_definition at 0x105a75080>)>`
- `get_available_decorators`: `classmethod` = `<classmethod(<function DynamicDecorator.get_available_decorators at 0x105a751c0>)>`
- `load_registry`: `classmethod` = `<classmethod(<function DynamicDecorator.load_registry at 0x105a74fe0>)>`
- `register_decorator`: `classmethod` = `<classmethod(<function DynamicDecorator.register_decorator at 0x105a75120>)>`

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

### `apply_decorator`

Apply a decorator to a prompt.

Args:
    decorator_name: Name of the decorator
    prompt: The prompt text
    **kwargs: Parameters for the decorator

Returns:
    The transformed prompt

**Signature:** `apply_decorator(decorator_name: str, prompt: str, **kwargs: Any) -> str`

**Parameters:**

- `decorator_name`: `str`
- `prompt`: `str`
- `kwargs`: `Any`

**Returns:** `str`

### `apply_dynamic_decorators`

Apply decorators to a prompt using the +++ syntax.

Args:
    prompt: The prompt text with decorator syntax

Returns:
    The transformed prompt

**Signature:** `apply_dynamic_decorators(prompt: str) -> str`

**Parameters:**

- `prompt`: `str`

**Returns:** `str`

### `create_decorator`

Create a decorator instance by name (alias for create_decorator_instance).

This function is maintained for backward compatibility with demo code.

Args:
    name: Name of the decorator
    **kwargs: Parameters for the decorator

Returns:
    A decorator instance

Raises:
    ValueError: If the decorator is not found

**Signature:** `create_decorator(name: str, **kwargs: Any) -> prompt_decorators.core.dynamic_decorator.DynamicDecorator`

**Parameters:**

- `name`: `str`
- `kwargs`: `Any`

**Returns:** `DynamicDecorator`

### `create_decorator_class`

Create a decorator class from a definition.

Args:
    definition: Decorator definition

Returns:
    A decorator class

**Signature:** `create_decorator_class(definition: prompt_decorators.dynamic_decorators_module.DecoratorDefinition) -> type`

**Parameters:**

- `definition`: `DecoratorDefinition`

**Returns:** `type`

### `create_decorator_instance`

Create a decorator instance by name.

Args:
    name: Name of the decorator
    **kwargs: Parameters for the decorator

Returns:
    A decorator instance

Raises:
    ValueError: If the decorator is not found

**Signature:** `create_decorator_instance(name: str, **kwargs: Any) -> prompt_decorators.core.dynamic_decorator.DynamicDecorator`

**Parameters:**

- `name`: `str`
- `kwargs`: `Any`

**Returns:** `DynamicDecorator`

### `extract_decorator_name`

Extract the decorator name from decorator text.

Args:
    decorator_text: Text containing a decorator definition

Returns:
    The decorator name

**Signature:** `extract_decorator_name(decorator_text: str) -> str`

**Parameters:**

- `decorator_text`: `str`

**Returns:** `str`

### `get_available_decorators`

Get a list of all available decorators.

Returns:
    List of decorator definitions

**Signature:** `get_available_decorators() -> List[prompt_decorators.dynamic_decorators_module.DecoratorDefinition]`

**Returns:** `List`

### `list_available_decorators`

List all available decorator names.

This function is maintained for backward compatibility with demo code.

Returns:
    A list of decorator names

**Signature:** `list_available_decorators() -> List[str]`

**Returns:** `List`

### `load_decorator_definitions`

Load decorator definitions from the registry.

**Signature:** `load_decorator_definitions() -> None`

### `parse_decorator_text`

Parse decorator text into name and parameters.

Args:
    decorator_text: Text containing a decorator definition

Returns:
    Tuple of (name, parameters)

**Signature:** `parse_decorator_text(decorator_text: str) -> tuple`

**Parameters:**

- `decorator_text`: `str`

**Returns:** `tuple`

### `register_decorator`

Register a decorator definition.

Args:
    definition: Decorator definition

Returns:
    None

**Signature:** `register_decorator(definition: prompt_decorators.dynamic_decorators_module.DecoratorDefinition) -> None`

**Parameters:**

- `definition`: `DecoratorDefinition`

### `transform_prompt`

Transform a prompt using a list of decorator strings.

This function is a wrapper around the core transform_prompt function
to ensure backward compatibility with the demo.

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
