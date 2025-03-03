# Decorator `TreeOfThought`

**Version:** 1.0.0

Organizes the response as a branching exploration of multiple reasoning paths. This decorator enables the AI to consider several possible approaches or hypotheses simultaneously, exploring the implications of each before reaching conclusions.

## Parameters

### `branches`

**Type:** number
**Required:** No
**Default:** `3`

Number of different reasoning branches to explore

### `depth`

**Type:** number
**Required:** No
**Default:** `3`

Maximum depth of reasoning in each branch

### `pruning`

**Type:** boolean
**Required:** No

Whether to eliminate less promising branches early

## Examples

### Multi-branch problem solving for a complex question

```
+++TreeOfThought
What might explain the Fermi Paradox?
```

Result:

Explores three different reasoning branches about potential explanations for the Fermi Paradox, developing each path to moderate depth

### Deep, focused exploration with pruning

```
+++TreeOfThought(branches=5, depth=5, pruning=true)
How might we solve the climate change crisis?
```

Result:

Starts with five different approaches to climate change, explores each in depth, and eliminates less promising branches to focus on the most viable solutions

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(branches=3, depth=3, pruning=False)`

Initialize TreeOfThought decorator.

Args:
    branches: Number of different reasoning branches to explore
    depth: Maximum depth of reasoning in each branch
    pruning: Whether to eliminate less promising branches early

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
