# Module `prompt_decorators.decorators.generated.decorators.table_format`

Implementation of the TableFormat decorator.

This module provides the TableFormat decorator class for use in prompt engineering.

Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.

## Classes

- [`TableFormat`](#class-tableformat): Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.

### Class `TableFormat`

Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.

Attributes:
    columns: List of column names for the table. (List[Any])
    format: Format style for the table representation. (Literal["markdown", "ascii", "csv"])
    alignment: Text alignment within table cells. (Literal["left", "center", "right"])

**Inherits from:** `BaseDecorator`

#### Methods

- `__init__(columns, format=markdown, alignment=left) -> <class 'NoneType'>`
- `apply(prompt) -> <class 'str'>`
- `apply_to_prompt(prompt) -> <class 'str'>`
- `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`
- `get_metadata() -> typing.Dict[str, typing.Any]`
- `is_compatible_with_version(version) -> <class 'bool'>`
- `to_dict() -> typing.Dict[str, typing.Any]`
- `to_string() -> <class 'str'>`
- `transform_response(response) -> <class 'str'>`
#### Properties

- `alignment`: Get the alignment parameter value.
- `columns`: Get the columns parameter value.
- `format`: Get the format parameter value.
- `name`: Get the name of the decorator.
