# Decorator `PeerReview`

**Version:** 1.0.0

Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.

## Parameters

### `criteria`

**Type:** enum
**Required:** No
**Default:** `all`

Primary criteria to focus on in the review

**Allowed values:**

- `accuracy`
- `methodology`
- `limitations`
- `completeness`
- `all`

### `style`

**Type:** enum
**Required:** No
**Default:** `balanced`

The tone and approach of the peer review

**Allowed values:**

- `constructive`
- `critical`
- `balanced`

### `position`

**Type:** enum
**Required:** No
**Default:** `after`

Where to place the peer review relative to the main content

**Allowed values:**

- `after`
- `before`
- `alongside`

## Examples

### Basic peer review of content accuracy

```
+++PeerReview(criteria=accuracy)
Explain the current understanding of dark matter in astrophysics.
```

Result:

Provides an explanation of dark matter, followed by a balanced peer review focusing on the accuracy of the information presented

### Critical peer review of multiple aspects, shown alongside content

```
+++PeerReview(criteria=all, style=critical, position=alongside)
Analyze the methodology used in Stanford's prison experiment.
```

Result:

Delivers an analysis of the Stanford prison experiment methodology with a parallel critical peer review addressing accuracy, methodology, limitations, and completeness

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(criteria=all, style=balanced, position=after) -> <class 'NoneType'>`

Initialize the PeerReview decorator.

Args:
    criteria: Primary criteria to focus on in the review
    style: The tone and approach of the peer review
    position: Where to place the peer review relative to the main content


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

This method transforms the prompt using the transformation template.

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
