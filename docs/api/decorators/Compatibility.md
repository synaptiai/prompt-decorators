# Decorator `Compatibility`

**Version:** 1.0.0

A meta-decorator that specifies model-specific adaptations or fall-back behaviors. This enables graceful degradation of decorator functionalities across different LLM capabilities and ensures optimal performance across model variants.

## Parameters

### `models`

**Type:** array
**Required:** Yes

List of specific models to adapt for (e.g., gpt-3.5-turbo, gpt-4, etc.)

### `fallback`

**Type:** string
**Required:** No

Decorator to apply if the current model doesn't match any in the models list

### `behaviors`

**Type:** string
**Required:** No

JSON string mapping model names to specific adaptations (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning", "gpt-4": "maximize detailed analysis"}')

## Examples

### Basic model-specific adaptation

```
+++Compatibility(models=[gpt-4], fallback=StepByStep)
+++TreeOfThought(branches=3, depth=3)
Solve this complex optimization problem.
```

Result:

If using GPT-4, applies the TreeOfThought decorator with full functionality; if using any other model, falls back to the simpler StepByStep decorator

### Detailed model-specific behavior adaptations

```
+++Compatibility(models=[gpt-4,gpt-3.5-turbo], behaviors={"gpt-4":"use full mathematical notation and derivations", "gpt-3.5-turbo":"use simplified equations and more intuitive explanations"})
+++Academic(style=scientific)
Explain quantum field theory.
```

Result:

Applies the Academic decorator but adapts how quantum field theory is explained based on the specific model capabilities, with full mathematical rigor for GPT-4 or simplified explanations for GPT-3.5-turbo

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(models, fallback, behaviors)`

Initialize Compatibility decorator.

Args:
    models: List of specific models to adapt for (e.g., gpt-3.5-turbo, gpt-4, etc.)
    fallback: Decorator to apply if the current model doesn't match any in the models list
    behaviors: JSON string mapping model names to specific adaptations (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning", "gpt-4": "maximize detailed analysis"}')

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
