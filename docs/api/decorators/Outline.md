# Decorator `Outline`

**Version:** 1.0.0

Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics.

## Parameters

### `depth`

**Type:** number
**Required:** No
**Default:** `3`

Maximum nesting level of the outline

### `style`

**Type:** enum
**Required:** No
**Default:** `numeric`

Numbering or bullet style for the outline

**Allowed values:**

- `numeric`
- `bullet`
- `roman`
- `alpha`
- `mixed`

### `detailed`

**Type:** boolean
**Required:** No

Whether to include brief explanations under each outline point

## Examples

### Simple numeric outline of a complex topic

```
+++Outline
Explain the structure of the United States government.
```

Result:

Presents the US government structure as a numbered outline with up to 3 levels of hierarchy

### Detailed outline with mixed notation and deep hierarchy

```
+++Outline(style=mixed, depth=5, detailed=true)
Provide a comprehensive overview of machine learning techniques.
```

Result:

Creates a 5-level deep outline using mixed notation (numbers, letters, roman numerals) with brief explanations under each point, covering machine learning techniques

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(depth=3, style=OutlineStyleEnum.NUMERIC, detailed=False)`

Initialize Outline decorator.

Args:
    depth: Maximum nesting level of the outline
    style: Numbering or bullet style for the outline
    detailed: Whether to include brief explanations under each outline point

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
