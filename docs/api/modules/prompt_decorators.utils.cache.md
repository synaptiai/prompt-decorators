# Module `prompt_decorators.utils.cache`

Decorator Cache Module

This module provides a caching system for decorator definitions and instances.

## Classes

- [`DecoratorCache`](#class-decoratorcache): Cache for decorator definitions and instances.

### Class `DecoratorCache`

Cache for decorator definitions and instances.

This class provides a caching system for decorator definitions and instances,
with support for cache invalidation and metrics.

#### Methods

- `clear() -> <class 'NoneType'>`
- `get_class(key) -> typing.Optional[typing.Type[prompt_decorators.core.base.BaseDecorator]]`
- `get_config() -> typing.Dict[str, typing.Any]`
- `get_definition(key) -> typing.Optional[typing.Dict[str, typing.Any]]`
- `get_instance(key) -> typing.Optional[prompt_decorators.core.base.BaseDecorator]`
- `get_metrics() -> typing.Dict[str, typing.Any]`
- `invalidate_definition(key) -> <class 'bool'>`
- `invalidate_instance(key) -> <class 'bool'>`
- `set_class(key, decorator_class) -> <class 'NoneType'>`
- `set_config(config) -> <class 'NoneType'>`
- `set_definition(key, definition) -> <class 'NoneType'>`
- `set_instance(key, instance) -> <class 'NoneType'>`

## Functions

- [`get_cache`](#function-get_cache): Get the global decorator cache.

### Function `get_cache`

**Signature:** `get_cache() -> <class 'prompt_decorators.utils.cache.DecoratorCache'>`

Get the global decorator cache.

Returns:
    The global decorator cache instance

