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

**Signature:** `__init__(intensity=moderate, focus=balanced, actionable=True) -> <class 'NoneType'>`

Initialize the Motivational decorator.

Args:
    intensity: The level of motivational energy and enthusiasm
    focus: The primary motivational approach to emphasize
    actionable: Whether to include specific actionable steps or only inspirational content


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

This method transforms the prompt using the transformation template.

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
