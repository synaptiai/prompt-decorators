# Decorator `Conditional`

**Version:** 1.0.0

A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.

## Parameters

### `if`

**Type:** string
**Required:** Yes

The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}')

### `then`

**Type:** string
**Required:** Yes

The decorator to apply if the condition is true (can be a specific decorator with parameters)

### `else`

**Type:** string
**Required:** No

The decorator to apply if the condition is false (can be a specific decorator with parameters)

## Examples

### Basic conditional application based on content complexity

```
+++Conditional(if=complex, then=StepByStep, else=Concise)
Explain how quantum computing works.
```

Result:

Evaluates if the topic is complex, which quantum computing is, so it applies the StepByStep decorator

### Conditional application with parameterized decorators

```
+++Conditional(if=controversial, then=Debate(perspectives=3), else=Reasoning(depth=moderate))
Discuss the ethical implications of gene editing in humans.
```

Result:

Determines that gene editing ethics is controversial, so it applies the Debate decorator with 3 perspectives rather than the Reasoning decorator

## Compatibility

**Supported models:**

- `gpt-4`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(if_param, then, else_param)`

Initialize Conditional decorator.

Args:
    if_param: The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}')
    then: The decorator to apply if the condition is true (can be a specific decorator with parameters)
    else_param: The decorator to apply if the condition is false (can be a specific decorator with parameters)

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
