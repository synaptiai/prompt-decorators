# ExtendCode Decorator

Requests extending or enhancing existing code with new functionality without complete rewrites.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `approach` | enum | How to extend the code | add-feature |
| `impact` | enum | Level of changes to existing code | minimal |
| `maintain` | enum | Aspects to maintain | all |

## Approach Options

- `add-function`: Add a new standalone function that implements the requested functionality.
- `add-method`: Add a new method to an existing class or object that implements the requested functionality.
- `add-feature`: Implement a new feature by extending the existing code structure.
- `enhance-existing`: Enhance existing functionality without adding new functions or methods.

## Impact Options

- `none`: Make no changes to existing code, only add new code.
- `minimal`: Make minimal changes to existing code, focusing on additions rather than modifications.
- `moderate`: Make moderate changes to existing code where necessary to support the new functionality.
- `significant`: Make significant changes to existing code if needed to properly implement the requested functionality.

## Maintain Options

- `api`: Maintain the existing API contracts and interfaces.
- `architecture`: Maintain the existing architectural patterns and structure.
- `naming`: Maintain the existing naming conventions and style.
- `performance`: Maintain the existing performance characteristics.
- `all`: Maintain all aspects of the existing code including API, architecture, naming conventions, and performance characteristics.

## Examples

### Adding a method to a user service class

```
+++ExtendCode(approach=add-method, impact=minimal, maintain=all)
Add a method to this user service class that allows retrieving users by email domain.
```

Adds a new method to the user service class that follows existing patterns and naming conventions, with minimal changes to existing code.

### Adding a new feature with moderate changes

```
+++ExtendCode(approach=add-feature, impact=moderate, maintain=architecture)
Add pagination support to this API endpoint.
```

Implements pagination by extending the existing code with moderate changes while maintaining the architectural patterns.

### Enhancing existing functionality

```
+++ExtendCode(approach=enhance-existing, impact=minimal, maintain=performance)
Improve the error handling in this function.
```

Enhances the error handling with minimal changes while ensuring performance is not degraded.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Add new functionality to the existing code without rewriting it. Follow the existing code style and patterns. For approach={approach}, impact={impact}, maintain={maintain}.

**Notes:** Simpler instruction format works better with GPT-3.5 Turbo's context window limitations.


## Implementation Guidance

### Adding a method to a user service class

**Original Prompt:**
```
Add a method to this user service class that allows retrieving users by email domain.
```

**Transformed Prompt:**
```
Extend the existing code with new functionality. Focus on adding to the codebase rather than rewriting it. Add a new method to an existing class or object that implements the requested functionality. Make minimal changes to existing code, focusing on additions rather than modifications. Maintain all aspects of the existing code including API, architecture, naming conventions, and performance characteristics.

Add a method to this user service class that allows retrieving users by email domain.
```

**Notes:** The decorator prepends instructions to maintain code style and minimize changes while adding the requested functionality.

## Transformation Details

**Base Instruction:** Extend the existing code with new functionality. Focus on adding to the codebase rather than rewriting it.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `approach`:
  - When set to `add-function`: Add a new standalone function that implements the requested functionality.
  - When set to `add-method`: Add a new method to an existing class or object that implements the requested functionality.
  - When set to `add-feature`: Implement a new feature by extending the existing code structure.
  - When set to `enhance-existing`: Enhance existing functionality without adding new functions or methods.

- `impact`:
  - When set to `none`: Make no changes to existing code, only add new code.
  - When set to `minimal`: Make minimal changes to existing code, focusing on additions rather than modifications.
  - When set to `moderate`: Make moderate changes to existing code where necessary to support the new functionality.
  - When set to `significant`: Make significant changes to existing code if needed to properly implement the requested functionality.

- `maintain`:
  - When set to `api`: Maintain the existing API contracts and interfaces.
  - When set to `architecture`: Maintain the existing architectural patterns and structure.
  - When set to `naming`: Maintain the existing naming conventions and style.
  - When set to `performance`: Maintain the existing performance characteristics.
  - When set to `all`: Maintain all aspects of the existing code including API, architecture, naming conventions, and performance characteristics.

## Compatibility

- **Requires**: None
- **Conflicts**: Refactor, RewriteCode
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, claude-instant
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances ExtendCode ExtendCode works well with CodeReview, which can be used to validate that the extensions maintain the specified aspects.
- **Refactor**: Conflicts with ExtendCode ExtendCode focuses on adding functionality with minimal changes, while Refactor focuses on restructuring existing code.
