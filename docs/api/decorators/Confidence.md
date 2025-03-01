# Decorator `Confidence`

**Version:** 1.0.0

Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.

## Parameters

### `scale`

**Type:** enum  
**Required:** No  
**Default:** `qualitative`  

The method used to express confidence levels

**Allowed values:**

- `percent`
- `qualitative`
- `stars`
- `numeric`

### `threshold`

**Type:** number  
**Required:** No  
**Default:** `50`  

Minimum confidence level for including information (as a percentage)

### `detailed`

**Type:** boolean  
**Required:** No  

Whether to provide explanations for confidence assessments

## Examples

### Qualitative confidence indicators for a complex topic

```
+++Confidence
Explain the current understanding of dark matter.
```

Result:

Explains dark matter theories with qualitative confidence indicators (high confidence, moderate confidence, etc.) for different claims

### Detailed percentage-based confidence with high threshold

```
+++Confidence(scale=percent, threshold=80, detailed=true)
What are the most effective treatments for depression?
```

Result:

Discusses only high-confidence (80%+) depression treatments with percentage indicators and explanations for confidence assessments

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(scale=ConfidenceScaleEnum.QUALITATIVE, threshold=50, detailed=False)`

Initialize Confidence decorator.

Args:
    scale: The method used to express confidence levels
    threshold: Minimum confidence level for including information (as a percentage)
    detailed: Whether to provide explanations for confidence assessments

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

