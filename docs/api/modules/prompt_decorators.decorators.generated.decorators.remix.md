# Module `prompt_decorators.decorators.generated.decorators.remix`

Remix Decorator

Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.

## Classes

- [`Remix`](#class-remix): Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.

### Class `Remix`

Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(target, preserve=RemixPreserveEnum.FACTS, contrast=False)`
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

- `contrast`: Whether to highlight differences between the original framing and the remixed version
- `preserve`: What aspects of the original content to prioritize preserving
- `target`: The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch')

