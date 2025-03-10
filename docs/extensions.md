# Prompt Decorators Extension System

This document describes the current extension capabilities and future plans for the prompt-decorators extension system.

## Current Extension Capabilities

The prompt-decorators system currently supports extensions in the following ways:

### 1. Registry Extensions

Extensions can be added to the registry in the `registry/extensions/` directory. These extensions are loaded at runtime when the decorator registry is initialized.

Current extension directories include:
- `registry/extensions/code_generation/`
- `registry/extensions/devops_and_infrastructure/`
- `registry/extensions/implementation-focused/`
- `registry/extensions/testing_and_debugging/`

### 2. Extension Package Format

Extensions follow the registry entry schema format as defined in `schemas/registry-entry.schema.json`. Each extension must include:

- `decoratorName`: The name of the decorator
- `version`: Semantic versioning
- `description`: What the decorator does
- `parameters`: Configuration parameters
- `transformationTemplate`: How the decorator transforms prompts

### 3. Loading Extensions

Extensions in the registry are automatically loaded when the `DynamicDecorator` class is initialized. The current implementation scans the registry directory and loads all decorator definitions.

Example of loading extensions:

```python
from prompt_decorators.core.dynamic_decorator import DynamicDecorator

# Load all decorators from the registry
DynamicDecorator.load_registry()

# Now extensions are available
code_review = DynamicDecorator("CodeReview", focus="security")
```

## Limitations and Future Plans

### Current Limitations

1. **No Remote Loading**: The current implementation does not support loading extensions from remote URLs as described in the specification.

2. **No Dynamic Extension Discovery**: Extensions must be included in the registry directory at package installation time.

3. **Limited Extension Validation**: While extension schemas are validated, there's limited validation of compatibility between extensions.

4. **No Extension Marketplace**: There's no centralized repository for discovering and sharing extensions.

### Future Extension Capabilities

The following capabilities are planned for future releases:

#### 1. Remote Extension Loading

Future versions will support loading extensions from remote URLs as described in the specification:

```
+++Extension(source=https://decorator-registry.ai/scientific-pack.json)
+++ScientificReasoning(discipline=physics)
```

This will:
- Securely load extension definitions from verified URLs
- Validate extensions against the registry schema
- Cache extensions locally for performance

#### 2. Extension Discovery Service

A central registry service is planned to allow:
- Publishing extensions to a central repository
- Discovering extensions through a web interface
- Rating and reviewing extensions
- Searching for extensions by category, name, or function

#### 3. Enhanced Compatibility Checking

Future versions will provide more robust compatibility checking:
- Verifying that extensions don't conflict with core decorators
- Checking for compatibility between extensions
- Validating required dependencies

#### 4. Extension Configuration

More advanced extension configuration options are planned:
- Per-environment configuration
- Model-specific optimizations
- User preference support

## Working with Extensions Today

### Creating a Custom Extension

To create a custom extension today:

1. Create a new JSON file in the `registry/extensions/` directory
2. Follow the registry entry schema format
3. Include all required fields (decoratorName, version, etc.)
4. Define parameters and transformation templates
5. Validate using the validation tools

Example of a minimal extension:

```json
{
  "decoratorName": "CustomExtension",
  "version": "1.0.0",
  "description": "A custom decorator extension",
  "parameters": [
    {
      "name": "level",
      "type": "enum",
      "description": "Level of detail",
      "enum": ["basic", "detailed", "comprehensive"],
      "default": "detailed"
    }
  ],
  "transformationTemplate": {
    "instruction": "Apply custom processing to this prompt.",
    "parameterMapping": {
      "level": {
        "valueMap": {
          "basic": "Use minimal processing.",
          "detailed": "Apply standard processing.",
          "comprehensive": "Use extensive processing."
        }
      }
    },
    "placement": "prepend",
    "compositionBehavior": "accumulate"
  }
}
```

### Using Extensions

To use extensions in your code:

```python
from prompt_decorators import transform_prompt

# Use an extension
prompt = """
+++CustomExtension(level=comprehensive)
Explain quantum computing.
"""

transformed = transform_prompt(prompt)
```

## Contributing Extensions

Contributions of new extensions are welcome! To contribute:

1. Review the existing extensions for patterns and examples
2. Create your extension following the registry entry schema
3. Add comprehensive documentation and examples
4. Include tests for your extension
5. Submit a pull request

All contributed extensions should be domain-specific and provide clear value beyond the core decorators.
