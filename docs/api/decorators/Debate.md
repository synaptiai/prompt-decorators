# Decorator `Debate`

**Version:** 1.0.0

Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.

## Parameters

### `perspectives`

**Type:** number
**Required:** No
**Default:** `2`

Number of different perspectives to include in the debate

### `balanced`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to ensure equal representation and strength of arguments for each perspective

## Examples

### Two-perspective debate on an ethical issue

```
+++Debate
Is it ethical to use AI-generated content without disclosure?
```

Result:

Presents balanced arguments for and against disclosure of AI-generated content

### Three-perspective debate on a policy issue with balanced representation

```
+++Debate(perspectives=3, balanced=true)
Should universal basic income be implemented nationally?
```

Result:

Presents three balanced perspectives on UBI in a debate format, ensuring equal representation of each viewpoint

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`
- `claude-3`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(perspectives=2, balanced=True)`

Initialize Debate decorator.

Args:
    perspectives: Number of different perspectives to include in the debate
    balanced: Whether to ensure equal representation and strength of arguments for each perspective

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
