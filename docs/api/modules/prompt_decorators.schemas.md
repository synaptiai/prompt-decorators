# schemas

Schema definitions for prompt decorators.

This package contains schema definitions for validating decorator definitions
and parameters.

## Public API

This module exports the following components:

- `DecoratorSchema`: Class - Schema for decorator definitions
- `ParameterSchema`: Class - Schema for decorator parameters

## Classes

### `DecoratorSchema`

*Imported from `prompt_decorators.schemas.decorator_schema`*

Schema for decorator definitions.

#### Attributes

- `from_dict`: `classmethod` = `<classmethod(<function DecoratorSchema.from_dict at 0x105a74ae0>)>`

#### Methods

##### `__init__`

Initialize a decorator schema.

Args:
    name: Name of the decorator
    description: Description of the decorator
    category: Category of the decorator
    parameters: List of parameter schemas
    transform_function: JavaScript function for transforming prompts
    version: Version of the decorator

**Signature:** `__init__(self, name: str, description: str, category: str, parameters: List[prompt_decorators.schemas.decorator_schema.ParameterSchema], transform_function: str, version: str = '1.0.0')`

**Parameters:**

- `name`: `str`
- `description`: `str`
- `category`: `str`
- `parameters`: `List`
- `transform_function`: `str`
- `version`: `str` (default: `1.0.0`)

##### `to_dict`

Convert the schema to a dictionary.

**Signature:** `to_dict(self) -> Dict[str, Any]`

**Parameters:**


**Returns:** `Dict`

### `ParameterSchema`

*Imported from `prompt_decorators.schemas.decorator_schema`*

Schema for decorator parameters.

#### Attributes

- `from_dict`: `classmethod` = `<classmethod(<function ParameterSchema.from_dict at 0x105a74900>)>`

#### Methods

##### `__init__`

Initialize a parameter schema.

Args:
    name: Name of the parameter
    description: Description of the parameter
    type_: Type of the parameter (string, integer, float, boolean, enum)
    required: Whether the parameter is required
    default: Default value for the parameter
    enum_values: Possible values for enum type
    min_value: Minimum value for numeric types
    max_value: Maximum value for numeric types
    min_length: Minimum length for string or array types
    max_length: Maximum length for string or array types
    pattern: Regex pattern for string validation

**Signature:** `__init__(self, name: str, description: str, type_: str = 'string', required: bool = False, default: Any = None, enum_values: Optional[List[str]] = None, min_value: Union[int, float, NoneType] = None, max_value: Union[int, float, NoneType] = None, min_length: Optional[int] = None, max_length: Optional[int] = None, pattern: Optional[str] = None)`

**Parameters:**

- `name`: `str`
- `description`: `str`
- `type_`: `str` (default: `string`)
- `required`: `bool` (default: `False`)
- `default`: `Any` (default: `None`)
- `enum_values`: `Optional` (default: `None`)
- `min_value`: `Union` (default: `None`)
- `max_value`: `Union` (default: `None`)
- `min_length`: `Optional` (default: `None`)
- `max_length`: `Optional` (default: `None`)
- `pattern`: `Optional` (default: `None`)

##### `to_dict`

Convert the schema to a dictionary.

**Signature:** `to_dict(self) -> Dict[str, Any]`

**Parameters:**


**Returns:** `Dict`
