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

**Signature:** `__init__(role, traits, goals) -> <class 'NoneType'>`

Initialize the Persona decorator.

Args:
    role: The specific persona or stakeholder role to adopt
    traits: Key personality traits or characteristics of the persona
    goals: Primary goals or concerns of the persona

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
