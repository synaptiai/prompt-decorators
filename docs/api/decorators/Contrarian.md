# Contrarian Decorator

Generates responses that deliberately challenge conventional wisdom or mainstream perspectives. This decorator encourages critical thinking by presenting counterarguments, alternative interpretations, or challenging established positions on a topic.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `approach` | enum | The specific contrarian approach to take | devils-advocate |
| `maintain` | boolean | Whether to maintain contrarian stance throughout (true) or provide balanced view at the end (false) | False |
| `focus` | string | Optional specific aspect of the topic to focus contrarian analysis on |  |

## Approach Options

- `outsider`: Adopt the perspective of someone completely outside the field or discipline, questioning fundamental assumptions that insiders might take for granted.
- `skeptic`: Take a deeply skeptical stance that questions the evidence, methodology, and logical foundations behind established views.
- `devils-advocate`: Present the strongest possible counterarguments to what would normally be considered the most reasonable position.

## Examples

### Basic devil's advocate approach with balanced conclusion

```
+++Contrarian
Why is renewable energy considered the future of power generation?
```

Challenges conventional thinking about renewable energy's dominance, presenting counterarguments and limitations, followed by a balanced perspective

### Maintained skeptical contrarian stance focused on a specific aspect

```
+++Contrarian(approach=skeptic, maintain=true, focus=methodology)
Discuss the reliability of climate models in predicting future global temperatures.
```

Provides a consistently skeptical analysis of climate model methodologies, questioning assumptions, limitations, and historical accuracy throughout the response

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Challenge the conventional or mainstream view on this topic. Take the role of a {approach} who questions accepted wisdom. Focus particularly on {focus}. Present strong counterarguments and alternative interpretations. {maintain}

**Notes:** This model sometimes needs more explicit instruction to maintain a truly challenging stance rather than reverting to conventional views


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Balanced**: Conflicts with Contrarian Contrarian with maintain=true directly conflicts with Balanced's aim for equal perspective representation
- **Debate**: Enhances Contrarian Debate can work well with Contrarian to present structured arguments for both conventional and contrarian views
- **StepByStep**: Enhances Contrarian StepByStep can help structure the contrarian reasoning in a clear, logical progression
