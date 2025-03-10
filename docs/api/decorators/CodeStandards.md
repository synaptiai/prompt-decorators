# CodeStandards Decorator

Applies coding standards and best practices.

**Category**: Developer Workflow

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `standard` | enum | Code standard type | language-specific |
| `strictness` | enum | Enforcement level | required |
| `focus` | enum | Areas of emphasis | all |

## Standard Options

- `company`: Apply company-specific coding standards and conventions.
- `language-specific`: Follow the idiomatic standards and best practices specific to the programming language.
- `custom`: Apply the custom coding standards as specified.
- `industry`: Follow industry-standard coding practices and patterns.

## Strictness Options

- `recommended`: Apply standards as recommendations, allowing for reasonable exceptions.
- `required`: Enforce standards as requirements with minimal exceptions.
- `strict`: Strictly enforce all standards with no exceptions.

## Focus Options

- `formatting`: Focus on code formatting, indentation, and style.
- `naming`: Focus on naming conventions for variables, functions, and classes.
- `patterns`: Focus on design patterns and architectural standards.
- `security`: Focus on security best practices and vulnerability prevention.
- `all`: Apply comprehensive standards covering formatting, naming, patterns, and security.

## Examples

### Applying JavaScript standards to React code

```
+++CodeStandards(standard=language-specific, strictness=required, focus=all)
Apply JavaScript best practices to this React component following Airbnb style guide.
```

The model will apply JavaScript-specific best practices to the React component, following required standards across all focus areas.

### Focusing on security standards

```
+++CodeStandards(standard=industry, strictness=strict, focus=security)
Review this Node.js API endpoint for security issues.
```

The model will strictly apply industry security standards to the Node.js API endpoint code.

### Using company standards for formatting

```
+++CodeStandards(standard=company, focus=formatting)
Format this Python code according to our company standards.
```

The model will apply company-specific formatting standards to the Python code with the default required strictness.

## Model-Specific Implementations

### gpt-4

**Instruction:** Apply coding standards and best practices to the code. Follow established conventions for readability and maintainability. Be specific about which standards you're applying and why.

**Notes:** GPT-4 can handle more detailed explanations of standards application.

### gpt-3.5-turbo

**Instruction:** Apply coding standards and best practices to the code. Follow established conventions for readability and maintainability.

**Notes:** Keep instructions more concise for GPT-3.5.


## Implementation Guidance

### JavaScript/React development

**Original Prompt:**
```
Refactor this React component to be more efficient.
```

**Transformed Prompt:**
```
Apply coding standards and best practices to the code. Follow established conventions for readability and maintainability. Follow the idiomatic standards and best practices specific to the programming language. Enforce standards as requirements with minimal exceptions. Apply comprehensive standards covering formatting, naming, patterns, and security.

Refactor this React component to be more efficient.
```

**Notes:** The decorator adds specific guidance about JavaScript and React best practices.

## Transformation Details

**Base Instruction:** Apply coding standards and best practices to the code. Follow established conventions for readability and maintainability.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `standard`:
  - When set to `company`: Apply company-specific coding standards and conventions.
  - When set to `language-specific`: Follow the idiomatic standards and best practices specific to the programming language.
  - When set to `custom`: Apply the custom coding standards as specified.
  - When set to `industry`: Follow industry-standard coding practices and patterns.

- `strictness`:
  - When set to `recommended`: Apply standards as recommendations, allowing for reasonable exceptions.
  - When set to `required`: Enforce standards as requirements with minimal exceptions.
  - When set to `strict`: Strictly enforce all standards with no exceptions.

- `focus`:
  - When set to `formatting`: Focus on code formatting, indentation, and style.
  - When set to `naming`: Focus on naming conventions for variables, functions, and classes.
  - When set to `patterns`: Focus on design patterns and architectural standards.
  - When set to `security`: Focus on security best practices and vulnerability prevention.
  - When set to `all`: Apply comprehensive standards covering formatting, naming, patterns, and security.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances CodeStandards CodeStandards works well with CodeReview by providing specific standards to check against.
- **Refactor**: Enhances CodeStandards CodeStandards can guide refactoring efforts with specific standards.
