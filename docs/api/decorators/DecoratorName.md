# Decorator `DecoratorName`

**Version:** 1.0.0

A detailed description of what the decorator does, its purpose, and how it modifies AI behavior.

## Parameters

### `parameterName`

**Type:** string|number|boolean|enum
**Required:** No
**Default:** `defaultValue`

Description of what this parameter does

## Examples

### Example of how to use this decorator with specific parameters

```
+++DecoratorName(parameterName=value)
User prompt text goes here
```

Result:

Expected behavior or output pattern from this decorator

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(parameterName=defaultValue) -> <class 'NoneType'>`

Initialize the DecoratorName decorator.

Args:
    parameterName: Description of what this parameter does

Returns:
    None

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the decorator to a prompt string.

Args:
    prompt: The original prompt string

Returns:
    The modified prompt string

#### `apply_to_prompt`

**Signature:** `apply_to_prompt(prompt) -> <class 'str'>`

Apply the decorator to a prompt.

Args:
    prompt: The prompt to decorate

Returns:
    The decorated prompt

#### `from_dict`

**Signature:** `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator instance from a dictionary representation.

Args:
    data: Dictionary representation of the decorator

Returns:
    A new decorator instance

Raises:
    ValidationError: If the dictionary is invalid

#### `get_metadata`

**Signature:** `get_metadata() -> typing.Dict[str, typing.Any]`

Get metadata about the decorator.

Returns:
    Dictionary containing metadata about the decorator

#### `is_compatible_with_version`

**Signature:** `is_compatible_with_version(version) -> <class 'bool'>`

Check if the decorator is compatible with a specific version.

Args:
    version: The version to check compatibility with

Returns:
    True if compatible, False otherwise

Raises:
    IncompatibleVersionError: If the version is incompatible

#### `to_dict`

**Signature:** `to_dict() -> typing.Dict[str, typing.Any]`

Convert the decorator to a dictionary.

Returns:
    Dictionary representation of the decorator

#### `to_string`

**Signature:** `to_string() -> <class 'str'>`

Convert the decorator to a string.

Returns:
    String representation of the decorator

#### `transform_response`

**Signature:** `transform_response(response) -> <class 'str'>`

Transform the response from the model.

Args:
    response: The response to transform

Returns:
    The transformed response
