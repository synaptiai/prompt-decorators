# BestPractices Decorator

Summarizes best practices for specific technologies or processes.

**Category**: Developer Education

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `for` | string | Practice domain | context-dependent |
| `context` | enum | Implementation environment | enterprise |
| `format` | enum | Output structure | detailed |

## Context Options

- `startup`: Focus on agile, cost-effective, and scalable approaches suitable for startup environments.
- `enterprise`: Emphasize enterprise-grade solutions with focus on security, compliance, and integration with existing systems.
- `personal`: Prioritize simplicity, ease of maintenance, and individual productivity.
- `open-source`: Consider community standards, contribution guidelines, and collaborative development practices.

## Format Options

- `list`: Present the best practices as a concise, numbered list of key points.
- `detailed`: Provide detailed explanations for each best practice with rationale and implementation considerations.
- `examples`: Include concrete code examples or implementation scenarios for each best practice.
- `cookbook`: Structure the response as a step-by-step guide with practical recipes for implementation.

## Examples

### Getting best practices for Node.js in an enterprise context with examples

```
+++BestPractices(for=node.js, context=enterprise, format=examples)
Provide best practices for building production-ready Node.js microservices.
```

The response will include best practices for Node.js development specifically tailored for enterprise environments, with concrete code examples for each practice.

### Getting best practices for cloud security as a concise list

```
+++BestPractices(for="AWS cloud security", format=list)
What should I know about securing AWS resources?
```

The response will provide a numbered list of key best practices for AWS cloud security.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Summarize industry best practices for {for} in a {format} format, optimized for {context} environments.

**Notes:** Simplified instruction for models with less context capacity.


## Implementation Guidance

### Node.js Development

**Original Prompt:**
```
How should I structure my Node.js project?
```

**Transformed Prompt:**
```
Provide a comprehensive summary of best practices for Node.js project structure. Emphasize enterprise-grade solutions with focus on security, compliance, and integration with existing systems. Provide detailed explanations for each best practice with rationale and implementation considerations.

How should I structure my Node.js project?
```

**Notes:** The decorator adds specific guidance for the LLM to focus on best practices in the enterprise context with detailed explanations.

## Transformation Details

**Base Instruction:** Provide a comprehensive summary of best practices for {for}.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `for`:
  - Format: Provide a comprehensive summary of best practices for {value}.

- `context`:
  - When set to `startup`: Focus on agile, cost-effective, and scalable approaches suitable for startup environments.
  - When set to `enterprise`: Emphasize enterprise-grade solutions with focus on security, compliance, and integration with existing systems.
  - When set to `personal`: Prioritize simplicity, ease of maintenance, and individual productivity.
  - When set to `open-source`: Consider community standards, contribution guidelines, and collaborative development practices.

- `format`:
  - When set to `list`: Present the best practices as a concise, numbered list of key points.
  - When set to `detailed`: Provide detailed explanations for each best practice with rationale and implementation considerations.
  - When set to `examples`: Include concrete code examples or implementation scenarios for each best practice.
  - When set to `cookbook`: Structure the response as a step-by-step guide with practical recipes for implementation.

## Compatibility

- **Requires**: None
- **Conflicts**: ELI5
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **CodeExamples**: Enhances BestPractices BestPractices works well with CodeExamples to provide practical implementations of the recommended practices.
- **Concise**: Conflicts with BestPractices When format=detailed or format=cookbook, this conflicts with the Concise decorator's goal of brevity.
