# TechDebt Decorator

Analyzes technical debt and provides remediation strategies.

**Category**: Developer Education

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `categorization` | `enum` | Classification approach | `severity` |
| `output` | `enum` | Analysis result | `comprehensive` |
| `scope` | `enum` | Analysis breadth | `all` |

## Categorization Options

- `martin-fowler`: Categorize technical debt according to Martin Fowler's quadrants (Reckless/Prudent vs. Deliberate/Inadvertent).
- `severity`: Categorize technical debt by severity level (Critical, High, Medium, Low).
- `age`: Categorize technical debt by age (Legacy, Recent, New).
- `custom`: Use a custom categorization approach based on the context provided.

## Output Options

- `identification`: Focus on identifying and documenting technical debt without detailed remediation plans.
- `prioritization`: Focus on prioritizing technical debt items based on business impact, risk, and effort to fix.
- `remediation`: Focus on detailed remediation strategies for the identified technical debt.
- `comprehensive`: Provide a comprehensive analysis including identification, prioritization, and remediation strategies.

## Scope Options

- `code`: Focus analysis on code-level technical debt (e.g., code smells, duplications, complexity).
- `architecture`: Focus analysis on architectural technical debt (e.g., design patterns, component coupling).
- `process`: Focus analysis on process-related technical debt (e.g., CI/CD, development workflows).
- `testing`: Focus analysis on testing-related technical debt (e.g., test coverage, test quality).
- `all`: Analyze all aspects of technical debt across code, architecture, process, and testing.

## Examples

### Basic technical debt analysis with default parameters

```
+++TechDebt
Review our payment processing service for technical debt.
```

Provides a comprehensive analysis of technical debt categorized by severity across all aspects of the payment processing service.

### Code-focused technical debt analysis with Martin Fowler categorization

```
+++TechDebt(categorization=martin-fowler, scope=code)
Analyze technical debt in our authentication module.
```

Analyzes code-level technical debt in the authentication module using Martin Fowler's quadrants for categorization.

### Comprehensive technical debt analysis with custom parameters

```
+++TechDebt(categorization=severity, output=comprehensive, scope=code)
Analyze technical debt in our authentication module and suggest a remediation plan.
```

Provides a comprehensive analysis of code-level technical debt in the authentication module, categorized by severity, with identification, prioritization, and remediation strategies.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Analyze the technical debt in the described system or codebase. Be specific about problems, their impact, and how to fix them.

**Notes:** Simplified instruction for models with less context capacity.


## Implementation Guidance

### Code review for a legacy system

**Original Prompt:**
```
Analyze technical debt in our authentication module and suggest a remediation plan.
```

**Transformed Prompt:**
```
Analyze the technical debt in the described system or codebase. Identify problematic areas, assess their impact, and provide actionable remediation strategies. Categorize technical debt by severity level (Critical, High, Medium, Low). Provide a comprehensive analysis including identification, prioritization, and remediation strategies. Focus analysis on code-level technical debt (e.g., code smells, duplications, complexity).

Analyze technical debt in our authentication module and suggest a remediation plan.
```

**Notes:** The decorator adds specific guidance on how to approach technical debt analysis with severity categorization, comprehensive output, and code-level scope.

## Transformation Details

**Base Instruction:** Analyze the technical debt in the described system or codebase. Identify problematic areas, assess their impact, and provide actionable remediation strategies.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `categorization`:
  - When set to `martin-fowler`: Categorize technical debt according to Martin Fowler's quadrants (Reckless/Prudent vs. Deliberate/Inadvertent).
  - When set to `severity`: Categorize technical debt by severity level (Critical, High, Medium, Low).
  - When set to `age`: Categorize technical debt by age (Legacy, Recent, New).
  - When set to `custom`: Use a custom categorization approach based on the context provided.

- `output`:
  - When set to `identification`: Focus on identifying and documenting technical debt without detailed remediation plans.
  - When set to `prioritization`: Focus on prioritizing technical debt items based on business impact, risk, and effort to fix.
  - When set to `remediation`: Focus on detailed remediation strategies for the identified technical debt.
  - When set to `comprehensive`: Provide a comprehensive analysis including identification, prioritization, and remediation strategies.

- `scope`:
  - When set to `code`: Focus analysis on code-level technical debt (e.g., code smells, duplications, complexity).
  - When set to `architecture`: Focus analysis on architectural technical debt (e.g., design patterns, component coupling).
  - When set to `process`: Focus analysis on process-related technical debt (e.g., CI/CD, development workflows).
  - When set to `testing`: Focus analysis on testing-related technical debt (e.g., test coverage, test quality).
  - When set to `all`: Analyze all aspects of technical debt across code, architecture, process, and testing.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances TechDebt TechDebt can enhance CodeReview by adding specific focus on technical debt aspects.
- **RefactorGuide**: Enhances TechDebt TechDebt works well with RefactorGuide to provide comprehensive code improvement strategies.
