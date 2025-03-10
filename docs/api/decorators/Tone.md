# Tone Decorator

Adjusts the writing style and tone of the AI's response. This decorator helps ensure that responses are appropriately styled for different audiences and contexts, from formal technical documentation to casual explanations.

**Category**: Minimal

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `style` | `enum` | The desired tone and style for the response | `formal` |

## Style Options

- `formal`: Use a formal, professional tone with proper terminology and minimal contractions. Maintain a structured approach with clear organization.
- `casual`: Use a casual, conversational tone as if speaking to a friend. Feel free to use contractions and a more relaxed writing style.
- `friendly`: Use a warm, approachable tone that builds rapport. Be encouraging and personable while still being informative.
- `technical`: Use precise technical language and terminology appropriate for a knowledgeable audience. Include specific details and technical concepts.
- `humorous`: Incorporate appropriate humor and a light-hearted tone in your response, while still providing accurate information.

## Examples

### Technical documentation tone

```
+++Tone(style=technical)
Explain how garbage collection works in Python
```

Provides a technically precise explanation using appropriate terminology

### Casual explanation

```
+++Tone(style=casual)
Why is the sky blue?
```

Delivers a relaxed, conversational explanation of atmospheric optics

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Please write your response in the following tone and style:

**Notes:** This model benefits from more direct tone instructions


## Implementation Guidance

### Technical style

**Original Prompt:**
```
Explain how cloud computing works.
```

**Transformed Prompt:**
```
Please adjust your writing style and tone for this response. Use precise technical language and terminology appropriate for a knowledgeable audience. Include specific details and technical concepts.

Explain how cloud computing works.
```

### Casual style

**Original Prompt:**
```
Why do leaves change color in autumn?
```

**Transformed Prompt:**
```
Please adjust your writing style and tone for this response. Use a casual, conversational tone as if speaking to a friend. Feel free to use contractions and a more relaxed writing style.

Why do leaves change color in autumn?
```

## Transformation Details

**Base Instruction:** Please adjust your writing style and tone for this response.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `style`:
  - When set to `formal`: Use a formal, professional tone with proper terminology and minimal contractions. Maintain a structured approach with clear organization.
  - When set to `casual`: Use a casual, conversational tone as if speaking to a friend. Feel free to use contractions and a more relaxed writing style.
  - When set to `friendly`: Use a warm, approachable tone that builds rapport. Be encouraging and personable while still being informative.
  - When set to `technical`: Use precise technical language and terminology appropriate for a knowledgeable audience. Include specific details and technical concepts.
  - When set to `humorous`: Incorporate appropriate humor and a light-hearted tone in your response, while still providing accurate information.

## Compatibility

- **Requires**: None
- **Conflicts**: ELI5
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ELI5**: Conflicts with Tone ELI5 requires a specific tone that may contradict certain tone settings
- **Academic**: Conflicts with Tone The Academic decorator enforces a scholarly tone that may conflict with casual or humorous tones
