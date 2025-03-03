# Decorator `Limitations`

**Version:** 1.0.0

Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.

## Parameters

### `detail`

**Type:** enum
**Required:** No
**Default:** `moderate`

The level of detail in the limitations statement

**Allowed values:**

- `brief`
- `moderate`
- `comprehensive`

### `position`

**Type:** enum
**Required:** No
**Default:** `end`

Where to place the limitations statement in the response

**Allowed values:**

- `beginning`
- `end`

### `focus`

**Type:** enum
**Required:** No
**Default:** `all`

The primary aspect to focus on in the limitations

**Allowed values:**

- `knowledge`
- `methodology`
- `context`
- `biases`
- `all`

## Examples

### Brief limitations statement at the end focused on methodology

```
+++Limitations(detail=brief, focus=methodology)
Explain how personality tests predict career success.
```

Result:

Explains personality tests and career success, concluding with a brief statement of methodological limitations

### Comprehensive limitations at the beginning covering all aspects

```
+++Limitations(detail=comprehensive, position=beginning, focus=all)
Describe the current understanding of consciousness.
```

Result:

Begins with a thorough discussion of the limitations in our understanding of consciousness before presenting the current state of knowledge

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(detail=moderate, position=end, focus=all) -> <class 'NoneType'>`

Initialize the Limitations decorator.

Args:
    detail: The level of detail in the limitations statement
    position: Where to place the limitations statement in the response
    focus: The primary aspect to focus on in the limitations

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
