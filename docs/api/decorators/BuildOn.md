# Decorator `BuildOn`

**Version:** 1.0.0

A meta-decorator that builds upon previous context or responses rather than starting from scratch. This enables continuity across interactions, allowing refinement, extension, or alteration of previous outputs in a coherent manner.

## Parameters

### `reference`

**Type:** enum
**Required:** No
**Default:** `last`

What to build upon from the previous context

**Allowed values:**

- `last`
- `specific`
- `all`

### `approach`

**Type:** enum
**Required:** No
**Default:** `extend`

How to build upon the referenced content

**Allowed values:**

- `extend`
- `refine`
- `contrast`
- `synthesize`

### `preserveStructure`

**Type:** boolean
**Required:** No
**Default:** `True`

Whether to maintain the structure of the referenced content

## Examples

### Basic extension of the previous response

```
+++BuildOn
Add more detail about implementation challenges.
```

Result:

Extends the previous response by adding more detailed information about implementation challenges while maintaining continuity

### Specific refinement with structural changes

```
+++BuildOn(reference=specific, approach=refine, preserveStructure=false)
Improve the section on risk analysis with more quantitative measures.
```

Result:

Refines specifically the risk analysis section from the previous content with more quantitative measures, potentially restructuring it

## Compatibility

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(reference=last, approach=extend, preserveStructure=True) -> <class 'NoneType'>`

Initialize the BuildOn decorator.

Args:
    reference: What to build upon from the previous context
    approach: How to build upon the referenced content
    preserveStructure: Whether to maintain the structure of the referenced content

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
