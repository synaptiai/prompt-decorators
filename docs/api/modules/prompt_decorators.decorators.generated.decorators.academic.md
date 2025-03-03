# Module `prompt_decorators.decorators.generated.decorators.academic`

Implementation of the Academic decorator.

This module provides the Academic decorator class for use in prompt engineering.

Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.

## Classes

- [`Academic`](#class-academic): Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.

### Class `Academic`

Adapts the response to follow scholarly writing conventions appropriate for academic publications. This decorator generates responses with formal language, structured argumentation, and proper citations following established academic citation styles.

Attributes:
    style: The academic discipline style to follow. (Literal["humanities", "scientific", "legal"])
    format: The citation format to use for references. (Literal["APA", "MLA", "Chicago", "Harvard", "IEEE"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(style=scientific, format=APA) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `format`: Get the format parameter value.
- `name`: Get the name of the decorator.
- `style`: Get the style parameter value.
