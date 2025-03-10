# Motivational Decorator

Enhances responses with encouraging, inspiring, and empowering language. This decorator is designed to motivate action, build confidence, and create a positive emotional impact while still delivering substantive content.

**Category**: Tone

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `intensity` | `enum` | The level of motivational energy and enthusiasm | `moderate` |
| `focus` | `enum` | The primary motivational approach to emphasize | `balanced` |
| `actionable` | `boolean` | Whether to include specific actionable steps or only inspirational content | `True` |

## Intensity Options

- `mild`: Use a mildly motivational tone with gentle encouragement and moderate positivity, maintaining a balanced and realistic perspective.
- `moderate`: Use a moderately motivational tone with clear encouragement, positive framing, and confidence-building language throughout the response.
- `high`: Use a highly motivational tone with energetic, enthusiastic, and empowering language throughout, creating strong emotional impact and inspiration.

## Focus Options

- `achievement`: Focus your motivational approach on accomplishment, success, and reaching goals, emphasizing concrete results and outcomes.
- `growth`: Focus your motivational approach on learning, development, and continuous improvement, emphasizing progress over perfection.
- `resilience`: Focus your motivational approach on overcoming obstacles, perseverance, and bouncing back from setbacks, emphasizing inner strength.
- `purpose`: Focus your motivational approach on meaning, values, and impact, emphasizing the deeper significance of actions and choices.
- `balanced`: Take a balanced motivational approach that incorporates elements of achievement, growth, resilience, and purpose in appropriate proportions.

## Examples

### Basic moderately motivational response

```
+++Motivational
What are some strategies for building healthy habits?
```

Provides strategies for building healthy habits with moderate motivational language, encouraging tone, and confidence-building framing

### High-intensity resilience-focused motivational content

```
+++Motivational(intensity=high, focus=resilience, actionable=true)
How can I overcome setbacks in my professional life?
```

Delivers highly energetic and inspiring advice for professional resilience, emphasizing overcoming adversity with specific actionable steps, using powerful language and empowering framing

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Use {intensity} motivational language throughout your response. Focus on {focus} as your primary theme. {actionable} Incorporate powerful words, positive framing, and confidence-building phrases. Address challenges honestly but frame them as opportunities for growth. Use second-person perspective ("you can", "your journey") to make it personal and direct.

**Notes:** This model sometimes needs explicit reminders to maintain consistent motivational tone throughout longer responses rather than only at the beginning and end


## Implementation Guidance

### Moderately motivational strategies for building healthy habits

**Original Prompt:**
```
What are some strategies for building healthy habits?
```

**Transformed Prompt:**
```
Please enhance your response with encouraging, inspiring, and empowering language. Use a motivational tone that builds confidence and creates a positive emotional impact while still delivering substantive content. Use a moderately motivational tone with clear encouragement, positive framing, and confidence-building language throughout the response. Take a balanced motivational approach that incorporates elements of achievement, growth, resilience, and purpose in appropriate proportions. Include specific, actionable steps or concrete recommendations that the person can implement, alongside the motivational content.

What are some strategies for building healthy habits?
```

### High-intensity resilience-focused advice for professional setbacks

**Original Prompt:**
```
How can I overcome setbacks in my professional life?
```

**Transformed Prompt:**
```
Please enhance your response with encouraging, inspiring, and empowering language. Use a motivational tone that builds confidence and creates a positive emotional impact while still delivering substantive content. Use a highly motivational tone with energetic, enthusiastic, and empowering language throughout, creating strong emotional impact and inspiration. Focus your motivational approach on overcoming obstacles, perseverance, and bouncing back from setbacks, emphasizing inner strength. Include specific, actionable steps or concrete recommendations that the person can implement, alongside the motivational content.

How can I overcome setbacks in my professional life?
```

## Transformation Details

**Base Instruction:** Please enhance your response with encouraging, inspiring, and empowering language. Use a motivational tone that builds confidence and creates a positive emotional impact while still delivering substantive content.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `intensity`:
  - When set to `mild`: Use a mildly motivational tone with gentle encouragement and moderate positivity, maintaining a balanced and realistic perspective.
  - When set to `moderate`: Use a moderately motivational tone with clear encouragement, positive framing, and confidence-building language throughout the response.
  - When set to `high`: Use a highly motivational tone with energetic, enthusiastic, and empowering language throughout, creating strong emotional impact and inspiration.

- `focus`:
  - When set to `achievement`: Focus your motivational approach on accomplishment, success, and reaching goals, emphasizing concrete results and outcomes.
  - When set to `growth`: Focus your motivational approach on learning, development, and continuous improvement, emphasizing progress over perfection.
  - When set to `resilience`: Focus your motivational approach on overcoming obstacles, perseverance, and bouncing back from setbacks, emphasizing inner strength.
  - When set to `purpose`: Focus your motivational approach on meaning, values, and impact, emphasizing the deeper significance of actions and choices.
  - When set to `balanced`: Take a balanced motivational approach that incorporates elements of achievement, growth, resilience, and purpose in appropriate proportions.

- `actionable`:
  - When set to `true`: Include specific, actionable steps or concrete recommendations that the person can implement, alongside the motivational content.
  - When set to `false`: Focus primarily on inspirational and encouraging content without specific action steps or detailed implementation guidance.

## Compatibility

- **Requires**: None
- **Conflicts**: Academic
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Academic**: Conflicts with Motivational Academic's formal, objective tone conflicts with Motivational's encouraging, emotionally resonant approach
- **Professional**: Enhances Motivational Professional can be enhanced with mild motivational elements while maintaining appropriate business context
- **StepByStep**: Enhances Motivational StepByStep works well with Motivational's actionable parameter to create encouraging yet structured guidance
