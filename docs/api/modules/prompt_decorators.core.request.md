# request

Request handling for prompt decorators.

This module provides the DecoratedRequest class for managing decorated prompts.

## Classes

### `DecoratedRequest`

Class representing a request decorated with prompt decorators.

#### Attributes

- `from_dict`: `classmethod` = `<classmethod(<function DecoratedRequest.from_dict at 0x105c199e0>)>`
- `from_json`: `classmethod` = `<classmethod(<function DecoratedRequest.from_json at 0x105c19a80>)>`

#### Methods

##### `__init__`

Initialize a decorated request.

Args:
    prompt: The base prompt text
    decorators: Optional list of decorators to apply
    model: Optional model identifier
    api_params: Optional additional API parameters

**Signature:** `__init__(self, prompt: str, decorators: Optional[List[prompt_decorators.core.base.DecoratorBase]] = None, model: Optional[str] = None, api_params: Optional[Dict[str, Any]] = None)`

**Parameters:**

- `prompt`: `str`
- `decorators`: `Optional` (default: `None`)
- `model`: `Optional` (default: `None`)
- `api_params`: `Optional` (default: `None`)

##### `add_decorator`

Add a decorator to the request.

Args:
    decorator: The decorator to add

Returns:
    Self for method chaining

Raises:
    ValueError: If a decorator with the same name already exists

**Signature:** `add_decorator(self, decorator: prompt_decorators.core.base.DecoratorBase) -> 'DecoratedRequest'`

**Parameters:**

- `decorator`: `DecoratorBase`

**Returns:** `DecoratedRequest`

##### `apply_decorators`

Apply all decorators to the prompt.

Args:
    self: The request instance

Returns:
    The decorated prompt text

Note:
    Decorators are applied in the order they were added.
    This allows for composing decorators in a specific sequence.

**Signature:** `apply_decorators(self) -> str`

**Parameters:**


**Returns:** `str`

##### `get_decorator`

Get a decorator by name.

Args:
    decorator_name: Name of the decorator to retrieve

Returns:
    The decorator if found, None otherwise

**Signature:** `get_decorator(self, decorator_name: str) -> Optional[prompt_decorators.core.base.DecoratorBase]`

**Parameters:**

- `decorator_name`: `str`

**Returns:** `Optional`

##### `remove_decorator`

Remove a decorator by name.

Args:
    decorator_name: Name of the decorator to remove

Returns:
    True if the decorator was removed, False if not found

**Signature:** `remove_decorator(self, decorator_name: str) -> bool`

**Parameters:**

- `decorator_name`: `str`

**Returns:** `bool`

##### `to_dict`

Convert the request to a dictionary representation.

Args:
    self: The request instance

Returns:
    Dictionary representation of the request

**Signature:** `to_dict(self) -> Dict[str, Any]`

**Parameters:**


**Returns:** `Dict`

##### `to_json`

Convert the request to a JSON string.

Args:
    indent: Optional indentation for pretty-printing

Returns:
    JSON string representation of the request

**Signature:** `to_json(self, indent: Optional[int] = None) -> str`

**Parameters:**

- `indent`: `Optional` (default: `None`)

**Returns:** `str`
