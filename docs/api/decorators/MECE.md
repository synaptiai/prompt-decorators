# Decorator `MECE`

**Version:** 1.0.0

Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.

## Parameters

### `dimensions`

**Type:** number
**Required:** No
**Default:** `3`

Number of top-level MECE dimensions to use for categorization

### `depth`

**Type:** number
**Required:** No
**Default:** `2`

Maximum level of hierarchical breakdown within each dimension

### `framework`

**Type:** enum
**Required:** No
**Default:** `custom`

Optional predefined MECE framework to apply

**Allowed values:**

- `issue tree`
- `value chain`
- `business segments`
- `stakeholders`
- `custom`

## Examples

### Basic MECE analysis of a business problem

```
+++MECE
What factors should we consider when expanding to a new market?
```

Result:

Organizes market expansion factors into 3 mutually exclusive, collectively exhaustive categories with no overlaps and full coverage of all considerations

### Detailed MECE framework with stakeholder focus

```
+++MECE(dimensions=4, depth=3, framework=stakeholders)
Analyze the implications of implementing a four-day work week.
```

Result:

Provides a 4-dimension MECE analysis of a four-day work week using a stakeholder framework, with up to 3 levels of hierarchical breakdown within each stakeholder category

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(dimensions=3, depth=2, framework=custom) -> <class 'NoneType'>`

Initialize the MECE decorator.

Args:
    dimensions: Number of top-level MECE dimensions to use for categorization
    depth: Maximum level of hierarchical breakdown within each dimension
    framework: Optional predefined MECE framework to apply


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
