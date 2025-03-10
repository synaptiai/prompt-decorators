# Prioritize Decorator

Structures the response by ranking information according to importance, urgency, or impact. This decorator helps identify the most critical aspects of a topic and presents information in a hierarchical manner from most to least important.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `criteria` | string | The specific criterion to use for prioritization (e.g., importance, urgency, ROI) | importance |
| `count` | number | Number of prioritized items to include | 5 |
| `showRationale` | boolean | Whether to explain the reasoning behind each priority ranking | False |

## Examples

### Basic prioritization of key factors

```
+++Prioritize
What factors should be considered when designing a mobile app?
```

Presents the top 5 factors for mobile app design, ranked by importance from most to least critical

### Detailed prioritization with custom criteria and rationale

```
+++Prioritize(criteria=ROI, count=7, showRationale=true)
What marketing strategies should our startup focus on?
```

Provides 7 marketing strategies ranked by return on investment, with explanations for each ranking position

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create a prioritized list of the {count} most important items related to this topic, ranked by {criteria}. Number them from 1 to {count}, with 1 being the highest priority. {showRationale} Make sure each item is distinct and clearly relevant to the question.

**Notes:** This model may need explicit reminders to maintain strict ordering throughout the response and to avoid adding unprioritized items after the ranked list


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **MECE**: Enhances Prioritize MECE ensures comprehensive coverage of categories while Prioritize ranks them by importance
- **Alternatives**: Enhances Prioritize Alternatives generates multiple options that Prioritize can then rank according to the specified criteria
- **DecisionMatrix**: Enhances Prioritize DecisionMatrix provides multi-criteria evaluation that can inform and complement the single-criterion ranking of Prioritize
