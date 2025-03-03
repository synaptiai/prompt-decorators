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

**Signature:** `__init__(depth=comprehensive, aspects, examples=True)`

Initialize the Detailed decorator.

Args:
    depth: The level of detail and comprehensiveness (moderate, comprehensive, exhaustive)
    aspects: Specific aspects or dimensions to explore in detail
    examples: Whether to include detailed examples to illustrate points

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the Detailed decorator to a prompt.

Args:
    prompt: The original prompt to decorate

Returns:
    The decorated prompt

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

Convert the decorator to a dictionary.

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
