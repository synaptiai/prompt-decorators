# CodeContext Decorator

Provides information about the existing codebase context to ensure proper integration.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `project` | string | Project type or framework | inferred |
| `patterns` | string | Established code patterns to follow | inferred |
| `conventions` | enum | Naming and style conventions | language-standard |

## Conventions Options

- `camelCase`: Use camelCase naming convention (e.g., myVariable, calculateTotal)
- `snake_case`: Use snake_case naming convention (e.g., my_variable, calculate_total)
- `PascalCase`: Use PascalCase naming convention (e.g., MyVariable, CalculateTotal)
- `kebab-case`: Use kebab-case naming convention (e.g., my-variable, calculate-total)
- `custom`: Follow the custom naming conventions established in the project

## Examples

### React hooks implementation with camelCase convention

```
+++CodeContext(project=react, patterns=hooks, conventions=camelCase)
Implement a shopping cart hook that matches our existing custom hooks pattern.
```

The model will implement a React hook using camelCase naming conventions and following standard React hooks patterns.

### Python backend with snake_case convention

```
+++CodeContext(project=django, patterns=MVT, conventions=snake_case)
Create a view for user authentication.
```

The model will implement a Django view following the Model-View-Template pattern with snake_case naming conventions.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Please follow these code context guidelines for your implementation:

**Notes:** More explicit instruction for models with less context understanding.


## Implementation Guidance

### React application

**Original Prompt:**
```
Implement a shopping cart hook that matches our existing custom hooks pattern.
```

**Transformed Prompt:**
```
Consider the following code context when implementing the solution:
Project/Framework: react
Design Patterns: hooks
Naming Convention: Use camelCase naming convention (e.g., myVariable, calculateTotal)

Implement a shopping cart hook that matches our existing custom hooks pattern.
```

**Notes:** The decorator adds context about the React framework, hooks pattern, and camelCase convention to guide the implementation.

## Transformation Details

**Base Instruction:** Consider the following code context when implementing the solution:

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `project`:
  - Format: Project/Framework: {value}

- `patterns`:
  - Format: Design Patterns: {value}

- `conventions`:
  - When set to `camelCase`: Use camelCase naming convention (e.g., myVariable, calculateTotal)
  - When set to `snake_case`: Use snake_case naming convention (e.g., my_variable, calculate_total)
  - When set to `PascalCase`: Use PascalCase naming convention (e.g., MyVariable, CalculateTotal)
  - When set to `kebab-case`: Use kebab-case naming convention (e.g., my-variable, calculate-total)
  - When set to `custom`: Follow the custom naming conventions established in the project
  - Format: Naming Convention: {value}

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances CodeContext CodeContext provides the baseline standards that CodeReview can check against.
- **LanguageSpecific**: Enhances CodeContext CodeContext complements language-specific guidance by providing project-level conventions.
