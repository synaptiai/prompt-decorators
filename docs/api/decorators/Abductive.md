# Decorator `Abductive`

**Version:** 1.0.0

Structures the response using abductive reasoning, developing the most likely explanations for observations or phenomena. This decorator emphasizes inference to the best explanation and hypothetical reasoning to address incomplete information.

## Parameters

### `hypotheses`

**Type:** number
**Required:** No
**Default:** `3`

Number of alternative hypotheses or explanations to generate

### `criteria`

**Type:** array
**Required:** No

Specific criteria to evaluate hypotheses against (e.g., simplicity, explanatory power)

### `rank`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to explicitly rank hypotheses by likelihood

## Examples

### Basic abductive reasoning with multiple hypotheses

```
+++Abductive
Why have bee populations been declining globally?
```

Result:

Presents observed facts about bee population decline, generates three possible explanations, and identifies the most likely causes based on available evidence

### Detailed abductive reasoning with specific evaluation criteria

```
+++Abductive(hypotheses=4, criteria=[comprehensiveness,simplicity,novelty,testability], rank=true)
What might explain the Fermi Paradox?
```

Result:

Develops four hypotheses explaining the Fermi Paradox, evaluates each against the specified criteria, and ranks them from most to least likely explanation

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(hypotheses=3, criteria, rank=True)`

Initialize Abductive decorator.

Args:
    hypotheses: Number of alternative hypotheses or explanations to generate
    criteria: Specific criteria to evaluate hypotheses against (e.g., simplicity, explanatory power)
    rank: Whether to explicitly rank hypotheses by likelihood

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
