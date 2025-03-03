# Decorator `Override`

**Version:** 1.0.0

A meta-decorator that overrides the default parameters or behaviors of other decorators. This enables customization of standard decorators without modifying their definitions, allowing for reuse of established patterns with specific adjustments.

## Parameters

### `decorator`

**Type:** string
**Required:** Yes

The specific decorator whose behavior to override

### `parameters`

**Type:** string
**Required:** No

JSON string specifying the parameters to override (e.g., '{"depth": "comprehensive", "focus": "methodology"}')

### `behavior`

**Type:** string
**Required:** No

Optional custom behavior modification instructions that override the standard decorator interpretation

## Examples

### Basic parameter override for a standard decorator

```
+++Override(decorator=StepByStep, parameters={"numbered": true, "steps": 7})
Explain how to bake bread.
```

Result:

Applies the StepByStep decorator to explain bread baking, but overrides its default parameters to ensure exactly 7 numbered steps

### Complex behavior override with custom instructions

```
+++Override(decorator=Debate, parameters={"perspectives": 2}, behavior=instead of presenting neutral perspectives, adopt strongly opposing viewpoints with clear advocacy for each position)
Discuss the ethics of gene editing.
```

Result:

Uses the Debate decorator structure for discussing gene editing ethics, but modifies its standard neutral approach to present strongly advocated opposing positions

## Compatibility

**Supported models:**

- `gpt-4`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(decorator, parameters, behavior)`

Initialize Override decorator.

Args:
    decorator: The specific decorator whose behavior to override
    parameters: JSON string specifying the parameters to override (e.g., '{"depth": "comprehensive", "focus": "methodology"}')
    behavior: Optional custom behavior modification instructions that override the standard decorator interpretation

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
