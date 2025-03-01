# Module `prompt_decorators.decorators.generated.decorators.precision`

Precision Decorator

Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.

## Classes

- [`Precision`](#class-precision): Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.

### Class `Precision`

Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(level=PrecisionLevelEnum.HIGH, units=True, definitions=False)`
- `apply(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `get_version() -> <class 'prompt_decorators.core.base.Version'>`
- `is_compatible_with_version(version_str) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_json(indent) -> <class 'str'>`
- `validate() -> <class 'NoneType'>`
#### Properties

- `definitions`: Whether to include precise definitions for key terms
- `level`: The degree of precision to apply
- `units`: Whether to consistently provide units for all measurements

