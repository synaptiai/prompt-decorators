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

**Signature:** `__init__(schema, strict=False)`

Initialize Schema decorator.

Args:
    schema: JSON Schema definition or reference to a predefined schema that defines the structure of the response
    strict: Whether to enforce strict schema compliance or allow flexibility

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
