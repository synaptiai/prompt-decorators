# discovery

Decorator discovery and registration utilities.

This module provides utilities for discovering and registering prompt decorators.

## Classes

### `DecoratorRegistry`

Registry for prompt decorators.

This class provides methods for registering and discovering decorators at runtime.

#### Methods

##### `__init__`

Initialize the registry.

This is a no-op for the singleton pattern.

Args:
    self: The DecoratorRegistry instance

Returns:
    None

**Signature:** `__init__(self)`

**Parameters:**


##### `clear`

Clear all registered decorators.

This is primarily used for testing.

Args:
    self: The DecoratorRegistry instance

Returns:
    None

**Signature:** `clear(self)`

**Parameters:**


##### `create_decorator`

Create a decorator instance by name with the specified parameters.

Args:
    name: The name of the decorator class to instantiate
    **parameters: Parameters to pass to the decorator constructor

Returns:
    The created decorator instance if successful, None otherwise

Raises:
    ValueError: If the decorator class is not found
    TypeError: If the parameters are invalid for the decorator

**Signature:** `create_decorator(self, name: str, **parameters) -> Optional[prompt_decorators.core.base.DecoratorBase]`

**Parameters:**

- `name`: `str`
- `parameters`:

**Returns:** `Optional`

##### `find_decorators_by_category`

Find all decorators in a specific category.

Args:
    category: The category to search for

Returns:
    Dictionary mapping decorator names to decorator classes

**Signature:** `find_decorators_by_category(self, category: str) -> Dict[str, Type[prompt_decorators.core.base.DecoratorBase]]`

**Parameters:**

- `category`: `str`

**Returns:** `Dict`

##### `get_all_decorator_instances`

Get all registered decorator instances.

Args:
    self: The DecoratorRegistry instance

Returns:
    Dictionary mapping decorator names to decorator instances

**Signature:** `get_all_decorator_instances(self) -> Dict[str, prompt_decorators.core.base.DecoratorBase]`

**Parameters:**


**Returns:** `Dict`

##### `get_all_decorators`

Get all registered decorator classes.

Args:
    self: The DecoratorRegistry instance

Returns:
    Dictionary mapping decorator names to decorator classes

**Signature:** `get_all_decorators(self) -> Dict[str, Type[prompt_decorators.core.base.DecoratorBase]]`

**Parameters:**


**Returns:** `Dict`

##### `get_categories`

Get all registered decorator categories.

Args:
    self: The DecoratorRegistry instance

Returns:
    Set of category names

**Signature:** `get_categories(self) -> Set[str]`

**Parameters:**


**Returns:** `Set`

##### `get_decorator`

Get a decorator class by name.

Args:
    name: The name of the decorator to retrieve

Returns:
    The decorator class if found, None otherwise

**Signature:** `get_decorator(self, name: str) -> Optional[Type[prompt_decorators.core.base.DecoratorBase]]`

**Parameters:**

- `name`: `str`

**Returns:** `Optional`

##### `get_decorator_instance`

Get a decorator instance by name.

Args:
    name: The name of the decorator instance to retrieve

Returns:
    The decorator instance if found, None otherwise

**Signature:** `get_decorator_instance(self, name: str) -> Optional[prompt_decorators.core.base.DecoratorBase]`

**Parameters:**

- `name`: `str`

**Returns:** `Optional`

##### `register_all_from_directory`

Register all decorators from Python files in a directory.

Args:
    directory: The directory to scan for decorator modules

Returns:
    Number of decorators registered

Note:
    This method will import all Python files in the directory and
    register any classes that inherit from BaseDecorator.

**Signature:** `register_all_from_directory(self, directory: str) -> int`

**Parameters:**

- `directory`: `str`

**Returns:** `int`

##### `register_all_from_json_directory`

Register all decorators from JSON files in a directory.

Args:
    directory: The directory to scan for JSON files

Returns:
    Number of decorators registered

Note:
    This method will attempt to register a decorator from each JSON file
    in the specified directory.

**Signature:** `register_all_from_json_directory(self, directory: str) -> int`

**Parameters:**

- `directory`: `str`

**Returns:** `int`

##### `register_decorator`

Register a decorator class.

Args:
    decorator_class: The decorator class to register

Returns:
    None

**Signature:** `register_decorator(self, decorator_class: Type[prompt_decorators.core.base.DecoratorBase]) -> None`

**Parameters:**

- `decorator_class`: `Type`

##### `register_decorator_instance`

Register a decorator instance.

Args:
    decorator: The decorator instance to register

Returns:
    None

**Signature:** `register_decorator_instance(self, decorator: prompt_decorators.core.base.DecoratorBase) -> None`

**Parameters:**

- `decorator`: `DecoratorBase`

##### `register_from_json_file`

Register a decorator from a JSON file.

Args:
    file_path: Path to the JSON file

Returns:
    The registered decorator class if successful, None otherwise

Raises:
    ValueError: If the file cannot be read or contains invalid JSON

**Signature:** `register_from_json_file(self, file_path: str) -> Optional[Type[prompt_decorators.core.base.DecoratorBase]]`

**Parameters:**

- `file_path`: `str`

**Returns:** `Optional`

##### `register_from_json_string`

Register a decorator from a JSON string.

Args:
    json_string: JSON string defining a decorator

Returns:
    The registered decorator class if successful, None otherwise

Raises:
    ValueError: If the JSON is invalid or missing required fields

**Signature:** `register_from_json_string(self, json_string: str) -> Optional[Type[prompt_decorators.core.base.DecoratorBase]]`

**Parameters:**

- `json_string`: `str`

**Returns:** `Optional`

## Functions

### `get_registry`

Get the global decorator registry.

Returns:
    The global decorator registry instance

**Signature:** `get_registry() -> prompt_decorators.utils.discovery.DecoratorRegistry`

**Returns:** `DecoratorRegistry`
