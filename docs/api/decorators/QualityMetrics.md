# QualityMetrics Decorator

Applies specific quality measurements to evaluate content against defined criteria. This decorator enhances verification by providing quantifiable assessments of aspects like accuracy, completeness, clarity, or other custom metrics.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `metrics` | array | Specific quality metrics to measure (e.g., accuracy, completeness, clarity, usefulness) |  |
| `scale` | enum | Rating scale to use for evaluations | 1-5 |
| `explanation` | boolean | Whether to provide detailed explanations for each metric score | True |

## Scale Options

- `1-5`: Use a 1-5 scale for your ratings, where 1 represents the lowest quality and 5 represents the highest quality.
- `1-10`: Use a 1-10 scale for your ratings, where 1 represents the lowest quality and 10 represents the highest quality.
- `percentage`: Express your ratings as percentages, ranging from 0% (lowest quality) to 100% (highest quality).
- `qualitative`: Use qualitative ratings (poor, fair, good, excellent) rather than numerical scores.

## Examples

### Basic quality assessment of an analysis

```
+++QualityMetrics
My analysis of the financial market trends is as follows...
```

Provides the analysis of financial market trends, followed by 1-5 ratings across standard quality metrics with explanations for each score

### Specific custom metrics with detailed qualitative assessment

```
+++QualityMetrics(metrics=[factual accuracy,predictive value,consideration of alternatives,logical flow], scale=qualitative, explanation=true)
Here's my policy proposal for urban housing...
```

Delivers the policy proposal, followed by qualitative assessments (poor/fair/good/excellent) of the four specified metrics, with detailed explanations for each evaluation

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** After providing your main response on this topic, evaluate the quality of your own response. Rate it on these metrics: {metrics} using a {scale} scale. {explanation} Present this evaluation in a clear 'Quality Assessment' section at the end of your response. Be honest and critical in your self-assessment.

**Notes:** This model may need explicit instructions to be sufficiently critical in its self-assessment rather than defaulting to consistently high ratings


## Implementation Guidance

### Financial market trend analysis with standard metrics

**Original Prompt:**
```
My analysis of the financial market trends is as follows...
```

**Transformed Prompt:**
```
Please include a quality assessment of your response using specific metrics. After presenting your main content, evaluate it against defined quality criteria with appropriate ratings and explanations where needed. Use a 1-5 scale for your ratings, where 1 represents the lowest quality and 5 represents the highest quality. For each metric, provide a detailed explanation that justifies the rating, citing specific aspects of the content.

My analysis of the financial market trends is as follows...
```

### Urban housing policy proposal with custom qualitative metrics

**Original Prompt:**
```
Here's my policy proposal for urban housing...
```

**Transformed Prompt:**
```
Please include a quality assessment of your response using specific metrics. After presenting your main content, evaluate it against defined quality criteria with appropriate ratings and explanations where needed. Evaluate your response against these specific quality metrics: [factual accuracy,predictive value,consideration of alternatives,logical flow]. For each metric, provide a rating and assess how well the content meets that particular quality standard. Use qualitative ratings (poor, fair, good, excellent) rather than numerical scores. For each metric, provide a detailed explanation that justifies the rating, citing specific aspects of the content.

Here's my policy proposal for urban housing...
```

## Transformation Details

**Base Instruction:** Please include a quality assessment of your response using specific metrics. After presenting your main content, evaluate it against defined quality criteria with appropriate ratings and explanations where needed.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `metrics`:
  - Format: Evaluate your response against these specific quality metrics: {value}. For each metric, provide a rating and assess how well the content meets that particular quality standard.

- `scale`:
  - When set to `1-5`: Use a 1-5 scale for your ratings, where 1 represents the lowest quality and 5 represents the highest quality.
  - When set to `1-10`: Use a 1-10 scale for your ratings, where 1 represents the lowest quality and 10 represents the highest quality.
  - When set to `percentage`: Express your ratings as percentages, ranging from 0% (lowest quality) to 100% (highest quality).
  - When set to `qualitative`: Use qualitative ratings (poor, fair, good, excellent) rather than numerical scores.

- `explanation`:
  - When set to `true`: For each metric, provide a detailed explanation that justifies the rating, citing specific aspects of the content.
  - When set to `false`: Provide ratings for each metric without detailed explanations.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **PeerReview**: Enhances QualityMetrics QualityMetrics provides structured quantitative assessment while PeerReview offers broader critique and improvement suggestions
- **FactCheck**: Enhances QualityMetrics FactCheck verifies specific claims while QualityMetrics assesses broader aspects including but not limited to factual accuracy
- **Confidence**: Enhances QualityMetrics Confidence indicates certainty in content while QualityMetrics evaluates multiple dimensions of quality
