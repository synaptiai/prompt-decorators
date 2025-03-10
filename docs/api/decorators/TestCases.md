# TestCases Decorator

Generates specific test cases for functionality, edge cases, or regressions.

**Category**: Testing And Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `coverage` | `enum` | Types of test cases to generate | `happy-path` |
| `format` | `enum` | Output format of the test cases | `code` |
| `assertions` | `enum` | Level of assertion detail | `comprehensive` |

## Coverage Options

- `happy-path`: Focus on testing the main functionality with valid inputs and expected behavior.
- `edge-cases`: Focus on testing edge cases and unusual inputs that might cause unexpected behavior.
- `error-conditions`: Focus on testing error conditions and how the system handles invalid inputs.
- `boundary`: Focus on testing boundary conditions and limits of the functionality.
- `all`: Provide comprehensive test coverage including happy paths, edge cases, error conditions, and boundary tests.

## Format Options

- `table`: Present the test cases in a tabular format with inputs, expected outputs, and test descriptions.
- `code`: Present the test cases as executable code with proper test functions and assertions.
- `gherkin`: Present the test cases in Gherkin format (Given-When-Then) suitable for behavior-driven development.

## Assertions Options

- `basic`: Include basic assertions that verify the core functionality.
- `comprehensive`: Include comprehensive assertions that verify both the core functionality and important side effects.
- `advanced`: Include advanced assertions that verify all aspects of the functionality, including edge cases and performance considerations.

## Examples

### Generating edge case tests for a date processing function

```
+++TestCases(coverage=edge-cases, format=code, assertions=comprehensive)
Generate test cases for a function that processes date ranges, including edge cases like leap years and timezone transitions.
```

The model will generate code-based test cases focusing on edge cases for date processing, with comprehensive assertions.

### Creating tabular test cases for error conditions

```
+++TestCases(coverage=error-conditions, format=table)
Generate test cases for a user registration form validation.
```

The model will generate a table of test cases focusing on error conditions in form validation, with comprehensive assertions (the default).

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create test cases for the following functionality. Be thorough and consider different scenarios.

**Notes:** Simplified instruction for models with less context capacity.


## Implementation Guidance

### Unit testing a date range function

**Original Prompt:**
```
Generate test cases for a function that processes date ranges.
```

**Transformed Prompt:**
```
Generate test cases for the following functionality. Focus on providing thorough test coverage. Focus on testing edge cases and unusual inputs that might cause unexpected behavior. Present the test cases as executable code with proper test functions and assertions. Include comprehensive assertions that verify both the core functionality and important side effects.

Generate test cases for a function that processes date ranges.
```

**Notes:** The decorator adds specific guidance on test coverage, format, and assertion level.

## Transformation Details

**Base Instruction:** Generate test cases for the following functionality. Focus on providing thorough test coverage.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `coverage`:
  - When set to `happy-path`: Focus on testing the main functionality with valid inputs and expected behavior.
  - When set to `edge-cases`: Focus on testing edge cases and unusual inputs that might cause unexpected behavior.
  - When set to `error-conditions`: Focus on testing error conditions and how the system handles invalid inputs.
  - When set to `boundary`: Focus on testing boundary conditions and limits of the functionality.
  - When set to `all`: Provide comprehensive test coverage including happy paths, edge cases, error conditions, and boundary tests.

- `format`:
  - When set to `table`: Present the test cases in a tabular format with inputs, expected outputs, and test descriptions.
  - When set to `code`: Present the test cases as executable code with proper test functions and assertions.
  - When set to `gherkin`: Present the test cases in Gherkin format (Given-When-Then) suitable for behavior-driven development.

- `assertions`:
  - When set to `basic`: Include basic assertions that verify the core functionality.
  - When set to `comprehensive`: Include comprehensive assertions that verify both the core functionality and important side effects.
  - When set to `advanced`: Include advanced assertions that verify all aspects of the functionality, including edge cases and performance considerations.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **CodeReview**: Enhances TestCases TestCases works well with CodeReview as it can generate tests that verify issues identified in code reviews.
- **Debugging**: Enhances TestCases TestCases can be used to create regression tests for bugs identified during debugging.
