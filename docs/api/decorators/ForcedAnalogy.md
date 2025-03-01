# Decorator `ForcedAnalogy`

**Version:** 1.0.0

Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.

## Parameters

### `source`

**Type:** string  
**Required:** Yes  

The specific domain, field, or context to draw analogies from

### `comprehensiveness`

**Type:** enum  
**Required:** No  
**Default:** `comprehensive`  

How comprehensively to map concepts between domains

**Allowed values:**

- `basic`
- `comprehensive`
- `detailed`

### `mappings`

**Type:** number  
**Required:** No  
**Default:** `3`  

Number of distinct concept mappings to create between domains

## Examples

### Explaining a technical concept using sports analogies

```
+++ForcedAnalogy(source=sports)
Explain how blockchain technology works.
```

Result:

Explains blockchain technology by mapping concepts to sports analogies (e.g., ledger as scoreboard, miners as referees, consensus as rulebook)

### Detailed cooking analogy for complex scientific process

```
+++ForcedAnalogy(source=cooking, comprehensiveness=detailed, mappings=5)
Describe how CRISPR gene editing works.
```

Result:

Provides a detailed explanation of CRISPR through cooking analogies, with 5 distinct concept mappings (e.g., DNA as recipe, Cas9 as kitchen knife, guide RNA as cooking instructions)

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(source, comprehensiveness=ForcedAnalogyComprehensivenessEnum.COMPREHENSIVE, mappings=3)`

Initialize ForcedAnalogy decorator.

Args:
    source: The specific domain, field, or context to draw analogies from
    comprehensiveness: How comprehensively to map concepts between domains
    mappings: Number of distinct concept mappings to create between domains

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

