# NegativeSpace Decorator

Focuses on analyzing what is not explicitly stated, implied, or missing from a topic or question. This decorator explores the 'negative space' by identifying unexplored angles, implicit assumptions, unasked questions, and contextual elements that may have been overlooked.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `focus` | enum | The specific aspect of negative space to emphasize | comprehensive |
| `depth` | enum | How deeply to explore the negative space | moderate |
| `structure` | enum | How to present the negative space analysis | integrated |

## Focus Options

- `implications`: Focus primarily on the unstated implications and logical consequences that may not be immediately obvious.
- `missing`: Focus primarily on identifying missing elements, overlooked factors, and gaps in the topic or question.
- `unstated`: Focus primarily on unstated assumptions, implicit premises, and underlying beliefs that frame the topic.
- `comprehensive`: Take a comprehensive approach to negative space, addressing implications, missing elements, unstated assumptions, and other overlooked aspects.

## Depth Options

- `surface`: Provide a surface-level exploration of the negative space, identifying the most obvious unstated elements without extensive analysis.
- `moderate`: Conduct a moderately deep exploration of the negative space, with substantial attention to important unstated elements and their significance.
- `deep`: Perform a deep examination of the negative space, with thorough exploration of subtle, non-obvious unstated elements and their complex interconnections.

## Structure Options

- `before`: Present the negative space analysis before addressing the explicit content of the topic.
- `after`: First address the explicit content of the topic, then follow with the negative space analysis.
- `integrated`: Integrate the negative space analysis throughout your response, addressing both explicit content and unstated elements in parallel.
- `separate`: Clearly separate the negative space analysis from the explicit content with distinct sections and headings.

## Examples

### Basic comprehensive negative space analysis

```
+++NegativeSpace
Discuss the impact of social media on society.
```

Provides a discussion of social media's societal impact while integrating analysis of unstated assumptions, overlooked factors, and typically unaddressed implications

### Deep negative space analysis focused on missing elements

```
+++NegativeSpace(focus=missing, depth=deep, structure=after)
Explain the current approaches to artificial intelligence safety.
```

First explains current AI safety approaches, then provides a separate deep analysis of missing elements in the discussion, such as unstudied risks, overlooked stakeholders, and neglected scenarios

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** For this topic, I want you to think about what's NOT being said or asked. Consider: 1) Unstated {focus} that aren't directly mentioned, 2) Questions that should be asked but aren't, 3) Assumptions that underlie the topic, and 4) Important context that's missing. Explore this {depth}. {structure} This is about identifying the 'negative space' - what's missing from the picture rather than what's in it.

**Notes:** This model may need explicit reminders to distinguish between negative space analysis and standard critical thinking analysis


## Implementation Guidance

### Comprehensive negative space analysis of social media impact

**Original Prompt:**
```
Discuss the impact of social media on society.
```

**Transformed Prompt:**
```
Please analyze the 'negative space' surrounding this topic - focusing on what is not explicitly stated, implied, or missing. Identify unexplored angles, implicit assumptions, unasked questions, and overlooked contextual elements. Take a comprehensive approach to negative space, addressing implications, missing elements, unstated assumptions, and other overlooked aspects. Conduct a moderately deep exploration of the negative space, with substantial attention to important unstated elements and their significance. Integrate the negative space analysis throughout your response, addressing both explicit content and unstated elements in parallel.

Discuss the impact of social media on society.
```

### Deep analysis of missing elements in AI safety approaches

**Original Prompt:**
```
Explain the current approaches to artificial intelligence safety.
```

**Transformed Prompt:**
```
Please analyze the 'negative space' surrounding this topic - focusing on what is not explicitly stated, implied, or missing. Identify unexplored angles, implicit assumptions, unasked questions, and overlooked contextual elements. Focus primarily on identifying missing elements, overlooked factors, and gaps in the topic or question. Perform a deep examination of the negative space, with thorough exploration of subtle, non-obvious unstated elements and their complex interconnections. First address the explicit content of the topic, then follow with the negative space analysis.

Explain the current approaches to artificial intelligence safety.
```

## Transformation Details

**Base Instruction:** Please analyze the 'negative space' surrounding this topic - focusing on what is not explicitly stated, implied, or missing. Identify unexplored angles, implicit assumptions, unasked questions, and overlooked contextual elements.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `focus`:
  - When set to `implications`: Focus primarily on the unstated implications and logical consequences that may not be immediately obvious.
  - When set to `missing`: Focus primarily on identifying missing elements, overlooked factors, and gaps in the topic or question.
  - When set to `unstated`: Focus primarily on unstated assumptions, implicit premises, and underlying beliefs that frame the topic.
  - When set to `comprehensive`: Take a comprehensive approach to negative space, addressing implications, missing elements, unstated assumptions, and other overlooked aspects.

- `depth`:
  - When set to `surface`: Provide a surface-level exploration of the negative space, identifying the most obvious unstated elements without extensive analysis.
  - When set to `moderate`: Conduct a moderately deep exploration of the negative space, with substantial attention to important unstated elements and their significance.
  - When set to `deep`: Perform a deep examination of the negative space, with thorough exploration of subtle, non-obvious unstated elements and their complex interconnections.

- `structure`:
  - When set to `before`: Present the negative space analysis before addressing the explicit content of the topic.
  - When set to `after`: First address the explicit content of the topic, then follow with the negative space analysis.
  - When set to `integrated`: Integrate the negative space analysis throughout your response, addressing both explicit content and unstated elements in parallel.
  - When set to `separate`: Clearly separate the negative space analysis from the explicit content with distinct sections and headings.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **BlindSpots**: Enhances NegativeSpace NegativeSpace explores what's missing in the topic itself, while BlindSpots identifies cognitive biases in the analysis
- **FindGaps**: Enhances NegativeSpace NegativeSpace examines unstated aspects of a topic, while FindGaps identifies specific missing elements in a plan or proposal
- **Limitations**: Enhances NegativeSpace Limitations focuses on constraints of a described approach, while NegativeSpace identifies what hasn't been addressed at all
