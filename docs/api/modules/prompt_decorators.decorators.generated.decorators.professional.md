# Module `prompt_decorators.decorators.generated.decorators.professional`

Professional Decorator

Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.

## Classes

- [`Professional`](#class-professional): Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.

### Class `Professional`

Adapts the response to use business-oriented language appropriate for professional contexts. This decorator generates content using formal business terminology, clear and concise phrasing, and industry-appropriate jargon when relevant.

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(industry=general, formality=ProfessionalFormalityEnum.STANDARD)`
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

- `formality`: The level of formality to maintain in the response
- `industry`: The specific industry context to adapt the language for

