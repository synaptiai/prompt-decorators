# Module `prompt_decorators.core.base`

Base Decorator Class

This module provides the base class for all prompt decorators.

## Classes

- [`BaseDecorator`](#class-basedecorator): Base class for all prompt decorators.
- [`IncompatibleVersionError`](#class-incompatibleversionerror): Exception raised for incompatible decorator versions.
- [`ValidationError`](#class-validationerror): Exception raised for parameter validation errors.
- [`Version`](#class-version): Class representing a semantic version.

### Class `BaseDecorator`

Base class for all prompt decorators.

All prompt decorators must inherit from this class and implement the
apply method.

**Inherits from:** `ABC`

#### Methods

- `__init__(name, version, parameters, metadata)`
- `apply(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `get_version() -> <class 'prompt_decorators.core.base.Version'>`
- `is_compatible_with_version(version_str) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_json(indent) -> <class 'str'>`
- `validate() -> <class 'NoneType'>`

### Class `IncompatibleVersionError`

Exception raised for incompatible decorator versions.

**Inherits from:** `Exception`

#### Methods

- `__init__(decorator_name, requested_version, available_version)`

### Class `ValidationError`

Exception raised for parameter validation errors.

**Inherits from:** `Exception`

#### Methods

- `__init__(decorator_name, param_name, message)`

### Class `Version`

Class representing a semantic version.

#### Methods

- `__init__(version_str)`
- `is_compatible_with(other) -> <class 'bool'>`

