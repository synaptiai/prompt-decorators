# Decorator `Bullet`

**Version:** 1.0.0

Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.

## Parameters

### `style`

**Type:** enum  
**Required:** No  
**Default:** `dash`  

The visual marker used for bullet points

**Allowed values:**

- `dash`
- `dot`
- `arrow`
- `star`
- `plus`

### `indented`

**Type:** boolean  
**Required:** No  
**Default:** `True`  

Whether to allow nested, indented bullet points

### `compact`

**Type:** boolean  
**Required:** No  

Whether to keep bullet points short and concise (true) or allow longer, more detailed points (false)

## Examples

### Basic bulleted list of key points

```
+++Bullet
What are the main factors to consider when buying a laptop?
```

Result:

Presents key laptop purchasing factors as a bulleted list with dash markers

### Compact star bullets with nesting disabled

```
+++Bullet(style=star, indented=false, compact=true)
List the benefits of regular exercise.
```

Result:

Provides a flat list of concise, star-bulleted points about exercise benefits, with no nested sub-points

## Compatibility

**Conflicts with:**

- `OutputFormat`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(style=BulletStyleEnum.DASH, indented=True, compact=False)`

Initialize Bullet decorator.

Args:
    style: The visual marker used for bullet points
    indented: Whether to allow nested, indented bullet points
    compact: Whether to keep bullet points short and concise (true) or allow longer, more detailed points (false)

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

