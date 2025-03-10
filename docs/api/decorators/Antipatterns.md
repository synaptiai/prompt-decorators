# Antipatterns Decorator

Identifies common mistakes and how to avoid them.

**Category**: Developer Education

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `domain` | enum | Problem area | context-dependent |
| `severity` | enum | Issue importance filter | major |
| `format` | enum | Presentation style | examples |

## Domain Options

- `architecture`: Focus on architectural antipatterns such as monolithic systems, tight coupling, and design flaws.
- `code`: Focus on code-level antipatterns such as code smells, anti-patterns in programming practices, and implementation issues.
- `database`: Focus on database antipatterns such as poor schema design, inefficient queries, and data integrity issues.
- `process`: Focus on process antipatterns such as inefficient workflows, communication issues, and development methodology problems.
- `security`: Focus on security antipatterns such as insecure coding practices, authentication flaws, and vulnerability patterns.

## Severity Options

- `all`: Include all antipatterns regardless of their severity or impact.
- `major`: Focus on significant antipatterns that can cause substantial problems but may not be immediately critical.
- `critical`: Focus only on the most severe antipatterns that pose immediate risks or significant technical debt.

## Format Options

- `examples`: Provide concrete examples of each antipattern with code or design snippets that illustrate the problem.
- `explanation`: Provide detailed explanations of each antipattern, including why it's problematic and its potential impacts.
- `refactoring-guide`: Structure the response as a step-by-step guide for identifying and refactoring each antipattern.

## Examples

### Identifying database antipatterns

```
+++Antipatterns(domain=database, severity=critical, format=examples)
Identify common antipatterns in MongoDB schema design and how to avoid them.
```

The response will identify critical antipatterns in MongoDB schema design with concrete examples of each problem pattern.

### Security code review

```
+++Antipatterns(domain=security, severity=all, format=refactoring-guide)
Review this authentication code for potential issues.
```

The response will provide a comprehensive refactoring guide for identifying and fixing all security antipatterns in authentication code.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Identify and explain common antipatterns and mistakes to avoid. For each antipattern, explain: 1) What it is, 2) Why it's problematic, 3) How to identify it, and 4) How to fix or avoid it.

**Notes:** More structured instruction helps smaller models organize their response effectively.


## Implementation Guidance

### Database design review

**Original Prompt:**
```
Review my MongoDB schema design.
```

**Transformed Prompt:**
```
Identify common antipatterns in MongoDB schema design. Focus on critical issues that pose immediate risks or significant technical debt. Provide concrete examples of each antipattern with code or design snippets that illustrate the problem. Then review my MongoDB schema design.
```

**Notes:** The decorator adds specific guidance to look for antipatterns before performing the requested review.

## Transformation Details

**Base Instruction:** Identify common antipatterns and mistakes in the specified domain. Focus on how to recognize these issues and provide guidance on how to avoid or fix them.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `domain`:
  - When set to `architecture`: Focus on architectural antipatterns such as monolithic systems, tight coupling, and design flaws.
  - When set to `code`: Focus on code-level antipatterns such as code smells, anti-patterns in programming practices, and implementation issues.
  - When set to `database`: Focus on database antipatterns such as poor schema design, inefficient queries, and data integrity issues.
  - When set to `process`: Focus on process antipatterns such as inefficient workflows, communication issues, and development methodology problems.
  - When set to `security`: Focus on security antipatterns such as insecure coding practices, authentication flaws, and vulnerability patterns.

- `severity`:
  - When set to `all`: Include all antipatterns regardless of their severity or impact.
  - When set to `major`: Focus on significant antipatterns that can cause substantial problems but may not be immediately critical.
  - When set to `critical`: Focus only on the most severe antipatterns that pose immediate risks or significant technical debt.

- `format`:
  - When set to `examples`: Provide concrete examples of each antipattern with code or design snippets that illustrate the problem.
  - When set to `explanation`: Provide detailed explanations of each antipattern, including why it's problematic and its potential impacts.
  - When set to `refactoring-guide`: Structure the response as a step-by-step guide for identifying and refactoring each antipattern.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, claude-instant
- **Standard Version**: 1.0.0 - 1.0.0

## Related Decorators

- **BestPractices**: Enhances Antipatterns Antipatterns works well with BestPractices, as one identifies what to avoid while the other identifies what to do.
- **CodeReview**: Enhances Antipatterns Antipatterns can enhance CodeReview by specifically focusing on problematic patterns.
