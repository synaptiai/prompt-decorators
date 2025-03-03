# Module `prompt_decorators.decorators.generated.decorators.contrarian`

Contrarian Decorator

Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.

## Classes

- [`Contrarian`](#class-contrarian): Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.

### Class `Contrarian`

Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(approach=ContrarianApproachEnum.DEVIL_S_ADVOCATE, maintain=False, focus)`
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

- `approach`: The specific contrarian approach to take
- `focus`: Optional specific aspect of the topic to focus contrarian analysis on
- `maintain`: Whether to maintain contrarian stance throughout (true) or provide balanced view at the end (false)
