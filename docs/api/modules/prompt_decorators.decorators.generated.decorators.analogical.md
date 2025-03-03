# Module `prompt_decorators.decorators.generated.decorators.analogical`

Analogical Decorator

Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.

## Classes

- [`Analogical`](#class-analogical): Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.

### Class `Analogical`

Enhances explanations through the use of analogies and metaphors. This decorator helps make complex or abstract concepts more accessible by systematically comparing them to more familiar domains or experiences.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(domain=general, count=1, depth=AnalogicalDepthEnum.MODERATE)`
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

- `count`: Number of distinct analogies to provide
- `depth`: Level of detail in developing the analogy
- `domain`: Specific domain or context to draw analogies from (if not specified, will choose appropriate domains)
