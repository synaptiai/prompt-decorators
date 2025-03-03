# Decorator `StressTest`

**Version:** 1.0.0

Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances.

## Parameters

### `scenarios`

**Type:** number
**Required:** No
**Default:** `3`

Number of stress test scenarios to apply

### `severity`

**Type:** enum
**Required:** No
**Default:** `severe`

The intensity level of the stress conditions

**Allowed values:**

- `moderate`
- `severe`
- `extreme`

### `domain`

**Type:** string
**Required:** No

Optional specific domain or dimension to stress test (e.g., financial, ethical, scalability)

## Examples

### Basic stress test of a business model

```
+++StressTest
Evaluate this subscription-based SaaS business model.
```

Result:

Provides an analysis of the business model followed by three severe stress test scenarios that challenge its core assumptions and viability

### Extreme stress test focused on a specific domain

```
+++StressTest(scenarios=5, severity=extreme, domain=security)
Assess our new authentication protocol design.
```

Result:

Delivers an assessment of the authentication protocol followed by five extreme security-focused stress test scenarios that identify potential vulnerabilities and breaking points

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(scenarios=3, severity=severe, domain) -> <class 'NoneType'>`

Initialize the StressTest decorator.

Args:
    scenarios: Number of stress test scenarios to apply
    severity: The intensity level of the stress conditions
    domain: Optional specific domain or dimension to stress test (e.g., financial, ethical, scalability)

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
