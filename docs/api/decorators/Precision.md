# Precision Decorator

Enhances responses with exact, specific, and precisely defined information. This decorator prioritizes accuracy in measurements, terms, definitions, and claims, avoiding vague language in favor of concrete specificity.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `level` | `enum` | The degree of precision to apply | `high` |
| `units` | `boolean` | Whether to consistently provide units for all measurements | `True` |
| `definitions` | `boolean` | Whether to include precise definitions for key terms | `False` |

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

### gpt-4-turbo

**Instruction:** Provide information with {level} precision. Use exact numbers, specific terminology, and avoid vague language. {units} {definitions} For every claim, aim for the highest possible accuracy and specificity. If you're uncertain about a precise value, acknowledge the uncertainty rather than giving approximate information.

**Notes:** This model may need explicit reminders to maintain precision throughout, especially for longer responses or complex topics


## Implementation Guidance

### Precise explanation of vaccine function

**Original Prompt:**
```
Explain how vaccines work.
```

**Transformed Prompt:**
```
Please provide information with a high degree of precision and specificity. Use exact measurements, specific terminology, and concrete details rather than vague or general statements. Prioritize accuracy in all claims and descriptions. Use highly precise language throughout the response, with exact figures, specific terminology, and detailed descriptions that leave minimal room for ambiguity. Always include appropriate units for all measurements and quantities, using standard notation (SI units preferred where applicable). Use precise terminology without interrupting the flow with explicit definitions unless absolutely necessary for understanding.

Explain how vaccines work.
```

### Scientific precision for photosynthesis explanation

**Original Prompt:**
```
Describe the process of photosynthesis.
```

**Transformed Prompt:**
```
Please provide information with a high degree of precision and specificity. Use exact measurements, specific terminology, and concrete details rather than vague or general statements. Prioritize accuracy in all claims and descriptions. Use scientific-grade precision with rigorous accuracy, including error margins where appropriate, precise technical terminology, and specific quantitative measurements. Always include appropriate units for all measurements and quantities, using standard notation (SI units preferred where applicable). Include precise definitions for key terms and concepts when first introduced, ensuring clarity and exact understanding of specialized vocabulary.

Describe the process of photosynthesis.
```

## Transformation Details

**Base Instruction:** Please provide information with a high degree of precision and specificity. Use exact measurements, specific terminology, and concrete details rather than vague or general statements. Prioritize accuracy in all claims and descriptions.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `level`:
  - When set to `moderate`: Use moderately precise language with specific details where important, while maintaining accessibility and clarity for a general audience.
  - When set to `high`: Use highly precise language throughout the response, with exact figures, specific terminology, and detailed descriptions that leave minimal room for ambiguity.
  - When set to `scientific`: Use scientific-grade precision with rigorous accuracy, including error margins where appropriate, precise technical terminology, and specific quantitative measurements.

- `units`:
  - When set to `true`: Always include appropriate units for all measurements and quantities, using standard notation (SI units preferred where applicable).
  - When set to `false`: Include units where necessary for clarity, but prioritize readability over comprehensive unit notation.

- `definitions`:
  - When set to `true`: Include precise definitions for key terms and concepts when first introduced, ensuring clarity and exact understanding of specialized vocabulary.
  - When set to `false`: Use precise terminology without interrupting the flow with explicit definitions unless absolutely necessary for understanding.

## Compatibility

- **Requires**: None
- **Conflicts**: ELI5
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Fact-Check**: Enhances Precision Precision complements Fact-Check by ensuring the verified information is presented with appropriate specificity
- **Academic**: Enhances Precision Precision enhances Academic by adding scientific rigor and exactitude to scholarly content
- **ELI5**: Conflicts with Precision The high precision and technical specificity conflicts with ELI5's goal of simplified, accessible explanations
