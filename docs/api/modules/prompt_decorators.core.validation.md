# validation

Parameter Validation Module.

This module provides utilities for validating decorator parameters.

## Module Variables

### `T`

Type: `TypeVar`

Value: `~T`

## Classes

### `DictValidator`

Validator for dictionary parameters.

**Bases:** `prompt_decorators.core.validation.Validator`

#### Methods

##### `__init__`

Initialize a dictionary validator.

Args:
    key_validator: Optional validator for dictionary keys
    value_validator: Optional validator for dictionary values
    required_keys: Optional list of required keys
    allow_extra_keys: Whether to allow keys not in required_keys
    allow_none: Whether None is allowed

**Signature:** `__init__(self, key_validator: Optional[prompt_decorators.core.validation.Validator] = None, value_validator: Optional[prompt_decorators.core.validation.Validator] = None, required_keys: Optional[List[str]] = None, allow_extra_keys: bool = True, allow_none: bool = False)`

**Parameters:**

- `key_validator`: `Optional` (default: `None`)
- `value_validator`: `Optional` (default: `None`)
- `required_keys`: `Optional` (default: `None`)
- `allow_extra_keys`: `bool` (default: `True`)
- `allow_none`: `bool` (default: `False`)

##### `validate`

Validate a dictionary parameter value.

Args:
    decorator_name: Name of the decorator
    param_name: Name of the parameter
    value: Parameter value to validate

Returns:
    Validated parameter value

Raises:
    ValidationError: If validation fails

**Signature:** `validate(self, decorator_name: str, param_name: str, value: Any) -> Optional[Dict[Any, Any]]`

**Parameters:**

- `decorator_name`: `str`
- `param_name`: `str`
- `value`: `Any`

**Returns:** `Optional`

### `EnumValidator`

Validator for enum values.

**Bases:** `prompt_decorators.core.validation.Validator`

#### Methods

##### `__init__`

Initialize an enum validator.

Args:
    enum_class: Enum class to validate against
    allow_none: Whether None is allowed

**Signature:** `__init__(self, enum_class: Type[enum.Enum], allow_none: bool = False)`

**Parameters:**

- `enum_class`: `Type`
- `allow_none`: `bool` (default: `False`)

##### `validate`

Validate an enum parameter value.

Args:
    decorator_name: Name of the decorator
    param_name: Name of the parameter
    value: Parameter value to validate

Returns:
    Validated parameter value (as Enum member)

Raises:
    ValidationError: If validation fails

**Signature:** `validate(self, decorator_name: str, param_name: str, value: Any) -> Optional[enum.Enum]`

**Parameters:**

- `decorator_name`: `str`
- `param_name`: `str`
- `value`: `Any`

**Returns:** `Optional`

### `ListValidator`

Validator for list parameters.

**Bases:** `prompt_decorators.core.validation.Validator`

#### Methods

##### `__init__`

Initialize a list validator.

Args:
    item_validator: Optional validator for list items
    min_length: Optional minimum list length
    max_length: Optional maximum list length
    allow_none: Whether None is allowed

**Signature:** `__init__(self, item_validator: Optional[prompt_decorators.core.validation.Validator] = None, min_length: Optional[int] = None, max_length: Optional[int] = None, allow_none: bool = False)`

**Parameters:**

- `item_validator`: `Optional` (default: `None`)
- `min_length`: `Optional` (default: `None`)
- `max_length`: `Optional` (default: `None`)
- `allow_none`: `bool` (default: `False`)

##### `validate`

Validate a list parameter value.

Args:
    decorator_name: Name of the decorator
    param_name: Name of the parameter
    value: Parameter value to validate

Returns:
    Validated parameter value

Raises:
    ValidationError: If validation fails

**Signature:** `validate(self, decorator_name: str, param_name: str, value: Any) -> Optional[List[Any]]`

**Parameters:**

- `decorator_name`: `str`
- `param_name`: `str`
- `value`: `Any`

**Returns:** `Optional`

### `PatternValidator`

Validator for string patterns.

**Bases:** `prompt_decorators.core.validation.Validator`

#### Methods

##### `__init__`

Initialize a pattern validator.

