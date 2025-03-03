# Decorator `Analogical`

**Version:** 1.0.0

Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.

## Parameters

### `domain`

**Type:** string
**Required:** No
**Default:** `general`

Specific domain or context to draw analogies from (if not specified, will choose appropriate domains)

### `count`

**Type:** number
**Required:** No
**Default:** `1`

Number of distinct analogies to provide

### `depth`

**Type:** enum
**Required:** No
**Default:** `moderate`

Level of detail in developing the analogy

**Allowed values:**

- `brief`
- `moderate`
- `extended`

## Examples

### Single analogy from a specific domain

```
+++Analogical(domain=sports)
Explain how the immune system works.
```

Result:

Explains the immune system using extended sports analogies, comparing immune cells to players, pathogens to opponents, etc.

### Multiple brief analogies from different domains

```
+++Analogical(count=3, depth=brief)
Describe how blockchain technology functions.
```

Result:

Provides three different brief analogies for blockchain from different domains (perhaps physical ledgers, chain of custody, and distributed networks)

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(domain=general, count=1, depth=AnalogicalDepthEnum.MODERATE)`

Initialize Analogical decorator.

Args:
    domain: Specific domain or context to draw analogies from (if not specified, will choose appropriate domains)
    count: Number of distinct analogies to provide
    depth: Level of detail in developing the analogy

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
