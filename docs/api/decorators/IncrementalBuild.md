# IncrementalBuild Decorator

Indicates that the code should be built incrementally, with focus on one feature/component at a time.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `focus` | enum | Current implementation focus | feature |
| `dependencies` | enum | How to handle dependencies | stub |
| `completion` | enum | Expected completion of this increment | functional |

## Focus Options

- `feature`: Focus on implementing a complete feature with all necessary components.
- `component`: Focus on building a specific UI or functional component that can be integrated later.
- `function`: Focus on implementing a specific function or method with well-defined inputs and outputs.
- `integration`: Focus on integrating previously implemented components or features.
- `refactoring`: Focus on improving existing code without changing functionality.

## Dependencies Options

- `mock`: Use mock objects or functions for all dependencies that aren't the focus of this increment.
- `stub`: Create minimal stub implementations for dependencies that return hardcoded values.
- `implement`: Implement all dependencies as part of this increment.
- `import-existing`: Use existing implementations for dependencies where available.

## Completion Options

- `minimal-viable`: Implement only the core functionality needed to demonstrate the concept.
- `functional`: Implement a complete solution that works for the main use cases.
- `robust`: Implement a solution that handles edge cases and includes error handling.
- `production-ready`: Implement a fully tested solution with documentation and optimizations.

## Examples

### Building a component with minimal viable implementation and mocked dependencies

```
+++IncrementalBuild(focus=component, dependencies=mock, completion=minimal-viable)
Implement the user profile card component that displays basic user information and an avatar.
```

The model will implement a minimal viable user profile card component, focusing only on the component itself and using mocks for any dependencies like user data services.

### Implementing a complete feature with robust implementation

```
+++IncrementalBuild(focus=feature, dependencies=implement, completion=robust)
Create a user authentication system with login, registration, and password reset.
```

The model will implement a robust user authentication system, including all necessary components and handling edge cases and error conditions.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Build this code step by step. First focus on {focus} with {completion} level of completeness. For dependencies, use the {dependencies} approach.

**Notes:** Simplified instruction for models with more limited context windows.


## Compatibility

- **Requires**: None
- **Conflicts**: CompleteSystem, MonolithicImplementation
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **TestDriven**: Enhances IncrementalBuild TestDriven works well with IncrementalBuild as tests can be written for each increment.
- **CompleteSystem**: Conflicts with IncrementalBuild CompleteSystem expects a full implementation which conflicts with the incremental approach.
