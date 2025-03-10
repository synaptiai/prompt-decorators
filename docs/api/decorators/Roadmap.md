# Roadmap Decorator

Plans development timelines and feature sequencing.

**Category**: Developer Workflow

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `timeframe` | enum | Planning horizon | quarter |
| `focus` | enum | Roadmap emphasis | balanced |
| `detail` | enum | Depth of planning | milestones |

## Timeframe Options

- `sprint`: Plan for a 2-4 week sprint cycle.
- `quarter`: Plan for a 3-month quarterly timeline.
- `halfyear`: Plan for a 6-month timeline.
- `year`: Plan for a 12-month annual timeline.

## Focus Options

- `features`: Prioritize new feature development and enhancements.
- `technical-debt`: Focus on addressing technical debt and code quality improvements.
- `security`: Emphasize security improvements and vulnerability remediation.
- `performance`: Concentrate on performance optimizations and efficiency gains.
- `balanced`: Maintain a balanced approach across features, maintenance, security, and performance.

## Detail Options

- `high-level`: Provide high-level objectives and general direction.
- `milestones`: Include key milestones and deliverables with approximate timelines.
- `detailed`: Create a detailed plan with specific tasks, dependencies, and precise timelines.

## Examples

### Quarterly feature-focused roadmap with milestone planning

```
+++Roadmap(timeframe=quarter, focus=features, detail=milestones)
Create a product roadmap for our e-commerce platform focusing on enhancing the checkout experience.
```

A 3-month roadmap with feature development emphasis and key milestones for improving an e-commerce checkout experience.

### Sprint-level technical debt planning

```
+++Roadmap(timeframe=sprint, focus=technical-debt, detail=detailed)
Develop a plan to address our authentication service's code quality issues.
```

A detailed 2-4 week sprint plan focusing specifically on technical debt remediation for the authentication service.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create a development roadmap with clear timelines and priorities as specified below:

**Notes:** Simplified instruction for models with less context handling capability.


## Implementation Guidance

### Software development planning

**Original Prompt:**
```
Create a product roadmap for our e-commerce platform focusing on enhancing the checkout experience.
```

**Transformed Prompt:**
```
Create a development roadmap with the following specifications:
Plan for a 3-month quarterly timeline.
Prioritize new feature development and enhancements.
Include key milestones and deliverables with approximate timelines.

Create a product roadmap for our e-commerce platform focusing on enhancing the checkout experience.
```

**Notes:** The decorator adds specific planning parameters to guide the roadmap creation process.

## Transformation Details

**Base Instruction:** Create a development roadmap with the following specifications:

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `timeframe`:
  - When set to `sprint`: Plan for a 2-4 week sprint cycle.
  - When set to `quarter`: Plan for a 3-month quarterly timeline.
  - When set to `halfyear`: Plan for a 6-month timeline.
  - When set to `year`: Plan for a 12-month annual timeline.

- `focus`:
  - When set to `features`: Prioritize new feature development and enhancements.
  - When set to `technical-debt`: Focus on addressing technical debt and code quality improvements.
  - When set to `security`: Emphasize security improvements and vulnerability remediation.
  - When set to `performance`: Concentrate on performance optimizations and efficiency gains.
  - When set to `balanced`: Maintain a balanced approach across features, maintenance, security, and performance.

- `detail`:
  - When set to `high-level`: Provide high-level objectives and general direction.
  - When set to `milestones`: Include key milestones and deliverables with approximate timelines.
  - When set to `detailed`: Create a detailed plan with specific tasks, dependencies, and precise timelines.

## Compatibility

- **Requires**: None
- **Conflicts**: QuickSolution, Brainstorm
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, gemini-pro
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ProjectManagement**: Enhances Roadmap Roadmap works well with ProjectManagement decorator to create more comprehensive project plans.
- **QuickSolution**: Conflicts with Roadmap Roadmap is focused on structured planning which conflicts with quick, immediate solutions.
