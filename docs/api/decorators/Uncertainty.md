# Decorator `Uncertainty`

**Version:** 1.0.0

Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.

## Parameters

### `format`

**Type:** enum
**Required:** No
**Default:** `inline`

How to format uncertainty indications in the response

**Allowed values:**

- `inline`
- `section`
- `confidence`

### `threshold`

**Type:** enum
**Required:** No
**Default:** `medium`

The threshold for flagging uncertain content

**Allowed values:**

- `low`
- `medium`
- `high`

### `reason`

**Type:** boolean
**Required:** No

Whether to explain the reason for uncertainty

## Examples

### Inline uncertainty markers in a technical explanation

```
+++Uncertainty
Explain the potential timeline for achieving artificial general intelligence.
```

Result:

Explains AGI timelines with inline uncertainty markers highlighting speculative predictions, areas of expert disagreement, and knowledge gaps

### Dedicated uncertainty section with detailed reasoning

```
+++Uncertainty(format=section, reason=true, threshold=low)
What are the environmental impacts of fusion energy?
```

Result:

Provides information about fusion energy's environmental impacts followed by a dedicated section discussing all points of uncertainty with explanations for why each point is uncertain

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(format=inline, threshold=medium, reason=False) -> <class 'NoneType'>`

Initialize the Uncertainty decorator.

Args:
    format: How to format uncertainty indications in the response
    threshold: The threshold for flagging uncertain content
    reason: Whether to explain the reason for uncertainty


Returns:
    None

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
