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

**Signature:** `__init__(decorator, parameters, behavior) -> <class 'NoneType'>`

Initialize the Override decorator.

Args:
    decorator: The specific decorator whose behavior to override
    parameters: JSON string specifying the parameters to override (e.g., '{"depth": "comprehensive", "focus": "methodology"}')
    behavior: Optional custom behavior modification instructions that override the standard decorator interpretation

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
