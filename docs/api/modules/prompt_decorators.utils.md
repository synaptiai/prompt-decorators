# utils

Utility functions for prompt decorators.

This package provides utility functions for working with prompt decorators.

## Public API

This module exports the following components:

- `extract_decorators_from_text`: Function - Extract decorator annotations from text
- `replace_decorators_in_text`: Function - Replace decorator annotations in text

## Functions

### `extract_decorators_from_text`

*Imported from `prompt_decorators.utils.string_utils`*

Extract decorator annotations from text.

Args:
    text: Text containing decorator annotations

Returns:
    Tuple of (list of decorator dictionaries, clean text)

**Signature:** `extract_decorators_from_text(text: str) -> Tuple[List[Dict[str, Any]], str]`

**Parameters:**

- `text`: `str`

**Returns:** `Tuple`

### `replace_decorators_in_text`

*Imported from `prompt_decorators.utils.string_utils`*

Replace decorator annotations in text.

Args:
    text: Text to modify
    decorators: List of decorator dictionaries

Returns:
    Text with decorator annotations replaced

**Signature:** `replace_decorators_in_text(text: str, decorators: List[Dict[str, Any]]) -> str`

**Parameters:**

- `text`: `str`
- `decorators`: `List`

**Returns:** `str`
