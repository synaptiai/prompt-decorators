# Decorator `Creative`

**Version:** 1.0.0

Enhances responses with imaginative, novel, and original content. This decorator encourages divergent thinking, metaphorical language, and unusual connections to generate engaging and non-obvious outputs.

## Parameters

### `level`

**Type:** enum
**Required:** No
**Default:** `high`

The degree of creative thinking to apply

**Allowed values:**

- `moderate`
- `high`
- `unconventional`

### `elements`

**Type:** array
**Required:** No

Specific creative elements to incorporate (e.g., metaphor, wordplay, narrative)

### `constraints`

**Type:** array
**Required:** No

Optional creative constraints to work within

## Examples

### Basic creative response to a standard question

```
+++Creative
Explain how the internet works.
```

Result:

Provides an imaginative explanation of the internet using unexpected metaphors and creative language while maintaining accuracy

### Highly creative response with specific elements

```
+++Creative(level=unconventional, elements=[metaphor,narrative,wordplay], constraints=[must reference nature])
Describe the principles of quantum computing.
```

Result:

Delivers an unconventional explanation of quantum computing through an engaging narrative filled with nature metaphors and clever wordplay

## Compatibility

**Conflicts with:**

- `Academic`
- `Professional`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(level=high, elements, constraints) -> <class 'NoneType'>`

Initialize the Creative decorator.

Args:
    level: The degree of creative thinking to apply
    elements: Specific creative elements to incorporate (e.g., metaphor, wordplay, narrative)
    constraints: Optional creative constraints to work within

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
