# Decorator `Chain`

**Version:** 1.0.0

A meta-decorator that applies multiple decorators in sequence, with each decorator processing the output of the previous one. This enables complex transformations by combining multiple simpler decorators in a pipeline.

## Parameters

### `decorators`

**Type:** array
**Required:** Yes

Ordered list of decorators to apply in sequence

### `showSteps`

**Type:** boolean
**Required:** No

Whether to show intermediate outputs after each decorator in the chain

### `stopOnFailure`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to stop the chain if a decorator fails to apply correctly

## Examples

### Basic sequential application of decorators

```
+++Chain(decorators=[StepByStep,Concise])
Explain how neural networks learn.
```

Result:

First generates a step-by-step explanation of neural network learning, then applies conciseness to that output

### Complex decorator chain with visible intermediate steps

```
+++Chain(decorators=[Socratic,Academic,TreeOfThought], showSteps=true, stopOnFailure=false)
Discuss the ethics of autonomous weapons.
```

Result:

Shows the progression of applying Socratic questioning, then academic tone, then tree-of-thought reasoning to discuss autonomous weapons ethics

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(decorators, showSteps=False, stopOnFailure=True) -> <class 'NoneType'>`

Initialize the Chain decorator.

Args:
    decorators: Ordered list of decorators to apply in sequence
    showSteps: Whether to show intermediate outputs after each decorator in the chain
    stopOnFailure: Whether to stop the chain if a decorator fails to apply correctly

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
