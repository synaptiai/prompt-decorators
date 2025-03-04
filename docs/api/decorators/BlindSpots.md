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

**Signature:** `__init__(categories, depth=thorough, position=after) -> <class 'NoneType'>`

Initialize the BlindSpots decorator.

Args:
    categories: Specific categories of blind spots to check for (e.g., cultural, temporal, confirmation bias)
    depth: How thoroughly to analyze for blind spots
    position: Where to place the blind spots analysis


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
