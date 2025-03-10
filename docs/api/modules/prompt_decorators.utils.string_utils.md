# string_utils

String utilities for working with prompt decorators.

This module provides utility functions for extracting and replacing decorators in text.

## Functions

### `extract_decorators_from_text`

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
