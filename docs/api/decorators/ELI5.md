# ELI5 Decorator

Adapts the response to explain a concept as if to a 5-year-old child. This decorator simplifies complex topics using basic vocabulary, concrete examples, and relatable analogies to make information accessible to non-experts or those new to a subject.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `strictness` | boolean | Whether to strictly maintain a child-appropriate level of simplicity or allow slightly more complexity when necessary | False |

## Examples

### Basic explanation of a complex scientific concept

```
+++ELI5
Explain how nuclear fusion works.
```

Explains nuclear fusion using simple language, analogies, and examples a child could understand

### Strict simplified explanation of a technical subject

```
+++ELI5(strictness=true)
How does the internet work?
```

Provides an extremely simplified explanation of the internet using only basic vocabulary and concrete examples appropriate for young children

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Explain this in the simplest possible terms, as if talking to a young child. Use words a 5-year-old would know. Compare complex ideas to everyday things like toys, food, or familiar activities. {strictness}

**Notes:** This model sometimes needs reminders to maintain the simplified level throughout longer responses


## Implementation Guidance

### Basic ELI5 explanation of nuclear fusion

**Original Prompt:**
```
Explain how nuclear fusion works.
```

**Transformed Prompt:**
```
Please explain this concept as you would to a 5-year-old child. Use simple vocabulary, concrete examples, and relatable analogies. Keep explanations simple and child-friendly, but you may introduce slightly more advanced concepts when absolutely necessary for understanding, as long as they're explained with simple analogies.

Explain how nuclear fusion works.
```

### Strict ELI5 explanation of the internet

**Original Prompt:**
```
How does the internet work?
```

**Transformed Prompt:**
```
Please explain this concept as you would to a 5-year-old child. Use simple vocabulary, concrete examples, and relatable analogies. Maintain an extremely simplified approach that a young child would understand, using only basic vocabulary and very concrete analogies. Avoid any technical terms or complex explanations entirely.

How does the internet work?
```

## Transformation Details

**Base Instruction:** Please explain this concept as you would to a 5-year-old child. Use simple vocabulary, concrete examples, and relatable analogies.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `strictness`:
  - When set to `true`: Maintain an extremely simplified approach that a young child would understand, using only basic vocabulary and very concrete analogies. Avoid any technical terms or complex explanations entirely.
  - When set to `false`: Keep explanations simple and child-friendly, but you may introduce slightly more advanced concepts when absolutely necessary for understanding, as long as they're explained with simple analogies.

## Compatibility

- **Requires**: None
- **Conflicts**: Academic, Professional, AsExpert, Precision, Tone
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Academic**: Conflicts with ELI5 ELI5's simplified language directly conflicts with Academic's scholarly approach
- **Professional**: Conflicts with ELI5 ELI5's child-like language conflicts with Professional's business-oriented language
- **AsExpert**: Conflicts with ELI5 ELI5 requires beginner-level explanations which conflict with expert-level discourse
- **Analogical**: Enhances ELI5 Analogical reasoning works well with ELI5 to create child-friendly analogies
