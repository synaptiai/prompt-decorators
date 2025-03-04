# Decorator `BreakAndBuild`

**Version:** 1.0.0

Structures responses in two distinct phases: first critically analyzing and 'breaking down' an idea by identifying flaws, assumptions, and weaknesses, then 'building it back up' with improvements, refinements, and solutions. This decorator enhances critical thinking while maintaining constructive output.

## Parameters

### `breakdown`

**Type:** enum
**Required:** No
**Default:** `comprehensive`

Primary approach for the critical breakdown phase

**Allowed values:**

- `weaknesses`
- `assumptions`
- `risks`
- `comprehensive`

### `intensity`

**Type:** enum
**Required:** No
**Default:** `thorough`

How thorough and challenging the breakdown phase should be

**Allowed values:**

- `mild`
- `thorough`
- `intense`

### `buildRatio`

**Type:** number
**Required:** No
**Default:** `1`

Approximate ratio of build-up content to breakdown content (e.g., 2 means twice as much reconstruction as critique)

## Examples

### Basic break and build analysis of a business concept

```
+++BreakAndBuild
Evaluate this startup idea: a subscription service for plant care.
```

Result:

First thoroughly critiques the plant care subscription concept by identifying weaknesses and risks, then reconstructs it with improvements and solutions of equal depth

### Intense breakdown of assumptions with substantial rebuilding

```
+++BreakAndBuild(breakdown=assumptions, intensity=intense, buildRatio=2)
Analyze this public policy proposal for reducing urban congestion.
```

Result:

Delivers an intense critique focused specifically on the assumptions underlying the urban congestion proposal, followed by twice as much content reconstructing it with stronger foundations and improvements

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(breakdown=comprehensive, intensity=thorough, buildRatio=1) -> <class 'NoneType'>`

Initialize the BreakAndBuild decorator.

Args:
    breakdown: Primary approach for the critical breakdown phase
    intensity: How thorough and challenging the breakdown phase should be
    buildRatio: Approximate ratio of build-up content to breakdown content (e.g., 2 means twice as much reconstruction as critique)

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
