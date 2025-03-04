# Decorator `Prioritize`

**Version:** 1.0.0

Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.

## Parameters

### `criteria`

**Type:** string
**Required:** No
**Default:** `importance`

The specific criterion to use for prioritization (e.g., importance, urgency, ROI)

### `count`

**Type:** number
**Required:** No
**Default:** `5`

Number of prioritized items to include

### `showRationale`

**Type:** boolean
**Required:** No

Whether to explain the reasoning behind each priority ranking

## Examples

### Basic prioritization of key factors

```
+++Prioritize
What factors should be considered when designing a mobile app?
```

Result:

Presents the top 5 factors for mobile app design, ranked by importance from most to least critical

### Detailed prioritization with custom criteria and rationale

```
+++Prioritize(criteria=ROI, count=7, showRationale=true)
What marketing strategies should our startup focus on?
```

Result:

Provides 7 marketing strategies ranked by return on investment, with explanations for each ranking position

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(criteria=importance, count=5, showRationale=False) -> <class 'NoneType'>`

Initialize the Prioritize decorator.

Args:
    criteria: The specific criterion to use for prioritization (e.g., importance, urgency, ROI)
    count: Number of prioritized items to include
    showRationale: Whether to explain the reasoning behind each priority ranking


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
