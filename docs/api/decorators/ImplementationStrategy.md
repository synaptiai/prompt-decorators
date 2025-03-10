# ImplementationStrategy Decorator

Guides the overall approach to implementing a feature or component.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `approach` | enum | Implementation methodology | standard |
| `direction` | enum | Implementation direction | top-down |
| `priority` | enum | Implementation priority | correctness |

## Approach Options

- `tdd`: Use Test-Driven Development (TDD) by writing tests before implementing functionality.
- `bdd`: Apply Behavior-Driven Development (BDD) focusing on business requirements and scenarios.
- `prototype-first`: Create a working prototype before refining the implementation.
- `interface-first`: Define interfaces and contracts before implementing the underlying functionality.
- `standard`: Follow standard development practices with a balanced approach.

## Direction Options

- `top-down`: Start with high-level components and work down to implementation details.
- `bottom-up`: Begin with foundational components and build upward to higher-level functionality.
- `outside-in`: Start with external interfaces and work inward toward core functionality.
- `inside-out`: Begin with core functionality and expand outward to external interfaces.

## Priority Options

- `correctness`: Prioritize correctness and accuracy above all other concerns.
- `clarity`: Focus on code clarity and maintainability as the primary goal.
- `performance`: Optimize for performance as a key consideration throughout development.
- `completeness`: Ensure comprehensive feature coverage before refining implementation.

## Examples

### TDD approach with outside-in direction for user registration

```
+++ImplementationStrategy(approach=tdd, direction=outside-in, priority=correctness)
Implement a user registration system starting with the acceptance tests and working inward to the core functionality.
```

The implementation will follow TDD methodology, starting with external interfaces and working inward, with a focus on correctness.

### Prototype-first approach for a new feature

```
+++ImplementationStrategy(approach=prototype-first, direction=top-down, priority=clarity)
Create a dashboard to visualize user analytics.
```

The implementation will start with a working prototype, using a top-down approach, with code clarity as the main priority.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Follow these implementation guidelines: approach={approach}, direction={direction}, priority={priority}. When implementing this solution, ensure you follow the specified methodology.

**Notes:** Simplified instruction for models with more limited context windows.


## Implementation Guidance

### Web application development

**Original Prompt:**
```
Implement a user registration system.
```

**Transformed Prompt:**
```
When implementing this solution, follow a structured approach that emphasizes methodical development. Use Test-Driven Development (TDD) by writing tests before implementing functionality. Start with external interfaces and work inward toward core functionality. Prioritize correctness and accuracy above all other concerns.

Implement a user registration system.
```

**Notes:** This transformation guides the implementation toward a TDD approach with outside-in direction and correctness as the priority.

## Transformation Details

**Base Instruction:** When implementing this solution, follow a structured approach that emphasizes methodical development.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `approach`:
  - When set to `tdd`: Use Test-Driven Development (TDD) by writing tests before implementing functionality.
  - When set to `bdd`: Apply Behavior-Driven Development (BDD) focusing on business requirements and scenarios.
  - When set to `prototype-first`: Create a working prototype before refining the implementation.
  - When set to `interface-first`: Define interfaces and contracts before implementing the underlying functionality.
  - When set to `standard`: Follow standard development practices with a balanced approach.

- `direction`:
  - When set to `top-down`: Start with high-level components and work down to implementation details.
  - When set to `bottom-up`: Begin with foundational components and build upward to higher-level functionality.
  - When set to `outside-in`: Start with external interfaces and work inward toward core functionality.
  - When set to `inside-out`: Begin with core functionality and expand outward to external interfaces.

- `priority`:
  - When set to `correctness`: Prioritize correctness and accuracy above all other concerns.
  - When set to `clarity`: Focus on code clarity and maintainability as the primary goal.
  - When set to `performance`: Optimize for performance as a key consideration throughout development.
  - When set to `completeness`: Ensure comprehensive feature coverage before refining implementation.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeQuality**: Enhances ImplementationStrategy ImplementationStrategy works well with CodeQuality to ensure both strategic approach and quality standards.
- **ArchitecturalPattern**: Enhances ImplementationStrategy Can be combined with ArchitecturalPattern to provide both high-level architecture and implementation approach.
