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

**Signature:** `__init__(versions=ExtremesVersionsEnum.BOTH, dimension=ambition, compare=True)`

Initialize Extremes decorator.

Args:
    versions: Which extreme versions to include
    dimension: The specific dimension along which to explore extremes (e.g., 'cost', 'time', 'ambition', 'complexity')
    compare: Whether to include a comparative analysis of the extreme versions

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

