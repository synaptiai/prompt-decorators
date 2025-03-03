# Decorator `Precision`

**Version:** 1.0.0

Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.

## Parameters

### `level`

**Type:** enum
**Required:** No
**Default:** `high`

The degree of precision to apply

**Allowed values:**

- `moderate`
- `high`
- `scientific`

### `units`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to consistently provide units for all measurements

### `definitions`

**Type:** boolean
**Required:** No

Whether to include precise definitions for key terms

## Examples

### Basic precise explanation of a scientific concept

```
+++Precision
Explain how vaccines work.
```

Result:

Provides an explanation of vaccine mechanisms using precise terminology, specific examples, and accurate measurements where relevant

### Highly precise response with scientific rigor

```
+++Precision(level=scientific, units=true, definitions=true)
Describe the process of photosynthesis.
```

Result:

Delivers a scientifically precise explanation of photosynthesis with exact units for all measurements, precise definitions for key terms, and specific chemical reactions

## Compatibility

**Conflicts with:**

- `ELI5`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(level=high, units=True, definitions=False) -> <class 'NoneType'>`

Initialize the Precision decorator.

Args:
    level: The degree of precision to apply
    units: Whether to consistently provide units for all measurements
    definitions: Whether to include precise definitions for key terms

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
