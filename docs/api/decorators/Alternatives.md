# Decorator `Alternatives`

**Version:** 1.0.0

Presents multiple distinct options, approaches, or solutions to a question or problem. This decorator encourages exploring different paths or perspectives rather than providing a single definitive answer.

## Parameters

### `count`

**Type:** number
**Required:** No
**Default:** `3`

Number of alternative options or approaches to generate

### `diversity`

**Type:** enum
**Required:** No
**Default:** `medium`

How different or varied the alternatives should be from each other

**Allowed values:**

- `low`
- `medium`
- `high`

### `comparison`

**Type:** boolean
**Required:** No

Whether to include a comparative analysis of the alternatives

## Examples

### Basic alternative approaches to a problem

```
+++Alternatives
How can I improve my public speaking skills?
```

Result:

Provides three distinct approaches to improving public speaking skills, each with its own methodology and focus

### Highly diverse alternatives with comparative analysis

```
+++Alternatives(count=5, diversity=high, comparison=true)
What are some ways to reduce carbon emissions in urban areas?
```

Result:

Presents five highly diverse approaches to reducing urban carbon emissions, followed by a comparative analysis of their effectiveness, cost, and implementation challenges

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(count=3, diversity=medium, comparison=False) -> <class 'NoneType'>`

Initialize the Alternatives decorator.

Args:
    count: Number of alternative options or approaches to generate
    diversity: How different or varied the alternatives should be from each other
    comparison: Whether to include a comparative analysis of the alternatives


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
