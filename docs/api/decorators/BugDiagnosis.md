# BugDiagnosis Decorator

Diagnoses issues from error messages, logs, or behavioral symptoms.

**Category**: Testing And Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `from` | `enum` | Source of diagnostic information | `input-dependent` |
| `depth` | `enum` | Thoroughness of analysis | `comprehensive` |
| `output` | `enum` | Type of output desired | `both` |

## From Options

- `stacktrace`: Focus your analysis on the provided stack trace to identify the error source.
- `behavior`: Analyze the described unexpected behavior to determine what's causing it.
- `logs`: Examine the log entries to identify patterns or anomalies that indicate the issue.
- `core-dump`: Analyze the core dump information to identify memory issues or crashes.
- `screenshot`: Examine the visual evidence to identify UI/UX issues or rendering problems.
- `reproduction`: Analyze the steps to reproduce to identify where the process is failing.

## Depth Options

- `quick`: Provide a rapid assessment focusing on the most likely cause and solution.
- `comprehensive`: Conduct a thorough analysis considering multiple potential causes and solutions, with detailed explanations.

## Output Options

- `explanation`: Focus on explaining what's causing the issue and why it's happening.
- `fix`: Focus on providing concrete steps to fix the issue.
- `both`: Provide both a detailed explanation of the cause and specific steps to fix the issue.

## Examples

### Diagnosing a JavaScript TypeError from a stack trace

```
+++BugDiagnosis(from=stacktrace, depth=comprehensive, output=both)
I'm getting this error in production - "TypeError: Cannot read property 'settings' of undefined" at UserProfile.js:143.
```

The model will analyze the stack trace, provide a comprehensive explanation of why the TypeError is occurring (likely because an object is undefined when its 'settings' property is being accessed), and suggest specific fixes like adding null checks or ensuring the object is properly initialized.

### Quick diagnosis of unexpected behavior

```
+++BugDiagnosis(from=behavior, depth=quick, output=fix)
When users click the submit button, the form clears but no confirmation message appears and the data isn't saved.
```

The model will provide a quick assessment focusing on the most likely causes for the form submission issue and offer specific code fixes or troubleshooting steps to resolve it.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** You are a debugging expert. Analyze this error or issue carefully and provide a diagnosis. Look for the root cause and suggest fixes.

**Notes:** Less capable models may need more explicit instructions to perform thorough debugging analysis.


## Implementation Guidance

### JavaScript error diagnosis

**Original Prompt:**
```
I'm getting this error in production - "TypeError: Cannot read property 'settings' of undefined" at UserProfile.js:143.
```

**Transformed Prompt:**
```
Analyze the provided information and diagnose the bug or issue. Focus your analysis on the provided stack trace to identify the error source. Conduct a thorough analysis considering multiple potential causes and solutions, with detailed explanations. Provide both a detailed explanation of the cause and specific steps to fix the issue.

I'm getting this error in production - "TypeError: Cannot read property 'settings' of undefined" at UserProfile.js:143.
```

**Notes:** The decorator adds specific instructions for analyzing a JavaScript TypeError based on a stack trace.

## Transformation Details

**Base Instruction:** Analyze the provided information and diagnose the bug or issue. Identify the root cause and potential solutions.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `from`:
  - When set to `stacktrace`: Focus your analysis on the provided stack trace to identify the error source.
  - When set to `behavior`: Analyze the described unexpected behavior to determine what's causing it.
  - When set to `logs`: Examine the log entries to identify patterns or anomalies that indicate the issue.
  - When set to `core-dump`: Analyze the core dump information to identify memory issues or crashes.
  - When set to `screenshot`: Examine the visual evidence to identify UI/UX issues or rendering problems.
  - When set to `reproduction`: Analyze the steps to reproduce to identify where the process is failing.

- `depth`:
  - When set to `quick`: Provide a rapid assessment focusing on the most likely cause and solution.
  - When set to `comprehensive`: Conduct a thorough analysis considering multiple potential causes and solutions, with detailed explanations.

- `output`:
  - When set to `explanation`: Focus on explaining what's causing the issue and why it's happening.
  - When set to `fix`: Focus on providing concrete steps to fix the issue.
  - When set to `both`: Provide both a detailed explanation of the cause and specific steps to fix the issue.

## Compatibility

- **Requires**: None
- **Conflicts**: Simplify
- **Compatible Models**: gpt-4o, gpt-4-turbo, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances BugDiagnosis BugDiagnosis works well after CodeReview to first review code quality then diagnose specific issues.
- **Simplify**: Conflicts with BugDiagnosis Simplify may reduce the technical details needed for proper bug diagnosis.
