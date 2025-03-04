# Decorator `Inductive`

**Version:** 1.0.0

Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.

## Parameters

### `examples`

**Type:** number
**Required:** No
**Default:** `3`

Number of specific examples or observations to include before generalizing

### `confidence`

**Type:** boolean
**Required:** No

Whether to explicitly state the confidence level of the inductive conclusions

### `structure`

**Type:** enum
**Required:** No
**Default:** `generalization`

The pattern of inductive reasoning to follow

**Allowed values:**

- `generalization`
- `causal`
- `statistical`
- `analogical`

## Examples

### Basic inductive reasoning from examples to general principles

```
+++Inductive
What factors contribute to successful startups?
```

Result:

Provides specific examples of successful startups, identifies patterns across them, and derives general principles of startup success

### Causal inductive reasoning with confidence levels

```
+++Inductive(examples=5, confidence=true, structure=causal)
How does screen time affect child development?
```

Result:

Presents 5 specific observations about screen time and child development, infers causal relationships, and generalizes with explicit confidence levels for each conclusion

## Compatibility

**Conflicts with:**

- `Deductive`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(examples=3, confidence=False, structure=generalization) -> <class 'NoneType'>`

Initialize the Inductive decorator.

Args:
    examples: Number of specific examples or observations to include before generalizing
    confidence: Whether to explicitly state the confidence level of the inductive conclusions
    structure: The pattern of inductive reasoning to follow

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
