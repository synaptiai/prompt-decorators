# Module `prompt_decorators.core.validation`

Parameter Validation Module

This module provides utilities for validating decorator parameters.

## Classes

- [`DictValidator`](#class-dictvalidator): Validator for dictionary parameters.
- [`EnumValidator`](#class-enumvalidator): Validator for enum values.
- [`ListValidator`](#class-listvalidator): Validator for list parameters.
- [`PatternValidator`](#class-patternvalidator): Validator for string patterns.
- [`RangeValidator`](#class-rangevalidator): Validator for numeric ranges.
- [`TypeValidator`](#class-typevalidator): Validator for parameter types.
- [`ValidationPipeline`](#class-validationpipeline): Pipeline for validating multiple parameters.
- [`Validator`](#class-validator): Base class for parameter validators.

### Class `DictValidator`

Validator for dictionary parameters.

**Inherits from:** `Validator`

#### Methods

- `__init__(key_validator, value_validator, required_keys, allow_extra_keys=True, allow_none=False)`
- `validate(decorator_name, param_name, value) -> typing.Optional[typing.Dict[typing.Any, typing.Any]]`

### Class `EnumValidator`

Validator for enum values.

**Inherits from:** `Validator`

#### Methods

- `__init__(enum_class, allow_none=False)`
- `validate(decorator_name, param_name, value) -> typing.Optional[enum.Enum]`

### Class `ListValidator`

Validator for list parameters.

**Inherits from:** `Validator`

#### Methods

- `__init__(item_validator, min_length, max_length, allow_none=False)`
- `validate(decorator_name, param_name, value) -> typing.Optional[typing.List[typing.Any]]`

### Class `PatternValidator`

Validator for string patterns.

**Inherits from:** `Validator`

#### Methods

- `__init__(pattern, allow_none=False)`
- `validate(decorator_name, param_name, value) -> typing.Optional[str]`

### Class `RangeValidator`

Validator for numeric ranges.

**Inherits from:** `Validator`

#### Methods

- `__init__(minimum, maximum, allow_none=False)`
- `validate(decorator_name, param_name, value) -> typing.Union[int, float, NoneType]`

### Class `TypeValidator`

Validator for parameter types.

**Inherits from:** `Validator`

#### Methods

- `__init__(expected_type, allow_none=False)`
- `validate(decorator_name, param_name, value) -> typing.Optional[~T]`

### Class `ValidationPipeline`

Pipeline for validating multiple parameters.

#### Methods

- `__init__(validators)`
- `validate(decorator_name, parameters) -> typing.Dict[str, typing.Any]`

### Class `Validator`

Base class for parameter validators.

#### Methods

- `validate(decorator_name, param_name, value) -> typing.Any`

