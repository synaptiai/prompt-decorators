# Module `prompt_decorators.core.base`

Base classes for prompt decorators.

This module provides the base classes and utilities for creating and using
prompt decorators.

## Classes

- [`BaseDecorator`](#class-basedecorator): Base class for all prompt decorators.
- [`Parameter`](#class-parameter): Represents a parameter for a decorator.
- [`ParameterType`](#class-parametertype): Types of parameters supported in decorators.
- [`ValidationError`](#class-validationerror): Exception raised when decorator validation fails.

### Class `BaseDecorator`

Base class for all prompt decorators.

This class defines the common interface and behavior for all decorators.
Subclasses should implement the apply_to_prompt and transform_response methods.

#### Methods

- `__init__(kwargs)`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `transform_response(response) -> <class 'str'>`

### Class `Parameter`

Represents a parameter for a decorator.

This class defines the metadata for a parameter, including its name, type,
description, default value, and constraints.

**Inherits from:** `BaseModel`

#### Methods

- `__init__(data) -> <class 'NoneType'>`
- `construct(_fields_set, values) -> Model`
- `copy(include, exclude, update, deep=False) -> Model`
- `dict(include, exclude, by_alias=False, exclude_unset=False, exclude_defaults=False, exclude_none=False) -> typing.Dict[str, Any]`
- `from_orm(obj) -> Model`
- `json(include, exclude, by_alias=False, exclude_unset=False, exclude_defaults=False, exclude_none=False, encoder=PydanticUndefined, models_as_dict=PydanticUndefined, dumps_kwargs) -> str`
- `model_construct(_fields_set, values) -> Model`
- `model_copy(update, deep=False) -> Model`
- `model_dump(mode=python, include, exclude, by_alias=False, exclude_unset=False, exclude_defaults=False, exclude_none=False, round_trip=False, warnings=True) -> dict[str, Any]`
- `model_dump_json(indent, include, exclude, by_alias=False, exclude_unset=False, exclude_defaults=False, exclude_none=False, round_trip=False, warnings=True) -> str`
- `model_json_schema(by_alias=True, ref_template=#/$defs/{model}, schema_generator=<class 'pydantic.json_schema.GenerateJsonSchema'>, mode=validation) -> dict[str, typing.Any]`
- `model_parametrized_name(params) -> <class 'str'>`
- `model_post_init(_BaseModel__context) -> <class 'NoneType'>`
- `model_rebuild(force=False, raise_errors=True, _parent_namespace_depth=2, _types_namespace) -> bool | None`
- `model_validate(obj, strict, from_attributes, context) -> Model`
- `model_validate_json(json_data, strict, context) -> Model`
- `model_validate_strings(obj, strict, context) -> Model`
- `parse_file(path, content_type, encoding=utf8, proto, allow_pickle=False) -> Model`
- `parse_obj(obj) -> Model`
- `parse_raw(b, content_type, encoding=utf8, proto, allow_pickle=False) -> Model`
- `schema(by_alias=True, ref_template=#/$defs/{model}) -> typing.Dict[str, typing.Any]`
- `schema_json(by_alias=True, ref_template=#/$defs/{model}, dumps_kwargs) -> <class 'str'>`
- `update_forward_refs(localns) -> <class 'NoneType'>`
- `validate(value) -> Model`
- `validate_value(value) -> typing.Any`
#### Properties

- `model_extra`: Get extra fields set during validation.
- `model_fields_set`: Returns the set of fields that have been explicitly set on this model instance.

### Class `ParameterType`

Types of parameters supported in decorators.

**Inherits from:** `str, Enum`

#### Methods

- `__init__(args, kwds)`

### Class `ValidationError`

Exception raised when decorator validation fails.

**Inherits from:** `Exception`

#### Methods

- `__init__(message, decorator_name)`
