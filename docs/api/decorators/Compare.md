# Compare Decorator

Compares different technologies, approaches, or tools.

**Category**: Developer Education

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `aspects` | `string` | Comparison dimensions | `performance,features,ecosystem,learning-curve` |
| `format` | `enum` | Comparison format | `table` |
| `bias` | `enum` | Fairness control | `neutral` |

## Format Options

- `table`: Present the comparison in a clear, tabular format with items as columns and aspects as rows.
- `prose`: Present the comparison as flowing paragraphs that discuss each aspect across all items.
- `pros-cons`: For each item, list the pros and cons relative to the alternatives.
- `decision-matrix`: Create a decision matrix that scores each item across all aspects, with a final recommendation.

## Bias Options

- `neutral`: Maintain a neutral, objective stance throughout the comparison.
- `weighted`: Weight the importance of different aspects based on common industry priorities.
- `opinionated`: Include your assessment of which option is superior for different use cases.

## Examples

### Comparing web frameworks with a decision matrix

```
+++Compare(aspects=performance,ecosystem,learning-curve, format=decision-matrix, bias=neutral)
Compare React, Vue, and Angular for a new enterprise web application.
```

A neutral comparison of React, Vue, and Angular across performance, ecosystem, and learning-curve dimensions, presented as a decision matrix with scores and a final recommendation.

### Comparing database technologies in tabular format

```
+++Compare(aspects=scalability,query-performance,data-types,community-support, format=table)
Compare PostgreSQL, MongoDB, and MySQL for a high-traffic e-commerce application.
```

A tabular comparison of PostgreSQL, MongoDB, and MySQL across the specified aspects, making it easy to see the strengths and weaknesses of each database option.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a detailed comparison of the following items. Analyze their similarities and differences systematically.

**Notes:** Simplified instruction for models with more limited context windows.


## Implementation Guidance

### Technology comparison

**Original Prompt:**
```
Compare React, Vue, and Angular for a new enterprise web application.
```

**Transformed Prompt:**
```
Compare the following items across multiple dimensions. Provide a thorough analysis that highlights similarities and differences. Compare across these specific aspects: performance,ecosystem,learning-curve. Present the comparison in a decision matrix that scores each item across all aspects, with a final recommendation. Maintain a neutral, objective stance throughout the comparison.

Compare React, Vue, and Angular for a new enterprise web application.
```

**Notes:** The decorator adds specific comparison instructions while maintaining the original request.

## Transformation Details

**Base Instruction:** Compare the following items across multiple dimensions. Provide a thorough analysis that highlights similarities and differences.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `aspects`:
  - Format: Compare across these specific aspects: {value}.

- `format`:
  - When set to `table`: Present the comparison in a clear, tabular format with items as columns and aspects as rows.
  - When set to `prose`: Present the comparison as flowing paragraphs that discuss each aspect across all items.
  - When set to `pros-cons`: For each item, list the pros and cons relative to the alternatives.
  - When set to `decision-matrix`: Create a decision matrix that scores each item across all aspects, with a final recommendation.

- `bias`:
  - When set to `neutral`: Maintain a neutral, objective stance throughout the comparison.
  - When set to `weighted`: Weight the importance of different aspects based on common industry priorities.
  - When set to `opinionated`: Include your assessment of which option is superior for different use cases.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **DetailLevel**: Enhances Compare DetailLevel can be used to control the depth of the comparison.
- **Audience**: Enhances Compare Audience can help tailor the comparison to specific knowledge levels.
