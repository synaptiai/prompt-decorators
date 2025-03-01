# Decorator `BuildOn`

**Version:** 1.0.0

A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.

## Parameters

### `reference`

**Type:** enum  
**Required:** No  
**Default:** `last`  

What to build upon from the previous context

**Allowed values:**

- `last`
- `specific`
- `all`

### `approach`

**Type:** enum  
**Required:** No  
**Default:** `extend`  

How to build upon the referenced content

**Allowed values:**

- `extend`
- `refine`
- `contrast`
- `synthesize`

### `preserveStructure`

**Type:** boolean  
**Required:** No  
**Default:** `True`  

Whether to maintain the structure of the referenced content

## Examples

### Basic extension of the previous response

```
+++BuildOn
Add more detail about implementation challenges.
```

Result:

Extends the previous response by adding more detailed information about implementation challenges while maintaining continuity

### Specific refinement with structural changes

```
+++BuildOn(reference=specific, approach=refine, preserveStructure=false)
Improve the section on risk analysis with more quantitative measures.
```

Result:

Refines specifically the risk analysis section from the previous content with more quantitative measures, potentially restructuring it

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(reference=BuildOnReferenceEnum.LAST, approach=BuildOnApproachEnum.EXTEND, preserveStructure=True)`

Initialize BuildOn decorator.

Args:
    reference: What to build upon from the previous context
    approach: How to build upon the referenced content
    preserveStructure: Whether to maintain the structure of the referenced content

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

