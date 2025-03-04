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

**Signature:** `__init__(domain=general, count=1, depth=moderate) -> <class 'NoneType'>`

Initialize the Analogical decorator.

Args:
    domain: Specific domain or context to draw analogies from (if not specified, will choose appropriate domains)
    count: Number of distinct analogies to provide
    depth: Level of detail in developing the analogy

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
