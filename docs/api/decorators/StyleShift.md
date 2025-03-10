# StyleShift Decorator

Modifies specific style characteristics of responses such as formality, persuasiveness, or urgency. This decorator enables fine-tuned control over particular aspects of communication style without changing the overall tone.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `aspect` | enum | The specific style aspect to modify | Required |
| `level` | number | The intensity level of the style aspect (1-5, where 1 is minimal and 5 is maximal) | 3 |
| `maintain` | array | Style aspects to explicitly maintain while modifying the target aspect |  |

## Aspect Options

- `formality`: Adjust the formality level of your response, paying attention to word choice, sentence structure, and adherence to communication conventions.
- `persuasion`: Adjust the persuasiveness of your response, focusing on rhetorical techniques, compelling arguments, and call-to-action elements.
- `urgency`: Adjust the sense of urgency in your response, emphasizing time sensitivity, immediate relevance, and priority framing.
- `confidence`: Adjust the level of confidence expressed in your response, through certainty markers, hedging language, and the strength of assertions.
- `complexity`: Adjust the complexity of your response, considering vocabulary, sentence structure, conceptual depth, and assumed background knowledge.

## Examples

### Highly formal style while maintaining normal complexity

```
+++StyleShift(aspect=formality, level=5, maintain=[complexity])
Explain the process of photosynthesis.
```

Provides a highly formal explanation of photosynthesis with elevated language and structure, while keeping the complexity at a moderate level

### Increased urgency for a business communication

```
+++StyleShift(aspect=urgency, level=4)
Describe the steps needed to prepare for the upcoming product launch.
```

Delivers a description of product launch preparation steps with heightened sense of urgency and time-sensitivity in the language and framing

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Adjust the {aspect} of your response to level {level}/5 (where 1 is minimal and 5 is maximal). {maintain} Pay special attention to word choice, sentence structure, and tone that reflects this specific style adjustment. Keep all other aspects of your communication style consistent.

**Notes:** This model may need more explicit examples of the target style aspect at the specified level to maintain consistency throughout the response


## Implementation Guidance

### Highly formal explanation maintaining normal complexity

**Original Prompt:**
```
Explain the process of photosynthesis.
```

**Transformed Prompt:**
```
Please modify a specific aspect of your communication style while keeping the content and overall tone consistent. Adjust the formality level of your response, paying attention to word choice, sentence structure, and adherence to communication conventions. Set the intensity of this style aspect to level 5 (on a scale of 1-5, where 1 is minimal and 5 is maximal). While adjusting the target style aspect, make sure to maintain your current level of these aspects: [complexity].

Explain the process of photosynthesis.
```

### Increased urgency for product launch preparation

**Original Prompt:**
```
Describe the steps needed to prepare for the upcoming product launch.
```

**Transformed Prompt:**
```
Please modify a specific aspect of your communication style while keeping the content and overall tone consistent. Adjust the sense of urgency in your response, emphasizing time sensitivity, immediate relevance, and priority framing. Set the intensity of this style aspect to level 4 (on a scale of 1-5, where 1 is minimal and 5 is maximal).

Describe the steps needed to prepare for the upcoming product launch.
```

## Transformation Details

**Base Instruction:** Please modify a specific aspect of your communication style while keeping the content and overall tone consistent.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `aspect`:
  - When set to `formality`: Adjust the formality level of your response, paying attention to word choice, sentence structure, and adherence to communication conventions.
  - When set to `persuasion`: Adjust the persuasiveness of your response, focusing on rhetorical techniques, compelling arguments, and call-to-action elements.
  - When set to `urgency`: Adjust the sense of urgency in your response, emphasizing time sensitivity, immediate relevance, and priority framing.
  - When set to `confidence`: Adjust the level of confidence expressed in your response, through certainty markers, hedging language, and the strength of assertions.
  - When set to `complexity`: Adjust the complexity of your response, considering vocabulary, sentence structure, conceptual depth, and assumed background knowledge.

- `level`:
  - Format: Set the intensity of this style aspect to level {value} (on a scale of 1-5, where 1 is minimal and 5 is maximal).

- `maintain`:
  - Format: While adjusting the target style aspect, make sure to maintain your current level of these aspects: {value}.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Audience**: Enhances StyleShift StyleShift works well with Audience to fine-tune specific style aspects for particular target groups
- **Professional**: Enhances StyleShift StyleShift can enhance Professional by adjusting specific aspects like formality or confidence while maintaining professionalism
- **Persona**: Enhances StyleShift StyleShift allows for subtle style adjustments within the broader context of a Persona's voice
