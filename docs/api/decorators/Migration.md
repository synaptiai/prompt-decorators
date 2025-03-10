# Migration Decorator

Plans migration approaches between system states.

**Category**: Architecture And Design

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `from` | `string` | Current state | `context-dependent` |
| `to` | `string` | Target state | `context-dependent` |
| `approach` | `enum` | Migration strategy | `incremental` |

## Approach Options

- `big-bang`: Use a big-bang migration approach, where the entire system is replaced at once.
- `incremental`: Use an incremental migration approach, where components are migrated one by one over time.
- `strangler-fig`: Use a strangler-fig migration approach, where the new system gradually replaces the old one.
- `parallel-run`: Use a parallel-run migration approach, where both systems operate simultaneously until the migration is complete.

## Examples

### Migration plan for transitioning from monolith to microservices

```
+++Migration(from=monolith, to=microservices, approach=strangler-fig)
Create a migration plan for transitioning our monolithic e-commerce application to microservices.
```

A detailed migration plan using the strangler-fig pattern to gradually transition from a monolithic architecture to microservices.

### Database migration planning

```
+++Migration(from=SQL, to=NoSQL, approach=parallel-run)
How should we migrate our customer data?
```

A migration plan for transitioning from SQL to NoSQL databases using a parallel-run approach, with specific focus on customer data.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a step-by-step migration plan to move from {from} to {to} using the {approach} approach. Include timeline, risks, and resource needs.

**Notes:** Simplified instruction for models with more limited context windows.


## Implementation Guidance

### Software Architecture Planning

**Original Prompt:**
```
Create a migration plan for transitioning our monolithic e-commerce application to microservices.
```

**Transformed Prompt:**
```
Create a detailed migration plan that addresses the transition from the current state to the target state. Include key considerations, risks, timeline estimates, and resource requirements. The current state is: monolith. The target state is: microservices. Use a strangler-fig migration approach, where the new system gradually replaces the old one.

Create a migration plan for transitioning our monolithic e-commerce application to microservices.
```

**Notes:** The decorator adds specific migration context and approach guidance to the original prompt.

## Transformation Details

**Base Instruction:** Create a detailed migration plan that addresses the transition from the current state to the target state. Include key considerations, risks, timeline estimates, and resource requirements.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `from`:
  - Format: The current state is: {value}.

- `to`:
  - Format: The target state is: {value}.

- `approach`:
  - When set to `big-bang`: Use a big-bang migration approach, where the entire system is replaced at once.
  - When set to `incremental`: Use an incremental migration approach, where components are migrated one by one over time.
  - When set to `strangler-fig`: Use a strangler-fig migration approach, where the new system gradually replaces the old one.
  - When set to `parallel-run`: Use a parallel-run migration approach, where both systems operate simultaneously until the migration is complete.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **SystemDesign**: Enhances Migration Migration works well with SystemDesign as it provides context for the migration planning.
- **RiskAnalysis**: Enhances Migration RiskAnalysis can be used to further elaborate on the risks associated with the migration.
