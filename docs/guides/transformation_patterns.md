# Common Transformation Patterns

This guide provides common patterns for implementing transformation templates in prompt decorators. Use these patterns as a starting point for your own decorators.

## Table of Contents
- [Introduction](#introduction)
- [Basic Patterns](#basic-patterns)
  - [Simple Instruction](#simple-instruction)
  - [Parameter-Based Variations](#parameter-based-variations)
  - [Format Strings](#format-strings)
- [Advanced Patterns](#advanced-patterns)
  - [Placement Strategies](#placement-strategies)
  - [Composition Behaviors](#composition-behaviors)
  - [Model-Specific Adaptations](#model-specific-adaptations)
- [Domain-Specific Patterns](#domain-specific-patterns)
  - [Reasoning Process Patterns](#reasoning-process-patterns)
  - [Output Format Patterns](#output-format-patterns)
  - [Tone and Style Patterns](#tone-and-style-patterns)
  - [Verification Patterns](#verification-patterns)
- [Best Practices](#best-practices)

## Introduction

Transformation templates define how decorators modify prompts by adding instructions, changing formats, or altering tone. These templates create consistency across implementations and make decorators more predictable.

## Basic Patterns

### Simple Instruction

The simplest pattern adds a fixed instruction to a prompt:

```json
{
  "transformationTemplate": {
    "instruction": "Please format your response as a numbered list.",
    "placement": "prepend"
  }
}
```

This pattern is ideal for decorators that don't require parameter customization.

### Parameter-Based Variations

For decorators with parameters, use `valueMap` to select different instructions based on parameter values:

```json
{
  "transformationTemplate": {
    "instruction": "Please explain the following concept.",
    "parameterMapping": {
      "level": {
        "valueMap": {
          "beginner": "Use simple language and basic analogies a 10-year-old would understand.",
          "intermediate": "Use moderately technical language and some field-specific terminology.",
          "expert": "Use technical language and detailed field-specific terminology."
        }
      }
    }
  }
}
```

This pattern allows the decorator to adapt its behavior based on parameter values.

### Format Strings

When a parameter value should be directly inserted into an instruction, use the `format` approach:

```json
{
  "transformationTemplate": {
    "instruction": "Please format your response according to the instructions below.",
    "parameterMapping": {
      "wordCount": {
        "format": "Limit your response to approximately {value} words."
      }
    }
  }
}
```

This pattern works well for numeric parameters or when the exact parameter value should appear in the instruction.

## Advanced Patterns

### Placement Strategies

Different decorators may require different placement strategies:

1. **Append** (default) - Places instructions after the prompt:
   ```json
   "placement": "append"
   ```
   Good for post-processing instructions like "Now review your answer and check for errors."

2. **Prepend** - Places instructions before the prompt:
   ```json
   "placement": "prepend"
   ```
   Useful when instructions need to set context before the model processes the prompt.

3. **Wrap** - Places instructions before and after the prompt:
   ```json
   "placement": "wrap"
   ```
   Useful for framing the context before and after the prompt.

### Composition Behaviors

Control how your decorator interacts with others:

1. **Accumulate** (default) - Instructions combine with other decorators:
   ```json
   "compositionBehavior": "accumulate"
   ```

2. **Override** - Later decorators replace earlier ones:
   ```json
   "compositionBehavior": "override"
   ```
   Use sparingly, as it can disrupt expected behavior.

3. **Selective-Override** - Override only specific aspects:
   ```json
   "compositionBehavior": "selective-override"
   ```
   For decorators that replace specific functionality but retain others.

### Model-Specific Adaptations

Some models require different phrasing. Provide alternatives in the implementation guidance:

```json
"implementationGuidance": {
  "modelSpecificImplementations": {
    "gpt-3.5-turbo": {
      "instruction": "Think step-by-step to solve this problem. Show all your reasoning.",
      "notes": "This model requires more explicit instructions for reasoning tasks."
    }
  }
}
```

## Domain-Specific Patterns

### Reasoning Process Patterns

For decorators that modify reasoning processes:

```json
{
  "transformationTemplate": {
    "instruction": "Please break down your reasoning into clear steps.",
    "parameterMapping": {
      "approach": {
        "valueMap": {
          "deductive": "Start with general principles and work towards specific conclusions.",
          "inductive": "Start with specific observations and identify patterns to form general principles.",
          "abductive": "Consider the most likely explanation based on the available evidence."
        }
      }
    }
  }
}
```

### Output Format Patterns

For decorators that specify output format:

```json
{
  "transformationTemplate": {
    "instruction": "Format your output as specified below.",
    "parameterMapping": {
      "format": {
        "valueMap": {
          "json": "Provide your answer as a valid JSON object with proper escaping and formatting.",
          "markdown": "Format your response using Markdown with appropriate headings, lists, and code blocks.",
          "table": "Present your data in a table format with clear row and column headings."
        }
      }
    }
  }
}
```

### Tone and Style Patterns

For decorators that modify tone:

```json
{
  "transformationTemplate": {
    "instruction": "Adjust your communication style as follows.",
    "parameterMapping": {
      "tone": {
        "valueMap": {
          "formal": "Use professional, academic language with proper terminology and minimal contractions.",
          "casual": "Use conversational language as if speaking to a friend, with contractions and simpler vocabulary.",
          "humorous": "Incorporate appropriate humor and a light-hearted tone in your response."
        }
      }
    }
  }
}
```

### Verification Patterns

For decorators that add verification steps:

```json
{
  "transformationTemplate": {
    "instruction": "After providing your answer, perform the following verification.",
    "parameterMapping": {
      "verifyType": {
        "valueMap": {
          "factChecking": "Explicitly verify key factual claims in your response and rate your confidence.",
          "selfReview": "Review your own response for potential logical errors or missing information.",
          "counterarguments": "Consider potential objections or alternative viewpoints to your answer."
        }
      }
    },
    "placement": "append"
  }
}
```

## Best Practices

1. **Be Specific**: Write clear, actionable instructions that models can follow precisely.

2. **Consider Context**: Design instructions that work well regardless of the original prompt's content.

3. **Test Combinations**: Ensure your decorator composes well with others, especially those in the same category.

4. **Use Natural Language**: Write instructions in natural language that's easy for models to understand.

5. **Provide Examples**: Include comprehensive examples in your `implementationGuidance` section.

6. **Isolation vs. Combination**: Consider whether your decorator should maintain its behavior when combined with others or adapt based on context.

7. **Documentation**: Document any unexpected interactions or edge cases in the `compatibility` section.

By following these patterns and best practices, you'll create decorators that behave consistently across implementations and compose well with other decorators in the ecosystem.
