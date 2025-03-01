# Decorator `Tone`

**Version:** 1.0.0

Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.

## Parameters

### `style`

**Type:** enum  
**Required:** Yes  
**Default:** `formal`  

The desired tone and style for the response

**Allowed values:**

- `formal`
- `casual`
- `friendly`
- `technical`
- `humorous`

## Examples

### Technical documentation tone

```
+++Tone(style=technical)
Explain how garbage collection works in Python
```

Result:

Provides a technically precise explanation using appropriate terminology

### Casual explanation

```
+++Tone(style=casual)
Why is the sky blue?
```

Result:

Delivers a relaxed, conversational explanation of atmospheric optics

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

**Signature:** `__init__(style)`

Initialize Tone decorator.

Args:
    style: The desired tone and style for the response

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

