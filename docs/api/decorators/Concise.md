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

**Signature:** `__init__(maxWords, bulletPoints=False, level=moderate) -> <class 'NoneType'>`

Initialize the Concise decorator.

Args:
    maxWords: Maximum word count for the entire response
    bulletPoints: Whether to use bullet points for maximum brevity
    level: The degree of conciseness to apply

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

Returns:
    Dictionary representation of the decorator

#### `to_string`

**Signature:** `to_string() -> <class 'str'>`

Convert the decorator to a string.

Returns:
    String representation of the decorator

#### `transform_response`

**Signature:** `transform_response(response) -> <class 'str'>`

Transform the response from the model.

Args:
    response: The response to transform

Returns:
    The transformed response
