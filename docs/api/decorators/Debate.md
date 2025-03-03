# Decorator `Debate`

**Version:** 1.0.0

Structures the response as a debate between multiple perspectives on a topic. This decorator encourages balanced representation of different viewpoints and helps explore complex issues from various angles.

## Parameters

### `perspectives`

**Type:** number
**Required:** No
**Default:** `2`

Number of different perspectives to include in the debate

### `balanced`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to ensure equal representation and strength of arguments for each perspective

## Examples

### Two-perspective debate on an ethical issue

```
+++Debate
Is it ethical to use AI-generated content without disclosure?
```

Result:

Presents balanced arguments for and against disclosure of AI-generated content

### Three-perspective debate on a policy issue with balanced representation

```
+++Debate(perspectives=3, balanced=true)
Should universal basic income be implemented nationally?
```

Result:

Presents three balanced perspectives on UBI in a debate format, ensuring equal representation of each viewpoint

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`
- `claude-3`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(perspectives=2, balanced=True) -> <class 'NoneType'>`

Initialize the Debate decorator.

Args:
    perspectives: Number of different perspectives to include in the debate
    balanced: Whether to ensure equal representation and strength of arguments for each perspective

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
