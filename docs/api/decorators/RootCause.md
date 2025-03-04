# Decorator `RootCause`

**Version:** 1.0.0

Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.

## Parameters

### `method`

**Type:** enum
**Required:** No
**Default:** `fivewhys`

The specific root cause analysis methodology to apply

**Allowed values:**

- `fivewhys`
- `fishbone`
- `pareto`

### `depth`

**Type:** number
**Required:** No
**Default:** `5`

Level of detail in the analysis (for fivewhys, represents number of 'why' iterations)

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

**Signature:** `__init__(method=fivewhys, depth=5) -> <class 'NoneType'>`

Initialize the RootCause decorator.

Args:
    method: The specific root cause analysis methodology to apply
    depth: Level of detail in the analysis (for fivewhys, represents number of 'why' iterations)

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
