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

**Signature:** `__init__(scenarios=3, severity=StressTestSeverityEnum.SEVERE, domain)`

Initialize StressTest decorator.

Args:
    scenarios: Number of stress test scenarios to apply
    severity: The intensity level of the stress conditions
    domain: Optional specific domain or dimension to stress test (e.g., financial, ethical, scalability)

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
