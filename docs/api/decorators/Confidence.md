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

**Signature:** `__init__(scale=qualitative, threshold=50, detailed=False) -> <class 'NoneType'>`

Initialize the Confidence decorator.

Args:
    scale: The method used to express confidence levels
    threshold: Minimum confidence level for including information (as a percentage)
    detailed: Whether to provide explanations for confidence assessments

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
