# Decorator `Concise`

**Version:** 1.0.0

Optimizes the response for brevity and directness, eliminating unnecessary details and verbose language. This decorator is ideal for obtaining quick answers, executive summaries, or essential information when time or space is limited.

## Parameters

### `maxWords`

**Type:** number
**Required:** No

Maximum word count for the entire response

### `bulletPoints`

**Type:** boolean
**Required:** No

Whether to use bullet points for maximum brevity

### `level`

**Type:** enum
**Required:** No
**Default:** `moderate`

The degree of conciseness to apply

**Allowed values:**

- `moderate`
- `high`
- `extreme`

## Examples

### Basic concise explanation of a complex topic

```
+++Concise
Explain how blockchain technology works.
```

Result:

Provides a brief, to-the-point explanation of blockchain technology focusing only on essential concepts

### Extremely concise bulleted answer with word limit

```
+++Concise(maxWords=50, bulletPoints=true, level=extreme)
What are the key factors in successful project management?
```

Result:

Delivers a set of extremely concise bullet points covering only the most critical project management factors, totaling under 50 words

## Compatibility

**Conflicts with:**

- `Detailed`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(maxWords, bulletPoints=False, level=ConciseLevelEnum.MODERATE)`

Initialize Concise decorator.

Args:
    maxWords: Maximum word count for the entire response
    bulletPoints: Whether to use bullet points for maximum brevity
    level: The degree of conciseness to apply

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
