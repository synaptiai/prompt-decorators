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

**Signature:** `__init__(level=CreativeLevelEnum.HIGH, elements, constraints)`

Initialize Creative decorator.

Args:
    level: The degree of creative thinking to apply
    elements: Specific creative elements to incorporate (e.g., metaphor, wordplay, narrative)
    constraints: Optional creative constraints to work within

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

