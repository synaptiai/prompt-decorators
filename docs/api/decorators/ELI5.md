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

### gpt-3.5-turbo

**Instruction:** Explain this in the simplest possible terms, as if talking to a young child. Use words a 5-year-old would know. Compare complex ideas to everyday things like toys, food, or familiar activities. {strictness}

**Notes:** This model sometimes needs reminders to maintain the simplified level throughout longer responses


## Compatibility

- **Requires**: None
- **Conflicts**: Academic, Professional, AsExpert, Precision, Tone
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Academic**: Conflicts with ELI5 ELI5's simplified language directly conflicts with Academic's scholarly approach
- **Professional**: Conflicts with ELI5 ELI5's child-like language conflicts with Professional's business-oriented language
- **AsExpert**: Conflicts with ELI5 ELI5 requires beginner-level explanations which conflict with expert-level discourse
- **Analogical**: Enhances ELI5 Analogical reasoning works well with ELI5 to create child-friendly analogies
