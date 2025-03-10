# factory

Decorator Factory Module.

This module provides utilities for creating decorator instances from JSON definitions.

## Module Variables

### `logger`

Type: `Logger`

Value: `<Logger prompt_decorators.utils.factory (INFO)>`

## Classes

### `DecoratorFactory`

Factory for creating decorator instances from JSON definitions.

This class provides utilities for creating decorator instances from JSON definitions,
either by using existing decorator classes or by dynamically generating new ones.

#### Methods

##### `__init__`

Initialize the decorator factory.

Args:
    registry: The decorator registry to use (optional)

**Signature:** `__init__(self, registry: Optional[prompt_decorators.utils.discovery.DecoratorRegistry] = None)`

**Parameters:**

- `registry`: `Optional` (default: `None`)

##### `create_all_from_directory`

Create decorator instances from all JSON files in a directory.

Args:
    directory_path: Path to the directory containing JSON files

Returns:
    List of decorator instances

**Signature:** `create_all_from_directory(self, directory_path: str) -> List[prompt_decorators.core.base.DecoratorBase]`

**Parameters:**

- `directory_path`: `str`

**Returns:** `List`

##### `create_dynamic_class`

Create a dynamic decorator class from a dictionary definition.

Args:
    decorator_data: Dictionary containing the decorator definition

Returns:
    A new decorator class

**Signature:** `create_dynamic_class(self, decorator_data: Dict[str, Any]) -> Type[prompt_decorators.core.base.DecoratorBase]`

**Parameters:**

- `decorator_data`: `Dict`

**Returns:** `Type`

##### `create_from_dict`

Create a decorator instance from a dictionary.

Args:
    decorator_data: Dictionary containing the decorator definition

Returns:
    The created decorator instance, or None if creation failed

**Signature:** `create_from_dict(self, decorator_data: Dict[str, Any]) -> Optional[prompt_decorators.core.base.DecoratorBase]`

**Parameters:**

- `decorator_data`: `Dict`

**Returns:** `Optional`

##### `create_from_file`

Create a decorator instance from a JSON file.

Args:
    file_path: Path to the JSON file containing the decorator definition

Returns:
    The created decorator instance, or None if creation failed

**Signature:** `create_from_file(self, file_path: str) -> Optional[prompt_decorators.core.base.DecoratorBase]`

**Parameters:**

- `file_path`: `str`

**Returns:** `Optional`

##### `create_from_json_string`

Create a decorator instance from a JSON string.

Args:
    json_string: JSON string containing the decorator definition

Returns:
    The created decorator instance, or None if creation failed

**Signature:** `create_from_json_string(self, json_string: str) -> Optional[prompt_decorators.core.base.DecoratorBase]`

**Parameters:**

- `json_string`: `str`

**Returns:** `Optional`

##### `extract_parameters`

Extract parameter values from a decorator definition.

Args:
    decorator_data: The decorator definition as a dictionary

Returns:
    Dictionary of parameter values

**Signature:** `extract_parameters(self, decorator_data: Dict[str, Any]) -> Dict[str, Any]`

**Parameters:**

- `decorator_data`: `Dict`

**Returns:** `Dict`

##### `find_decorator_class`

Find a decorator class by name.

Args:
    decorator_name: The name of the decorator

Returns:
    The decorator class, or None if not found

**Signature:** `find_decorator_class(self, decorator_name: str) -> Optional[Type[prompt_decorators.core.base.DecoratorBase]]`

**Parameters:**

- `decorator_name`: `str`

**Returns:** `Optional`
