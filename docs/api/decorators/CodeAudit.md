# CodeAudit Decorator

Requests an audit of existing code to identify issues before making changes.

**Category**: Systematic Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `scope` | enum | Audit scope | component |
| `focus` | enum | Audit focus areas | all |
| `output` | enum | Audit output format | detailed |

## Scope Options

- `function`: Focus your audit on the specific function provided.
- `component`: Examine the entire component for issues.
- `module`: Conduct a thorough audit of the complete module.
- `system`: Perform a system-wide audit to identify issues across all components.
- `specific-issue`: Focus your audit specifically on the issue described.

## Focus Options

- `bugs`: Concentrate on identifying logical errors, edge cases, and potential runtime exceptions.
- `performance`: Analyze for performance bottlenecks, inefficient algorithms, and resource usage issues.
- `security`: Identify security vulnerabilities, injection risks, and data protection concerns.
- `maintainability`: Evaluate code quality, documentation, and adherence to best practices.
- `all`: Examine all aspects including bugs, performance, security, and maintainability.

## Output Options

- `summary`: Provide a concise summary of the key issues found.
- `detailed`: Deliver a comprehensive report with detailed explanations of each issue.
- `categorized`: Organize findings by category (bugs, performance, security, etc.).
- `prioritized`: Present issues in order of importance, with critical issues first.

## Examples

### Basic code audit for a payment module

```
+++CodeAudit(scope=module, focus=bugs, output=prioritized)
Audit the payment processing module to identify potential bugs and issues. Provide a prioritized list of problems found.
```

The model will perform a thorough audit of the payment processing module, focusing specifically on bugs and logical errors, and will present the findings as a prioritized list with the most critical issues first.

### Security-focused audit of a component

```
+++CodeAudit(scope=component, focus=security, output=detailed)
Review this authentication component for security vulnerabilities.
```

The model will examine the authentication component with a focus on security vulnerabilities, providing a detailed report of all potential security issues found.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Analyze this code carefully before suggesting any changes. Look for issues related to {focus} within the {scope} and provide a {output} report.

**Notes:** Simplified instruction for models with more limited context windows.


## Compatibility

- **Requires**: None
- **Conflicts**: QuickFix
- **Compatible Models**: gpt-4, gpt-3.5-turbo, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeRefactor**: Enhances CodeAudit CodeAudit works well before CodeRefactor to ensure issues are identified before making changes.
- **QuickFix**: Conflicts with CodeAudit CodeAudit's thorough analysis approach conflicts with QuickFix's rapid solution focus.
