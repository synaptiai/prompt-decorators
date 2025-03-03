# Module `prompt_decorators.decorators.generated.decorators.red_team`

Implementation of the RedTeam decorator.

This module provides the RedTeam decorator class for use in prompt engineering.

Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws. This decorator simulates how an opponent or critic would evaluate and attack ideas, plans, or arguments.

## Classes

- [`RedTeam`](#class-redteam): Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws. This decorator simulates how an opponent or critic would evaluate and attack ideas, plans, or arguments.

### Class `RedTeam`

Applies adversarial analysis to test assumptions, identify vulnerabilities, and strengthen proposals by actively looking for flaws. This decorator simulates how an opponent or critic would evaluate and attack ideas, plans, or arguments.

Attributes:
    strength: How aggressive or challenging the red team analysis should be. (Literal["moderate", "aggressive", "steelman"])
    focus: Specific aspects to focus the red team analysis on. (List[Any])
    constructive: Whether to include constructive suggestions for improvement after critiques. (bool)

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(strength=moderate, focus, constructive=True) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `constructive`: Get the constructive parameter value.
- `focus`: Get the focus parameter value.
- `name`: Get the name of the decorator.
- `strength`: Get the strength parameter value.
