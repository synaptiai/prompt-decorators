# TaskBreakdown Decorator

Requests identification and prioritization of tasks needed to fix an issue or implement a change.

**Category**: Systematic Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `detail` | enum | Task breakdown detail level | detailed |
| `priority` | enum | Task prioritization approach | dependency-order |
| `format` | enum | Task output format | checklist |

## Detail Options

- `high-level`: Provide a high-level breakdown of the main tasks required.
- `detailed`: Provide a detailed breakdown of tasks with subtasks where appropriate.
- `comprehensive`: Provide a comprehensive breakdown with detailed subtasks, considerations, and potential challenges for each step.

## Priority Options

- `dependency-order`: Order tasks based on dependencies, with prerequisite tasks first.
- `impact`: Prioritize tasks based on their impact on resolving the overall issue.
- `effort`: Prioritize tasks based on effort required, starting with quick wins.
- `risk`: Prioritize tasks based on risk level, addressing high-risk items first.

## Format Options

- `list`: Present the tasks as a numbered list.
- `checklist`: Present the tasks as a checklist with checkable items.
- `kanban`: Organize tasks into 'To Do', 'In Progress', and 'Done' categories.
- `detailed`: Present each task with a title, description, priority level, and estimated effort.

## Examples

### Basic task breakdown for debugging a software issue

```
+++TaskBreakdown(detail=comprehensive, priority=risk, format=checklist)
Break down the tasks needed to fix the data synchronization issues.
```

The model will provide a comprehensive checklist of tasks needed to fix data synchronization issues, prioritized by risk level.

### High-level project planning

```
+++TaskBreakdown(detail=high-level, priority=dependency-order, format=kanban)
What steps should we take to implement the new user authentication system?
```

The model will provide a high-level kanban board of tasks organized by dependencies for implementing a new authentication system.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Please break down this problem into specific tasks that need to be completed. For each task, include details based on the specified level and prioritize according to the given approach.

**Notes:** For models with more limited context windows, the instruction is simplified while maintaining the core functionality.


## Implementation Guidance

### Software debugging scenario

**Original Prompt:**
```
Fix the data synchronization issues in our application.
```

**Transformed Prompt:**
```
Break down this task into discrete steps or components. Identify the key tasks needed to address this issue. Provide a comprehensive breakdown with detailed subtasks, considerations, and potential challenges for each step. Prioritize tasks based on risk level, addressing high-risk items first. Present the tasks as a checklist with checkable items.

Fix the data synchronization issues in our application.
```

**Notes:** The decorator adds structure to a vague request by asking for specific task breakdown with prioritization.

## Transformation Details

**Base Instruction:** Break down this task into discrete steps or components. Identify the key tasks needed to address this issue.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `detail`:
  - When set to `high-level`: Provide a high-level breakdown of the main tasks required.
  - When set to `detailed`: Provide a detailed breakdown of tasks with subtasks where appropriate.
  - When set to `comprehensive`: Provide a comprehensive breakdown with detailed subtasks, considerations, and potential challenges for each step.

- `priority`:
  - When set to `dependency-order`: Order tasks based on dependencies, with prerequisite tasks first.
  - When set to `impact`: Prioritize tasks based on their impact on resolving the overall issue.
  - When set to `effort`: Prioritize tasks based on effort required, starting with quick wins.
  - When set to `risk`: Prioritize tasks based on risk level, addressing high-risk items first.

- `format`:
  - When set to `list`: Present the tasks as a numbered list.
  - When set to `checklist`: Present the tasks as a checklist with checkable items.
  - When set to `kanban`: Organize tasks into 'To Do', 'In Progress', and 'Done' categories.
  - When set to `detailed`: Present each task with a title, description, priority level, and estimated effort.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 1.0.0

## Related Decorators

- **StepByStep**: Enhances TaskBreakdown TaskBreakdown works well with StepByStep, as it identifies the tasks that can then be executed in sequence.
- **PrioritizationFramework**: Enhances TaskBreakdown Can be combined with PrioritizationFramework for more sophisticated prioritization approaches.
