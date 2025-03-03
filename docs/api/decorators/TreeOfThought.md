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

**Signature:** `__init__(branches=3, depth=3, pruning=False) -> <class 'NoneType'>`

Initialize the TreeOfThought decorator.

Args:
    branches: Number of different reasoning branches to explore
    depth: Maximum depth of reasoning in each branch
    pruning: Whether to eliminate less promising branches early

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

Returns:
    Dictionary representation of the decorator

#### `to_string`

**Signature:** `to_string() -> <class 'str'>`

Convert the decorator to a string.

Returns:
    String representation of the decorator

#### `transform_response`

**Signature:** `transform_response(response) -> <class 'str'>`

Transform the response from the model.

Args:
    response: The response to transform

Returns:
    The transformed response
