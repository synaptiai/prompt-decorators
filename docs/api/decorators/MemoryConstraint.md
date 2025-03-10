# MemoryConstraint Decorator

Helps manage implementation within AI context window limitations by focusing on specific code portions.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `focus` | `enum` | Part of the code to focus on | `component` |
| `implementation` | `enum` | Implementation completeness | `core-logic` |
| `context` | `enum` | How to handle surrounding code | `summarize` |

## Focus Options

- `single-function`: Focus only on implementing a single function or method.
- `component`: Implement a complete component with its related functions.
- `interface`: Focus on defining the interface or API surface.
- `specific-feature`: Implement a specific feature across relevant functions/components.

## Implementation Options

- `skeleton`: Provide only the structure/skeleton of the implementation with minimal logic.
- `core-logic`: Implement the core logic while omitting edge cases and optimizations.
- `full-implementation`: Provide a complete implementation with error handling and edge cases.
- `with-tests`: Include both implementation and unit tests for the code.

## Context Options

- `ignore`: Ignore any surrounding code context in your implementation.
- `summarize`: Briefly summarize how this implementation fits into the broader codebase.
- `interface-only`: Only reference interfaces or signatures of surrounding code.
- `stub`: Include stub implementations for surrounding code dependencies.

## Examples

### Implementing a single authentication function with full implementation

```
+++MemoryConstraint(focus=single-function, implementation=full-implementation, context=interface-only)
Implement the user authentication function that verifies credentials against our database.
```

A complete implementation of just the authentication function with error handling and edge cases, referencing only the interfaces of surrounding code.

### Creating a component skeleton with stubbed dependencies

```
+++MemoryConstraint(focus=component, implementation=skeleton, context=stub)
Implement a shopping cart component for our e-commerce application.
```

A structural skeleton of the shopping cart component with stubbed implementations of dependencies.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Due to context window limitations, focus specifically on: {focus} with {implementation} level of detail. For surrounding code, {context}.

**Notes:** More explicit instructions needed for models with smaller context windows.


## Implementation Guidance

### Web application development

**Original Prompt:**
```
Implement the user authentication function that verifies credentials against our database.
```

**Transformed Prompt:**
```
Focus only on implementing a single function or method. Provide a complete implementation with error handling and edge cases. Only reference interfaces or signatures of surrounding code.

Implement the user authentication function that verifies credentials against our database.
```

**Notes:** The decorator helps focus the implementation on just the authentication function with complete implementation while only referencing interfaces of surrounding code.

## Transformation Details

**Base Instruction:** Focus on implementing the specified code portion while managing memory constraints. Prioritize clarity and correctness within the scope.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `focus`:
  - When set to `single-function`: Focus only on implementing a single function or method.
  - When set to `component`: Implement a complete component with its related functions.
  - When set to `interface`: Focus on defining the interface or API surface.
  - When set to `specific-feature`: Implement a specific feature across relevant functions/components.

- `implementation`:
  - When set to `skeleton`: Provide only the structure/skeleton of the implementation with minimal logic.
  - When set to `core-logic`: Implement the core logic while omitting edge cases and optimizations.
  - When set to `full-implementation`: Provide a complete implementation with error handling and edge cases.
  - When set to `with-tests`: Include both implementation and unit tests for the code.

- `context`:
  - When set to `ignore`: Ignore any surrounding code context in your implementation.
  - When set to `summarize`: Briefly summarize how this implementation fits into the broader codebase.
  - When set to `interface-only`: Only reference interfaces or signatures of surrounding code.
  - When set to `stub`: Include stub implementations for surrounding code dependencies.

## Compatibility

- **Requires**: None
- **Conflicts**: FullSystemDesign, ComprehensiveImplementation
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeStyle**: Enhances MemoryConstraint Can be combined with CodeStyle to specify both memory constraints and coding style preferences.
- **FullSystemDesign**: Conflicts with MemoryConstraint Conflicts with decorators that request comprehensive system designs as MemoryConstraint deliberately limits scope.
