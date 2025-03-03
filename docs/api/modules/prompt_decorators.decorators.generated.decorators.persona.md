# Module `prompt_decorators.decorators.generated.decorators.persona`

Implementation of the Persona decorator.

This module provides the Persona decorator class for use in prompt engineering.

Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic.

## Classes

- [`Persona`](#class-persona): Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic.

### Class `Persona`

Adapts the response to reflect the perspective and concerns of a specific persona. This decorator helps explore how different stakeholders or personality types would view a situation or topic.

Attributes:
    role: The specific persona or stakeholder role to adopt. (str)
    traits: Key personality traits or characteristics of the persona. (List[Any])
    goals: Primary goals or concerns of the persona. (List[Any])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(role, traits, goals) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `goals`: Get the goals parameter value.
- `name`: Get the name of the decorator.
- `role`: Get the role parameter value.
- `traits`: Get the traits parameter value.
