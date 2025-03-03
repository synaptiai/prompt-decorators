# Decorator `StyleShift`

**Version:** 1.0.0

Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.

## Parameters

### `aspect`

**Type:** enum
**Required:** Yes

The specific style aspect to modify

**Allowed values:**

- `formality`
- `persuasion`
- `urgency`
- `confidence`
- `complexity`

### `level`

**Type:** number
**Required:** No
**Default:** `3`

The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal)

### `maintain`

**Type:** array
**Required:** No

Style aspects to explicitly maintain while modifying the target aspect

## Examples

### Highly formal style while maintaining normal complexity

```
+++StyleShift(aspect=formality, level=5, maintain=[complexity])
Explain the process of photosynthesis.
```

Result:

Provides a highly formal explanation of photosynthesis with elevated language and structure, while keeping the complexity at a moderate level

### Increased urgency for a business communication

```
+++StyleShift(aspect=urgency, level=4)
Describe the steps needed to prepare for the upcoming product launch.
```

Result:

Delivers a description of product launch preparation steps with heightened sense of urgency and time-sensitivity in the language and framing

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(aspect, level=3, maintain)`

Initialize StyleShift decorator.

Args:
    aspect: The specific style aspect to modify
    level: The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal)
    maintain: Style aspects to explicitly maintain while modifying the target aspect

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
