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

**Signature:** `__init__(options, criteria, weighted=False, scale=1-5) -> <class 'NoneType'>`

Initialize the DecisionMatrix decorator.

Args:
    options: Specific options or alternatives to evaluate in the matrix
    criteria: Evaluation criteria to assess each option against
    weighted: Whether to include weights for criteria importance
    scale: Rating scale to use for evaluations

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
