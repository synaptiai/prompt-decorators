# TechDebtControl Decorator

Guides how technical debt should be handled during implementation.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `accept` | enum | Level of acceptable technical debt | minimal |
| `document` | enum | How tech debt should be documented | todos |
| `tradeoff` | enum | What can be traded for quality | elegance |

## Accept Options

- `none`: Do not introduce any technical debt. Implement a complete, high-quality solution even if it takes longer.
- `minimal`: Minimize technical debt. Only accept small compromises that can be easily addressed later.
- `moderate`: Accept a moderate amount of technical debt where necessary to meet deadlines, but keep it manageable.
- `pragmatic`: Prioritize shipping working code. Technical debt is acceptable if it helps meet immediate business needs.

## Document Options

- `none`: No documentation of technical debt is required.
- `comments`: Document technical debt with inline code comments where compromises were made.
- `todos`: Use TODO comments to mark areas of technical debt that need future improvement.
- `issues`: Create formal issue tickets for each piece of technical debt introduced.
- `comprehensive`: Provide comprehensive documentation including inline comments, TODOs, and a separate technical debt register with prioritization.

## Tradeoff Options

- `nothing`: Do not trade off any aspect of quality.
- `completeness`: It's acceptable to implement a partial solution now and complete it later.
- `performance`: Optimize for correctness first; performance optimizations can come later.
- `elegance`: Focus on functional correctness over code elegance or perfect architecture.

## Examples

### Pragmatic approach for a demo feature

```
+++TechDebtControl(accept=pragmatic, document=todos, tradeoff=elegance)
Implement a quick solution for the file upload feature we need for the demo next week. Note areas that will need improvement.
```

The model will implement a functional file upload solution prioritizing speed over perfection, using TODO comments to mark areas needing improvement, and focusing on functionality over elegant code.

### High-quality implementation for critical component

```
+++TechDebtControl(accept=none, document=comprehensive, tradeoff=nothing)
Implement the authentication system for our banking application.
```

The model will create a complete, high-quality authentication system with no technical debt, comprehensive documentation, and no quality trade-offs.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** For this implementation, follow these technical debt guidelines: {accept} {document} {tradeoff}

**Notes:** Simplified format works better with gpt-4's context handling.


## Implementation Guidance

### Web development sprint with tight deadline

**Original Prompt:**
```
Implement a file upload feature for our web application.
```

**Transformed Prompt:**
```
When implementing this solution, consider the following technical debt guidelines:
Prioritize shipping working code. Technical debt is acceptable if it helps meet immediate business needs.
Use TODO comments to mark areas of technical debt that need future improvement.
Focus on functional correctness over code elegance or perfect architecture.

Implement a file upload feature for our web application.
```

**Notes:** The decorator sets clear expectations about technical debt tolerance for time-sensitive features.

## Transformation Details

**Base Instruction:** When implementing this solution, consider the following technical debt guidelines:

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `accept`:
  - When set to `none`: Do not introduce any technical debt. Implement a complete, high-quality solution even if it takes longer.
  - When set to `minimal`: Minimize technical debt. Only accept small compromises that can be easily addressed later.
  - When set to `moderate`: Accept a moderate amount of technical debt where necessary to meet deadlines, but keep it manageable.
  - When set to `pragmatic`: Prioritize shipping working code. Technical debt is acceptable if it helps meet immediate business needs.

- `document`:
  - When set to `none`: No documentation of technical debt is required.
  - When set to `comments`: Document technical debt with inline code comments where compromises were made.
  - When set to `todos`: Use TODO comments to mark areas of technical debt that need future improvement.
  - When set to `issues`: Create formal issue tickets for each piece of technical debt introduced.
  - When set to `comprehensive`: Provide comprehensive documentation including inline comments, TODOs, and a separate technical debt register with prioritization.

- `tradeoff`:
  - When set to `nothing`: Do not trade off any aspect of quality.
  - When set to `completeness`: It's acceptable to implement a partial solution now and complete it later.
  - When set to `performance`: Optimize for correctness first; performance optimizations can come later.
  - When set to `elegance`: Focus on functional correctness over code elegance or perfect architecture.

## Compatibility

- **Requires**: None
- **Conflicts**: PerfectionistCode
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeQuality**: Conflicts with TechDebtControl CodeQuality decorator typically enforces stricter quality standards that may conflict with permissive technical debt settings.
- **DeadlineOriented**: Enhances TechDebtControl Works well with DeadlineOriented to balance speed and quality considerations.
