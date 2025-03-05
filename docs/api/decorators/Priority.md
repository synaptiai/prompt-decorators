# Decorator `Priority`

**Version:** 1.0.0

A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.

## Parameters

### `decorators`

**Type:** array
**Required:** Yes

Ordered list of decorators by priority (highest priority first)

### `explicit`

**Type:** boolean
**Required:** No

Whether to explicitly mention overridden behaviors in the response

### `mode`

**Type:** enum
**Required:** No
**Default:** `override`

How to handle conflicts between decorators

**Allowed values:**

- `override`
- `merge`
- `cascade`

## Examples

### Basic priority ordering between potentially conflicting decorators

```
+++Priority(decorators=[Concise,Detailed])
Explain quantum computing.
```

Result:

Applies both decorators, but when conflicts arise, Concise takes precedence over Detailed, resulting in a more concise explanation of quantum computing

### Complex priority with explicit conflict resolution

```
+++Priority(decorators=[Academic,Creative,StepByStep], explicit=true, mode=cascade)
Explain the water cycle.
```

Result:

Implements a cascading priority where Academic style dominates, with Creative elements where they don't conflict with Academic style, and StepByStep structure throughout, explicitly noting where decorator behaviors were modified due to conflicts

## Compatibility

**Supported models:**

- `gpt-4`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(decorators, explicit=False, mode=override) -> <class 'NoneType'>`

Initialize the Priority decorator.

Args:
    decorators: Ordered list of decorators by priority (highest priority first)
    explicit: Whether to explicitly mention overridden behaviors in the response
    mode: How to handle conflicts between decorators


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

This method transforms the prompt using the transformation template.

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
