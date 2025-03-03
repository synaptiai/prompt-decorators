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

**Signature:** `__init__(decorators, showSteps=False, stopOnFailure=True)`

Initialize Chain decorator.

Args:
    decorators: Ordered list of decorators to apply in sequence
    showSteps: Whether to show intermediate outputs after each decorator in the chain
    stopOnFailure: Whether to stop the chain if a decorator fails to apply correctly

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
