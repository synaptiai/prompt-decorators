# Decorator `Uncertainty`

**Version:** 1.0.0

Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.

## Parameters

### `format`

**Type:** enum
**Required:** No
**Default:** `inline`

How to format uncertainty indications in the response

**Allowed values:**

- `inline`
- `section`
- `confidence`

### `threshold`

**Type:** enum
**Required:** No
**Default:** `medium`

The threshold for flagging uncertain content

**Allowed values:**

- `low`
- `medium`
- `high`

### `reason`

**Type:** boolean
**Required:** No

Whether to explain the reason for uncertainty

## Examples

### Inline uncertainty markers in a technical explanation

```
+++Uncertainty
Explain the potential timeline for achieving artificial general intelligence.
```

Result:

Explains AGI timelines with inline uncertainty markers highlighting speculative predictions, areas of expert disagreement, and knowledge gaps

### Dedicated uncertainty section with detailed reasoning

```
+++Uncertainty(format=section, reason=true, threshold=low)
What are the environmental impacts of fusion energy?
```

Result:

Provides information about fusion energy's environmental impacts followed by a dedicated section discussing all points of uncertainty with explanations for why each point is uncertain

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(format=UncertaintyFormatEnum.INLINE, threshold=UncertaintyThresholdEnum.MEDIUM, reason=False)`

Initialize Uncertainty decorator.

Args:
    format: How to format uncertainty indications in the response
    threshold: The threshold for flagging uncertain content
    reason: Whether to explain the reason for uncertainty

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
