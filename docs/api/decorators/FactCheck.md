# Decorator `FactCheck`

**Version:** 1.0.0

Enhances the response with verification of factual claims and explicit indication of confidence levels. This decorator promotes accuracy by distinguishing between well-established facts, likely facts, and uncertain or speculative information.

## Parameters

### `confidence`

**Type:** boolean  
**Required:** No  
**Default:** `True`  

Whether to include explicit confidence levels for claims

### `uncertain`

**Type:** enum  
**Required:** No  
**Default:** `mark`  

How to handle uncertain information

**Allowed values:**

- `mark`
- `exclude`
- `qualify`

### `strictness`

**Type:** enum  
**Required:** No  
**Default:** `moderate`  

The threshold for considering information verified

**Allowed values:**

- `low`
- `moderate`
- `high`

## Examples

### Basic fact checking with confidence indicators

```
+++FactCheck
Explain the history and effectiveness of vaccines.
```

Result:

Provides information about vaccines with clear indications of confidence levels for different claims

### High-strictness fact checking that excludes uncertain information

```
+++FactCheck(strictness=high, uncertain=exclude)
Describe what we know about dark matter.
```

Result:

Presents only well-established scientific facts about dark matter, excluding speculative or uncertain information

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(confidence=True, uncertain=FactCheckUncertainEnum.MARK, strictness=FactCheckStrictnessEnum.MODERATE)`

Initialize FactCheck decorator.

Args:
    confidence: Whether to include explicit confidence levels for claims
    uncertain: How to handle uncertain information
    strictness: The threshold for considering information verified

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

