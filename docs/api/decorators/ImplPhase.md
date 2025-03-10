# ImplPhase Decorator

Indicates which phase of implementation the AI should focus on, controlling scope and detail level.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `stage` | `enum` | Current implementation phase | `core` |
| `scope` | `enum` | Implementation scope boundary | `component` |
| `iteration` | `number` | Implementation iteration number | `1` |

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

### gpt-4-turbo

**Instruction:** You are working on a {scope} in the {stage} phase (iteration #{iteration}). Focus specifically on this phase and don't try to implement features beyond this scope.

**Notes:** More explicit instructions help gpt-4 maintain focus on the specific implementation phase.


## Implementation Guidance

### Web development

**Original Prompt:**
```
Create a user authentication component with login/register forms.
```

**Transformed Prompt:**
```
Focus on the scaffold phase of implementation for this component, iteration #1.

Scaffolding phase: Create the basic structure and interfaces without full implementation.
Focus on a self-contained component with defined interfaces.
This is iteration #1 of the implementation process.

Create a user authentication component with login/register forms.
```

**Notes:** The transformed prompt guides the AI to focus on creating the basic structure without full implementation details.

## Transformation Details

**Base Instruction:** Focus on the {stage} phase of implementation for this {scope}, iteration #{iteration}.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `stage`:
  - When set to `design`: Design phase: Create high-level architecture and design patterns without implementation details.
  - When set to `scaffold`: Scaffolding phase: Create the basic structure and interfaces without full implementation.
  - When set to `core`: Core implementation phase: Implement the essential functionality with basic error handling.
  - When set to `refinement`: Refinement phase: Enhance the implementation with better error handling and edge cases.
  - When set to `optimization`: Optimization phase: Improve performance, reduce complexity, and enhance efficiency.
  - When set to `documentation`: Documentation phase: Add comprehensive comments, documentation, and usage examples.

- `scope`:
  - When set to `function`: Limit implementation to a single function or method.
  - When set to `component`: Focus on a self-contained component with defined interfaces.
  - When set to `module`: Implement a complete module with multiple related components.
  - When set to `service`: Develop a service that may interact with multiple modules.
  - When set to `system`: Consider the entire system architecture and integration points.

- `iteration`:
  - Format: This is iteration #{value} of the implementation process.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **CodeStyle**: Enhances ImplPhase CodeStyle can be used alongside ImplPhase to specify coding conventions for the implementation.
- **Language**: Enhances ImplPhase Language decorator can specify the programming language for the implementation.
