# Precision Decorator

Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `level` | enum | The degree of precision to apply | high |
| `units` | boolean | Whether to consistently provide units for all measurements | True |
| `definitions` | boolean | Whether to include precise definitions for key terms | False |

## Level Options

- `moderate`: Use moderately precise language with specific details where important, while maintaining accessibility and clarity for a general audience.
- `high`: Use highly precise language throughout the response, with exact figures, specific terminology, and detailed descriptions that leave minimal room for ambiguity.
- `scientific`: Use scientific-grade precision with rigorous accuracy, including error margins where appropriate, precise technical terminology, and specific quantitative measurements.

## Examples

### Basic precise explanation of a scientific concept

```
+++Precision
Explain how vaccines work.
```

Provides an explanation of vaccine mechanisms using precise terminology, specific examples, and accurate measurements where relevant

### Highly precise response with scientific rigor

```
+++Precision(level=scientific, units=true, definitions=true)
Describe the process of photosynthesis.
```

Delivers a scientifically precise explanation of photosynthesis with exact units for all measurements, precise definitions for key terms, and specific chemical reactions

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Provide information with {level} precision. Use exact numbers, specific terminology, and avoid vague language. {units} {definitions} For every claim, aim for the highest possible accuracy and specificity. If you're uncertain about a precise value, acknowledge the uncertainty rather than giving approximate information.

**Notes:** This model may need explicit reminders to maintain precision throughout, especially for longer responses or complex topics


## Compatibility

- **Requires**: None
- **Conflicts**: ELI5
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Fact-Check**: Enhances Precision Precision complements Fact-Check by ensuring the verified information is presented with appropriate specificity
- **Academic**: Enhances Precision Precision enhances Academic by adding scientific rigor and exactitude to scholarly content
- **ELI5**: Conflicts with Precision The high precision and technical specificity conflicts with ELI5's goal of simplified, accessible explanations
