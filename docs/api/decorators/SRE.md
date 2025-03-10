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

### gpt-3.5-turbo

**Instruction:** Use Site Reliability Engineering (SRE) principles in your response. Consider system reliability, monitoring, automation, and incident management.

**Notes:** Simplified instruction for models with less context capacity.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, claude-instant
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **DevOps**: Enhances SRE SRE complements DevOps practices by adding reliability engineering focus.
- **CloudArchitecture**: Enhances SRE SRE provides reliability considerations for cloud architecture designs.
