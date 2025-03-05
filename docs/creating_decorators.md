# Creating New Prompt Decorators

This guide will walk you through the process of creating new prompt decorators that are compliant with the Prompt Decorators specification.

## Table of Contents

- [Overview](#overview)
- [Understanding the Schemas](#understanding-the-schemas)
- [Creating a New Decorator](#creating-a-new-decorator)
  - [Define the Decorator's Purpose](#1-define-the-decorators-purpose)
  - [Create a Registry Entry](#2-create-a-registry-entry)
  - [Implement the Decorator's Behavior](#3-implement-the-decorators-behavior)
  - [Define Transformation Templates](#4-define-transformation-templates)
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

### 4. Define Transformation Templates

Transformation templates specify exactly how a decorator modifies a prompt. They provide a standardized way to implement prompt transformations across different decorator implementations.

#### What are Transformation Templates?

A transformation template defines:
1. The base instruction to add to the prompt
2. How each parameter modifies the instruction
3. Where to place the instruction relative to the original prompt
4. How the decorator behaves when combined with others

#### Example Transformation Template

Here's an example of a transformation template for a `Reasoning` decorator:

```json
{
  "decoratorName": "Reasoning",
  "version": "1.0.0",
  "description": "Modifies the AI's response to provide explicit reasoning paths",
  "parameters": [
    {
      "name": "depth",
      "type": "enum",
      "description": "The level of detail in the reasoning process",
      "enum": ["basic", "moderate", "comprehensive"],
      "default": "moderate",
      "required": false
    }
  ],
  "transformationTemplate": {
    "instruction": "Please provide detailed reasoning in your response. Show your thought process before reaching a conclusion.",
    "parameterMapping": {
      "depth": {
        "valueMap": {
          "basic": "Focus on the most important logical steps.",
          "moderate": "Balance detail with clarity in your reasoning.",
          "comprehensive": "Provide a very thorough and detailed analysis with multiple perspectives."
        }
      }
    },
    "placement": "prepend",
    "compositionBehavior": "accumulate"
  }
}
```

#### How Transformation Templates Work

1. **Base Instruction**: The `instruction` field contains the primary directive to add to the prompt.

2. **Parameter Mapping**: The `parameterMapping` field defines how each parameter affects the instruction:
   - `valueMap`: Maps specific parameter values to additional instructions
   - `format`: Provides a format string for inserting parameter values

3. **Placement Strategy**: The `placement` field determines where the instruction is placed:
   - `prepend`: Adds the instruction before the prompt (default)
   - `append`: Adds the instruction after the prompt
   - `wrap`: Adds the instruction before and after the prompt

4. **Composition Behavior**: The `compositionBehavior` field determines how the decorator combines with others:
   - `accumulate`: Instructions from multiple decorators accumulate (default)
   - `override`: Later decorators override instructions from earlier ones
   - `selective-override`: Overrides only specific parts of earlier instructions

#### Implementation Guidance

You can also include implementation examples in your registry entry to show exactly how the transformation should work:

```json
"implementationGuidance": {
  "examples": [
    {
      "context": "Standard implementation",
      "originalPrompt": "What are the implications of artificial intelligence for education?",
      "transformedPrompt": "Please provide detailed reasoning in your response. Show your thought process before reaching a conclusion. Provide a very thorough and detailed analysis with multiple perspectives.\n\nWhat are the implications of artificial intelligence for education?"
    },
    {
      "context": "Basic depth implementation",
      "originalPrompt": "How does compound interest work?",
      "transformedPrompt": "Please provide detailed reasoning in your response. Show your thought process before reaching a conclusion. Focus on the most important logical steps.\n\nHow does compound interest work?"
    }
  ],
  "compatibilityNotes": [
    {
      "decorator": "Concise",
      "relationship": "conflicts",
      "notes": "The objectives of comprehensive reasoning and concise responses contradict each other"
    }
  ]
}
```

#### Best Practices for Transformation Templates

1. **Clear Instructions**: Write clear, concise instructions that models can easily understand and follow.
2. **Parameter Context**: Ensure parameter-specific instructions make sense when appended to the base instruction.
3. **Model Compatibility**: Consider how different models might interpret your instructions.
4. **Composition**: Design templates that compose well with other decorators.
5. **Testing**: Test your transformation with various prompts and models to ensure consistent behavior.

#### Example Transformation Flow

Let's walk through a complete example of how a prompt is transformed using decorators:

**Original Prompt:**
```
Explain how photosynthesis works.
```

**Step 1: Apply the Audience Decorator**
```json
{
  "decoratorName": "Audience",
  "parameters": {
    "level": "beginner"
  },
  "transformationTemplate": {
    "instruction": "Please tailor your response for the appropriate audience.",
    "parameterMapping": {
      "level": {
        "valueMap": {
          "beginner": "Make your explanation accessible to someone with minimal background knowledge. Use simple language and familiar analogies.",
          "intermediate": "Assume some background knowledge but explain technical concepts. Balance depth with accessibility.",
          "expert": "Use field-specific terminology and provide detailed technical explanations appropriate for specialists."
        }
      }
    },
    "placement": "append"
  }
}
```
<!-- Note: "append" is the default placement strategy, which places instructions after the prompt -->

**Transformed Prompt After Audience Decorator:**
```
Explain how photosynthesis works.

Please tailor your response for the appropriate audience. Make your explanation accessible to someone with minimal background knowledge. Use simple language and familiar analogies.
```

**Step 2: Apply the StepByStep Decorator**
```json
{
  "decoratorName": "StepByStep",
  "parameters": {
    "numbered": true
  },
  "transformationTemplate": {
    "instruction": "Break down your explanation into a sequence of discrete steps.",
    "parameterMapping": {
      "numbered": {
        "valueMap": {
          "true": "Number each step clearly.",
          "false": "Separate each step with clear headings or transitions."
        }
      }
    },
    "placement": "prepend"
  }
}
```
<!-- Note: "prepend" explicitly places instructions before the prompt, overriding the default "append" behavior -->

**Final Transformed Prompt:**
```
Break down your explanation into a sequence of discrete steps. Number each step clearly.

Explain how photosynthesis works.

Please tailor your response for the appropriate audience. Make your explanation accessible to someone with minimal background knowledge. Use simple language and familiar analogies.
```

This example illustrates how:
1. Each decorator's transformation template specifies how to modify the prompt
2. The placement strategy determines where instructions are positioned relative to the original prompt
3. Multiple decorators compose to create a comprehensive set of instructions
4. Parameter values influence the specific instructions that are applied

The LLM would then process this transformed prompt, incorporating all the instructions into its response generation process.

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
