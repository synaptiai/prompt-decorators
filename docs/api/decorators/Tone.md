# Decorator `Tone`

**Version:** 1.0.0

Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.

## Parameters

### `style`

**Type:** enum
**Required:** Yes
**Default:** `formal`

The desired tone and style for the response

**Allowed values:**

- `formal`
- `casual`
- `friendly`
- `technical`
- `humorous`

## Examples

### Technical documentation tone

```
+++Tone(style=technical)
Explain how garbage collection works in Python
```

Result:

Provides a technically precise explanation using appropriate terminology

### Casual explanation

```
+++Tone(style=casual)
Why is the sky blue?
```

Result:

Delivers a relaxed, conversational explanation of atmospheric optics

## Compatibility

**Conflicts with:**

- `ELI5`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(style) -> <class 'NoneType'>`

Initialize the Tone decorator.

Args:
    style: The desired tone and style for the response

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
