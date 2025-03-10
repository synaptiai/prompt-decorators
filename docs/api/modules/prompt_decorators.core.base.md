# base

Base classes for prompt decorators.

This module provides the base classes and utilities for creating and using
prompt decorators.

## Classes

### `BaseDecorator`

Base class for all prompt decorators.

This class defines the common interface and behavior for all decorators.
Subclasses should implement the apply_to_prompt and transform_response methods.

#### Attributes

- `conflicts_with`: `set` = `set()`
- `description`: `str` = `'Base decorator class'`
- `from_dict`: `classmethod` = `<classmethod(<function DecoratorBase.from_dict at 0x10651f4c0>)>`
- `name`: `str` = `'DecoratorBase'`
- `parameters`: `dict` = `{}`
- `transformation_template`: `dict` = `{'instruction': '', 'parameterMapping': {}, 'placement': 'prepend', 'compositionBehavior': 'accumulate'}`

#### Methods

##### `__init__`

Initialize a decorator with parameter values.

Args:
    **kwargs: Parameter values for the decorator

Raises:
    ValidationError: If any parameter values are invalid

**Signature:** `__init__(self, **kwargs)`

**Parameters:**

- `kwargs`:

##### `apply_to_prompt`

Apply the decorator to a prompt.

This method uses the transformation_template to transform the prompt
according to the decorator's intended behavior.

Args:
    prompt: The prompt to decorate

Returns:
    The decorated prompt

**Signature:** `apply_to_prompt(self, prompt: str) -> str`

**Parameters:**

- `prompt`: `str`

**Returns:** `str`

##### `transform_response`

Transform the LLM response according to the decorator's behavior.

The base implementation returns the response unchanged. Subclasses
should override this method if they need to modify the response.

Args:
    response: The LLM response to transform

Returns:
    The transformed response

**Signature:** `transform_response(self, response: str) -> str`

**Parameters:**

- `response`: `str`

**Returns:** `str`

### `DecoratorBase`

Base class for all prompt decorators.

This class defines the common interface and behavior for all decorators.
Subclasses should implement the apply_to_prompt and transform_response methods.

#### Attributes

- `conflicts_with`: `set` = `set()`
- `description`: `str` = `'Base decorator class'`
- `from_dict`: `classmethod` = `<classmethod(<function DecoratorBase.from_dict at 0x10651f4c0>)>`
- `name`: `str` = `'DecoratorBase'`
- `parameters`: `dict` = `{}`
- `transformation_template`: `dict` = `{'instruction': '', 'parameterMapping': {}, 'placement': 'prepend', 'compositionBehavior': 'accumulate'}`

#### Methods

##### `__init__`

Initialize a decorator with parameter values.

Args:
    **kwargs: Parameter values for the decorator

Raises:
    ValidationError: If any parameter values are invalid

**Signature:** `__init__(self, **kwargs)`

**Parameters:**

- `kwargs`:

##### `apply_to_prompt`

Apply the decorator to a prompt.

This method uses the transformation_template to transform the prompt
according to the decorator's intended behavior.

Args:
    prompt: The prompt to decorate

Returns:
    The decorated prompt

**Signature:** `apply_to_prompt(self, prompt: str) -> str`

**Parameters:**

- `prompt`: `str`

**Returns:** `str`

##### `transform_response`

Transform the LLM response according to the decorator's behavior.

The base implementation returns the response unchanged. Subclasses
should override this method if they need to modify the response.

Args:
    response: The LLM response to transform

Returns:
    The transformed response

**Signature:** `transform_response(self, response: str) -> str`

**Parameters:**

- `response`: `str`

**Returns:** `str`

### `DecoratorParameter`

Represents a parameter for a decorator.

This class is used by dynamic decorators to define parameters and validate values.

#### Attributes

- `from_dict`: `classmethod` = `<classmethod(<function DecoratorParameter.from_dict at 0x10651f380>)>`

#### Methods

##### `__init__`

Initialize a decorator parameter.

Args:
    name: The name of the parameter
    description: A description of the parameter
    type_: The type of the parameter (string, integer, float, boolean, enum)
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

Convert the parameter to a dictionary representation.

**Signature:** `to_dict(self) -> Dict[str, Any]`

