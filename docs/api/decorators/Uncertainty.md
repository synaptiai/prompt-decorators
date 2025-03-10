# Uncertainty Decorator

Explicitly highlights areas of uncertainty in the response. This decorator promotes intellectual honesty by clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `format` | `enum` | How to format uncertainty indications in the response | `inline` |
| `threshold` | `enum` | The threshold for flagging uncertain content | `medium` |
| `reason` | `boolean` | Whether to explain the reason for uncertainty | `False` |

## Format Options

- `inline`: Mark uncertain statements directly within the text using phrases like 'may be', 'possibly', 'uncertain', or 'subject to debate' as appropriate.
- `section`: Include a dedicated section at the end titled 'Areas of Uncertainty' that lists and discusses all uncertain aspects of the topic.
- `confidence`: Assign explicit confidence levels (e.g., 'high confidence', 'medium confidence', 'low confidence', 'speculative') to different statements or claims throughout the response.

## Threshold Options

- `low`: Flag even slightly uncertain information, being extremely cautious about presenting anything as definitive unless it is very well established.
- `medium`: Flag moderately uncertain information while presenting consensus views and well-supported claims with confidence.
- `high`: Only flag highly uncertain or speculative information, treating established scientific theories and widespread expert consensus as certain.

## Examples

### Inline uncertainty markers in a technical explanation

```
+++Uncertainty
Explain the potential timeline for achieving artificial general intelligence.
```

Explains AGI timelines with inline uncertainty markers highlighting speculative predictions, areas of expert disagreement, and knowledge gaps

### Dedicated uncertainty section with detailed reasoning

```
+++Uncertainty(format=section, reason=true, threshold=low)
What are the environmental impacts of fusion energy?
```

Provides information about fusion energy's environmental impacts followed by a dedicated section discussing all points of uncertainty with explanations for why each point is uncertain

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Be explicit about what is uncertain in your response. Use {format} to mark uncertainty. Apply a {threshold} threshold for identifying uncertain information. {reason} Make sure to differentiate between established facts and more speculative claims.

**Notes:** This model sometimes needs stronger prompting to acknowledge uncertainty in topics where it has high confidence


## Implementation Guidance

### Inline uncertainty markers in AGI timeline explanation

**Original Prompt:**
```
Explain the potential timeline for achieving artificial general intelligence.
```

**Transformed Prompt:**
```
Please explicitly highlight areas of uncertainty in your response, clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate. Mark uncertain statements directly within the text using phrases like 'may be', 'possibly', 'uncertain', or 'subject to debate' as appropriate. Flag moderately uncertain information while presenting consensus views and well-supported claims with confidence. Simply mark uncertain information without explaining the reasons for the uncertainty.

Explain the potential timeline for achieving artificial general intelligence.
```

### Dedicated uncertainty section with reasoning for fusion energy

**Original Prompt:**
```
What are the environmental impacts of fusion energy?
```

**Transformed Prompt:**
```
Please explicitly highlight areas of uncertainty in your response, clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate. Include a dedicated section at the end titled 'Areas of Uncertainty' that lists and discusses all uncertain aspects of the topic. Flag even slightly uncertain information, being extremely cautious about presenting anything as definitive unless it is very well established. For each point of uncertainty, briefly explain why it is uncertain (e.g., limited data, conflicting studies, theoretical gaps, etc.).

What are the environmental impacts of fusion energy?
```

## Transformation Details

**Base Instruction:** Please explicitly highlight areas of uncertainty in your response, clearly indicating what is known with confidence versus what is speculative, unknown, or subject to debate.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `format`:
  - When set to `inline`: Mark uncertain statements directly within the text using phrases like 'may be', 'possibly', 'uncertain', or 'subject to debate' as appropriate.
  - When set to `section`: Include a dedicated section at the end titled 'Areas of Uncertainty' that lists and discusses all uncertain aspects of the topic.
  - When set to `confidence`: Assign explicit confidence levels (e.g., 'high confidence', 'medium confidence', 'low confidence', 'speculative') to different statements or claims throughout the response.

- `threshold`:
  - When set to `low`: Flag even slightly uncertain information, being extremely cautious about presenting anything as definitive unless it is very well established.
  - When set to `medium`: Flag moderately uncertain information while presenting consensus views and well-supported claims with confidence.
  - When set to `high`: Only flag highly uncertain or speculative information, treating established scientific theories and widespread expert consensus as certain.

- `reason`:
  - When set to `true`: For each point of uncertainty, briefly explain why it is uncertain (e.g., limited data, conflicting studies, theoretical gaps, etc.).
  - When set to `false`: Simply mark uncertain information without explaining the reasons for the uncertainty.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Confidence**: Enhances Uncertainty Confidence and Uncertainty are complementary, with Confidence focusing on quantifying certainty while Uncertainty highlights the unknown
- **FactCheck**: Enhances Uncertainty FactCheck pairs well with Uncertainty to verify claims while acknowledging limitations in knowledge
- **Limitations**: Enhances Uncertainty Limitations complements Uncertainty by addressing broader constraints in addition to specific uncertain points
