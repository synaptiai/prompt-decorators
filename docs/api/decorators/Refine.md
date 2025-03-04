# Decorator `Refine`

**Version:** 1.0.0

A meta-decorator that iteratively improves the output based on specified criteria or dimensions. This decorator simulates multiple drafts or revisions of content, with each iteration focusing on enhancing particular aspects of the response.

## Parameters

### `iterations`

**Type:** number
**Required:** No
**Default:** `2`

Number of refinement cycles to perform

### `focus`

**Type:** array
**Required:** No

Specific aspects to focus on during refinement (e.g., clarity, conciseness, evidence)

### `showProcess`

**Type:** boolean
**Required:** No

Whether to show the intermediate steps in the refinement process

## Examples

### Basic refinement of a complex explanation

```
+++Refine
Explain the implications of quantum computing for cybersecurity.
```

Result:

Provides a refined explanation of quantum computing implications for cybersecurity, with two hidden iterations improving clarity and accuracy

### Detailed refinement with visible iterations

```
+++Refine(iterations=3, focus=[clarity,evidence,conciseness], showProcess=true)
Analyze the economic impacts of artificial intelligence.
```

Result:

Shows three visible iterations of analyzing AI economic impacts, with each step focusing on improving clarity, strengthening evidence, and enhancing conciseness

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(iterations=2, focus, showProcess=False) -> <class 'NoneType'>`

Initialize the Refine decorator.

Args:
    iterations: Number of refinement cycles to perform
    focus: Specific aspects to focus on during refinement (e.g., clarity, conciseness, evidence)
    showProcess: Whether to show the intermediate steps in the refinement process

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
