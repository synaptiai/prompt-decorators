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

**Signature:** `__init__(models, fallback, behaviors) -> <class 'NoneType'>`

Initialize the Compatibility decorator.

Args:
    models: List of specific models to adapt for (e.g., gpt-3.5-turbo, gpt-4, etc.)
    fallback: Decorator to apply if the current model doesn't match any in the models list
    behaviors: JSON string mapping model names to specific adaptations (e.g., '{"gpt-3.5-turbo": "simplify complex reasoning", "gpt-4": "maximize detailed analysis"}')

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
