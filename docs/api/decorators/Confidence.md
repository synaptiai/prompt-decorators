# Confidence Decorator

Enhances the response with explicit indications of confidence levels for different statements or claims. This decorator promotes transparency about knowledge certainty and helps differentiate between well-established facts and more speculative content.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `scale` | enum | The method used to express confidence levels | qualitative |
| `threshold` | number | Minimum confidence level for including information (as a percentage) | 50 |
| `detailed` | boolean | Whether to provide explanations for confidence assessments | False |

## Scale Options

- `percent`: Express confidence levels as percentages (e.g., 95% confidence, 70% confidence).
- `qualitative`: Express confidence levels using qualitative descriptors (e.g., high confidence, moderate confidence, low confidence).
- `stars`: Express confidence levels using a star rating system (e.g., ⭐⭐⭐⭐⭐ for highest confidence, ⭐ for lowest).
- `numeric`: Express confidence levels using a numeric scale from 1-10, where 10 represents the highest confidence.

## Examples

### Qualitative confidence indicators for a complex topic

```
+++Confidence
Explain the current understanding of dark matter.
```

Explains dark matter theories with qualitative confidence indicators (high confidence, moderate confidence, etc.) for different claims

### Detailed percentage-based confidence with high threshold

```
+++Confidence(scale=percent, threshold=80, detailed=true)
What are the most effective treatments for depression?
```

Discusses only high-confidence (80%+) depression treatments with percentage indicators and explanations for confidence assessments

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** For each claim or statement in your response, indicate how confident you are using {scale} measures. Only include information where your confidence is at least {threshold}%. {detailed}

**Notes:** This model sometimes needs more explicit reminders to maintain consistent confidence indicators throughout a long response


## Implementation Guidance

### Qualitative confidence indicators for dark matter

**Original Prompt:**
```
Explain the current understanding of dark matter.
```

**Transformed Prompt:**
```
Please include explicit indications of your confidence level for different statements or claims in your response. Express confidence levels using qualitative descriptors (e.g., high confidence, moderate confidence, low confidence). Only include information for which your confidence level is at least 50%. State confidence levels without explaining the reasoning behind the assessments.

Explain the current understanding of dark matter.
```

### Detailed percentage-based confidence for depression treatments

**Original Prompt:**
```
What are the most effective treatments for depression?
```

**Transformed Prompt:**
```
Please include explicit indications of your confidence level for different statements or claims in your response. Express confidence levels as percentages (e.g., 95% confidence, 70% confidence). Only include information for which your confidence level is at least 80%. Provide brief explanations for why certain confidence levels were assigned to specific claims.

What are the most effective treatments for depression?
```

## Transformation Details

**Base Instruction:** Please include explicit indications of your confidence level for different statements or claims in your response.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `scale`:
  - When set to `percent`: Express confidence levels as percentages (e.g., 95% confidence, 70% confidence).
  - When set to `qualitative`: Express confidence levels using qualitative descriptors (e.g., high confidence, moderate confidence, low confidence).
  - When set to `stars`: Express confidence levels using a star rating system (e.g., ⭐⭐⭐⭐⭐ for highest confidence, ⭐ for lowest).
  - When set to `numeric`: Express confidence levels using a numeric scale from 1-10, where 10 represents the highest confidence.

- `threshold`:
  - Format: Only include information for which your confidence level is at least {value}%.

- `detailed`:
  - When set to `true`: Provide brief explanations for why certain confidence levels were assigned to specific claims.
  - When set to `false`: State confidence levels without explaining the reasoning behind the assessments.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **FactCheck**: Enhances Confidence FactCheck and Confidence work well together to provide both verification and quantification of certainty
- **Limitations**: Enhances Confidence Limitations complements Confidence by explaining broader constraints where Confidence quantifies specific certainty levels
