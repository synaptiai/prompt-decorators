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

**Signature:** `__init__(criteria=PeerReviewCriteriaEnum.ALL, style=PeerReviewStyleEnum.BALANCED, position=PeerReviewPositionEnum.AFTER)`

Initialize PeerReview decorator.

Args:
    criteria: Primary criteria to focus on in the review
    style: The tone and approach of the peer review
    position: Where to place the peer review relative to the main content

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

