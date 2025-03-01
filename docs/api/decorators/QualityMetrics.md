# Decorator `QualityMetrics`

**Version:** 1.0.0

Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.

## Parameters

### `metrics`

**Type:** array  
**Required:** No  

Specific quality metrics to measure (e.g., accuracy, completeness, clarity, usefulness)

### `scale`

**Type:** enum  
**Required:** No  
**Default:** `1-5`  

Rating scale to use for evaluations

**Allowed values:**

- `1-5`
- `1-10`
- `percentage`
- `qualitative`

### `explanation`

**Type:** boolean  
**Required:** No  
**Default:** `True`  

Whether to provide detailed explanations for each metric score

## Examples

### Basic quality assessment of an analysis

```
+++QualityMetrics
My analysis of the financial market trends is as follows...
```

Result:

Provides the analysis of financial market trends, followed by 1-5 ratings across standard quality metrics with explanations for each score

### Specific custom metrics with detailed qualitative assessment

```
+++QualityMetrics(metrics=[factual accuracy,predictive value,consideration of alternatives,logical flow], scale=qualitative, explanation=true)
Here's my policy proposal for urban housing...
```

Result:

Delivers the policy proposal, followed by qualitative assessments (poor/fair/good/excellent) of the four specified metrics, with detailed explanations for each evaluation

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(metrics, scale=QualityMetricsScaleEnum.VALUE_1_5, explanation=True)`

Initialize QualityMetrics decorator.

Args:
    metrics: Specific quality metrics to measure (e.g., accuracy, completeness, clarity, usefulness)
    scale: Rating scale to use for evaluations
    explanation: Whether to provide detailed explanations for each metric score

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

