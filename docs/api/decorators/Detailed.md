# Decorator `Detailed`

**Version:** 1.0.0

Enhances the response with comprehensive information, thorough explanations, and rich context. This decorator is ideal for in-depth learning, complex topics requiring nuance, or when completeness is valued over brevity.

## Parameters

### `depth`

**Type:** enum
**Required:** No
**Default:** `comprehensive`

The level of detail and comprehensiveness

**Allowed values:**

- `moderate`
- `comprehensive`
- `exhaustive`

### `aspects`

**Type:** array
**Required:** No

Specific aspects or dimensions to explore in detail

### `examples`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to include detailed examples to illustrate points

## Examples

### Comprehensive detailed explanation of a concept

```
+++Detailed
Explain how the human immune system works.
```

Result:

Provides a thorough, in-depth explanation of the immune system covering all major components, processes, and functions with illustrative examples

### Exhaustive detailed analysis of specific aspects

```
+++Detailed(depth=exhaustive, aspects=[economic,environmental,social,technological], examples=true)
Analyze the implications of transitioning to renewable energy.
```

Result:

Delivers an extremely detailed analysis of renewable energy transition, exhaustively covering all four specified aspects with comprehensive examples

## Compatibility

**Conflicts with:**

- `Concise`
- `Summary`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(depth=comprehensive, aspects, examples=True) -> <class 'NoneType'>`

Initialize the Detailed decorator.

Args:
    depth: The level of detail and comprehensiveness
    aspects: Specific aspects or dimensions to explore in detail
    examples: Whether to include detailed examples to illustrate points

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