Args:
    pattern: Regex pattern to match
    allow_none: Whether None is allowed

**Signature:** `__init__(self, pattern: Union[str, Pattern], allow_none: bool = False)`

**Parameters:**

- `pattern`: `Union`
- `allow_none`: `bool` (default: `False`)

##### `validate`

Validate a string parameter value against the pattern.

Args:
    decorator_name: Name of the decorator
    param_name: Name of the parameter
    value: Parameter value to validate

Returns:
    Validated parameter value

Raises:
    ValidationError: If validation fails

**Signature:** `validate(self, decorator_name: str, param_name: str, value: Any) -> Optional[str]`

**Parameters:**

- `decorator_name`: `str`
- `param_name`: `str`
- `value`: `Any`

**Returns:** `Optional`

### `RangeValidator`

Validator for numeric ranges.

**Bases:** `prompt_decorators.core.validation.Validator`

#### Methods

##### `__init__`

Initialize a range validator.

Args:
    minimum: Optional minimum value (inclusive)
    maximum: Optional maximum value (inclusive)
    allow_none: Whether None is allowed

**Signature:** `__init__(self, minimum: Union[int, float, NoneType] = None, maximum: Union[int, float, NoneType] = None, allow_none: bool = False)`

**Parameters:**

- `minimum`: `Union` (default: `None`)
- `maximum`: `Union` (default: `None`)
- `allow_none`: `bool` (default: `False`)

##### `validate`

Validate a numeric parameter value against the range constraints.

Args:
    decorator_name: Name of the decorator
    param_name: Name of the parameter
    value: Parameter value to validate

Returns:
    Validated parameter value

Raises:
    ValidationError: If validation fails

**Signature:** `validate(self, decorator_name: str, param_name: str, value: Any) -> Union[int, float, NoneType]`

**Parameters:**

- `decorator_name`: `str`
- `param_name`: `str`
- `value`: `Any`

**Returns:** `Union`

### `TypeValidator`

Validator for parameter types.

**Bases:** `prompt_decorators.core.validation.Validator`

#### Methods

##### `__init__`

Initialize a type validator.

Args:
    expected_type: Expected type for the parameter
    allow_none: Whether None is allowed

**Signature:** `__init__(self, expected_type: Type[~T], allow_none: bool = False)`

**Parameters:**

- `expected_type`: `Type`
- `allow_none`: `bool` (default: `False`)

##### `validate`

Validate a parameter value against the expected type.

Args:
    decorator_name: Name of the decorator
    param_name: Name of the parameter
    value: Parameter value to validate

Returns:
    Validated parameter value

Raises:
    ValidationError: If validation fails

**Signature:** `validate(self, decorator_name: str, param_name: str, value: Any) -> Optional[~T]`

**Parameters:**

- `decorator_name`: `str`
- `param_name`: `str`
- `value`: `Any`

**Returns:** `Optional`

### `ValidationPipeline`

Pipeline for validating multiple parameters.

#### Methods

##### `__init__`

Initialize a validation pipeline.

Args:
    validators: Dictionary mapping parameter names to validators

**Signature:** `__init__(self, validators: Dict[str, prompt_decorators.core.validation.Validator])`

**Parameters:**

- `validators`: `Dict`

##### `validate`

Validate multiple parameters.

Args:
    decorator_name: Name of the decorator
    parameters: Dictionary of parameter values

Returns:
    Dictionary of validated parameter values

Raises:
    ValidationError: If any parameter fails validation

**Signature:** `validate(self, decorator_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]`

**Parameters:**

- `decorator_name`: `str`
- `parameters`: `Dict`

**Returns:** `Dict`

### `Validator`

Base class for parameter validators.

#### Methods

##### `validate`

Validate a parameter value.

Args:
    decorator_name: Name of the decorator
    param_name: Name of the parameter
    value: Parameter value to validate

Returns:
    Validated parameter value (possibly converted)

Raises:
    ValidationError: If validation fails

**Signature:** `validate(self, decorator_name: str, param_name: str, value: Any) -> Any`

**Parameters:**

- `decorator_name`: `str`
- `param_name`: `str`
- `value`: `Any`

**Returns:** `Any`
