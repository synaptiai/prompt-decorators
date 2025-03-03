# Decorator `Remix`

**Version:** 1.0.0

Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.

## Parameters

### `target`

**Type:** string
**Required:** Yes

The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch')

### `preserve`

**Type:** enum
**Required:** No
**Default:** `facts`

What aspects of the original content to prioritize preserving

**Allowed values:**

- `facts`
- `structure`
- `tone`
- `comprehensiveness`

### `contrast`

**Type:** boolean
**Required:** No

Whether to highlight differences between the original framing and the remixed version

## Examples

### Basic remix for a different audience

```
+++Remix(target=high school students)
Explain how neural networks function in artificial intelligence.
```

Result:

Reframes the technical explanation of neural networks to be accessible and engaging for high school students while preserving the core facts

### Business remix with contrasting approach

```
+++Remix(target=board presentation, preserve=comprehensiveness, contrast=true)
Describe the technical details of our new software architecture.
```

Result:

Transforms the technical software architecture description into a board-appropriate presentation format, maintaining comprehensive coverage while highlighting how this differs from a technical explanation

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(target, preserve=RemixPreserveEnum.FACTS, contrast=False)`

Initialize Remix decorator.

Args:
    target: The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch')
    preserve: What aspects of the original content to prioritize preserving
    contrast: Whether to highlight differences between the original framing and the remixed version

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
