# CodeReview Decorator

Performs a review of code quality, identifying issues and suggesting improvements.

**Category**: Testing And Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `focus` | `enum` | Aspects to focus on during review | `all` |
| `strictness` | `enum` | Level of scrutiny | `standard` |
| `format` | `enum` | Review output format | `detailed` |

## Focus Options

- `security`: Focus specifically on security vulnerabilities, input validation, authentication issues, and potential exploits.
- `performance`: Focus specifically on performance bottlenecks, inefficient algorithms, and optimization opportunities.
- `best-practices`: Focus specifically on adherence to coding standards, design patterns, and industry best practices.
- `maintainability`: Focus specifically on code readability, documentation, modularity, and long-term maintenance concerns.
- `all`: Review all aspects including security, performance, best practices, and maintainability.

## Strictness Options

- `relaxed`: Apply a relaxed level of scrutiny, focusing only on major issues.
- `standard`: Apply a standard level of scrutiny, balancing thoroughness with pragmatism.
- `strict`: Apply a strict level of scrutiny, identifying all potential issues regardless of severity.

## Format Options

- `comment-style`: Present the review as code comments that could be directly added to the source.
- `summary`: Present a concise summary of findings with key points only.
- `detailed`: Present a comprehensive review with sections for different types of issues and detailed explanations.
- `inline`: Present the review as inline comments within the code itself.

## Examples

### Security-focused code review with strict scrutiny

```
+++CodeReview(focus=security, strictness=strict, format=detailed)
Review this authentication controller for security issues.
```

A detailed security-focused code review that identifies potential vulnerabilities, authentication issues, and security best practices violations with a high level of scrutiny.

### Performance review with standard scrutiny and summary format

```
+++CodeReview(focus=performance, strictness=standard, format=summary)
Review this data processing function for performance issues.
```

A summary of performance-related issues in the code, including potential bottlenecks and optimization opportunities with a balanced level of scrutiny.

### Comprehensive code review with default parameters

```
+++CodeReview
Review this utility class implementation.
```

A detailed review covering all aspects (security, performance, best practices, maintainability) with standard scrutiny level.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** You are a code reviewer. Analyze the following code and provide feedback according to these guidelines:

**Notes:** For smaller models, more explicit instructions about the review process may be needed.

### claude-3-7-sonnet-latest

**Instruction:** Perform a thorough code review on the provided code. Identify issues and suggest improvements based on the following criteria:

**Notes:** Claude models may benefit from more structured review instructions.


## Implementation Guidance

### Security review of authentication code

**Original Prompt:**
```
Review this authentication controller code:

function login(username, password) {
  if(username === 'admin' && password === 'password123') {
    return generateToken(username);
  }
  return null;
}
```

**Transformed Prompt:**
```
Perform a code review on the provided code. Identify issues and suggest improvements. Focus specifically on security vulnerabilities, input validation, authentication issues, and potential exploits. Apply a strict level of scrutiny, identifying all potential issues regardless of severity. Present a comprehensive review with sections for different types of issues and detailed explanations.

Review this authentication controller code:

function login(username, password) {
  if(username === 'admin' && password === 'password123') {
    return generateToken(username);
  }
  return null;
}
```

**Notes:** The decorator adds specific instructions for a security-focused code review with strict scrutiny and detailed output format.

## Transformation Details

**Base Instruction:** Perform a code review on the provided code. Identify issues and suggest improvements.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `focus`:
  - When set to `security`: Focus specifically on security vulnerabilities, input validation, authentication issues, and potential exploits.
  - When set to `performance`: Focus specifically on performance bottlenecks, inefficient algorithms, and optimization opportunities.
  - When set to `best-practices`: Focus specifically on adherence to coding standards, design patterns, and industry best practices.
  - When set to `maintainability`: Focus specifically on code readability, documentation, modularity, and long-term maintenance concerns.
  - When set to `all`: Review all aspects including security, performance, best practices, and maintainability.

- `strictness`:
  - When set to `relaxed`: Apply a relaxed level of scrutiny, focusing only on major issues.
  - When set to `standard`: Apply a standard level of scrutiny, balancing thoroughness with pragmatism.
  - When set to `strict`: Apply a strict level of scrutiny, identifying all potential issues regardless of severity.

- `format`:
  - When set to `comment-style`: Present the review as code comments that could be directly added to the source.
  - When set to `summary`: Present a concise summary of findings with key points only.
  - When set to `detailed`: Present a comprehensive review with sections for different types of issues and detailed explanations.
  - When set to `inline`: Present the review as inline comments within the code itself.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo, claude-3-7-sonnet-latest, llama-3.2, palm-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ExplainCode**: Enhances CodeReview CodeReview can be used after ExplainCode to first understand the code and then review it.
- **FixCode**: Enhances CodeReview CodeReview can be used before FixCode to identify issues that need fixing.
