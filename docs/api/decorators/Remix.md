# Remix Decorator

Reframes or adapts content for a different context, purpose, or audience than originally intended. This decorator transforms the presentation style while preserving core information, making it accessible and relevant to specific scenarios or demographics.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `target` | string | The specific audience or context to adapt the content for (e.g., 'executives', 'teenagers', 'technical team', 'sales pitch') | Required |
| `preserve` | enum | What aspects of the original content to prioritize preserving | facts |
| `contrast` | boolean | Whether to highlight differences between the original framing and the remixed version | False |

## Preserve Options

- `facts`: Prioritize preserving the accurate factual content while allowing flexibility in presentation style, structure, and level of detail.
- `structure`: Maintain the original organizational structure and flow of ideas while adapting language, examples, and level of detail.
- `tone`: Keep the original tone and voice consistent while adapting other elements like vocabulary, examples, and level of detail.
- `comprehensiveness`: Ensure all key points and details from the original content are included, even while completely adapting the presentation style.

## Examples

### Basic remix for a different audience

```
+++Remix(target=high school students)
Explain how neural networks function in artificial intelligence.
```

Reframes the technical explanation of neural networks to be accessible and engaging for high school students while preserving the core facts

### Business remix with contrasting approach

```
+++Remix(target=board presentation, preserve=comprehensiveness, contrast=true)
Describe the technical details of our new software architecture.
```

Transforms the technical software architecture description into a board-appropriate presentation format, maintaining comprehensive coverage while highlighting how this differs from a technical explanation

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Reimagine this content specifically for {target}. Think about: 1) What this audience already knows, 2) What they care about most, 3) What vocabulary and examples will resonate with them, and 4) How to structure the information for maximum impact. Make sure to {preserve} above all else. {contrast} Use terminology, examples, and a communication style that would feel natural and engaging to this specific audience.

**Notes:** This model may need explicit reminders to maintain the core information while significantly transforming the presentation style


## Implementation Guidance

### Neural networks explanation for high school students

**Original Prompt:**
```
Explain how neural networks function in artificial intelligence.
```

**Transformed Prompt:**
```
Please reframe or adapt this content for a different audience or context than might normally be expected. Transform the presentation style while preserving core information to make it relevant to the specified target audience. Adapt this content specifically for high school students. Consider the background, needs, interests, and communication preferences of this audience when reframing the material. Prioritize preserving the accurate factual content while allowing flexibility in presentation style, structure, and level of detail. Focus solely on the adapted version without explicitly comparing it to how the content might be presented in other contexts.

Explain how neural networks function in artificial intelligence.
```

### Technical software architecture for board presentation

**Original Prompt:**
```
Describe the technical details of our new software architecture.
```

**Transformed Prompt:**
```
Please reframe or adapt this content for a different audience or context than might normally be expected. Transform the presentation style while preserving core information to make it relevant to the specified target audience. Adapt this content specifically for board presentation. Consider the background, needs, interests, and communication preferences of this audience when reframing the material. Ensure all key points and details from the original content are included, even while completely adapting the presentation style. Include an explicit comparison highlighting key differences between how this content would typically be presented versus how it's being adapted for the target audience.

Describe the technical details of our new software architecture.
```

## Transformation Details

**Base Instruction:** Please reframe or adapt this content for a different audience or context than might normally be expected. Transform the presentation style while preserving core information to make it relevant to the specified target audience.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `target`:
  - Format: Adapt this content specifically for {value}. Consider the background, needs, interests, and communication preferences of this audience when reframing the material.

- `preserve`:
  - When set to `facts`: Prioritize preserving the accurate factual content while allowing flexibility in presentation style, structure, and level of detail.
  - When set to `structure`: Maintain the original organizational structure and flow of ideas while adapting language, examples, and level of detail.
  - When set to `tone`: Keep the original tone and voice consistent while adapting other elements like vocabulary, examples, and level of detail.
  - When set to `comprehensiveness`: Ensure all key points and details from the original content are included, even while completely adapting the presentation style.

- `contrast`:
  - When set to `true`: Include an explicit comparison highlighting key differences between how this content would typically be presented versus how it's being adapted for the target audience.
  - When set to `false`: Focus solely on the adapted version without explicitly comparing it to how the content might be presented in other contexts.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Audience**: Enhances Remix Remix provides more transformative adaptation than Audience alone, reframing content rather than just adjusting to audience expertise level
- **ELI5**: Enhances Remix Remix can target specific audiences beyond simplification, while ELI5 focuses exclusively on making content extremely simple
- **StyleShift**: Enhances Remix StyleShift modifies specific style aspects, while Remix performs comprehensive reframing for different contexts
