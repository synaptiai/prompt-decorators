# Creating New Prompt Decorators

This guide will walk you through the process of creating new prompt decorators that are compliant with the Prompt Decorators specification.

## Table of Contents

- [Overview](#overview)
- [Understanding the Schemas](#understanding-the-schemas)
- [Creating a New Decorator](#creating-a-new-decorator)
- [Validation](#validation)
- [Best Practices](#best-practices)
- [Contributing to the Registry](#contributing-to-the-registry)
- [Examples](#examples)

## Overview

Prompt Decorators follow a standardized format defined by JSON schemas. Before creating new decorators, you should understand the core components:

1. **Decorator Definition**: The core definition of a decorator, its parameters, and behavior
2. **Registry Entry**: Metadata for publishing a decorator to the central registry
3. **Extension Package**: Collections of related decorators bundled together

## Understanding the Schemas

The repository contains several schema files that define the valid structure for decorators:

### 1. `decorator.schema.json`

This schema defines the structure of individual decorator instances used within prompts:

```json
{
  "name": "YourDecorator",
  "version": "1.0.0",
  "parameters": {
    "paramName": "value"
  },
  "metadata": {
    "description": "What your decorator does",
    "category": "reasoning"
  }
}
```

### 2. `registry-entry.schema.json`

This schema defines how decorators are registered in the central registry:

```json
{
  "decoratorName": "YourDecorator",
  "version": "1.0.0",
  "description": "Detailed description of what your decorator does",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "url": "https://yourwebsite.com"
  },
  "parameters": [
    {
      "name": "paramName",
      "type": "string",
      "description": "Description of the parameter",
      "default": "defaultValue",
      "required": false
    }
  ],
  "examples": [
    {
      "description": "Example of decorator usage",
      "usage": "+++YourDecorator(paramName=value)\nWhat is the meaning of life?",
      "result": "Expected response pattern"
    }
  ],
  "compatibility": {
    "requires": [],
    "conflicts": [],
    "minStandardVersion": "1.0.0",
    "maxStandardVersion": "2.0.0",
    "models": [
      "gpt-4"
    ]
  }
}
```

### 3. `extension-package.schema.json`

This schema defines how decorators are packaged together:

```json
{
  "name": "your-extension-package",
  "version": "1.0.0",
  "description": "A collection of related decorators",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "url": "https://yourwebsite.com"
  },
  "license": "Apache 2.0",
  "keywords": ["keyword1", "keyword2"],
  "decorators": [
    // Array of registry entries
  ]
}
```

## Creating a New Decorator

Follow these steps to create a new prompt decorator:

### 1. Define the Decorator's Purpose

First, clearly define what your decorator will do:
- What behavior will it modify?
- What parameters will it accept?
- How will it interact with other decorators?

### 2. Create a Registry Entry

Create a new JSON file in the appropriate directory, following the registry entry schema:

```json
{
  "decoratorName": "YourDecorator",
  "version": "1.0.0",
  "description": "Detailed description of your decorator's purpose",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com",
    "url": "https://yourwebsite.com"
  },
  "parameters": [
    {
      "name": "mode",
      "type": "enum",
      "description": "The operational mode",
      "enum": ["basic", "advanced", "expert"],
      "default": "basic",
      "required": false
    }
  ],
  "examples": [
    {
      "description": "Basic example",
      "usage": "+++YourDecorator(mode=basic)\nHow does photosynthesis work?",
      "result": "Provides a description of the response format"
    }
  ],
  "compatibility": {
    "requires": [],
    "conflicts": [],
    "minStandardVersion": "1.0.0",
    "maxStandardVersion": "2.0.0",
    "models": [
      "gpt-4"
    ]
  }
}
```

### 3. Implement the Decorator's Behavior

For each implementation language, create the necessary code to implement your decorator:

#### Python Example
```python
class YourDecorator(BaseDecorator):
    """Your decorator implementation."""

    def __init__(self, mode: str = "basic"):
        """Initialize with parameters."""
        super().__init__(name="YourDecorator", version="1.0.0")
        self.parameters = {"mode": mode}

    def to_system_instructions(self) -> str:
        """Convert decorator to system instructions."""
        mode = self.parameters.get("mode", "basic")
        if mode == "basic":
            return "When responding, use a simplified approach..."
        elif mode == "advanced":
            return "When responding, provide a more detailed analysis..."
        else:
            return "When responding, provide an expert-level analysis..."
```

## Validation

Always validate your decorators against the schemas to ensure compliance. Use the provided validator tool:

```bash
# Validate a registry entry
./validate_decorators.py registry path/to/your-decorator.json

# Validate all registry entries in a directory
./validate_decorators.py directory path/to/registry/dir --type registry
```

## Best Practices

1. **Clear Purpose**: Each decorator should have a clear, distinct purpose
2. **Minimal Parameters**: Keep parameters minimal and intuitive
3. **Meaningful Defaults**: Provide sensible default values for parameters
4. **Documentation**: Include comprehensive examples and descriptions
5. **Testing**: Test your decorator with various LLMs
6. **Compatibility**: Clearly specify compatibility with other decorators
7. **Versioning**: Follow semantic versioning for your decorators

## Contributing to the Registry

To contribute your decorator to the central registry:

1. Ensure your decorator passes validation
2. Create a pull request with your registry entry
3. Include comprehensive documentation and examples
4. Specify any dependencies or conflicts with other decorators

## Examples

### Example: Citation Decorator

```json
{
  "decoratorName": "Citation",
  "version": "1.0.0",
  "description": "Instructs the AI to include citations for factual claims in its response",
  "author": {
    "name": "Academic AI Group",
    "email": "contact@example.org",
    "url": "https://example.org"
  },
  "parameters": [
    {
      "name": "style",
      "type": "enum",
      "description": "The citation style to use",
      "enum": ["apa", "mla", "chicago", "ieee"],
      "default": "apa",
      "required": false
    },
    {
      "name": "inline",
      "type": "boolean",
      "description": "Whether to include inline citations or only a references section",
      "default": true,
      "required": false
    }
  ],
  "examples": [
    {
      "description": "Research paper with APA citations",
      "usage": "+++Citation(style=apa, inline=true)\nExplain the evidence for climate change over the past century.",
      "result": "Provides a response with APA-style inline citations and a references section"
    }
  ],
  "compatibility": {
    "requires": [],
    "conflicts": [],
    "minStandardVersion": "1.0.0",
    "maxStandardVersion": "2.0.0",
    "models": [
      "gpt-4",
      "claude-3-opus"
    ]
  }
}
```

### Example: Debate Decorator

```json
{
  "decoratorName": "Debate",
  "version": "1.0.0",
  "description": "Structures the response as a debate between multiple perspectives on a topic",
  "author": {
    "name": "Dialectic AI",
    "email": "contact@example.org",
    "url": "https://example.org"
  },
  "parameters": [
    {
      "name": "perspectives",
      "type": "number",
      "description": "Number of different perspectives to include",
      "default": 2,
      "required": false,
      "validation": {
        "minimum": 2,
        "maximum": 5
      }
    },
    {
      "name": "balanced",
      "type": "boolean",
      "description": "Whether to ensure equal representation of each perspective",
      "default": true,
      "required": false
    }
  ],
  "examples": [
    {
      "description": "Three-perspective debate on a policy issue",
      "usage": "+++Debate(perspectives=3, balanced=true)\nShould universal basic income be implemented nationally?",
      "result": "Presents three balanced perspectives on UBI in a debate format"
    }
  ],
  "compatibility": {
    "requires": [],
    "conflicts": ["OutputFormat"],
    "minStandardVersion": "1.0.0",
    "maxStandardVersion": "2.0.0",
    "models": [
      "gpt-4"
    ]
  }
}
```
