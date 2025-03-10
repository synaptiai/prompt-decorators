# DecisionMatrix Decorator

Structures the response as a decision matrix, evaluating options against multiple criteria. This decorator facilitates systematic comparison and selection between alternatives based on weighted or unweighted criteria.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `options` | array | Specific options or alternatives to evaluate in the matrix |  |
| `criteria` | array | Evaluation criteria to assess each option against |  |
| `weighted` | boolean | Whether to include weights for criteria importance | False |
| `scale` | enum | Rating scale to use for evaluations | 1-5 |

## Scale Options

- `1-5`: Use a 1-5 rating scale for each criterion (where 1 is poor/lowest and 5 is excellent/highest).
- `1-10`: Use a 1-10 rating scale for each criterion (where 1 is poor/lowest and 10 is excellent/highest).
- `qualitative`: Use qualitative ratings (Poor, Fair, Good, Very Good, Excellent) for each criterion.
- `percentage`: Use percentage scores (0-100%) for rating each criterion.

## Examples

### Simple decision matrix for comparing options

```
+++DecisionMatrix
What smartphone should I buy?
```

Creates a decision matrix comparing top smartphone options against key purchasing criteria, with 1-5 ratings for each combination

### Weighted decision matrix with custom options and criteria

```
+++DecisionMatrix(options=[Python,JavaScript,Go,Rust], criteria=[learning curve,performance,ecosystem,job market], weighted=true, scale=1-10)
Which programming language should I learn next?
```

Generates a weighted decision matrix comparing the specified programming languages against the given criteria, with weighted scores on a 1-10 scale

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create a decision matrix comparing {options} against {criteria}. Rate each option-criterion pair using a {scale} scale. {weighted} Include a brief explanation for each rating, and conclude with a recommendation based on the matrix results.

**Notes:** This model sometimes needs more explicit instructions about formatting the matrix clearly and providing final scores


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **TableFormat**: Enhances DecisionMatrix TableFormat can provide additional formatting options for the decision matrix presentation
- **Comparison**: Enhances DecisionMatrix Comparison works well with DecisionMatrix by providing structure for qualitative comparisons alongside the quantitative matrix
- **OutputFormat**: Enhances DecisionMatrix OutputFormat can be used to specify the format for the matrix (e.g., as markdown or CSV)
