# Decorator `Persona`

**Version:** 1.0.0

Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic.

## Parameters

### `role`

**Type:** string
**Required:** Yes

The specific persona or stakeholder role to adopt

### `traits`

**Type:** array
**Required:** No

Key personality traits or characteristics of the persona

### `goals`

**Type:** array
**Required:** No

Primary goals or concerns of the persona

## Examples

### Response from the perspective of a specific stakeholder

```
+++Persona(role=customer)
What are the implications of implementing a new subscription model?
```

Result:

Analyzes the subscription model from a customer's perspective, focusing on value, convenience, and potential concerns

### Detailed persona with specific traits and goals

```
+++Persona(role=senior software engineer, traits=[pragmatic,detail-oriented,experienced], goals=[code quality,maintainability,efficiency])
Evaluate the proposal to switch from monolith to microservices.
```

Result:

Provides a detailed analysis of the monolith-to-microservices transition from the perspective of a pragmatic, detail-oriented senior engineer who prioritizes code quality and maintainability

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(role, traits, goals)`

Initialize Persona decorator.

Args:
    role: The specific persona or stakeholder role to adopt
    traits: Key personality traits or characteristics of the persona
    goals: Primary goals or concerns of the persona

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

This base implementation does basic type checking.
Subclasses should override for specific validation.

Raises:
    ValidationError: If any parameter fails validation
