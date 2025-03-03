# Module `prompt_decorators.decorators.generated.decorators.cite_sources`

CiteSources Decorator

Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.

## Classes

- [`CiteSources`](#class-citesources): Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.

### Class `CiteSources`

Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(style=CiteSourcesStyleEnum.INLINE, format=CiteSourcesFormatEnum.APA, comprehensive=False)`
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

- `comprehensive`: Whether to cite every claim (true) or only major claims (false)
- `format`: The citation format to use
- `style`: The placement and format of citations within the response
