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

**Signature:** `__init__(hypotheses=3, criteria, rank=True) -> <class 'NoneType'>`

Initialize the Abductive decorator.

Args:
    hypotheses: Number of alternative hypotheses or explanations to generate
    criteria: Specific criteria to evaluate hypotheses against (e.g., simplicity, explanatory power)
    rank: Whether to explicitly rank hypotheses by likelihood

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
