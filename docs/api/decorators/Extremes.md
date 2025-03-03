# Decorator `Extremes`

**Version:** 1.0.0

Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.

## Parameters

### `versions`

**Type:** enum
**Required:** No
**Default:** `both`

Which extreme versions to include

**Allowed values:**

- `radical`
- `minimal`
- `both`

### `dimension`

**Type:** string
**Required:** No
**Default:** `ambition`

The specific dimension along which to explore extremes (e.g., 'cost', 'time', 'ambition', 'complexity')

### `compare`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to include a comparative analysis of the extreme versions

## Examples

### Basic exploration of minimal and radical approaches

```
+++Extremes
Describe a strategy for reducing carbon emissions.
```

Result:

Presents both a minimal, immediately achievable carbon reduction strategy and a radical, transformative approach, with a comparison of their respective impacts, feasibility, and trade-offs

### Only radical version along a specific dimension

```
+++Extremes(versions=radical, dimension=technological innovation, compare=false)
Outline the future of transportation.
```

Result:

Provides only a technologically radical vision of transportation's future, focusing on the most innovative and disruptive possibilities without comparison to other approaches

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(versions=both, dimension=ambition, compare=True) -> <class 'NoneType'>`

Initialize the Extremes decorator.

Args:
    versions: Which extreme versions to include
    dimension: The specific dimension along which to explore extremes (e.g., 'cost', 'time', 'ambition', 'complexity')
    compare: Whether to include a comparative analysis of the extreme versions

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
