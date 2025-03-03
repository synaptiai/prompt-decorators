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

**Signature:** `__init__(perspectives=2, structure=BalancedStructureEnum.SEQUENTIAL, equal=True)`

Initialize Balanced decorator.

Args:
    perspectives: Number of different perspectives to include
    structure: How to structure the different perspectives
    equal: Whether to strictly enforce equal word count for each perspective

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
