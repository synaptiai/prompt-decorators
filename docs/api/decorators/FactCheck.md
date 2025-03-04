# Decorator `FactCheck`

**Version:** 1.0.0

Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.

## Parameters

### `confidence`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to include explicit confidence levels for claims

### `uncertain`

**Type:** enum
**Required:** No
**Default:** `mark`

How to handle uncertain information

**Allowed values:**

- `mark`
- `exclude`
- `qualify`

### `strictness`

**Type:** enum
**Required:** No
**Default:** `moderate`

The threshold for considering information verified

**Allowed values:**

- `low`
- `moderate`
- `high`

## Examples

### Basic fact checking with confidence indicators

```
+++FactCheck
Explain the history and effectiveness of vaccines.
```

Result:

Provides information about vaccines with clear indications of confidence levels for different claims

### High-strictness fact checking that excludes uncertain information

```
+++FactCheck(strictness=high, uncertain=exclude)
Describe what we know about dark matter.
```

Result:

Presents only well-established scientific facts about dark matter, excluding speculative or uncertain information

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(confidence=True, uncertain=mark, strictness=moderate) -> <class 'NoneType'>`

Initialize the FactCheck decorator.

Args:
    confidence: Whether to include explicit confidence levels for claims
    uncertain: How to handle uncertain information
    strictness: The threshold for considering information verified

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
