# Decorator `Extension`

**Version:** 1.0.0

A meta-decorator that enables loading of community-defined decorators from external sources. This facilitates the use of specialized decorator packages, domain-specific extensions, or custom decorator libraries maintained by communities or organizations.

## Parameters

### `source`

**Type:** string
**Required:** Yes

URI or identifier for the extension package (e.g., URL, namespace, or registry identifier)

### `version`

**Type:** string
**Required:** No

Specific version of the extension package to use

### `decorators`

**Type:** array
**Required:** No

Specific decorators to load from the extension (if empty, loads all decorators from the package)

## Examples

### Basic loading of an extension package

```
+++Extension(source=https://decorator-registry.ai/scientific-pack.json)
+++ScientificReasoning(discipline=physics)
Explain dark matter.
```

Result:

Loads decorators from the scientific-pack extension and then applies the ScientificReasoning decorator (defined in that pack) with physics discipline to explain dark matter

### Loading specific decorators from a versioned extension

```
+++Extension(source=medical-decorators, version=2.1.0, decorators=[ClinicalCase,EvidenceBased])
+++ClinicalCase(format=SOAP)
Describe the treatment approach for Type 2 diabetes.
```

Result:

Loads only the ClinicalCase and EvidenceBased decorators from version 2.1.0 of the medical-decorators package, then applies the ClinicalCase decorator with SOAP format to describe diabetes treatment

## Compatibility

**Supported models:**

- `gpt-4`

## Implementation

Inherits from: `BaseDecorator`

### Methods

#### `__init__`

**Signature:** `__init__(source, version, decorators)`

Initialize Extension decorator.

Args:
    source: URI or identifier for the extension package (e.g., URL, namespace, or registry identifier)
    version: Specific version of the extension package to use
    decorators: Specific decorators to load from the extension (if empty, loads all decorators from the package)

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the decorator to a prompt.

Args:
    prompt: The original prompt

Returns:
    The modified prompt with the decorator applied

#### `from_dict`

**Signature:** `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator from a dictionary.

Args:
    data: Dictionary representation of a decorator

Returns:
    New decorator instance

Raises:
    ValueError: If the data is invalid or incompatible with this class
    IncompatibleVersionError: If the version is incompatible

#### `from_json`

**Signature:** `from_json(json_str) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator from a JSON string.

Args:
    json_str: JSON string representation of a decorator

Returns:
    New decorator instance

Raises:
    ValueError: If the JSON is invalid or incompatible with this class
    json.JSONDecodeError: If the JSON is malformed
    IncompatibleVersionError: If the version is incompatible

#### `get_metadata`

**Signature:** `get_metadata() -> typing.Dict[str, typing.Any]`

Get metadata about this decorator class.

Returns:
    Dictionary with decorator metadata

#### `get_version`

**Signature:** `get_version() -> <class 'prompt_decorators.core.base.Version'>`

Get the decorator version.

Returns:
    Version object for the decorator

#### `is_compatible_with_version`

**Signature:** `is_compatible_with_version(version_str) -> <class 'bool'>`

Check if this decorator is compatible with the specified version.

Args:
    version_str: Version string to check compatibility with

Returns:
    True if compatible, False otherwise

#### `to_dict`

**Signature:** `to_dict() -> typing.Dict[str, typing.Any]`

Convert decorator to a dictionary representation.

Returns:
    Dictionary representation of the decorator

#### `to_json`

**Signature:** `to_json(indent) -> <class 'str'>`

Convert decorator to a JSON string.

Args:
    indent: Optional indentation for pretty-printing

Returns:
    JSON string representation of the decorator

#### `validate`

**Signature:** `validate() -> <class 'NoneType'>`

Validate decorator parameters.

This base implementation does basic type checking.
Subclasses should override for specific validation.

Raises:
    ValidationError: If any parameter fails validation
