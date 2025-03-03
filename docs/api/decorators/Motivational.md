# Decorator `Motivational`

**Version:** 1.0.0

Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.

## Parameters

### `intensity`

**Type:** enum
**Required:** No
**Default:** `moderate`

The level of motivational energy and enthusiasm

**Allowed values:**

- `mild`
- `moderate`
- `high`

### `focus`

**Type:** enum
**Required:** No
**Default:** `balanced`

The primary motivational approach to emphasize

**Allowed values:**

- `achievement`
- `growth`
- `resilience`
- `purpose`
- `balanced`

### `actionable`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to include specific actionable steps or only inspirational content

## Examples

### Basic moderately motivational response

```
+++Motivational
What are some strategies for building healthy habits?
```

Result:

Provides strategies for building healthy habits with moderate motivational language, encouraging tone, and confidence-building framing

### High-intensity resilience-focused motivational content

```
+++Motivational(intensity=high, focus=resilience, actionable=true)
How can I overcome setbacks in my professional life?
```

Result:

Delivers highly energetic and inspiring advice for professional resilience, emphasizing overcoming adversity with specific actionable steps, using powerful language and empowering framing

## Compatibility

**Conflicts with:**

- `Academic`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(intensity=MotivationalIntensityEnum.MODERATE, focus=MotivationalFocusEnum.BALANCED, actionable=True)`

Initialize Motivational decorator.

Args:
    intensity: The level of motivational energy and enthusiasm
    focus: The primary motivational approach to emphasize
    actionable: Whether to include specific actionable steps or only inspirational content

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
