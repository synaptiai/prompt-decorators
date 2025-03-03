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

**Signature:** `__init__(focus=NegativeSpaceFocusEnum.COMPREHENSIVE, depth=NegativeSpaceDepthEnum.MODERATE, structure=NegativeSpaceStructureEnum.INTEGRATED)`

Initialize NegativeSpace decorator.

Args:
    focus: The specific aspect of negative space to emphasize
    depth: How deeply to explore the negative space
    structure: How to present the negative space analysis

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
