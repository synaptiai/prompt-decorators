# Decorator `ELI5`

**Version:** 1.0.0

Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.

## Parameters

### `strictness`

**Type:** boolean
**Required:** No

Whether to strictly maintain a child-appropriate level of simplicity or allow slightly more complexity when necessary

## Examples

### Basic explanation of a complex scientific concept

```
+++ELI5
Explain how nuclear fusion works.
```

Result:

Explains nuclear fusion using simple language, analogies, and examples a child could understand

### Strict simplified explanation of a technical subject

```
+++ELI5(strictness=true)
How does the internet work?
```

Result:

Provides an extremely simplified explanation of the internet using only basic vocabulary and concrete examples appropriate for young children

## Compatibility

**Conflicts with:**

- `Academic`
- `Professional`
- `AsExpert`
- `Precision`
- `Tone`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(strictness=False) -> <class 'NoneType'>`

Initialize the ELI5 decorator.

Args:
    strictness: Whether to strictly maintain a child-appropriate level of simplicity or allow slightly more complexity when necessary


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

This method transforms the prompt using the transformation template.

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
