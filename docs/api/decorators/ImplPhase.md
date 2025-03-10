# ImplPhase Decorator

Indicates which phase of implementation the AI should focus on, controlling scope and detail level.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `stage` | enum | Current implementation phase | core |
| `scope` | enum | Implementation scope boundary | component |
| `iteration` | number | Implementation iteration number | 1 |

## Stage Options

- `design`: Design phase: Create high-level architecture and design patterns without implementation details.
- `scaffold`: Scaffolding phase: Create the basic structure and interfaces without full implementation.
- `core`: Core implementation phase: Implement the essential functionality with basic error handling.
- `refinement`: Refinement phase: Enhance the implementation with better error handling and edge cases.
- `optimization`: Optimization phase: Improve performance, reduce complexity, and enhance efficiency.
- `documentation`: Documentation phase: Add comprehensive comments, documentation, and usage examples.

## Scope Options

- `function`: Limit implementation to a single function or method.
- `component`: Focus on a self-contained component with defined interfaces.
- `module`: Implement a complete module with multiple related components.
- `service`: Develop a service that may interact with multiple modules.
- `system`: Consider the entire system architecture and integration points.

## Examples

### Scaffolding a component

```
+++ImplPhase(stage=scaffold, scope=component, iteration=1)
Create the initial structure for a user authentication component with login/register forms.
```

The AI will focus on creating the basic structure and interfaces for the authentication component without implementing all functionality.

### Core implementation of a function

```
+++ImplPhase(stage=core, scope=function, iteration=2)
Implement a password validation function that checks for minimum length, special characters, and numbers.
```

The AI will implement the essential functionality of the password validation function with basic error handling.

### Documentation for a module

```
+++ImplPhase(stage=documentation, scope=module, iteration=1)
Create documentation for the user management module including all public APIs.
```

The AI will focus on creating comprehensive documentation for the user management module rather than implementing new features.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** You are working on a {scope} in the {stage} phase (iteration #{iteration}). Focus specifically on this phase and don't try to implement features beyond this scope.

**Notes:** More explicit instructions help GPT-3.5 maintain focus on the specific implementation phase.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo, claude-2, llama-2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **CodeStyle**: Enhances ImplPhase CodeStyle can be used alongside ImplPhase to specify coding conventions for the implementation.
- **Language**: Enhances ImplPhase Language decorator can specify the programming language for the implementation.
