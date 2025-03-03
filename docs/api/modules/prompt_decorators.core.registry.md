# Module `prompt_decorators.core.registry`

Registry for prompt decorators.

This module maintains a global registry of all available decorators and provides
functions for registering and retrieving them.

## Functions

- [`clear_registry`](#function-clear_registry): Clear the decorator registry.
- [`get_categories`](#function-get_categories): Get all decorator categories and their members.
- [`get_decorator`](#function-get_decorator): Get a decorator class by name.
- [`get_decorators_by_category`](#function-get_decorators_by_category): Get all decorators in a specific category.
- [`get_registry`](#function-get_registry): Get the complete decorator registry.
- [`register_decorator`](#function-register_decorator): Register a decorator class in the global registry.

### Function `clear_registry`

**Signature:** `clear_registry() -> <class 'NoneType'>`

Clear the decorator registry.

This is primarily used for testing.

Returns:
    None

### Function `get_categories`

**Signature:** `get_categories() -> typing.Dict[str, typing.Set[str]]`

Get all decorator categories and their members.

Returns:
    Dictionary mapping category names to sets of decorator names

### Function `get_decorator`

**Signature:** `get_decorator(name) -> typing.Optional[typing.Type[prompt_decorators.core.base.BaseDecorator]]`

Get a decorator class by name.

Args:
    name: Name of the decorator

Returns:
    The decorator class if found, None otherwise

### Function `get_decorators_by_category`

**Signature:** `get_decorators_by_category(category) -> typing.List[typing.Type[prompt_decorators.core.base.BaseDecorator]]`

Get all decorators in a specific category.

Args:
    category: The category name

Returns:
    List of decorator classes in the specified category

### Function `get_registry`

**Signature:** `get_registry() -> typing.Dict[str, typing.Type[prompt_decorators.core.base.BaseDecorator]]`

Get the complete decorator registry.

Returns:
    Dictionary mapping decorator names to decorator classes

### Function `register_decorator`

**Signature:** `register_decorator(decorator_class, category=unknown) -> <class 'NoneType'>`

Register a decorator class in the global registry.

Args:
    decorator_class: The decorator class to register
    category: Optional category for organizing decorators

Returns:
    None
