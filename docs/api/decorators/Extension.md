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

**Signature:** `__init__(source, version, decorators) -> <class 'NoneType'>`

Initialize the Extension decorator.

Args:
    source: URI or identifier for the extension package (e.g., URL, namespace, or registry identifier)
    version: Specific version of the extension package to use
    decorators: Specific decorators to load from the extension (if empty, loads all decorators from the package)

#### `apply`

**Signature:** `apply(prompt) -> <class 'str'>`

Apply the decorator to a prompt string.

Args:
    prompt: The prompt to apply the decorator to


Returns:
    The modified prompt

#### `apply_to_prompt`

**Signature:** `apply_to_prompt(prompt) -> <class 'str'>`

Apply the decorator to a prompt.

Args:
    prompt: The prompt to decorate

Returns:
    The decorated prompt

#### `from_dict`

**Signature:** `from_dict(data) -> <class 'prompt_decorators.core.base.BaseDecorator'>`

Create a decorator instance from a dictionary representation.

Args:
    data: Dictionary representation of the decorator

Returns:
    A new decorator instance

Raises:
    ValidationError: If the dictionary is invalid

#### `get_metadata`

**Signature:** `get_metadata() -> typing.Dict[str, typing.Any]`

Get metadata about the decorator.

Returns:
    Dictionary containing metadata about the decorator

#### `is_compatible_with_version`

**Signature:** `is_compatible_with_version(version) -> <class 'bool'>`

Check if the decorator is compatible with a specific version.

Args:
    version: The version to check compatibility with.


Returns:
    True if compatible, False otherwise.


Raises:
    IncompatibleVersionError: If the version is incompatible.

#### `to_dict`

**Signature:** `to_dict() -> typing.Dict[str, typing.Any]`

Convert the decorator to a dictionary.

Args:
    self: The decorator instance

Returns:
    Dictionary representation of the decorator

#### `to_string`

**Signature:** `to_string() -> <class 'str'>`

Convert the decorator to a string.

Args:
    self: The decorator instance

Returns:
    String representation of the decorator

#### `transform_response`

**Signature:** `transform_response(response) -> <class 'str'>`

Transform the response from the model.

Args:
    response: The response to transform

Returns:
    The transformed response
