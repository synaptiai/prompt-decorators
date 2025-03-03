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

**Signature:** `__init__(breakdown=BreakAndBuildBreakdownEnum.COMPREHENSIVE, intensity=BreakAndBuildIntensityEnum.THOROUGH, buildRatio=1)`

Initialize BreakAndBuild decorator.

Args:
    breakdown: Primary approach for the critical breakdown phase
    intensity: How thorough and challenging the breakdown phase should be
    buildRatio: Approximate ratio of build-up content to breakdown content (e.g., 2 means twice as much reconstruction as critique)

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
