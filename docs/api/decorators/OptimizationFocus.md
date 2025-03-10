# OptimizationFocus Decorator

Guides targeted optimization efforts with specific constraints and goals.

**Category**: Systematic Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `target` | enum | Optimization target | performance |
| `constraints` | enum | Optimization constraints | no-functional-changes |
| `approach` | enum | Optimization approach | profiling |

## Target Options

- `performance`: Focus on optimizing overall execution speed and responsiveness.
- `memory`: Focus on reducing memory usage and improving memory management.
- `network`: Focus on optimizing network requests, reducing payload sizes, and improving caching strategies.
- `size`: Focus on reducing the overall size of the application or its assets.
- `mobile`: Focus on optimizing specifically for mobile device constraints and capabilities.

## Constraints Options

- `no-visual-changes`: Ensure that no visual changes occur as a result of the optimization.
- `no-functional-changes`: Ensure that the functionality remains identical after optimization.
- `both`: Ensure that neither visual appearance nor functionality changes during optimization.
- `minimal-changes`: Allow minimal changes to appearance or functionality if they significantly improve optimization outcomes.

## Approach Options

- `profiling`: Use profiling tools to identify bottlenecks and optimization opportunities.
- `code-review`: Perform a systematic code review to identify inefficiencies and improvement opportunities.
- `algorithm-improvements`: Focus on improving the underlying algorithms and data structures.
- `resource-management`: Focus on better management of system resources like memory, disk, and network.

## Examples

### Optimizing a web application for performance

```
+++OptimizationFocus(target=performance, constraints=no-functional-changes, approach=profiling)
How can I improve the loading time of my e-commerce website?
```

The model will provide optimization suggestions focused on performance, ensuring functionality doesn't change, using profiling-based approaches.

### Mobile optimization with code review

```
+++OptimizationFocus(target=mobile, constraints=no-visual-changes, approach=code-review)
Review this React Native code for my mobile app.
```

The model will review the code specifically looking for mobile optimization opportunities while preserving the visual design.

### Memory optimization with algorithm improvements

```
+++OptimizationFocus(target=memory, constraints=minimal-changes, approach=algorithm-improvements)
How can I reduce the memory usage of this data processing function?
```

The model will suggest algorithm improvements to reduce memory usage, allowing for minimal changes to functionality if necessary.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** I need you to help optimize an application with these specific requirements:

**Notes:** More direct instruction works better with this model.

### claude-2

**Instruction:** Please analyze the following for optimization opportunities, focusing on the specified target and constraints:

**Notes:** Claude benefits from a more analytical framing.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo, claude-2, llama-2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **CodeReview**: Enhances OptimizationFocus OptimizationFocus can enhance CodeReview by adding specific optimization targets and constraints.
- **PerformanceAnalysis**: Enhances OptimizationFocus Combines well with PerformanceAnalysis for more comprehensive optimization guidance.
