# Module `prompt_decorators.utils.discovery`

Decorator Discovery Module

This module provides utilities for discovering and registering decorators at runtime.

## Classes

- [`DecoratorRegistry`](#class-decoratorregistry): Registry for prompt decorators.

### Class `DecoratorRegistry`

Registry for prompt decorators.

This class provides methods for registering and discovering decorators at runtime.

#### Methods

- `__init__()`
- `clear()`
- `create_decorator(name, parameters) -> typing.Optional[prompt_decorators.core.base.BaseDecorator]`
- `find_decorators_by_category(category) -> typing.Dict[str, typing.Type[prompt_decorators.core.base.BaseDecorator]]`
- `get_all_decorator_instances() -> typing.Dict[str, prompt_decorators.core.base.BaseDecorator]`
- `get_all_decorators() -> typing.Dict[str, typing.Type[prompt_decorators.core.base.BaseDecorator]]`
- `get_categories() -> typing.Set[str]`
- `get_decorator(name) -> typing.Optional[typing.Type[prompt_decorators.core.base.BaseDecorator]]`
- `get_decorator_instance(name) -> typing.Optional[prompt_decorators.core.base.BaseDecorator]`
- `register_all_from_directory(directory) -> <class 'int'>`
- `register_all_from_json_directory(directory) -> <class 'int'>`
- `register_decorator(decorator_class) -> <class 'NoneType'>`
- `register_decorator_instance(decorator) -> <class 'NoneType'>`
- `register_from_json_file(file_path) -> typing.Optional[typing.Type[prompt_decorators.core.base.BaseDecorator]]`
- `register_from_json_string(json_string) -> typing.Optional[typing.Type[prompt_decorators.core.base.BaseDecorator]]`

## Functions

- [`get_registry`](#function-get_registry): Get the global decorator registry.

### Function `get_registry`

**Signature:** `get_registry() -> <class 'prompt_decorators.utils.discovery.DecoratorRegistry'>`

Get the global decorator registry.

Returns:
    The global decorator registry instance
