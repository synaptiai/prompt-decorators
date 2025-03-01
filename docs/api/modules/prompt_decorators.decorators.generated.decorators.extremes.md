# Module `prompt_decorators.decorators.generated.decorators.extremes`

Extremes Decorator

Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.

## Classes

- [`Extremes`](#class-extremes): Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.

### Class `Extremes`

Presents content at the extreme ends of a spectrum, showing both a radical, ambitious, or maximalist version alongside a minimal, conservative, or basic version. This decorator helps explore the range of possibilities from the simplest implementation to the most expansive vision.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(versions=ExtremesVersionsEnum.BOTH, dimension=ambition, compare=True)`
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

- `compare`: Whether to include a comparative analysis of the extreme versions
- `dimension`: The specific dimension along which to explore extremes (e.g., 'cost', 'time', 'ambition', 'complexity')
- `versions`: Which extreme versions to include

