# CodeWalkthrough Decorator

Provides detailed explanations of code functionality.

**Category**: Developer Education

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `focus` | enum | Walkthrough emphasis | how |
| `detail` | enum | Explanation granularity | key-parts |
| `audience` | enum | Target reader | peer |

## Focus Options

- `how`: Explain how the code works, focusing on its mechanics and implementation details.
- `why`: Explain why the code is designed this way, focusing on design decisions and rationale.
- `optimization`: Explain how the code is optimized, focusing on performance considerations and efficiency.
- `security`: Explain the security aspects of the code, focusing on potential vulnerabilities and safeguards.

## Detail Options

- `overview`: Provide a high-level overview of the code structure and functionality.
- `key-parts`: Focus on explaining the key components and important sections of the code.
- `line-by-line`: Provide a detailed line-by-line explanation of how the code works.

## Audience Options

- `junior`: Explain the code for a junior developer with basic programming knowledge.
- `peer`: Explain the code as you would to a peer developer with similar experience.
- `senior`: Explain the code with advanced concepts and patterns for a senior developer.
- `non-technical`: Explain the code in simple terms for someone without technical background.

## Examples

### Basic code walkthrough for junior developers

```
+++CodeWalkthrough(focus=how, detail=key-parts, audience=junior)
Walk through this authentication middleware explaining how it works.
```

A detailed explanation of how the authentication middleware works, focusing on key components and written for junior developers to understand.

### Security-focused code review for senior developers

```
+++CodeWalkthrough(focus=security, detail=line-by-line, audience=senior)
Explain this encryption implementation.
```

A comprehensive line-by-line security analysis of the encryption implementation, using advanced terminology appropriate for senior developers.

### High-level explanation for non-technical stakeholders

```
+++CodeWalkthrough(focus=why, detail=overview, audience=non-technical)
Explain what this payment processing code does.
```

A non-technical overview explaining why the payment processing code is designed the way it is, avoiding jargon and technical details.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Explain this code in detail. Make sure to cover how it works, focusing on {focus}. Provide a {detail} explanation suitable for a {audience} developer.

**Notes:** Simplified instruction format works better with GPT-3.5-turbo.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **CodeReview**: Enhances CodeWalkthrough CodeWalkthrough can enhance CodeReview by providing educational context to review comments.
- **ELI5**: Conflicts with CodeWalkthrough When audience is set to anything other than 'non-technical', this may conflict with ELI5's simplification approach.
