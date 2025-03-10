# TestCases Decorator

Generates specific test cases for functionality, edge cases, or regressions.

**Category**: Testing And Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `coverage` | enum | Types of test cases to generate | happy-path |
| `format` | enum | Output format of the test cases | code |
| `assertions` | enum | Level of assertion detail | comprehensive |

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

### gpt-3.5-turbo

**Instruction:** Create test cases for the following functionality. Be thorough and consider different scenarios.

**Notes:** Simplified instruction for models with less context capacity.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **CodeReview**: Enhances TestCases TestCases works well with CodeReview as it can generate tests that verify issues identified in code reviews.
- **Debugging**: Enhances TestCases TestCases can be used to create regression tests for bugs identified during debugging.
