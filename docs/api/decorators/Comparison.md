# Decorator `Comparison`

**Version:** 1.0.0

Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.

## Parameters

### `aspects`

**Type:** array
**Required:** No

Specific aspects or dimensions to compare

### `format`

**Type:** enum
**Required:** No
**Default:** `table`

The presentation format for the comparison

**Allowed values:**

- `table`
- `prose`
- `bullets`

### `highlight`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to explicitly emphasize key differences

## Examples

### Basic tabular comparison of specific aspects

```
+++Comparison(aspects=[performance,cost,ease of use,ecosystem])
Compare React, Angular, and Vue for front-end development.
```

Result:

Creates a table comparing React, Angular, and Vue across the specified aspects, with key differences highlighted

### Prose-based comparison without specific aspects

```
+++Comparison(format=prose, highlight=false)
Compare democracy and authoritarianism as political systems.
```

Result:

Delivers a flowing prose comparison between democracy and authoritarianism, covering key differences and similarities in paragraph form

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(aspects, format=ComparisonFormatEnum.TABLE, highlight=True)`

Initialize Comparison decorator.

Args:
    aspects: Specific aspects or dimensions to compare
    format: The presentation format for the comparison
    highlight: Whether to explicitly emphasize key differences

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
