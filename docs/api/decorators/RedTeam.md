# Decorator `RedTeam`

**Version:** 1.0.0

Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws. This decorator simulates how an opponent or critic would evaluate and attack ideas, plans, or arguments.

## Parameters

### `strength`

**Type:** enum
**Required:** No
**Default:** `moderate`

How aggressive or challenging the red team analysis should be

**Allowed values:**

- `moderate`
- `aggressive`
- `steelman`

### `focus`

**Type:** array
**Required:** No

Specific aspects to focus the red team analysis on

### `constructive`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to include constructive suggestions for improvement after critiques

## Examples

### Basic red team analysis of a business proposal

```
+++RedTeam
Here's our plan to launch a new subscription service...
```

Result:

Analyzes the subscription service plan from an adversarial perspective, identifying potential weaknesses, oversights, and challenges

### Aggressive red team analysis with specific focus areas

```
+++RedTeam(strength=aggressive, focus=[security,scalability,market-fit], constructive=true)
Review our new authentication system design.
```

Result:

Aggressively challenges the authentication system design, specifically targeting security, scalability, and market-fit concerns, followed by constructive improvement suggestions

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(strength=RedTeamStrengthEnum.MODERATE, focus, constructive=True)`

Initialize RedTeam decorator.

Args:
    strength: How aggressive or challenging the red team analysis should be
    focus: Specific aspects to focus the red team analysis on
    constructive: Whether to include constructive suggestions for improvement after critiques

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
