# Limitations Decorator

Adds an explicit statement of limitations, caveats, or uncertainties related to the provided information. This decorator promotes intellectual honesty by acknowledging the boundaries of current knowledge, potential biases, or contextual constraints.

**Category**: Verification

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `detail` | enum | The level of detail in the limitations statement | moderate |
| `position` | enum | Where to place the limitations statement in the response | end |
| `focus` | enum | The primary aspect to focus on in the limitations | all |

## Detail Options

- `brief`: Add a concise, focused statement highlighting only the most critical limitations.
- `moderate`: Provide a balanced discussion of several important limitations with some supporting context.
- `comprehensive`: Include a thorough examination of all significant limitations with detailed explanations and implications.

## Position Options

- `beginning`: Place the limitations statement at the beginning of your response, before presenting the main information.
- `end`: Place the limitations statement at the end of your response, after presenting the main information.

## Focus Options

- `knowledge`: Focus primarily on limitations related to the current state of knowledge or understanding in this field.
- `methodology`: Focus primarily on limitations in the methodology, research approaches, or analytical techniques used in this area.
- `context`: Focus primarily on contextual limitations such as time period, geographical scope, or situational constraints.
- `biases`: Focus primarily on potential biases, including research biases, sampling biases, or perspective biases.
- `all`: Address a balanced mix of limitations across knowledge gaps, methodological issues, contextual constraints, and potential biases.

## Examples

### Brief limitations statement at the end focused on methodology

```
+++Limitations(detail=brief, focus=methodology)
Explain how personality tests predict career success.
```

Explains personality tests and career success, concluding with a brief statement of methodological limitations

### Comprehensive limitations at the beginning covering all aspects

```
+++Limitations(detail=comprehensive, position=beginning, focus=all)
Describe the current understanding of consciousness.
```

Begins with a thorough discussion of the limitations in our understanding of consciousness before presenting the current state of knowledge

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Your response must include a clear section on the limitations of the information you're providing. Be honest about what isn't fully understood, potential issues with methodologies, and other important caveats. {position} Make the limitations {detail} and focus on {focus}.

**Notes:** This model sometimes needs explicit prompting to acknowledge limitations, especially in domains where it has high confidence


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **FactCheck**: Enhances Limitations FactCheck and Limitations work well together to provide both factual accuracy and transparent acknowledgment of knowledge boundaries
- **Confidence**: Enhances Limitations Confidence ratings complement Limitations by quantifying uncertainty where Limitations describes it qualitatively
