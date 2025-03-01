# Decorator `DecisionMatrix`

**Version:** 1.0.0

Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.

## Parameters

### `options`

**Type:** array  
**Required:** No  

Specific options or alternatives to evaluate in the matrix

### `criteria`

**Type:** array  
**Required:** No  

Evaluation criteria to assess each option against

### `weighted`

**Type:** boolean  
**Required:** No  

Whether to include weights for criteria importance

### `scale`

**Type:** enum  
**Required:** No  
**Default:** `1-5`  

Rating scale to use for evaluations

**Allowed values:**

- `1-5`
- `1-10`
- `qualitative`
- `percentage`

## Examples

### Simple decision matrix for comparing options

```
+++DecisionMatrix
What smartphone should I buy?
```

Result:

Creates a decision matrix comparing top smartphone options against key purchasing criteria, with 1-5 ratings for each combination

### Weighted decision matrix with custom options and criteria

```
+++DecisionMatrix(options=[Python,JavaScript,Go,Rust], criteria=[learning curve,performance,ecosystem,job market], weighted=true, scale=1-10)
Which programming language should I learn next?
```

Result:

Generates a weighted decision matrix comparing the specified programming languages against the given criteria, with weighted scores on a 1-10 scale

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(options, criteria, weighted=False, scale=DecisionMatrixScaleEnum.VALUE_1_5)`

Initialize DecisionMatrix decorator.

Args:
    options: Specific options or alternatives to evaluate in the matrix
    criteria: Evaluation criteria to assess each option against
    weighted: Whether to include weights for criteria importance
    scale: Rating scale to use for evaluations

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

