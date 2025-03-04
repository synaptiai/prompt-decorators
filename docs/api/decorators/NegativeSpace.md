# Decorator `NegativeSpace`

**Version:** 1.0.0

Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.

## Parameters

### `focus`

**Type:** enum
**Required:** No
**Default:** `comprehensive`

The specific aspect of negative space to emphasize

**Allowed values:**

- `implications`
- `missing`
- `unstated`
- `comprehensive`

### `depth`

**Type:** enum
**Required:** No
**Default:** `moderate`

How deeply to explore the negative space

**Allowed values:**

- `surface`
- `moderate`
- `deep`

### `structure`

**Type:** enum
**Required:** No
**Default:** `integrated`

How to present the negative space analysis

**Allowed values:**

- `before`
- `after`
- `integrated`
- `separate`

## Examples

### Basic comprehensive negative space analysis

```
+++NegativeSpace
Discuss the impact of social media on society.
```

Result:

Provides a discussion of social media's societal impact while integrating analysis of unstated assumptions, overlooked factors, and typically unaddressed implications

### Deep negative space analysis focused on missing elements

```
+++NegativeSpace(focus=missing, depth=deep, structure=after)
Explain the current approaches to artificial intelligence safety.
```

Result:

First explains current AI safety approaches, then provides a separate deep analysis of missing elements in the discussion, such as unstudied risks, overlooked stakeholders, and neglected scenarios

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(focus=comprehensive, depth=moderate, structure=integrated) -> <class 'NoneType'>`

Initialize the NegativeSpace decorator.

Args:
    focus: The specific aspect of negative space to emphasize
    depth: How deeply to explore the negative space
    structure: How to present the negative space analysis


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
