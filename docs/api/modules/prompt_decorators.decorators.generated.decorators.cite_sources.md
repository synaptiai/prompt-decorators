# Module `prompt_decorators.decorators.generated.decorators.cite_sources`

Implementation of the CiteSources decorator.

This module provides the CiteSources decorator class for use in prompt engineering.

Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.

## Classes

- [`CiteSources`](#class-citesources): Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.

### Class `CiteSources`

Structures the response to include citations for claims and information. This decorator enhances credibility by providing references to source material, enabling fact verification and further exploration of topics.

Attributes:
    style: The placement and format of citations within the response. (Literal["inline", "footnote", "endnote"])
    format: The citation format to use. (Literal["APA", "MLA", "Chicago", "Harvard", "IEEE"])
    comprehensive: Whether to cite every claim (true) or only major claims (false). (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(style=inline, format=APA, comprehensive=False) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `comprehensive`: Get the comprehensive parameter value.
- `format`: Get the format parameter value.
- `name`: Get the name of the decorator.
- `style`: Get the style parameter value.
