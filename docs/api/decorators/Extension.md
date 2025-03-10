# Extension Decorator

A meta-decorator that enables loading of community-defined decorators from external sources. This facilitates the use of specialized decorator packages, domain-specific extensions, or custom decorator libraries maintained by communities or organizations.

**Category**: Meta

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `source` | `string` | URI or identifier for the extension package (e.g., URL, namespace, or registry identifier) | `Required` |
| `version` | `string` | Specific version of the extension package to use | `` |
| `decorators` | `array` | Specific decorators to load from the extension (if empty, loads all decorators from the package) | `` |

## Examples

### Basic loading of an extension package

```
+++Extension(source=https://decorator-registry.ai/scientific-pack.json)
+++ScientificReasoning(discipline=physics)
Explain dark matter.
```

Loads decorators from the scientific-pack extension and then applies the ScientificReasoning decorator (defined in that pack) with physics discipline to explain dark matter

### Loading specific decorators from a versioned extension

```
+++Extension(source=medical-decorators, version=2.1.0, decorators=[ClinicalCase,EvidenceBased])
+++ClinicalCase(format=SOAP)
Describe the treatment approach for Type 2 diabetes.
```

Loads only the ClinicalCase and EvidenceBased decorators from version 2.1.0 of the medical-decorators package, then applies the ClinicalCase decorator with SOAP format to describe diabetes treatment

## Model-Specific Implementations

### gpt-4o

**Instruction:** This request will load specialized decorators from {source}. If any decorators in the following prompt come from this extension, apply them according to their definitions in the extension package.

**Notes:** This model handles extension loading well but requires clear indications of which decorators come from the extension


## Implementation Guidance

### Loading scientific package for dark matter explanation

**Original Prompt:**
```
+++Extension(source=https://decorator-registry.ai/scientific-pack.json)
+++ScientificReasoning(discipline=physics)
Explain dark matter.
```

**Transformed Prompt:**
```
Please load and apply specialized decorators from an external source to enhance your response capabilities. Load the extension package from this source: https://decorator-registry.ai/scientific-pack.json.

+++ScientificReasoning(discipline=physics)
Explain dark matter.
```

### Loading specific medical decorators for diabetes treatment

**Original Prompt:**
```
+++Extension(source=medical-decorators, version=2.1.0, decorators=[ClinicalCase,EvidenceBased])
+++ClinicalCase(format=SOAP)
Describe the treatment approach for Type 2 diabetes.
```

**Transformed Prompt:**
```
Please load and apply specialized decorators from an external source to enhance your response capabilities. Load the extension package from this source: medical-decorators. Use version 2.1.0 of the extension package. Load only these specific decorators from the package: ClinicalCase,EvidenceBased.

+++ClinicalCase(format=SOAP)
Describe the treatment approach for Type 2 diabetes.
```

## Transformation Details

**Base Instruction:** Please load and apply specialized decorators from an external source to enhance your response capabilities.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `source`:
  - Format: Load the extension package from this source: {value}.

- `version`:
  - Format: Use version {value} of the extension package.

- `decorators`:
  - Format: Load only these specific decorators from the package: {value}.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Context**: Enhances Extension Context can help adapt the loaded extension decorators to domain-specific requirements
- **Custom**: Enhances Extension Custom provides flexibility for working with extension decorators that might require customization
- **Version**: Enhances Extension Version helps ensure compatibility between core decorators and loaded extensions
