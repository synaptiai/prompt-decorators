# Narrative Decorator

Structures the response as a story-based delivery with narrative elements. This decorator employs storytelling techniques to make information more engaging, memorable, and contextually rich.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `structure` | enum | The narrative structure to employ | classic |
| `characters` | boolean | Whether to include character elements in the narrative | True |
| `length` | enum | The relative length of the narrative | moderate |

## Structure Options

- `classic`: Use a traditional narrative arc with a clear beginning, middle, and end, following a logical progression of setup, conflict/challenge, and resolution.
- `nonlinear`: Use a nonlinear narrative structure that may include flashbacks, flash-forwards, or parallel storylines to present the information from multiple temporal perspectives.
- `case-study`: Structure the response as a real or hypothetical case study that examines specific situations, decisions, and outcomes to illustrate the key points.

## Length Options

- `brief`: Keep the narrative concise and focused, using storytelling elements economically while still conveying the essential information.
- `moderate`: Develop the narrative with sufficient detail to engage the reader while maintaining a balanced pace and moderate length.
- `extended`: Create a fully developed narrative with rich details, multiple story beats, and thorough exploration of the topic through storytelling.

## Examples

### Classic narrative structure to explain a concept

```
+++Narrative
Explain how the stock market works.
```

Explains the stock market through a classic narrative structure, introducing character elements and following a traditional story arc

### Brief case study without character elements

```
+++Narrative(structure=case-study, characters=false, length=brief)
Describe the impact of social media on mental health.
```

Presents a concise case study narrative about social media's impact on mental health, focusing on situations and outcomes without personified characters

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Present this information as a {length} {structure} story. {characters} Use narrative elements like setting, plot development, and thematic threads to explain the concepts. Make the information engaging while ensuring accuracy.

**Notes:** This model sometimes needs reminder to maintain factual accuracy while employing narrative techniques


## Implementation Guidance

### Classic narrative explanation of the stock market

**Original Prompt:**
```
Explain how the stock market works.
```

**Transformed Prompt:**
```
Please structure your response as a story-based delivery that uses narrative elements and storytelling techniques to make the information engaging, memorable, and contextually rich. Use a traditional narrative arc with a clear beginning, middle, and end, following a logical progression of setup, conflict/challenge, and resolution. Include character elements such as personas, stakeholders, or representative individuals that the audience can relate to and follow throughout the narrative. Develop the narrative with sufficient detail to engage the reader while maintaining a balanced pace and moderate length.

Explain how the stock market works.
```

### Brief case study of social media impact without characters

**Original Prompt:**
```
Describe the impact of social media on mental health.
```

**Transformed Prompt:**
```
Please structure your response as a story-based delivery that uses narrative elements and storytelling techniques to make the information engaging, memorable, and contextually rich. Structure the response as a real or hypothetical case study that examines specific situations, decisions, and outcomes to illustrate the key points. Focus on situations, processes, and outcomes without personifying the narrative through specific characters or personas. Keep the narrative concise and focused, using storytelling elements economically while still conveying the essential information.

Describe the impact of social media on mental health.
```

## Transformation Details

**Base Instruction:** Please structure your response as a story-based delivery that uses narrative elements and storytelling techniques to make the information engaging, memorable, and contextually rich.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `structure`:
  - When set to `classic`: Use a traditional narrative arc with a clear beginning, middle, and end, following a logical progression of setup, conflict/challenge, and resolution.
  - When set to `nonlinear`: Use a nonlinear narrative structure that may include flashbacks, flash-forwards, or parallel storylines to present the information from multiple temporal perspectives.
  - When set to `case-study`: Structure the response as a real or hypothetical case study that examines specific situations, decisions, and outcomes to illustrate the key points.

- `characters`:
  - When set to `true`: Include character elements such as personas, stakeholders, or representative individuals that the audience can relate to and follow throughout the narrative.
  - When set to `false`: Focus on situations, processes, and outcomes without personifying the narrative through specific characters or personas.

- `length`:
  - When set to `brief`: Keep the narrative concise and focused, using storytelling elements economically while still conveying the essential information.
  - When set to `moderate`: Develop the narrative with sufficient detail to engage the reader while maintaining a balanced pace and moderate length.
  - When set to `extended`: Create a fully developed narrative with rich details, multiple story beats, and thorough exploration of the topic through storytelling.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Creative**: Enhances Narrative Creative and Narrative work exceptionally well together to produce engaging and imaginative storytelling
- **Academic**: Conflicts with Narrative Academic's formal scholarly conventions may conflict with Narrative's story-based approach, though case studies can bridge this gap
- **Timeline**: Enhances Narrative Timeline can complement Narrative by adding clear chronological structure to story-based explanations
