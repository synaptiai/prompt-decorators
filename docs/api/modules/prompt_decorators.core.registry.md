# registry

Registry for prompt decorators.

This module maintains a global registry of all available decorators and provides
functions for registering and retrieving them.

## Classes

### `DecoratorRegistry`

Registry class for managing prompt decorators.

This class provides an object-oriented interface to the decorator registry,
allowing for easier management and access to registered decorators.

#### Attributes

- `categories`: `property` = `<property object at 0x106517e20>`
- `decorators`: `property` = `<property object at 0x106517dd0>`

#### Methods

##### `__init__`

Initialize the decorator registry.

**Signature:** `__init__(self) -> None`

**Parameters:**


##### `clear`

Clear the registry.

**Signature:** `clear(self) -> None`

**Parameters:**


##### `get_by_category`

Get all decorators in a category.

Args:
    category: The category to get decorators for

Returns:
    List of decorator classes in the category

**Signature:** `get_by_category(self, category: str) -> List[Type[prompt_decorators.core.base.DecoratorBase]]`

**Parameters:**

- `category`: `str`

**Returns:** `List`

##### `get_decorator`

Get a decorator class by name.

Args:
    name: The name of the decorator to get

Returns:
    The decorator class, or None if not found

**Signature:** `get_decorator(self, name: str) -> Optional[Type[prompt_decorators.core.base.DecoratorBase]]`

**Parameters:**

- `name`: `str`

**Returns:** `Optional`

##### `register`

Register a decorator class.

Args:
    decorator_class: The decorator class to register
    category: The category to register the decorator under

Returns:
    None

**Signature:** `register(self, decorator_class: Type[prompt_decorators.core.base.DecoratorBase], category: str = 'unknown') -> None`

**Parameters:**

- `decorator_class`: `Type`
- `category`: `str` (default: `unknown`)

## Functions

### `clear_registry`

Clear the global decorator registry.

**Signature:** `clear_registry() -> None`

### `get_categories`

Get all decorator categories from the global registry.

Returns:
    Dictionary mapping category names to sets of decorator names

**Signature:** `get_categories() -> Dict[str, Set[str]]`

**Returns:** `Dict`

### `get_decorator`

Get a decorator class by name from the global registry.

Args:
    name: The name of the decorator to get

Returns:
    The decorator class, or None if not found

**Signature:** `get_decorator(name: str) -> Optional[Type[prompt_decorators.core.base.DecoratorBase]]`

**Parameters:**

- `name`: `str`

**Returns:** `Optional`

### `get_decorators_by_category`

Get all decorators in a category from the global registry.

Args:
    category: The category to get decorators for

Returns:
    List of decorator classes in the category

**Signature:** `get_decorators_by_category(category: str) -> List[Type[prompt_decorators.core.base.DecoratorBase]]`

**Parameters:**

- `category`: `str`

**Returns:** `List`

### `get_registry`

Get the global decorator registry.

Returns:
    Dictionary mapping decorator names to decorator classes

**Signature:** `get_registry() -> Dict[str, Type[prompt_decorators.core.base.DecoratorBase]]`

**Returns:** `Dict`

### `register_decorator`

Register a decorator class in the global registry.

This function registers a decorator class in the global registry,
making it available for use in the system.

Args:
    decorator_class: The decorator class to register
    category: The category to register the decorator under

Returns:
    None

**Signature:** `register_decorator(decorator_class: Type[prompt_decorators.core.base.DecoratorBase], category: str = 'unknown') -> None`

**Parameters:**

- `decorator_class`: `Type`
- `category`: `str` (default: `unknown`)
