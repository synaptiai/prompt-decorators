# PeerReview Decorator

Augments the response with a simulated peer review of the content. This decorator enhances critical thinking by evaluating the response's strengths, weaknesses, methodological soundness, and potential improvements as an academic reviewer would.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `criteria` | enum | Primary criteria to focus on in the review | all |
| `style` | enum | The tone and approach of the peer review | balanced |
| `position` | enum | Where to place the peer review relative to the main content | after |

## Criteria Options

- `accuracy`: Focus the peer review primarily on the factual accuracy and precision of the information presented.
- `methodology`: Focus the peer review primarily on the methodological approach, analytical framework, or reasoning process used.
- `limitations`: Focus the peer review primarily on identifying limitations, gaps, or unaddressed aspects in the analysis.
- `completeness`: Focus the peer review primarily on how thoroughly the topic is covered and whether key elements are missing.
- `all`: Include a comprehensive peer review addressing accuracy, methodology, limitations, and completeness of the content.

## Style Options

- `constructive`: Maintain a supportive tone in the peer review, emphasizing positive aspects while gently suggesting improvements.
- `critical`: Adopt a rigorously critical stance in the peer review, thoroughly identifying weaknesses and challenging assumptions.
- `balanced`: Provide a balanced peer review that equally addresses strengths and weaknesses with a neutral academic tone.

## Position Options

- `after`: Present the main content first, followed by the peer review section.
- `before`: Begin with the peer review section, then present the main content.
- `alongside`: Integrate the peer review comments throughout the content, marking them clearly as reviewer notes.

## Examples

### Basic peer review of content accuracy

```
+++PeerReview(criteria=accuracy)
Explain the current understanding of dark matter in astrophysics.
```

Provides an explanation of dark matter, followed by a balanced peer review focusing on the accuracy of the information presented

### Critical peer review of multiple aspects, shown alongside content

```
+++PeerReview(criteria=all, style=critical, position=alongside)
Analyze the methodology used in Stanford's prison experiment.
```

Delivers an analysis of the Stanford prison experiment methodology with a parallel critical peer review addressing accuracy, methodology, limitations, and completeness

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** First, generate your response to the query. Then, adopt the role of an academic peer reviewer to evaluate that content. In your review, focus on {criteria} with a {style} approach. Format your response with the review {position} the main content. Clearly label the peer review section.

**Notes:** This model sometimes needs explicit prompting to maintain appropriate critical distance between the content creation and review aspects


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Academic**: Enhances PeerReview Academic style complements PeerReview by maintaining scholarly language throughout both content and review
- **CiteSources**: Enhances PeerReview CiteSources works well with PeerReview to provide academic references that the peer review can evaluate
- **Limitations**: Enhances PeerReview Limitations pairs well with PeerReview when focusing on limitation criteria, offering complementary perspectives
