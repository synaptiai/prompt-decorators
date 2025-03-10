# parser

Parser module for extracting decorators from prompts.

This module provides functionality to parse and extract decorator annotations
from prompt text using the +++ syntax.

## Classes

### `DecoratorParser`

Parser for extracting decorator annotations from prompts.

This class handles the parsing of decorator annotations in the format:
+++DecoratorName(param1=value1, param2=value2)

#### Attributes

- `DECORATOR_PATTERN`: `str` = `'\\+\\+\\+([A-Za-z0-9_]+)(?:\\(([^)]*)\\))?'`

#### Methods

##### `__init__`

Initialize the decorator parser.

Args:
    registry: Optional decorator registry to use for creating decorators. If not provided, the global registry will be used.

**Signature:** `__init__(self, registry: Optional[prompt_decorators.core.registry.DecoratorRegistry] = None)`

**Parameters:**

- `registry`: `Optional` (default: `None`)

##### `extract_decorators`

Extract decorator annotations from a prompt.

This method extracts all decorator annotations from the prompt text,
creates decorator instances for each annotation, and returns both the
list of decorators and the cleaned prompt text.

Args:
    prompt: The prompt text to parse

Returns:
    A tuple containing:
        - A list of decorator instances
        - The prompt text with decorator annotations removed

**Signature:** `extract_decorators(self, prompt: str) -> Tuple[List[prompt_decorators.core.base.DecoratorBase], str]`

**Parameters:**

- `prompt`: `str`

**Returns:** `Tuple`
