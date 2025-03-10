# Priority Decorator

A meta-decorator that establishes a precedence hierarchy among multiple decorators. This allows explicit control over which decorator's parameters or behaviors take precedence when conflicts arise, overriding the default last-decorator-wins behavior.

**Category**: Meta

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `decorators` | array | Ordered list of decorators by priority (highest priority first) | Required |
| `explicit` | boolean | Whether to explicitly mention overridden behaviors in the response | False |
| `mode` | enum | How to handle conflicts between decorators | override |

## Mode Options

- `override`: When decorators conflict, completely override lower-priority decorator instructions with those from higher-priority decorators.
- `merge`: When decorators conflict, attempt to merge their instructions by integrating compatible aspects of each.
- `cascade`: When decorators conflict, apply higher-priority decorator instructions first, then apply lower-priority instructions where they don't directly conflict.

## Examples

### Basic priority ordering between potentially conflicting decorators

```
+++Priority(decorators=[Concise,Detailed])
Explain quantum computing.
```

Applies both decorators, but when conflicts arise, Concise takes precedence over Detailed, resulting in a more concise explanation of quantum computing

### Complex priority with explicit conflict resolution

```
+++Priority(decorators=[Academic,Creative,StepByStep], explicit=true, mode=cascade)
Explain the water cycle.
```

Implements a cascading priority where Academic style dominates, with Creative elements where they don't conflict with Academic style, and StepByStep structure throughout, explicitly noting where decorator behaviors were modified due to conflicts

## Model-Specific Implementations

### gpt-4o

**Instruction:** Follow a strict priority order when applying these decorators: {decorators}. When conflicts occur between decorators, resolve them using '{mode}' approach. Focus on implementing each decorator's functionality according to this priority hierarchy.

**Notes:** Even gpt-4o sometimes needs explicit reminders about priority order when multiple decorators have complex interactions


## Implementation Guidance

### Simple priority between conflicting decorators

**Original Prompt:**
```
Explain quantum computing.
```

**Transformed Prompt:**
```
Please apply the following decorators with a specific priority hierarchy to resolve any conflicts between them. Apply these decorators in priority order (highest priority first): Concise, Detailed. When decorators conflict, completely override lower-priority decorator instructions with those from higher-priority decorators. Handle conflicts between decorators without explicitly mentioning the resolution in your response.

Explain quantum computing.
```

### Complex cascading priority with explicit notes

**Original Prompt:**
```
Explain the water cycle.
```

**Transformed Prompt:**
```
Please apply the following decorators with a specific priority hierarchy to resolve any conflicts between them. Apply these decorators in priority order (highest priority first): Academic, Creative, StepByStep. When decorators conflict, apply higher-priority decorator instructions first, then apply lower-priority instructions where they don't directly conflict. When a conflict between decorators occurs, explicitly note in your response which decorator's behavior took precedence.

Explain the water cycle.
```

## Transformation Details

**Base Instruction:** Please apply the following decorators with a specific priority hierarchy to resolve any conflicts between them.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `decorators`:
  - Format: Apply these decorators in priority order (highest priority first): {value}.

- `explicit`:
  - When set to `true`: When a conflict between decorators occurs, explicitly note in your response which decorator's behavior took precedence.
  - When set to `false`: Handle conflicts between decorators without explicitly mentioning the resolution in your response.

- `mode`:
  - When set to `override`: When decorators conflict, completely override lower-priority decorator instructions with those from higher-priority decorators.
  - When set to `merge`: When decorators conflict, attempt to merge their instructions by integrating compatible aspects of each.
  - When set to `cascade`: When decorators conflict, apply higher-priority decorator instructions first, then apply lower-priority instructions where they don't directly conflict.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Conditional**: Enhances Priority Priority complements Conditional by determining which decorators take precedence when conditions are met
- **Override**: Conflicts with Priority Priority and Override both attempt to control decorator behavior conflicts in different ways
