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

### gpt-3.5-turbo

**Instruction:** Please follow these code context guidelines for your implementation:

**Notes:** More explicit instruction for models with less context understanding.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances CodeContext CodeContext provides the baseline standards that CodeReview can check against.
- **LanguageSpecific**: Enhances CodeContext CodeContext complements language-specific guidance by providing project-level conventions.
