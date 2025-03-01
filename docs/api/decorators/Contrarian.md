# Decorator `Contrarian`

**Version:** 1.0.0

Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.

## Parameters

### `approach`

**Type:** enum  
**Required:** No  
**Default:** `devil's-advocate`  

The specific contrarian approach to take

**Allowed values:**

- `outsider`
- `skeptic`
- `devil's-advocate`

### `maintain`

**Type:** boolean  
**Required:** No  

Whether to maintain contrarian stance throughout (true) or provide balanced view at the end (false)

### `focus`

**Type:** string  
**Required:** No  

Optional specific aspect of the topic to focus contrarian analysis on

## Examples

### Basic devil's advocate approach with balanced conclusion

```
+++Contrarian
Why is renewable energy considered the future of power generation?
```

Result:

Challenges conventional thinking about renewable energy's dominance, presenting counterarguments and limitations, followed by a balanced perspective

### Maintained skeptical contrarian stance focused on a specific aspect

```
+++Contrarian(approach=skeptic, maintain=true, focus=methodology)
Discuss the reliability of climate models in predicting future global temperatures.
```

Result:

Provides a consistently skeptical analysis of climate model methodologies, questioning assumptions, limitations, and historical accuracy throughout the response

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(approach=ContrarianApproachEnum.DEVIL_S_ADVOCATE, maintain=False, focus)`

Initialize Contrarian decorator.

Args:
    approach: The specific contrarian approach to take
    maintain: Whether to maintain contrarian stance throughout (true) or provide balanced view at the end (false)
    focus: Optional specific aspect of the topic to focus contrarian analysis on

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

