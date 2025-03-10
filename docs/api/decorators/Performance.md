# Performance Decorator

Optimizes system performance focusing on specific bottlenecks.

**Category**: Devops And Infrastructure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `bottleneck` | enum | Performance limitation area | context-dependent |
| `approach` | enum | Performance analysis methodology | comprehensive |
| `constraints` | enum | Optimization constraints | none |

## Bottleneck Options

- `cpu`: Focus on CPU optimization strategies including algorithm efficiency, parallel processing, and computational load balancing.
- `memory`: Focus on memory usage optimization including allocation patterns, garbage collection, caching strategies, and memory leaks.
- `io`: Focus on I/O performance including disk access patterns, buffering strategies, and asynchronous operations.
- `network`: Focus on network performance including latency reduction, bandwidth optimization, and connection management.
- `database`: Focus on database performance including query optimization, indexing strategies, connection pooling, and data access patterns.
- `algorithm`: Focus on algorithmic efficiency including time complexity, space complexity, and algorithm selection.

## Approach Options

- `identify`: Identify the specific performance bottlenecks through profiling and analysis without implementing solutions.
- `measure`: Measure and quantify performance metrics to establish baselines and identify improvement opportunities.
- `optimize`: Implement specific optimization techniques to address known performance issues.
- `comprehensive`: Perform a comprehensive performance analysis including identification, measurement, and optimization recommendations.

## Constraints Options

- `cost`: Optimize within cost constraints, prioritizing solutions with minimal additional resource requirements.
- `time`: Optimize with time constraints in mind, focusing on solutions that can be implemented quickly.
- `complexity`: Optimize while maintaining code simplicity and maintainability.
- `compatibility`: Optimize while ensuring compatibility with existing systems and interfaces.
- `none`: Optimize for maximum performance without specific constraints.

## Examples

### Database performance optimization with compatibility constraints

```
+++Performance(bottleneck=database, approach=comprehensive, constraints=compatibility)
Optimize the performance of our product search functionality which is currently taking 5+ seconds to return results.
```

A comprehensive analysis of database performance issues affecting the product search functionality, with optimization recommendations that maintain compatibility with existing systems.

### CPU performance identification

```
+++Performance(bottleneck=cpu, approach=identify)
Our image processing service is using 100% CPU during peak loads.
```

An analysis identifying specific CPU bottlenecks in the image processing service without implementation details.

### Algorithm optimization with time constraints

```
+++Performance(bottleneck=algorithm, approach=optimize, constraints=time)
Our sorting algorithm needs to be faster for the upcoming release.
```

Specific algorithm optimization recommendations that can be implemented quickly before the upcoming release.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Analyze and improve system performance by identifying and resolving bottlenecks.

**Notes:** Simplified instruction for models with more limited context windows.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances Performance Performance decorator can enhance code review by focusing specifically on performance aspects of the code.
- **Simplify**: Conflicts with Performance Performance optimizations sometimes increase code complexity, which may conflict with simplification goals.
