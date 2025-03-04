# Decorator `Layered`

**Version:** 1.0.0

Presents content at multiple levels of explanation depth, allowing readers to engage with information at their preferred level of detail. This decorator structures responses with progressive disclosure, from high-level summaries to increasingly detailed explanations.

## Parameters

### `levels`

**Type:** enum
**Required:** No
**Default:** `summary-detail-technical`

The granularity of explanation levels to include

**Allowed values:**

- `sentence-paragraph-full`
- `basic-intermediate-advanced`
- `summary-detail-technical`

### `count`

**Type:** number
**Required:** No
**Default:** `3`

Number of distinct explanation layers to provide

### `progression`

**Type:** enum
**Required:** No
**Default:** `separate`

How to structure the progression between layers

**Allowed values:**

- `separate`
- `nested`
- `incremental`

## Examples

### Basic three-level explanation of a complex concept

```
+++Layered
Explain how blockchain technology works.
```

Result:

Provides a summary-level explanation of blockchain, followed by a detailed explanation, and finally a technical deep dive with implementation details

### Multi-layered nested progression with custom levels

```
+++Layered(levels=basic-intermediate-advanced, count=4, progression=nested)
Describe the principles of quantum computing.
```

Result:

Delivers a nested explanation of quantum computing with four progressive layers of understanding, each building on the previous and increasing in complexity from basic to advanced

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(levels=summary-detail-technical, count=3, progression=separate) -> <class 'NoneType'>`

Initialize the Layered decorator.

Args:
    levels: The granularity of explanation levels to include
    count: Number of distinct explanation layers to provide
    progression: How to structure the progression between layers


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
