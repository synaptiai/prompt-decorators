# Decorator `Summary`

**Version:** 1.0.0

Provides a condensed summary of information that would otherwise be presented in a more detailed format. This decorator is useful for generating executive summaries, article summaries, or concise overviews of complex topics.

## Parameters

### `length`

**Type:** enum
**Required:** No
**Default:** `medium`

Relative length of the summary

**Allowed values:**

- `short`
- `medium`
- `long`

### `wordCount`

**Type:** number
**Required:** No

Approximate target word count for the summary

### `position`

**Type:** enum
**Required:** No
**Default:** `standalone`

Where to position the summary in relation to any full content

**Allowed values:**

- `beginning`
- `end`
- `standalone`

## Examples

### Short standalone summary of a complex topic

```
+++Summary(length=short)
Explain quantum computing and its potential applications.
```

Result:

Delivers a concise overview of quantum computing and its applications in approximately 2-3 sentences

### Specific word count summary at the beginning of a response

```
+++Summary(wordCount=100, position=beginning)
Describe the causes and effects of climate change.
```

Result:

Starts with a 100-word summary of climate change causes and effects, followed by more detailed information

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

**Signature:** `__init__(length=medium, wordCount, position=standalone) -> <class 'NoneType'>`

Initialize the Summary decorator.

Args:
    length: Relative length of the summary
    wordCount: Approximate target word count for the summary
    position: Where to position the summary in relation to any full content


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
