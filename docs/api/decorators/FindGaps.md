# Decorator `FindGaps`

**Version:** 1.0.0

Identifies missing elements, unanswered questions, or overlooked considerations in an idea, plan, or argument. This decorator helps improve completeness by systematically discovering and highlighting gaps that need addressing.

## Parameters

### `aspects`

**Type:** enum
**Required:** No
**Default:** `comprehensive`

The specific types of gaps to focus on finding

**Allowed values:**

- `questions`
- `resources`
- `stakeholders`
- `risks`
- `dependencies`
- `comprehensive`

### `depth`

**Type:** enum
**Required:** No
**Default:** `thorough`

How thoroughly to analyze for gaps

**Allowed values:**

- `basic`
- `thorough`
- `exhaustive`

### `solutions`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to suggest solutions or approaches for addressing the identified gaps

## Examples

### Basic comprehensive gap analysis of a business plan

```
+++FindGaps
We plan to launch our SaaS product with these features and marketing channels...
```

Result:

First identifies gaps across various aspects of the SaaS product launch plan, then suggests solutions for addressing each gap

### Exhaustive stakeholder-focused gap analysis without solutions

```
+++FindGaps(aspects=stakeholders, depth=exhaustive, solutions=false)
Here's our urban redevelopment proposal...
```

Result:

Provides an exhaustive analysis of overlooked or inadequately considered stakeholders in the urban redevelopment proposal, without suggesting solutions

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(aspects=comprehensive, depth=thorough, solutions=True) -> <class 'NoneType'>`

Initialize the FindGaps decorator.

Args:
    aspects: The specific types of gaps to focus on finding
    depth: How thoroughly to analyze for gaps
    solutions: Whether to suggest solutions or approaches for addressing the identified gaps


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
