# Decorator `Conditional`

**Version:** 1.0.0

A meta-decorator that applies different decorators based on specified conditions. This enables dynamic behavior where the response formatting and approach changes depending on the content, context, or user-specified parameters.

## Parameters

### `if_param`

**Type:** string
**Required:** Yes

The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}')

### `then`

**Type:** string
**Required:** Yes

The decorator to apply if the condition is true (can be a specific decorator with parameters)

### `else_param`

**Type:** string
**Required:** No

The decorator to apply if the condition is false (can be a specific decorator with parameters)

## Examples

### Basic conditional application based on content complexity

```
+++Conditional(if_param=complex, then=StepByStep, else_param=Concise)
Explain how quantum computing works.
```

Result:

Evaluates if the topic is complex, which quantum computing is, so it applies the StepByStep decorator

### Conditional application with parameterized decorators

```
+++Conditional(if_param=controversial, then=Debate(perspectives=3), else_param=Reasoning(depth=moderate))
Discuss the ethical implications of gene editing in humans.
```

Result:

Determines that gene editing ethics is controversial, so it applies the Debate decorator with 3 perspectives rather than the Reasoning decorator

## Compatibility

**Supported models:**

- `gpt-4`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(if_param, then, else_param) -> <class 'NoneType'>`

Initialize the Conditional decorator.

Args:
    if_param: The condition to evaluate (e.g., 'technical', 'complex', 'controversial', or a parameter like '{param}')
    then: The decorator to apply if the condition is true (can be a specific decorator with parameters)
    else_param: The decorator to apply if the condition is false (can be a specific decorator with parameters)


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
