# Module `prompt_decorators.core.request`

API Request Handling Module

This module provides utilities for handling API requests with decorators.

## Classes

- [`DecoratedRequest`](#class-decoratedrequest): Class representing a request decorated with prompt decorators.

### Class `DecoratedRequest`

Class representing a request decorated with prompt decorators.

#### Methods

- `__init__(prompt, decorators, model, api_params)`
- `add_decorator(decorator) -> <class 'prompt_decorators.core.request.DecoratedRequest'>`
- `apply_decorators() -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.request.DecoratedRequest'>`
- `from_json(json_str) -> <class 'prompt_decorators.core.request.DecoratedRequest'>`
- `get_decorator(decorator_name) -> typing.Optional[prompt_decorators.core.base.BaseDecorator]`
- `remove_decorator(decorator_name) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_json(indent) -> <class 'str'>`
