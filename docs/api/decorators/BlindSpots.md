# BlindSpots Decorator

Identifies potential cognitive blind spots, unstated assumptions, and overlooked perspectives in the response. This decorator helps mitigate bias by explicitly acknowledging the limitations of one's thinking and analysis.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `categories` | array | Specific categories of blind spots to check for (e.g., cultural, temporal, confirmation bias) |  |
| `depth` | enum | How thoroughly to analyze for blind spots | thorough |
| `position` | enum | Where to place the blind spots analysis | after |

## Depth Options

- `basic`: Provide a basic assessment of key blind spots, focusing on the most significant limitations without extensive elaboration.
- `thorough`: Conduct a thorough analysis of blind spots, with substantial attention to underlying assumptions and alternative perspectives.
- `comprehensive`: Perform a comprehensive examination of blind spots, including detailed exploration of subtle biases, edge cases, and interconnected limitations.

## Position Options

- `after`: Present your main analysis first, then follow it with a separate section that identifies blind spots and limitations in your reasoning.
- `before`: Begin with an acknowledgment of potential blind spots and limitations that might affect your analysis, then proceed with your main response.
- `integrated`: Integrate the identification of blind spots throughout your analysis, pointing out limitations and alternative perspectives as they become relevant to each aspect of the topic.

## Examples

### Basic blind spots analysis after a response

```
+++BlindSpots
What factors drive economic growth?
```

Provides an analysis of economic growth factors, followed by identification of unstated assumptions and potential blind spots in the analysis

### Comprehensive blind spots analysis integrated throughout

```
+++BlindSpots(categories=[cultural,historical,methodological], depth=comprehensive, position=integrated)
Evaluate the impact of social media on society.
```

Delivers an evaluation of social media's societal impact with comprehensive blind spot analysis woven throughout, specifically addressing cultural, historical, and methodological blind spots

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** When analyzing this topic, be vigilant about identifying {depth} blind spots such as {categories}. Consider what assumptions you're making, what perspectives might be missing, and what biases could be influencing your thinking. {position} Challenge your own conclusions and consider alternative viewpoints that might contradict your initial analysis.

**Notes:** This model sometimes needs explicit prompting to avoid defaulting to surface-level blind spot analysis that merely acknowledges limitations without substantive exploration


## Implementation Guidance

### Basic blind spots analysis after economic growth factors

**Original Prompt:**
```
What factors drive economic growth?
```

**Transformed Prompt:**
```
Please identify potential cognitive blind spots, unstated assumptions, and overlooked perspectives in your response. Explicitly acknowledge the limitations and biases that might affect your analysis of the topic. Conduct a thorough analysis of blind spots, with substantial attention to underlying assumptions and alternative perspectives. Present your main analysis first, then follow it with a separate section that identifies blind spots and limitations in your reasoning.

What factors drive economic growth?
```

### Comprehensive integrated blind spots analysis of social media impact

**Original Prompt:**
```
Evaluate the impact of social media on society.
```

**Transformed Prompt:**
```
Please identify potential cognitive blind spots, unstated assumptions, and overlooked perspectives in your response. Explicitly acknowledge the limitations and biases that might affect your analysis of the topic. Focus specifically on identifying these categories of blind spots: [cultural,historical,methodological]. For each category, explain how it might influence the analysis. Perform a comprehensive examination of blind spots, including detailed exploration of subtle biases, edge cases, and interconnected limitations. Integrate the identification of blind spots throughout your analysis, pointing out limitations and alternative perspectives as they become relevant to each aspect of the topic.

Evaluate the impact of social media on society.
```

## Transformation Details

**Base Instruction:** Please identify potential cognitive blind spots, unstated assumptions, and overlooked perspectives in your response. Explicitly acknowledge the limitations and biases that might affect your analysis of the topic.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `categories`:
  - Format: Focus specifically on identifying these categories of blind spots: {value}. For each category, explain how it might influence the analysis.

- `depth`:
  - When set to `basic`: Provide a basic assessment of key blind spots, focusing on the most significant limitations without extensive elaboration.
  - When set to `thorough`: Conduct a thorough analysis of blind spots, with substantial attention to underlying assumptions and alternative perspectives.
  - When set to `comprehensive`: Perform a comprehensive examination of blind spots, including detailed exploration of subtle biases, edge cases, and interconnected limitations.

- `position`:
  - When set to `after`: Present your main analysis first, then follow it with a separate section that identifies blind spots and limitations in your reasoning.
  - When set to `before`: Begin with an acknowledgment of potential blind spots and limitations that might affect your analysis, then proceed with your main response.
  - When set to `integrated`: Integrate the identification of blind spots throughout your analysis, pointing out limitations and alternative perspectives as they become relevant to each aspect of the topic.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Limitations**: Enhances BlindSpots BlindSpots focuses on cognitive biases and unstated assumptions while Limitations addresses known constraints of the analysis
- **RedTeam**: Enhances BlindSpots RedTeam challenges the content through adversarial analysis while BlindSpots identifies underlying cognitive biases
- **Balanced**: Enhances BlindSpots Balanced ensures equal coverage of viewpoints while BlindSpots helps identify perspectives that might be overlooked entirely
