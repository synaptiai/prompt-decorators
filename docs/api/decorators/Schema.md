# Decorator `Schema`

**Version:** 1.0.0

Defines a custom structure for the AI's response using a specified schema format. This decorator enables precise control over the output structure, ensuring responses follow a consistent, well-defined format optimized for specific use cases or data processing needs.

## Parameters

### `schema`

**Type:** string
**Required:** Yes

JSON Schema definition or reference to a predefined schema that defines the structure of the response

### `strict`

**Type:** boolean
**Required:** No

Whether to enforce strict schema compliance or allow flexibility

## Examples

### Basic schema for a person's information

```
+++Schema(schema={"type":"object","properties":{"name":{"type":"string"},"age":{"type":"number"},"interests":{"type":"array","items":{"type":"string"}}}})
Describe a fictional character.
```

Result:

Returns information about a fictional character structured according to the specified schema with name, age, and interests

### Strict schema for product information

```
+++Schema(schema={"type":"object","required":["productName","price","features"],"properties":{"productName":{"type":"string"},"price":{"type":"number"},"features":{"type":"array"},"availability":{"type":"boolean"}}}, strict=true)
Describe a smartphone.
```

Result:

Returns smartphone information strictly following the specified schema with all required fields and proper data types

## Compatibility

**Conflicts with:**

- `OutputFormat`

**Supported models:**

- `gpt-4`
- `gpt-3.5-turbo`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(schema, strict=False) -> <class 'NoneType'>`

Initialize the Schema decorator.

Args:
    schema: JSON Schema definition or reference to a predefined schema that defines the structure of the response
    strict: Whether to enforce strict schema compliance or allow flexibility

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
