# Decorator `MECE`

**Version:** 1.0.0

Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.

## Parameters

### `dimensions`

**Type:** number
**Required:** No
**Default:** `3`

Number of top-level MECE dimensions to use for categorization

### `depth`

**Type:** number
**Required:** No
**Default:** `2`

Maximum level of hierarchical breakdown within each dimension

### `framework`

**Type:** enum
**Required:** No
**Default:** `custom`

Optional predefined MECE framework to apply

**Allowed values:**

- `issue tree`
- `value chain`
- `business segments`
- `stakeholders`
- `custom`

## Examples

### Basic MECE analysis of a business problem

```
+++MECE
What factors should we consider when expanding to a new market?
```

Result:

Organizes market expansion factors into 3 mutually exclusive, collectively exhaustive categories with no overlaps and full coverage of all considerations

### Detailed MECE framework with stakeholder focus

```
+++MECE(dimensions=4, depth=3, framework=stakeholders)
Analyze the implications of implementing a four-day work week.
```

Result:

Provides a 4-dimension MECE analysis of a four-day work week using a stakeholder framework, with up to 3 levels of hierarchical breakdown within each stakeholder category

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(dimensions=3, depth=2, framework=MECEFrameworkEnum.CUSTOM)`

Initialize MECE decorator.

Args:
    dimensions: Number of top-level MECE dimensions to use for categorization
    depth: Maximum level of hierarchical breakdown within each dimension
    framework: Optional predefined MECE framework to apply

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
