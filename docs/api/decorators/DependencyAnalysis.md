# DependencyAnalysis Decorator

Focuses on analyzing dependencies and their impacts on a system or component.

**Category**: Systematic Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `type` | `enum` | Dependency type | `all` |
| `direction` | `enum` | Dependency direction | `both` |
| `detail` | `enum` | Analysis detail | `detailed` |

## Type Options

- `code`: Focus on code-level dependencies such as imports, libraries, and modules.
- `data`: Focus on data dependencies such as database relationships, data flows, and storage requirements.
- `service`: Focus on service dependencies such as API calls, microservices, and external integrations.
- `all`: Analyze all types of dependencies including code, data, and service relationships.

## Direction Options

- `inbound`: Examine what depends on this component (inbound dependencies).
- `outbound`: Examine what this component depends on (outbound dependencies).
- `both`: Examine both inbound and outbound dependencies for a complete picture.

## Detail Options

- `summary`: Provide a high-level summary of key dependencies.
- `detailed`: Provide a detailed analysis of dependencies with specific examples.
- `comprehensive`: Provide an exhaustive analysis of all dependencies with technical details.
- `impact-focused`: Focus on how dependencies affect system stability, performance, and change management.

## Examples

### Analyzing code dependencies of a component

```
+++DependencyAnalysis(type=code, direction=outbound, detail=detailed)
Analyze the authentication module to understand what libraries and frameworks it depends on.
```

Provides a detailed analysis of external libraries, frameworks, and other code components that the authentication module depends on.

### Impact-focused analysis of all dependencies

```
+++DependencyAnalysis(type=all, direction=both, detail=impact-focused)
Analyze all dependencies of the user profile component to understand what might be affected by our planned changes.
```

Delivers an analysis focused on how changes to the user profile component might impact other systems and how changes in dependent systems might affect it.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Analyze dependencies between components. Identify what depends on what and how changes might affect the system.

**Notes:** Simplified instruction for models with less context capacity.


## Implementation Guidance

### Software architecture analysis

**Original Prompt:**
```
Analyze the user profile component in our application.
```

**Transformed Prompt:**
```
Analyze the dependencies in the system or component described. Identify relationships and potential impacts of changes. Analyze all types of dependencies including code, data, and service relationships. Examine both inbound and outbound dependencies for a complete picture. Provide a detailed analysis of dependencies with specific examples.

Analyze the user profile component in our application.
```

**Notes:** The decorator adds specific instructions for dependency analysis before the original prompt.

## Transformation Details

**Base Instruction:** Analyze the dependencies in the system or component described. Identify relationships and potential impacts of changes.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `type`:
  - When set to `code`: Focus on code-level dependencies such as imports, libraries, and modules.
  - When set to `data`: Focus on data dependencies such as database relationships, data flows, and storage requirements.
  - When set to `service`: Focus on service dependencies such as API calls, microservices, and external integrations.
  - When set to `all`: Analyze all types of dependencies including code, data, and service relationships.

- `direction`:
  - When set to `inbound`: Examine what depends on this component (inbound dependencies).
  - When set to `outbound`: Examine what this component depends on (outbound dependencies).
  - When set to `both`: Examine both inbound and outbound dependencies for a complete picture.

- `detail`:
  - When set to `summary`: Provide a high-level summary of key dependencies.
  - When set to `detailed`: Provide a detailed analysis of dependencies with specific examples.
  - When set to `comprehensive`: Provide an exhaustive analysis of all dependencies with technical details.
  - When set to `impact-focused`: Focus on how dependencies affect system stability, performance, and change management.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **SystematicDebugging**: Enhances DependencyAnalysis DependencyAnalysis works well with SystematicDebugging by providing deeper insights into component relationships.
- **CodeReview**: Enhances DependencyAnalysis Can be combined with CodeReview to focus on dependency-related issues in code.
