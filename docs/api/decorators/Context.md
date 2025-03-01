# Decorator `Context`

**Version:** 1.0.0

A meta-decorator that adapts standard decorators for domain-specific contexts. This provides specialized interpretations of decorators based on particular fields, industries, or subject matter to ensure appropriate adaptation to contextual requirements.

## Parameters

### `domain`

**Type:** string  
**Required:** Yes  

The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education')

### `scope`

**Type:** enum  
**Required:** No  
**Default:** `all`  

Which aspects of decorators to contextualize

**Allowed values:**

- `terminology`
- `examples`
- `structure`
- `all`

### `level`

**Type:** enum  
**Required:** No  
**Default:** `mixed`  

The expertise level to target within the domain

**Allowed values:**

- `beginner`
- `intermediate`
- `expert`
- `mixed`

## Examples

### Basic domain-specific adaptation of decorators

```
+++Context(domain=medicine)
+++StepByStep
+++Detailed
Explain how vaccines are developed.
```

Result:

Applies the StepByStep and Detailed decorators with medical context-awareness, using appropriate medical terminology, examples, and structures for explaining vaccine development

### Targeted contextualization for specific expertise level

```
+++Context(domain=programming, scope=examples, level=beginner)
+++Reasoning
+++ELI5
Explain how databases work.
```

Result:

Uses the Reasoning and ELI5 decorators with programming-appropriate examples specifically tailored for beginners, while keeping general terminology and structure accessible

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(domain, scope=ContextScopeEnum.ALL, level=ContextLevelEnum.MIXED)`

Initialize Context decorator.

Args:
    domain: The specific domain, field, or industry to contextualize decorators for (e.g., 'medicine', 'legal', 'engineering', 'education')
    scope: Which aspects of decorators to contextualize
    level: The expertise level to target within the domain

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

