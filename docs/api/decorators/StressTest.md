# StressTest Decorator

Tests the robustness of ideas, theories, plans, or systems by applying extreme conditions, edge cases, and unlikely scenarios. This decorator helps identify vulnerabilities, limitations, and breaking points that might not be apparent under normal circumstances.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `scenarios` | number | Number of stress test scenarios to apply | 3 |
| `severity` | enum | The intensity level of the stress conditions | severe |
| `domain` | string | Optional specific domain or dimension to stress test (e.g., financial, ethical, scalability) |  |

## Severity Options

- `moderate`: Apply realistic but challenging conditions that test important aspects without going to extremes.
- `severe`: Apply highly challenging conditions that push the subject to its likely breaking points and reveal significant vulnerabilities.
- `extreme`: Apply worst-case scenarios and highly improbable but catastrophic conditions to find absolute breaking points and critical vulnerabilities.

## Examples

### Basic stress test of a business model

```
+++StressTest
Evaluate this subscription-based SaaS business model.
```

Provides an analysis of the business model followed by three severe stress test scenarios that challenge its core assumptions and viability

### Extreme stress test focused on a specific domain

```
+++StressTest(scenarios=5, severity=extreme, domain=security)
Assess our new authentication protocol design.
```

Delivers an assessment of the authentication protocol followed by five extreme security-focused stress test scenarios that identify potential vulnerabilities and breaking points

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** First, provide a standard analysis of this topic. Then, apply {scenarios} different stress test scenarios at a {severity} level of intensity to find weaknesses and vulnerabilities. {domain} Each stress test should focus on a different aspect and clearly explain the scenario, the likely outcome, and what this reveals about potential weaknesses.

**Notes:** This model sometimes needs guidance to develop truly challenging scenarios rather than obvious or simplistic tests


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **RedTeam**: Enhances StressTest RedTeam and StressTest complement each other well, with RedTeam providing adversarial thinking and StressTest providing scenario-based challenges
- **BreakAndBuild**: Enhances StressTest StressTest can identify weaknesses that BreakAndBuild can then reconstruct solutions for
- **FindGaps**: Enhances StressTest FindGaps works well with StressTest to identify both what's missing and what might break
