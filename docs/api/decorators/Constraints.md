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

**Signature:** `__init__(wordCount, timeframe, vocabulary, custom) -> <class 'NoneType'>`

Initialize the Constraints decorator.

Args:
    wordCount: Maximum number of words allowed in the response
    timeframe: Maximum time required to implement or consume the response (e.g., '5min', '1hr', '1week')
    vocabulary: Constraints on vocabulary usage
    custom: Custom constraint to apply (e.g., 'no negatives', 'use only questions', 'each sentence starts with consecutive letters of the alphabet')


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
