# Decorator `Balanced`

**Version:** 1.0.0

Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position.

## Parameters

### `perspectives`

**Type:** number
**Required:** No
**Default:** `2`

Number of different perspectives to include

### `structure`

**Type:** enum
**Required:** No
**Default:** `sequential`

How to structure the different perspectives

**Allowed values:**

- `alternating`
- `sequential`
- `comparative`

### `equal`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to strictly enforce equal word count for each perspective

## Examples

### Basic balanced view of a controversial topic

```
+++Balanced
Discuss the pros and cons of nuclear energy.
```

Result:

Presents the benefits and drawbacks of nuclear energy with equal attention and detail given to both perspectives

### Balanced presentation of multiple perspectives in comparative structure

```
+++Balanced(perspectives=4, structure=comparative, equal=true)
What are the different views on artificial intelligence regulation?
```

Result:

Provides a balanced side-by-side comparison of four different perspectives on AI regulation, with equal word count allocated to each viewpoint

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(perspectives=2, structure=sequential, equal=True) -> <class 'NoneType'>`

Initialize the Balanced decorator.

Args:
    perspectives: Number of different perspectives to include
    structure: How to structure the different perspectives
    equal: Whether to strictly enforce equal word count for each perspective


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
