# Decorator `Constraints`

**Version:** 1.0.0

Applies specific limitations to the output format, length, or content. This decorator enforces creative constraints that can enhance focus, brevity, or precision by requiring the response to work within defined boundaries.

## Parameters

### `wordCount`

**Type:** number
**Required:** No

Maximum number of words allowed in the response

### `timeframe`

**Type:** string
**Required:** No

Maximum time required to implement or consume the response (e.g., '5min', '1hr', '1week')

### `vocabulary`

**Type:** enum
**Required:** No

Constraints on vocabulary usage

**Allowed values:**

- `simple`
- `technical`
- `domain-specific`
- `creative`

### `custom`

**Type:** string
**Required:** No

Custom constraint to apply (e.g., 'no negatives', 'use only questions', 'each sentence starts with consecutive letters of the alphabet')

## Examples

### Word count constraint for a complex topic

```
+++Constraints(wordCount=100)
Explain quantum computing principles.
```

Result:

Provides a concise explanation of quantum computing, carefully limiting the response to exactly 100 words

### Multiple constraints for a creative response

```
+++Constraints(wordCount=200, vocabulary=creative, custom=each paragraph must contain exactly three sentences)
Describe a futuristic city.
```

Result:

Delivers a 200-word description of a futuristic city using creative vocabulary, with each paragraph containing exactly three sentences

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(wordCount, timeframe, vocabulary, custom)`

Initialize Constraints decorator.

Args:
    wordCount: Maximum number of words allowed in the response
    timeframe: Maximum time required to implement or consume the response (e.g., '5min', '1hr', '1week')
    vocabulary: Constraints on vocabulary usage
    custom: Custom constraint to apply (e.g., 'no negatives', 'use only questions', 'each sentence starts with consecutive letters of the alphabet')

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
