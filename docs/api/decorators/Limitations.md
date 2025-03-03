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

**Signature:** `__init__(detail=LimitationsDetailEnum.MODERATE, position=LimitationsPositionEnum.END, focus=LimitationsFocusEnum.ALL)`

Initialize Limitations decorator.

Args:
    detail: The level of detail in the limitations statement
    position: Where to place the limitations statement in the response
    focus: The primary aspect to focus on in the limitations

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the decorator to a prompt.

Args:
    prompt: The original prompt

Returns:
    The modified prompt with the decorator applied

#### `from_dict`

**Signature:** `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator from a dictionary.

Args:
    data: Dictionary representation of a decorator

Returns:
    New decorator instance

Raises:
    ValueError: If the data is invalid or incompatible with this class
    IncompatibleVersionError: If the version is incompatible

#### `from_json`

**Signature:** `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator from a JSON string.

Args:
    json_str: JSON string representation of a decorator

Returns:
    New decorator instance

Raises:
    ValueError: If the JSON is invalid or incompatible with this class
    json.JSONDecodeError: If the JSON is malformed
    IncompatibleVersionError: If the version is incompatible

#### `get_metadata`

**Signature:** `get_metadata() -> typing.Dict[str, typing.Any]`

Get metadata about this decorator class.

Returns:
    Dictionary with decorator metadata

#### `get_version`

**Signature:** `get_version() -> <class 'prompt_decorators.core.base.Version'>`

Get the decorator version.

Returns:
    Version object for the decorator

#### `is_compatible_with_version`

**Signature:** `is_compatible_with_version(version_str) -> <class 'bool'>`

Check if this decorator is compatible with the specified version.

Args:
    version_str: Version string to check compatibility with

Returns:
    True if compatible, False otherwise

#### `to_dict`

**Signature:** `to_dict() -> typing.Dict[str, typing.Any]`

Convert decorator to a dictionary representation.

Returns:
    Dictionary representation of the decorator

#### `to_json`

**Signature:** `to_json(indent) -> <class 'str'>`

Convert decorator to a JSON string.

Args:
    indent: Optional indentation for pretty-printing

Returns:
    JSON string representation of the decorator

#### `validate`

**Signature:** `validate() -> <class 'NoneType'>`

Validate decorator parameters.

This base implementation does basic type checking.
Subclasses should override for specific validation.

Raises:
    ValidationError: If any parameter fails validation
