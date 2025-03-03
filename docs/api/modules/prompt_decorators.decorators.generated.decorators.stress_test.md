# Module `prompt_decorators.decorators.generated.decorators.stress_test`

Implementation of the StressTest decorator.

This module provides the StressTest decorator class for use in prompt engineering.

Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances.

## Classes

- [`StressTest`](#class-stresstest): Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances.

### Class `StressTest`

Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances.

Attributes:
    scenarios: Number of stress test scenarios to apply. (Any)
    severity: The intensity level of the stress conditions. (Literal["moderate", "severe", "extreme"])
    domain: Optional specific domain or dimension to stress test (e.g., financial, ethical, scalability). (str)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(scenarios=3, severity=severe, domain) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `domain`: Get the domain parameter value.
- `name`: Get the name of the decorator.
- `scenarios`: Get the scenarios parameter value.
- `severity`: Get the severity parameter value.
