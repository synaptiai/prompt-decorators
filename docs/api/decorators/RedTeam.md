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

**Signature:** `__init__(strength=moderate, focus, constructive=True) -> <class 'NoneType'>`

Initialize the RedTeam decorator.

Args:
    strength: How aggressive or challenging the red team analysis should be
    focus: Specific aspects to focus the red team analysis on
    constructive: Whether to include constructive suggestions for improvement after critiques


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
