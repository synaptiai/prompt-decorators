# RootCause Decorator

Structures the response to systematically analyze underlying causes of problems or situations. This decorator applies formal root cause analysis methodologies to identify fundamental factors rather than just symptoms or immediate causes.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `method` | enum | The specific root cause analysis methodology to apply | fivewhys |
| `depth` | number | Level of detail in the analysis (for fivewhys, represents number of 'why' iterations) | 5 |

## Method Options

- `fivewhys`: Use the '5 Whys' technique by repeatedly asking why to drill down to the root cause(s). For each identified factor, ask 'why' to go deeper until reaching fundamental causes.
- `fishbone`: Apply the Fishbone (Ishikawa) diagram approach by categorizing potential causes into major categories (e.g., People, Process, Equipment, Environment, Management, Materials) and analyzing each systematically.
- `pareto`: Use the Pareto principle (80/20 rule) to identify and focus on the vital few causes that likely contribute to most of the problem, prioritizing them by impact.

## Examples

### Basic 5 Whys analysis of a business problem

```
+++RootCause
Why is our website's bounce rate increasing?
```

Performs a systematic 5 Whys analysis to trace the increasing bounce rate back to its fundamental causes

### Fishbone diagram approach to a technical issue

```
+++RootCause(method=fishbone)
Why do our application servers crash under moderate load?
```

Analyzes the server crashes using the fishbone (Ishikawa) methodology, categorizing potential causes into major categories like People, Process, Equipment, etc.

### Pareto analysis with deeper investigation

```
+++RootCause(method=pareto, depth=7)
What factors are causing our manufacturing defects?
```

Uses Pareto principle to identify the vital few causes responsible for most manufacturing defects, with an exceptionally thorough analysis

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Perform a systematic root cause analysis using the {method} approach. Don't stop at surface-level causes - keep investigating until you find the fundamental underlying factors. Be methodical and thorough in your analysis.

**Notes:** This model benefits from more explicit instruction about the need to go beyond superficial causes


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **FirstPrinciples**: Enhances RootCause FirstPrinciples complements RootCause by providing a philosophical foundation for the causal analysis
- **StepByStep**: Enhances RootCause StepByStep can help organize the progressive analysis of causes in a clear sequence
