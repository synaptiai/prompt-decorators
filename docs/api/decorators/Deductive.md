# Decorator `Deductive`

**Version:** 1.0.0

Structures the response using deductive reasoning, moving from general principles to specific conclusions. This decorator emphasizes logical argument development, starting with premises and working methodically to necessary conclusions.

## Parameters

### `premises`

**Type:** number  
**Required:** No  
**Default:** `2`  

Number of main premises to include before deducing conclusions

### `formal`

**Type:** boolean  
**Required:** No  

Whether to use formal logical structures with explicit syllogisms

### `steps`

**Type:** number  
**Required:** No  
**Default:** `3`  

Number of logical steps to include in the deductive process

## Examples

### Basic deductive reasoning from principles to specific conclusions

```
+++Deductive
Should social media companies be regulated like utilities?
```

Result:

Starts with general principles about utilities and regulation, establishes premises about social media characteristics, and deduces conclusions about appropriate regulatory approaches

### Formal deductive logic with multiple steps

```
+++Deductive(formal=true, steps=5)
Is artificial intelligence conscious?
```

Result:

Presents formal logical syllogisms about consciousness and intelligence, proceeding through 5 distinct logical steps to reach conclusions about AI consciousness

## Compatibility

**Conflicts with:**

- `Inductive`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(premises=2, formal=False, steps=3)`

Initialize Deductive decorator.

Args:
    premises: Number of main premises to include before deducing conclusions
    formal: Whether to use formal logical structures with explicit syllogisms
    steps: Number of logical steps to include in the deductive process

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

