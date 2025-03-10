# Troubleshoot Decorator

Creates troubleshooting guides for resolving system issues.

**Category**: Devops And Infrastructure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `component` | `enum` | System area | `application` |
| `format` | `enum` | Guide structure | `step-by-step` |
| `audience` | `enum` | Target user | `sre` |

## Component Options

- `network`: Focus on network-related issues such as connectivity, latency, DNS problems, and routing.
- `database`: Address database issues including performance problems, query optimization, data integrity, and availability.
- `application`: Cover application-level problems including bugs, performance bottlenecks, error handling, and service integration.
- `infrastructure`: Examine infrastructure concerns like server health, resource utilization, scaling issues, and deployment problems.
- `security`: Focus on security vulnerabilities, access control issues, authentication problems, and potential breaches.

## Format Options

- `decision-tree`: Structure the guide as a decision tree with clear branching paths based on symptoms and diagnostic results.
- `step-by-step`: Present a sequential, ordered list of troubleshooting steps with clear instructions at each stage.
- `flowchart`: Organize the troubleshooting process as a visual flowchart with decision points and action steps.
- `runbook`: Create a detailed operational runbook with procedures, commands, and expected outputs for each scenario.

## Audience Options

- `developer`: Target the guide for software developers with appropriate technical depth and code-level details.
- `sre`: Design for Site Reliability Engineers with focus on system-level diagnostics and operational concerns.
- `support`: Create for support personnel with clear escalation paths and customer-facing considerations.
- `end-user`: Simplify for end-users with minimal technical jargon and focus on user interface interactions.

## Examples

### Database troubleshooting guide in decision tree format for SREs

```
+++Troubleshoot(component=database, format=decision-tree, audience=sre)
Create a troubleshooting guide for PostgreSQL performance issues in production.
```

A decision tree-structured troubleshooting guide for PostgreSQL performance issues, targeted at Site Reliability Engineers with appropriate technical depth.

### Network troubleshooting guide for support staff

```
+++Troubleshoot(component=network, format=step-by-step, audience=support)
Create a guide for diagnosing and resolving VPN connection failures.
```

A step-by-step troubleshooting guide for VPN connection issues, designed for support personnel with appropriate escalation paths.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a troubleshooting guide for {component} issues. Use a {format} format designed for {audience} users. Include clear steps, diagnostic procedures, and solutions.

**Notes:** Simplified instruction for models with more limited context windows.


## Implementation Guidance

### Database troubleshooting for SREs

**Original Prompt:**
```
Create a troubleshooting guide for PostgreSQL performance issues in production.
```

**Transformed Prompt:**
```
Create a comprehensive troubleshooting guide that helps identify and resolve issues. The guide should be clear, methodical, and focused on practical solutions. Address database issues including performance problems, query optimization, data integrity, and availability. Present a sequential, ordered list of troubleshooting steps with clear instructions at each stage. Design for Site Reliability Engineers with focus on system-level diagnostics and operational concerns.

Create a troubleshooting guide for PostgreSQL performance issues in production.
```

**Notes:** The decorator adds specific guidance on the type of troubleshooting content to create, tailored to the specified component, format, and audience.

## Transformation Details

**Base Instruction:** Create a comprehensive troubleshooting guide that helps identify and resolve issues. The guide should be clear, methodical, and focused on practical solutions.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `component`:
  - When set to `network`: Focus on network-related issues such as connectivity, latency, DNS problems, and routing.
  - When set to `database`: Address database issues including performance problems, query optimization, data integrity, and availability.
  - When set to `application`: Cover application-level problems including bugs, performance bottlenecks, error handling, and service integration.
  - When set to `infrastructure`: Examine infrastructure concerns like server health, resource utilization, scaling issues, and deployment problems.
  - When set to `security`: Focus on security vulnerabilities, access control issues, authentication problems, and potential breaches.

- `format`:
  - When set to `decision-tree`: Structure the guide as a decision tree with clear branching paths based on symptoms and diagnostic results.
  - When set to `step-by-step`: Present a sequential, ordered list of troubleshooting steps with clear instructions at each stage.
  - When set to `flowchart`: Organize the troubleshooting process as a visual flowchart with decision points and action steps.
  - When set to `runbook`: Create a detailed operational runbook with procedures, commands, and expected outputs for each scenario.

- `audience`:
  - When set to `developer`: Target the guide for software developers with appropriate technical depth and code-level details.
  - When set to `sre`: Design for Site Reliability Engineers with focus on system-level diagnostics and operational concerns.
  - When set to `support`: Create for support personnel with clear escalation paths and customer-facing considerations.
  - When set to `end-user`: Simplify for end-users with minimal technical jargon and focus on user interface interactions.

## Compatibility

- **Requires**: None
- **Conflicts**: StepByStep
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **Explain**: Enhances Troubleshoot Can be combined with Explain to create more detailed explanations within the troubleshooting steps.
- **StepByStep**: Conflicts with Troubleshoot The format parameter with 'step-by-step' value overlaps with StepByStep decorator functionality.