**Parameters:**


**Returns:** `Dict`

##### `validate`

Validate a parameter value against constraints.

Args:
    value: The value to validate

Returns:
    The validated value (possibly converted to the correct type)

Raises:
    ValidationError: If the value is invalid

**Signature:** `validate(self, value: Any) -> Any`

**Parameters:**

- `value`: `Any`

**Returns:** `Any`

### `Parameter`

Represents a parameter for a decorator.

This class defines the metadata for a parameter, including its name, type,
description, default value, and constraints.

**Bases:** `pydantic.main.BaseModel`

#### Attributes

- `model_config`: `dict` = `{}`

#### Methods

##### `__init__`

Create a new model by parsing and validating input data from keyword arguments.

Raises `ValidationError` if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

**Signature:** `__init__(self, /, **data: 'Any') -> 'None'`

**Parameters:**

- `data`: `Any`

**Returns:** `None`

##### `copy`

Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```python {test="skip" lint="skip"}
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

Args:
    include: Optional set or mapping specifying which fields to include in the copied model.
    exclude: Optional set or mapping specifying which fields to exclude in the copied model.
    update: Optional dictionary of field-value pairs to override field values in the copied model.
    deep: If True, the values of fields that are Pydantic models will be deep-copied.

Returns:
    A copy of the model with included, excluded and updated fields as specified.

**Signature:** `copy(self, *, include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'`

**Parameters:**

- `include`: `AbstractSetIntStr | MappingIntStrAny | None` (default: `None`)
- `exclude`: `AbstractSetIntStr | MappingIntStrAny | None` (default: `None`)
- `update`: `Dict[str, Any] | None` (default: `None`)
- `deep`: `bool` (default: `False`)

**Returns:** `Self`

##### `dict`

**Signature:** `dict(self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False) -> 'Dict[str, Any]'`

**Parameters:**

- `include`: `IncEx | None` (default: `None`)
- `exclude`: `IncEx | None` (default: `None`)
- `by_alias`: `bool` (default: `False`)
- `exclude_unset`: `bool` (default: `False`)
- `exclude_defaults`: `bool` (default: `False`)
- `exclude_none`: `bool` (default: `False`)

**Returns:** `Dict[str, Any]`

##### `json`

**Signature:** `json(self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any') -> 'str'`

**Parameters:**

- `include`: `IncEx | None` (default: `None`)
- `exclude`: `IncEx | None` (default: `None`)
- `by_alias`: `bool` (default: `False`)
- `exclude_unset`: `bool` (default: `False`)
- `exclude_defaults`: `bool` (default: `False`)
- `exclude_none`: `bool` (default: `False`)
- `encoder`: `Callable[[Any], Any] | None` (default: `PydanticUndefined`)
- `models_as_dict`: `bool` (default: `PydanticUndefined`)
- `dumps_kwargs`: `Any`

**Returns:** `str`

##### `model_copy`

Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#model_copy

Returns a copy of the model.

Args:
    update: Values to change/add in the new model. Note: the data is not validated
        before creating the new model. You should trust this data.
    deep: Set to `True` to make a deep copy of the model.

Returns:
    New model instance.

**Signature:** `model_copy(self, *, update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'`

**Parameters:**

- `update`: `Mapping[str, Any] | None` (default: `None`)
- `deep`: `bool` (default: `False`)

**Returns:** `Self`

##### `model_dump`

Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Args:
    mode: The mode in which `to_python` should run.
        If mode is 'json', the output will only contain JSON serializable types.
        If mode is 'python', the output may contain non-JSON-serializable Python objects.
    include: A set of fields to include in the output.
    exclude: A set of fields to exclude from the output.
    context: Additional context to pass to the serializer.
    by_alias: Whether to use the field's alias in the dictionary key if defined.
    exclude_unset: Whether to exclude fields that have not been explicitly set.
    exclude_defaults: Whether to exclude fields that are set to their default value.
    exclude_none: Whether to exclude fields that have a value of `None`.
    round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
    warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
        "error" raises a `PydanticSerializationError`.
    serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.

Returns:
    A dictionary representation of the model.

**Signature:** `model_dump(self, *, mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'dict[str, Any]'`

**Parameters:**

- `mode`: `Literal['json', 'python'] | str` (default: `python`)
- `include`: `IncEx | None` (default: `None`)
- `exclude`: `IncEx | None` (default: `None`)
- `context`: `Any | None` (default: `None`)
- `by_alias`: `bool` (default: `False`)
- `exclude_unset`: `bool` (default: `False`)
- `exclude_defaults`: `bool` (default: `False`)
- `exclude_none`: `bool` (default: `False`)
- `round_trip`: `bool` (default: `False`)
- `warnings`: `bool | Literal['none', 'warn', 'error']` (default: `True`)
- `serialize_as_any`: `bool` (default: `False`)

**Returns:** `dict[str, Any]`

##### `model_dump_json`

Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

Args:
    indent: Indentation to use in the JSON output. If None is passed, the output will be compact.
    include: Field(s) to include in the JSON output.
    exclude: Field(s) to exclude from the JSON output.
    context: Additional context to pass to the serializer.
    by_alias: Whether to serialize using field aliases.
    exclude_unset: Whether to exclude fields that have not been explicitly set.
    exclude_defaults: Whether to exclude fields that are set to their default value.
    exclude_none: Whether to exclude fields that have a value of `None`.
    round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
    warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
        "error" raises a `PydanticSerializationError`.
    serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.

Returns:
    A JSON string representation of the model.

**Signature:** `model_dump_json(self, *, indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'str'`

**Parameters:**

- `indent`: `int | None` (default: `None`)
- `include`: `IncEx | None` (default: `None`)
- `exclude`: `IncEx | None` (default: `None`)
- `context`: `Any | None` (default: `None`)
- `by_alias`: `bool` (default: `False`)
- `exclude_unset`: `bool` (default: `False`)
- `exclude_defaults`: `bool` (default: `False`)
- `exclude_none`: `bool` (default: `False`)
- `round_trip`: `bool` (default: `False`)
- `warnings`: `bool | Literal['none', 'warn', 'error']` (default: `True`)
- `serialize_as_any`: `bool` (default: `False`)

**Returns:** `str`

##### `model_post_init`

Override this method to perform additional initialization after `__init__` and `model_construct`.
This is useful if you want to do some validation that requires the entire model to be initialized.

**Signature:** `model_post_init(self, _BaseModel__context: 'Any') -> 'None'`

**Parameters:**

- `_BaseModel__context`: `Any`

**Returns:** `None`

##### `validate_value`

Validate a parameter value against the parameter's constraints.

Args:
    value: The value to validate

Returns:
    The validated value (possibly converted to the correct type)

Raises:
    ValidationError: If the value is invalid

**Signature:** `validate_value(self, value: Any) -> Any`

**Parameters:**

- `value`: `Any`

**Returns:** `Any`

### `ParameterType`

Types of parameters supported in decorators.

**Bases:** `builtins.str`, `enum.Enum`

#### Attributes

- `ARRAY`: `ParameterType` = `<ParameterType.ARRAY: 'array'>`
- `BOOLEAN`: `ParameterType` = `<ParameterType.BOOLEAN: 'boolean'>`
- `ENUM`: `ParameterType` = `<ParameterType.ENUM: 'enum'>`
- `FLOAT`: `ParameterType` = `<ParameterType.FLOAT: 'float'>`
- `INTEGER`: `ParameterType` = `<ParameterType.INTEGER: 'integer'>`
- `OBJECT`: `ParameterType` = `<ParameterType.OBJECT: 'object'>`
- `STRING`: `ParameterType` = `<ParameterType.STRING: 'string'>`

#### Methods

##### `__init__`

**Signature:** `__init__(self, *args, **kwds)`

**Parameters:**

- `args`:
- `kwds`:

### `ValidationError`

Exception raised when decorator validation fails.

**Bases:** `builtins.Exception`

#### Methods

##### `__init__`

Initialize ValidationError.

Args:
    message: The error message
    decorator_name: Optional name of the decorator where validation failed

**Signature:** `__init__(self, message: str, decorator_name: Optional[str] = None)`

**Parameters:**

- `message`: `str`
- `decorator_name`: `Optional` (default: `None`)
