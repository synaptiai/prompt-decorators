# cache

Decorator Cache Module.

This module provides a caching system for decorator definitions and instances.

## Module Variables

### `cache`

Type: `DecoratorCache`

Value: `<prompt_decorators.utils.cache.DecoratorCache object at 0x1073d5710>`

### `logger`

Type: `Logger`

Value: `<Logger prompt_decorators.utils.cache (INFO)>`

## Classes

### `DecoratorCache`

Cache for decorator definitions and instances.

This class provides a caching system for decorator definitions and instances,
with support for cache invalidation and metrics.

#### Methods

##### `clear`

Clear the cache.

**Signature:** `clear(self) -> None`

**Parameters:**


##### `get_class`

Get a decorator class from the cache.

Args:
    key: The cache key for the class

Returns:
    The decorator class, or None if not found

**Signature:** `get_class(self, key: str) -> Optional[Type[prompt_decorators.core.base.DecoratorBase]]`

**Parameters:**

- `key`: `str`

**Returns:** `Optional`

##### `get_config`

Get the current cache configuration.

Args:
    self: The DecoratorCache instance

Returns:
    Dictionary with configuration options

**Signature:** `get_config(self) -> Dict[str, Any]`

**Parameters:**


**Returns:** `Dict`

##### `get_definition`

Get a decorator definition from the cache.

Args:
    key: The cache key for the definition

Returns:
    The decorator definition, or None if not found or expired

**Signature:** `get_definition(self, key: str) -> Optional[Dict[str, Any]]`

**Parameters:**

- `key`: `str`

**Returns:** `Optional`

##### `get_instance`

Get a decorator instance from the cache.

Args:
    key: The cache key for the instance

Returns:
    The decorator instance, or None if not found or expired

**Signature:** `get_instance(self, key: str) -> Optional[prompt_decorators.core.base.DecoratorBase]`

**Parameters:**

- `key`: `str`

**Returns:** `Optional`

##### `get_metrics`

Get cache metrics.

Args:
    self: The DecoratorCache instance

Returns:
    Dictionary with metrics

**Signature:** `get_metrics(self) -> Dict[str, Any]`

**Parameters:**


**Returns:** `Dict`

##### `invalidate_definition`

Invalidate a cached decorator definition.

Args:
    key: The cache key for the definition

Returns:
    True if the item was found and invalidated, False otherwise

**Signature:** `invalidate_definition(self, key: str) -> bool`

**Parameters:**

- `key`: `str`

**Returns:** `bool`

##### `invalidate_instance`

Invalidate a cached decorator instance.

Args:
    key: The cache key for the instance

Returns:
    True if the item was found and invalidated, False otherwise

**Signature:** `invalidate_instance(self, key: str) -> bool`

**Parameters:**

- `key`: `str`

**Returns:** `bool`

##### `set_class`

Store a decorator class in the cache.

Args:
    key: The cache key for the class
    decorator_class: The decorator class to store

Returns:
    None

**Signature:** `set_class(self, key: str, decorator_class: Type[prompt_decorators.core.base.DecoratorBase]) -> None`

**Parameters:**

- `key`: `str`
- `decorator_class`: `Type`

##### `set_config`

Update the cache configuration.

Args:
    config: Dictionary with configuration options to update

Returns:
    None

**Signature:** `set_config(self, config: Dict[str, Any]) -> None`

**Parameters:**

- `config`: `Dict`

##### `set_definition`

Store a decorator definition in the cache.

Args:
    key: The cache key for the definition
    definition: The decorator definition to store

Returns:
    None

**Signature:** `set_definition(self, key: str, definition: Dict[str, Any]) -> None`

**Parameters:**

- `key`: `str`
- `definition`: `Dict`

##### `set_instance`

Store a decorator instance in the cache.

Args:
    key: The cache key for the instance
    instance: The decorator instance to store

Returns:
    None

**Signature:** `set_instance(self, key: str, instance: prompt_decorators.core.base.DecoratorBase) -> None`

**Parameters:**

- `key`: `str`
- `instance`: `DecoratorBase`

## Functions

### `get_cache`

Get the global decorator cache instance.

Returns:
    The global decorator cache instance

**Signature:** `get_cache() -> prompt_decorators.utils.cache.DecoratorCache`

**Returns:** `DecoratorCache`
