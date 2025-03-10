# Iterate Decorator

Indicates this is an iteration on previously generated code, with specific improvements needed.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `version` | number | Iteration number | 2 |
| `feedback` | enum | Type of feedback addressed | review-comments |
| `priority` | enum | Implementation priority | correctness |

## Feedback Options

- `review-comments`: code review comments
- `bug-fixes`: bug fixes
- `performance-issues`: performance issues
- `feature-requests`: feature requests

## Priority Options

- `correctness`: ensuring code correctness
- `completeness`: ensuring feature completeness
- `performance`: optimizing performance
- `readability`: improving code readability

## Examples

### Basic iteration on authentication middleware

```
+++Iterate(version=2, feedback=review-comments, priority=correctness)
Update the authentication middleware based on these code review comments: 1) Token expiration is not properly checked, 2) Error messages are not consistent.
```

The model will understand this is the second iteration of code, focusing on fixing specific review comments with correctness as the priority.

### Performance improvement iteration

```
+++Iterate(feedback=performance-issues, priority=performance)
The database query in the user service is taking too long. Please optimize it.
```

The model will understand this is an iteration focused on performance issues, with performance optimization as the priority.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** This is iteration {version}. I need you to improve the previously generated code based on {feedback} feedback. Focus primarily on {priority}.

**Notes:** Simpler phrasing works better with this model.


## Implementation Guidance

### Web development

**Original Prompt:**
```
Create an authentication middleware for Express.js
```

**Transformed Prompt:**
```
This is iteration 2 of the code implementation. Please focus on addressing the following feedback: code review comments, with priority on ensuring code correctness.

Create an authentication middleware for Express.js
```

**Notes:** The decorator indicates this is a follow-up request to improve previously generated code.

## Transformation Details

**Base Instruction:** This is iteration {version} of the code implementation. Please focus on addressing the following feedback: {feedback}, with priority on {priority}.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `version`:
  - Format: {value}

- `feedback`:
  - When set to `review-comments`: code review comments
  - When set to `bug-fixes`: bug fixes
  - When set to `performance-issues`: performance issues
  - When set to `feature-requests`: feature requests

- `priority`:
  - When set to `correctness`: ensuring code correctness
  - When set to `completeness`: ensuring feature completeness
  - When set to `performance`: optimizing performance
  - When set to `readability`: improving code readability

## Compatibility

- **Requires**: None
- **Conflicts**: FromScratch
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances Iterate Iterate works well after CodeReview to implement suggested changes.
- **FromScratch**: Conflicts with Iterate Iterate assumes existing code to improve upon, which conflicts with FromScratch's purpose.
