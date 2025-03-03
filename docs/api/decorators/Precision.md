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

**Signature:** `__init__(level=PrecisionLevelEnum.HIGH, units=True, definitions=False)`

Initialize Precision decorator.

Args:
    level: The degree of precision to apply
    units: Whether to consistently provide units for all measurements
    definitions: Whether to include precise definitions for key terms

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
