# Module `prompt_decorators.utils.factory`

Decorator Factory Module

This module provides utilities for creating decorator instances from JSON definitions.

## Classes

- [`DecoratorFactory`](#class-decoratorfactory): Factory for creating decorator instances from JSON definitions.

### Class `DecoratorFactory`

Factory for creating decorator instances from JSON definitions.

This class provides utilities for creating decorator instances from JSON definitions,
either by using existing decorator classes or by dynamically generating new ones.

#### Methods

- `__init__(registry)`
- `create_all_from_directory(directory_path) -> typing.List[prompt_decorators.core.base.BaseDecorator]`
- `create_dynamic_class(decorator_data) -> typing.Type[prompt_decorators.core.base.BaseDecorator]`
- `create_from_dict(decorator_data) -> typing.Optional[prompt_decorators.core.base.BaseDecorator]`
- `create_from_file(file_path) -> typing.Optional[prompt_decorators.core.base.BaseDecorator]`
- `create_from_json_string(json_string) -> typing.Optional[prompt_decorators.core.base.BaseDecorator]`
- `extract_parameters(decorator_data) -> typing.Dict[str, typing.Any]`
- `find_decorator_class(decorator_name) -> typing.Optional[typing.Type[prompt_decorators.core.base.BaseDecorator]]`

