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

**Signature:** `__init__(metrics, scale=1-5, explanation=True) -> <class 'NoneType'>`

Initialize the QualityMetrics decorator.

Args:
    metrics: Specific quality metrics to measure (e.g., accuracy, completeness, clarity, usefulness)
    scale: Rating scale to use for evaluations
    explanation: Whether to provide detailed explanations for each metric score

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the decorator to a prompt string.

Args:
    prompt: The prompt to apply the decorator to


Returns:
    The modified prompt

#### `apply_to_prompt`

**Signature:** `apply_to_prompt(prompt) -> <class 'str'>`

Apply the decorator to a prompt.

Args:
    prompt: The prompt to decorate

Returns:
    The decorated prompt

#### `from_dict`

**Signature:** `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator instance from a dictionary representation.

Args:
    data: Dictionary representation of the decorator

Returns:
    A new decorator instance

Raises:
    ValidationError: If the dictionary is invalid

#### `get_metadata`

**Signature:** `get_metadata() -> typing.Dict[str, typing.Any]`

Get metadata about the decorator.

Returns:
    Dictionary containing metadata about the decorator


Args:
    cls: The decorator class

#### `is_compatible_with_version`

**Signature:** `is_compatible_with_version(version) -> <class 'bool'>`

Check if the decorator is compatible with a specific version.

Args:
    version: The version to check compatibility with.


Returns:
    True if compatible, False otherwise.


Raises:
    IncompatibleVersionError: If the version is incompatible.

#### `to_dict`

**Signature:** `to_dict() -> typing.Dict[str, typing.Any]`

Convert the decorator to a dictionary.

Args:
    self: The decorator instance

Returns:
    Dictionary representation of the decorator

#### `to_string`

**Signature:** `to_string() -> <class 'str'>`

Convert the decorator to a string.

Args:
    self: The decorator instance

Returns:
    String representation of the decorator

#### `transform_response`

**Signature:** `transform_response(response) -> <class 'str'>`

Transform the response from the model.

Args:
    response: The response to transform

Returns:
    The transformed response
