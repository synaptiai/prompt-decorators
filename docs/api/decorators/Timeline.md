# Decorator `Timeline`

**Version:** 1.0.0

Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.

## Parameters

### `granularity`

**Type:** enum
**Required:** No
**Default:** `year`

The level of time detail to include in the timeline

**Allowed values:**

- `day`
- `month`
- `year`
- `decade`
- `century`
- `era`

### `format`

**Type:** enum
**Required:** No
**Default:** `list`

The presentation format for the timeline

**Allowed values:**

- `list`
- `narrative`
- `table`

### `details`

**Type:** enum
**Required:** No
**Default:** `moderate`

The level of detail to include for each timeline event

**Allowed values:**

- `minimal`
- `moderate`
- `comprehensive`

## Examples

### Basic chronological timeline of major events

```
+++Timeline
Describe the key developments in artificial intelligence.
```

Result:

Presents a year-by-year list of important AI milestones and breakthroughs from earliest developments to present day

### Detailed narrative timeline with specific date granularity

```
+++Timeline(granularity=month, format=narrative, details=comprehensive)
What were the major events of the Apollo 11 mission?
```

Result:

Provides a flowing narrative account of the Apollo 11 mission with month/day dates and comprehensive details of each significant event

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(granularity=year, format=list, details=moderate) -> <class 'NoneType'>`

Initialize the Timeline decorator.

Args:
    granularity: The level of time detail to include in the timeline
    format: The presentation format for the timeline
    details: The level of detail to include for each timeline event


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
