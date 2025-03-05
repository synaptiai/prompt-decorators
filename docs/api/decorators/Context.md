# Decorator `Context`

**Version:** 1.0.0

A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.

## Parameters

### `domain`

**Type:** string
**Required:** Yes

The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education')

### `scope`

**Type:** enum
**Required:** No
**Default:** `all`

Which aspects of decorators to contextualize

**Allowed values:**

- `terminology`
- `examples`
- `structure`
- `all`

### `level`

**Type:** enum
**Required:** No
**Default:** `mixed`

The expertise level to target within the domain

**Allowed values:**

- `beginner`
- `intermediate`
- `expert`
- `mixed`

## Examples

### Basic domain-specific adaptation of decorators

```
+++Context(domain=medicine)
+++StepByStep
+++Detailed
Explain how vaccines are developed.
```

Result:

Applies the StepByStep and Detailed decorators with medical context-awareness, using appropriate medical terminology, examples, and structures for explaining vaccine development

### Targeted contextualization for specific expertise level

```
+++Context(domain=programming, scope=examples, level=beginner)
+++Reasoning
+++ELI5
Explain how databases work.
```

Result:

Uses the Reasoning and ELI5 decorators with programming-appropriate examples specifically tailored for beginners, while keeping general terminology and structure accessible

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(domain, scope=all, level=mixed) -> <class 'NoneType'>`

Initialize the Context decorator.

Args:
    domain: The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education')
    scope: Which aspects of decorators to contextualize
    level: The expertise level to target within the domain


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
