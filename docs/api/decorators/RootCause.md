# Decorator `RootCause`

**Version:** 1.0.0

Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.

## Parameters

### `method`

**Type:** enum
**Required:** No
**Default:** `5whys`

The specific root cause analysis methodology to apply

**Allowed values:**

- `5whys`
- `fishbone`
- `pareto`

### `depth`

**Type:** number
**Required:** No
**Default:** `5`

Level of detail in the analysis (for 5whys, represents number of 'why' iterations)

## Examples

### Basic 5 Whys analysis of a business problem

```
+++RootCause
Why is our website's bounce rate increasing?
```

Result:

Performs a systematic 5 Whys analysis to trace the increasing bounce rate back to its fundamental causes

### Fishbone diagram approach to a technical issue

```
+++RootCause(method=fishbone)
Why do our application servers crash under moderate load?
```

Result:

Analyzes the server crashes using the fishbone (Ishikawa) methodology, categorizing potential causes into major categories like People, Process, Equipment, etc.

### Pareto analysis with deeper investigation

```
+++RootCause(method=pareto, depth=7)
What factors are causing our manufacturing defects?
```

Result:

Uses Pareto principle to identify the vital few causes responsible for most manufacturing defects, with an exceptionally thorough analysis

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(method=RootCauseMethodEnum.VALUE_5WHYS, depth=5)`

Initialize RootCause decorator.

Args:
    method: The specific root cause analysis methodology to apply
    depth: Level of detail in the analysis (for 5whys, represents number of 'why' iterations)

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
