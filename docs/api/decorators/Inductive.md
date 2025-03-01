# Decorator `Inductive`

**Version:** 1.0.0

Structures the response using inductive reasoning, moving from specific observations to broader generalizations and theories. This decorator emphasizes pattern recognition and the derivation of general principles from particular instances.

## Parameters

### `examples`

**Type:** number  
**Required:** No  
**Default:** `3`  

Number of specific examples or observations to include before generalizing

### `confidence`

**Type:** boolean  
**Required:** No  

Whether to explicitly state the confidence level of the inductive conclusions

### `structure`

**Type:** enum  
**Required:** No  
**Default:** `generalization`  

The pattern of inductive reasoning to follow

**Allowed values:**

- `generalization`
- `causal`
- `statistical`
- `analogical`

## Examples

### Basic inductive reasoning from examples to general principles

```
+++Inductive
What factors contribute to successful startups?
```

Result:

Provides specific examples of successful startups, identifies patterns across them, and derives general principles of startup success

### Causal inductive reasoning with confidence levels

```
+++Inductive(examples=5, confidence=true, structure=causal)
How does screen time affect child development?
```

Result:

Presents 5 specific observations about screen time and child development, infers causal relationships, and generalizes with explicit confidence levels for each conclusion

## Compatibility

**Conflicts with:**

- `Deductive`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(examples=3, confidence=False, structure=InductiveStructureEnum.GENERALIZATION)`

Initialize Inductive decorator.

Args:
    examples: Number of specific examples or observations to include before generalizing
    confidence: Whether to explicitly state the confidence level of the inductive conclusions
    structure: The pattern of inductive reasoning to follow

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

