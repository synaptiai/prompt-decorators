# Decorator `FirstPrinciples`

**Version:** 1.0.0

Structures the response by breaking down complex topics into their fundamental truths or axioms, then building up from there. This decorator promotes a deeper understanding by examining the most basic elements of a concept before constructing more complex ideas.

## Parameters

### `depth`

**Type:** number
**Required:** No
**Default:** `3`

Level of detail in breaking down to fundamental principles

## Examples

### Basic first principles analysis of a concept

```
+++FirstPrinciples
How do electric vehicles work?
```

Result:

Breaks down electric vehicles into fundamental principles of electricity, motors, and energy storage before explaining the complete system

### Deep first principles analysis with maximum depth

```
+++FirstPrinciples(depth=5)
What makes machine learning effective?
```

Result:

Provides an extensive breakdown of machine learning starting from mathematical foundations and progressively building up to complex algorithms

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(depth=3) -> <class 'NoneType'>`

Initialize the FirstPrinciples decorator.

Args:
    depth: Level of detail in breaking down to fundamental principles

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
