# Combined Decorator Examples

This document demonstrates how to combine multiple decorators for more complex interactions.

## Reasoning + StepByStep

Combining reasoning with step-by-step structuring provides detailed explanations in a sequential format.

### Example:

```
+++Reasoning(depth=comprehensive)
+++StepByStep(numbered=true)
How does public key cryptography work?
```

### Expected Result:

The AI will provide a comprehensive reasoning process broken down into numbered steps:

1. **Understanding the Problem**: First, let's consider why traditional encryption is problematic...
2. **The Key Exchange Problem**: The fundamental challenge in cryptography is securely exchanging keys...
3. **Asymmetric Solution**: Public key cryptography solves this by using two mathematically linked keys...
4. **Mathematical Foundation**: The security relies on one-way functions that are easy to compute but difficult to reverse...
5. **Encryption Process**: When Alice wants to send a message to Bob...
6. **Decryption Process**: Upon receiving the encrypted message, Bob uses his private key...
7. **Digital Signatures**: Public key cryptography also enables digital signatures by reversing the process...
8. **Real-world Applications**: This technology underpins secure websites (HTTPS), secure email (PGP), and cryptocurrencies...

## OutputFormat + Tone

Combining output formatting with tone adjustment allows for precisely styled responses.

### Example:

```
+++OutputFormat(format=markdown)
+++Tone(style=academic)
Explain the impact of climate change on marine ecosystems
```

### Expected Result:

The AI will respond with a formally structured academic explanation in Markdown format:

```markdown
# The Impact of Climate Change on Marine Ecosystems

## Abstract
This analysis examines the multifaceted effects of anthropogenic climate change on marine ecological systems...

## 1. Introduction
Marine ecosystems constitute approximately 71% of Earth's surface and are critical regulators of global climate...

## 2. Primary Effects
### 2.1 Ocean Acidification
The absorption of atmospheric CO₂ by oceanic waters has resulted in a 0.1 pH unit decrease...

### 2.2 Temperature Increases
Mean sea surface temperatures have risen by approximately 0.13°C per decade...

## 3. Ecological Consequences
...

## 4. Conclusion
...

## References
...
```

## Reasoning + OutputFormat + StepByStep

This powerful combination provides structured, well-reasoned responses in a specific format.

### Example:

```
+++Reasoning(depth=moderate)
+++StepByStep(numbered=true)
+++OutputFormat(format=json)
What factors should I consider when choosing a programming language for a new project?
```

### Expected Result:

The AI will provide a reasoned analysis in numbered steps, formatted as JSON:

```json
{
  "reasoning_process": {
    "initial_considerations": "Choosing a programming language involves balancing various factors specific to your project needs...",
    "key_decision_factors": "We need to evaluate technical requirements, team expertise, ecosystem support, and future maintenance..."
  },
  "steps": [
    {
      "number": 1,
      "title": "Define Project Requirements",
      "description": "Analyze the technical needs of your project...",
      "considerations": [
        "Performance requirements",
        "Scalability needs",
        "Deployment environment",
        "Integration requirements"
      ]
    },
    {
      "number": 2,
      "title": "Assess Team Expertise",
      "description": "Evaluate your team's current knowledge and learning curve...",
      "considerations": [
        "Current language proficiency",
        "Learning resources available",
        "Development timeline constraints"
      ]
    },
    {
      "number": 3,
      "title": "Evaluate Ecosystem",
      "description": "Consider the libraries, frameworks, and tools available...",
      "considerations": [
        "Package availability",
        "Community support",
        "Documentation quality"
      ]
    },
    {
      "number": 4,
      "title": "Consider Long-term Maintenance",
      "description": "Think about the future of your project...",
      "considerations": [
        "Language stability",
        "Hiring pool",
        "Backward compatibility"
      ]
    },
    {
      "number": 5,
      "title": "Make the Decision",
      "description": "Balance all factors to select the most appropriate language...",
      "considerations": [
        "Prioritize critical requirements",
        "Consider using multiple languages if appropriate",
        "Plan for potential migration paths"
      ]
    }
  ],
  "conclusion": "The optimal programming language choice depends on your specific context and priorities..."
}
```

## All Core Decorators Combined

This example shows how all five core decorators can work together.

### Example:

```
+++Version(standard=1.0.0)
+++Reasoning(depth=comprehensive)
+++StepByStep(numbered=true)
+++OutputFormat(format=markdown)
+++Tone(style=technical)
Explain how machine learning models can be deployed in production environments
```

### Expected Result:

The AI will provide a comprehensive, technical explanation with detailed reasoning, structured as numbered steps, formatted in Markdown, and written in a technical tone. The response will follow version 1.0.0 of the standard. 