# SRE Decorator

Applies Site Reliability Engineering practices.

**Category**: Devops And Infrastructure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `focus` | enum | SRE practice area | context-dependent |
| `maturity` | enum | Organization SRE maturity | intermediate |
| `output` | enum | Deliverable type | implementation |

## Focus Options

- `slos`: Focus on defining appropriate Service Level Objectives (SLOs) that balance reliability with innovation velocity.
- `error-budgets`: Implement error budgets to quantify acceptable service disruption and guide development priorities.
- `runbooks`: Develop clear, actionable runbooks for operational procedures and incident response.
- `postmortems`: Create blameless postmortem processes to learn from incidents and prevent recurrence.
- `chaos-eng`: Apply chaos engineering principles to proactively identify system weaknesses.
- `automation`: Prioritize automation to reduce toil and increase operational efficiency.

## Maturity Options

- `beginner`: Provide foundational SRE concepts and implementation steps suitable for organizations new to SRE practices.
- `intermediate`: Offer more sophisticated SRE strategies for organizations with established but evolving SRE practices.
- `advanced`: Present cutting-edge SRE approaches for organizations with mature SRE functions seeking optimization.

## Output Options

- `implementation`: Provide specific, actionable implementation guidance with concrete examples and code where appropriate.
- `roadmap`: Develop a phased approach to implementing or improving the specified SRE practices over time.
- `assessment`: Evaluate current practices against SRE best practices and identify gaps and improvement opportunities.

## Examples

### Creating SLOs for an e-commerce platform

```
+++SRE(focus=slos, maturity=intermediate, output=implementation)
Develop SLOs and error budgets for our e-commerce platform focusing on checkout and payment processing.
```

Provides specific implementation guidance for creating appropriate SLOs and error budgets for checkout and payment processing systems, tailored to an organization with intermediate SRE maturity.

### Developing a chaos engineering roadmap

```
+++SRE(focus=chaos-eng, maturity=beginner, output=roadmap)
How should we introduce chaos engineering to our organization?
```

Delivers a phased roadmap for introducing chaos engineering practices to an organization new to SRE, starting with basic principles and progressing to more advanced techniques.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Use Site Reliability Engineering (SRE) principles in your response. Consider system reliability, monitoring, automation, and incident management.

**Notes:** Simplified instruction for models with less context capacity.


## Implementation Guidance

### Cloud infrastructure reliability

**Original Prompt:**
```
How can we improve our AWS infrastructure reliability?
```

**Transformed Prompt:**
```
Apply Site Reliability Engineering practices to this task. Consider reliability, scalability, and operational excellence in your response. Focus on defining appropriate Service Level Objectives (SLOs) that balance reliability with innovation velocity. Offer more sophisticated SRE strategies for organizations with established but evolving SRE practices. Provide specific, actionable implementation guidance with concrete examples and code where appropriate.

How can we improve our AWS infrastructure reliability?
```

**Notes:** This example shows how the decorator adds SRE context with a focus on SLOs for an intermediate organization seeking implementation guidance.

## Transformation Details

**Base Instruction:** Apply Site Reliability Engineering practices to this task. Consider reliability, scalability, and operational excellence in your response.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `focus`:
  - When set to `slos`: Focus on defining appropriate Service Level Objectives (SLOs) that balance reliability with innovation velocity.
  - When set to `error-budgets`: Implement error budgets to quantify acceptable service disruption and guide development priorities.
  - When set to `runbooks`: Develop clear, actionable runbooks for operational procedures and incident response.
  - When set to `postmortems`: Create blameless postmortem processes to learn from incidents and prevent recurrence.
  - When set to `chaos-eng`: Apply chaos engineering principles to proactively identify system weaknesses.
  - When set to `automation`: Prioritize automation to reduce toil and increase operational efficiency.

- `maturity`:
  - When set to `beginner`: Provide foundational SRE concepts and implementation steps suitable for organizations new to SRE practices.
  - When set to `intermediate`: Offer more sophisticated SRE strategies for organizations with established but evolving SRE practices.
  - When set to `advanced`: Present cutting-edge SRE approaches for organizations with mature SRE functions seeking optimization.

- `output`:
  - When set to `implementation`: Provide specific, actionable implementation guidance with concrete examples and code where appropriate.
  - When set to `roadmap`: Develop a phased approach to implementing or improving the specified SRE practices over time.
  - When set to `assessment`: Evaluate current practices against SRE best practices and identify gaps and improvement opportunities.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, claude-instant
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **DevOps**: Enhances SRE SRE complements DevOps practices by adding reliability engineering focus.
- **CloudArchitecture**: Enhances SRE SRE provides reliability considerations for cloud architecture designs.
