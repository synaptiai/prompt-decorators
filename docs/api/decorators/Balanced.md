# Balanced Decorator

Ensures equal representation of different perspectives or viewpoints on a topic. This decorator promotes fairness and comprehensiveness by giving proportional attention to multiple sides of an issue, avoiding bias toward any particular position.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `perspectives` | number | Number of different perspectives to include | 2 |
| `structure` | enum | How to structure the different perspectives | sequential |
| `equal` | boolean | Whether to strictly enforce equal word count for each perspective | True |

## Structure Options

- `alternating`: Present the different perspectives in an alternating point-by-point format, addressing the same aspects from each viewpoint before moving to the next aspect.
- `sequential`: Present each perspective fully and separately in sequence, with clear sections for each viewpoint.
- `comparative`: Present the perspectives in a side-by-side comparative analysis, highlighting agreements and differences across specific dimensions.

## Examples

### Basic balanced view of a controversial topic

```
+++Balanced
Discuss the pros and cons of nuclear energy.
```

Presents the benefits and drawbacks of nuclear energy with equal attention and detail given to both perspectives

### Balanced presentation of multiple perspectives in comparative structure

```
+++Balanced(perspectives=4, structure=comparative, equal=true)
What are the different views on artificial intelligence regulation?
```

Provides a balanced side-by-side comparison of four different perspectives on AI regulation, with equal word count allocated to each viewpoint

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Present multiple perspectives on this topic, giving equal attention to each viewpoint. Avoid showing bias toward any particular position. Make sure to address the strongest arguments from each perspective.

**Notes:** This model may need more explicit reminders about maintaining balance throughout the response


## Implementation Guidance

### Basic balanced view with two perspectives

**Original Prompt:**
```
Discuss the pros and cons of nuclear energy.
```

**Transformed Prompt:**
```
Please ensure your response presents a balanced view with equal representation of different perspectives on the topic. Include 2 different perspectives or viewpoints on this topic. Present each perspective fully and separately in sequence, with clear sections for each viewpoint. Ensure that each perspective receives equal attention, detail, and word count in your response.

Discuss the pros and cons of nuclear energy.
```

### Comparative analysis of multiple perspectives

**Original Prompt:**
```
What are the different views on artificial intelligence regulation?
```

**Transformed Prompt:**
```
Please ensure your response presents a balanced view with equal representation of different perspectives on the topic. Include 4 different perspectives or viewpoints on this topic. Present the perspectives in a side-by-side comparative analysis, highlighting agreements and differences across specific dimensions. Ensure that each perspective receives equal attention, detail, and word count in your response.

What are the different views on artificial intelligence regulation?
```

## Transformation Details

**Base Instruction:** Please ensure your response presents a balanced view with equal representation of different perspectives on the topic.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `perspectives`:
  - Format: Include {value} different perspectives or viewpoints on this topic.

- `structure`:
  - When set to `alternating`: Present the different perspectives in an alternating point-by-point format, addressing the same aspects from each viewpoint before moving to the next aspect.
  - When set to `sequential`: Present each perspective fully and separately in sequence, with clear sections for each viewpoint.
  - When set to `comparative`: Present the perspectives in a side-by-side comparative analysis, highlighting agreements and differences across specific dimensions.

- `equal`:
  - When set to `true`: Ensure that each perspective receives equal attention, detail, and word count in your response.
  - When set to `false`: Each perspective should be adequately represented, but strict equality in length is not required.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Debate**: Enhances Balanced Balanced pairs well with Debate to ensure fair representation in dialectical formats
- **Steelman**: Enhances Balanced Balanced ensures equal representation while Steelman strengthens the quality of each perspective
