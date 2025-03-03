# Decorator `BlindSpots`

**Version:** 1.0.0

Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.

## Parameters

### `categories`

**Type:** array
**Required:** No

Specific categories of blind spots to check for (e.g., cultural, temporal, confirmation bias)

### `depth`

**Type:** enum
**Required:** No
**Default:** `thorough`

How thoroughly to analyze for blind spots

**Allowed values:**

- `basic`
- `thorough`
- `comprehensive`

### `position`

**Type:** enum
**Required:** No
**Default:** `after`

Where to place the blind spots analysis

**Allowed values:**

- `after`
- `before`
- `integrated`

## Examples

### Basic blind spots analysis after a response

```
+++BlindSpots
What factors drive economic growth?
```

Result:

Provides an analysis of economic growth factors, followed by identification of unstated assumptions and potential blind spots in the analysis

### Comprehensive blind spots analysis integrated throughout

```
+++BlindSpots(categories=[cultural,historical,methodological], depth=comprehensive, position=integrated)
Evaluate the impact of social media on society.
```

Result:

Delivers an evaluation of social media's societal impact with comprehensive blind spot analysis woven throughout, specifically addressing cultural, historical, and methodological blind spots

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(categories, depth=BlindSpotsDepthEnum.THOROUGH, position=BlindSpotsPositionEnum.AFTER)`

Initialize BlindSpots decorator.

Args:
    categories: Specific categories of blind spots to check for (e.g., cultural, temporal, confirmation bias)
    depth: How thoroughly to analyze for blind spots
    position: Where to place the blind spots analysis

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
