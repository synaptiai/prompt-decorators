# Decorator `Priority`

**Version:** 1.0.0

A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.

## Parameters

### `decorators`

**Type:** array  
**Required:** Yes  

Ordered list of decorators by priority (highest priority first)

### `explicit`

**Type:** boolean  
**Required:** No  

Whether to explicitly mention overridden behaviors in the response

### `mode`

**Type:** enum  
**Required:** No  
**Default:** `override`  

How to handle conflicts between decorators

**Allowed values:**

- `override`
- `merge`
- `cascade`

## Examples

### Basic priority ordering between potentially conflicting decorators

```
+++Priority(decorators=[Concise,Detailed])
Explain quantum computing.
```

Result:

Applies both decorators, but when conflicts arise, Concise takes precedence over Detailed, resulting in a more concise explanation of quantum computing

### Complex priority with explicit conflict resolution

```
+++Priority(decorators=[Academic,Creative,StepByStep], explicit=true, mode=cascade)
Explain the water cycle.
```

Result:

Implements a cascading priority where Academic style dominates, with Creative elements where they don't conflict with Academic style, and StepByStep structure throughout, explicitly noting where decorator behaviors were modified due to conflicts

## Compatibility

**Supported models:**

- `gpt-4`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(decorators, explicit=False, mode=PriorityModeEnum.OVERRIDE)`

Initialize Priority decorator.

Args:
    decorators: Ordered list of decorators by priority (highest priority first)
    explicit: Whether to explicitly mention overridden behaviors in the response
    mode: How to handle conflicts between decorators

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

