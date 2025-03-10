# MECE Decorator

Structures the response using the Mutually Exclusive, Collectively Exhaustive framework - a principle where categories have no overlaps and cover all possibilities. This decorator ensures comprehensive analysis with clear categorization for decision-making and problem-solving.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `dimensions` | number | Number of top-level MECE dimensions to use for categorization | 3 |
| `depth` | number | Maximum level of hierarchical breakdown within each dimension | 2 |
| `framework` | enum | Optional predefined MECE framework to apply | custom |

## Framework Options

- `issue tree`: Use an issue tree framework to break down the topic into a hierarchy of questions and sub-questions, ensuring comprehensive coverage of all relevant issues.
- `value chain`: Apply a value chain framework to analyze the topic across all activities that add value, from inputs to final outputs/outcomes.
- `business segments`: Categorize the analysis using business segments such as products/services, customer segments, geographical regions, and operational functions.
- `stakeholders`: Structure the analysis around all relevant stakeholders, ensuring every entity affected by or influencing the topic is considered.
- `custom`: Develop a custom MECE framework tailored specifically to this topic, with categories that best fit the subject matter.

## Examples

### Basic MECE analysis of a business problem

```
+++MECE
What factors should we consider when expanding to a new market?
```

Organizes market expansion factors into 3 mutually exclusive, collectively exhaustive categories with no overlaps and full coverage of all considerations

### Detailed MECE framework with stakeholder focus

```
+++MECE(dimensions=4, depth=3, framework=stakeholders)
Analyze the implications of implementing a four-day work week.
```

Provides a 4-dimension MECE analysis of a four-day work week using a stakeholder framework, with up to 3 levels of hierarchical breakdown within each stakeholder category

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create a MECE (Mutually Exclusive, Collectively Exhaustive) analysis with {dimensions} main categories that don't overlap and together cover everything about this topic. Use the {framework} approach. For each main category, break it down into {depth} levels of sub-categories. Make sure there are no gaps in your analysis and no overlaps between categories.

**Notes:** This model sometimes struggles with maintaining true MECE principles and may need explicit reminders to check for category overlaps or gaps


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Prioritize**: Enhances MECE MECE provides comprehensive categorization, while Prioritize helps rank the identified categories by importance
- **Structured**: Enhances MECE MECE and Structured work well together to create clearly organized and comprehensive content
- **FindGaps**: Enhances MECE FindGaps can help verify the 'collectively exhaustive' aspect of a MECE analysis by identifying any missing categories
