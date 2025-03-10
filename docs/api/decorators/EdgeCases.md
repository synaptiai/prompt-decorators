# EdgeCases Decorator

Identifies edge cases and boundary conditions for testing.

**Category**: Testing And Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `focus` | `enum` | Types of edge cases to identify | `all` |
| `risk` | `enum` | Risk level of edge cases to consider | `common` |
| `output` | `enum` | Format of identified edge cases | `test-cases` |

## Focus Options

- `input-validation`: Focus on edge cases related to input validation, such as invalid inputs, boundary values, and type mismatches.
- `error-handling`: Focus on edge cases related to error handling, such as exception paths, error propagation, and recovery mechanisms.
- `resource-limits`: Focus on edge cases related to resource limitations, such as memory constraints, timeout conditions, and storage limits.
- `concurrency`: Focus on edge cases related to concurrency issues, such as race conditions, deadlocks, and synchronization problems.
- `all`: Consider all types of edge cases including input validation, error handling, resource limitations, and concurrency issues.

## Risk Options

- `common`: Focus on common edge cases that are likely to occur in normal usage scenarios.
- `rare`: Include rare edge cases that might occur infrequently but could have significant impact.
- `extreme`: Consider extreme edge cases, including highly unlikely scenarios that could lead to catastrophic failures.

## Output Options

- `description`: Provide detailed descriptions of each edge case, explaining the conditions and potential impacts.
- `test-cases`: Format the edge cases as specific test cases that could be implemented to verify system behavior.
- `examples`: Present concrete examples demonstrating each edge case in action with expected outcomes.

## Examples

### Identifying concurrency edge cases for a document editing feature

```
+++EdgeCases(focus=concurrency, risk=rare, output=test-cases)
Identify edge cases for a multi-user document editing feature.
```

The model will identify rare concurrency-related edge cases for a multi-user document editing feature, formatted as specific test cases that could be implemented.

### Finding input validation edge cases for a form submission

```
+++EdgeCases(focus=input-validation, risk=common)
Identify edge cases for a user registration form.
```

The model will identify common input validation edge cases for a user registration form, formatted as test cases (the default output format).

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Identify edge cases, corner cases, and boundary conditions for the following scenario. Consider what could go wrong, unexpected inputs, and system limitations.

**Notes:** Simpler phrasing works better with this model.


## Implementation Guidance

### Software testing for a web application

**Original Prompt:**
```
Identify edge cases for a multi-user document editing feature.
```

**Transformed Prompt:**
```
Identify and analyze edge cases and boundary conditions for the given scenario. Consider potential failures, unexpected inputs, and system limitations. Focus on edge cases related to concurrency issues, such as race conditions, deadlocks, and synchronization problems. Include rare edge cases that might occur infrequently but could have significant impact. Format the edge cases as specific test cases that could be implemented to verify system behavior.

Identify edge cases for a multi-user document editing feature.
```

**Notes:** The decorator adds specific guidance on focusing on concurrency issues with rare risk levels, formatted as test cases.

## Transformation Details

**Base Instruction:** Identify and analyze edge cases and boundary conditions for the given scenario. Consider potential failures, unexpected inputs, and system limitations.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `focus`:
  - When set to `input-validation`: Focus on edge cases related to input validation, such as invalid inputs, boundary values, and type mismatches.
  - When set to `error-handling`: Focus on edge cases related to error handling, such as exception paths, error propagation, and recovery mechanisms.
  - When set to `resource-limits`: Focus on edge cases related to resource limitations, such as memory constraints, timeout conditions, and storage limits.
  - When set to `concurrency`: Focus on edge cases related to concurrency issues, such as race conditions, deadlocks, and synchronization problems.
  - When set to `all`: Consider all types of edge cases including input validation, error handling, resource limitations, and concurrency issues.

- `risk`:
  - When set to `common`: Focus on common edge cases that are likely to occur in normal usage scenarios.
  - When set to `rare`: Include rare edge cases that might occur infrequently but could have significant impact.
  - When set to `extreme`: Consider extreme edge cases, including highly unlikely scenarios that could lead to catastrophic failures.

- `output`:
  - When set to `description`: Provide detailed descriptions of each edge case, explaining the conditions and potential impacts.
  - When set to `test-cases`: Format the edge cases as specific test cases that could be implemented to verify system behavior.
  - When set to `examples`: Present concrete examples demonstrating each edge case in action with expected outcomes.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **TestCases**: Enhances EdgeCases EdgeCases works well with TestCases decorator, providing more comprehensive test coverage.
- **SecurityAnalysis**: Enhances EdgeCases EdgeCases can complement SecurityAnalysis by identifying boundary conditions that might lead to security vulnerabilities.
