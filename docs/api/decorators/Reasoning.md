# Decorator `Reasoning`

**Version:** 1.0.0

Modifies the AI's response to provide explicit reasoning paths before reaching conclusions. This decorator encourages the model to show its thought process, making responses more transparent and trustworthy.

## Parameters

### `depth`

**Type:** enum
**Required:** No
**Default:** `moderate`

The level of detail in the reasoning process

**Allowed values:**

- `basic`
- `moderate`
- `comprehensive`

## Examples

### Basic reasoning for a simple question

```
+++Reasoning(depth=basic)
What is the best programming language for beginners?
```

Result:

Provides a brief explanation of key factors before recommending a language

### Comprehensive analysis of a complex topic

```
+++Reasoning(depth=comprehensive)
What are the implications of quantum computing for cybersecurity?
```

Result:

Delivers an in-depth analysis covering multiple aspects and their interconnections

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(depth=moderate) -> <class 'NoneType'>`

Initialize the Reasoning decorator.

Args:
    depth: The level of detail in the reasoning process


Returns:
    None

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the decorator to a prompt string.

Args:
    prompt: The prompt to apply the decorator to


Returns:
    The modified prompt

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


Args:
    cls: The decorator class

#### `is_compatible_with_version`

**Signature:** `is_compatible_with_version(version) -> <class 'bool'>`

Check if the decorator is compatible with a specific version.

Args:
    version: The version to check compatibility with.


Returns:
    True if compatible, False otherwise.


Raises:
    IncompatibleVersionError: If the version is incompatible.

#### `to_dict`

**Signature:** `to_dict() -> typing.Dict[str, typing.Any]`

Convert the decorator to a dictionary.

Args:
    self: The decorator instance

Returns:
    Dictionary representation of the decorator

#### `to_string`

**Signature:** `to_string() -> <class 'str'>`

Convert the decorator to a string.

Args:
    self: The decorator instance

Returns:
    String representation of the decorator

#### `transform_response`

**Signature:** `transform_response(response) -> <class 'str'>`

Transform the response from the model.

Args:
    response: The response to transform

Returns:
    The transformed response
