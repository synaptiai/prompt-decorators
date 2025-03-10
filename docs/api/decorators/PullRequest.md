# PullRequest Decorator

Generates descriptive pull request templates and descriptions.

**Category**: Developer Workflow

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `detail` | `enum` | Description depth | `standard` |
| `sections` | `enum` | PR sections to include | `all` |
| `reviewers` | `enum` | Guidance for reviewers | `focused` |

## Detail Options

- `minimal`: Keep the description concise and focus only on essential information.
- `standard`: Provide a balanced level of detail that covers the main aspects of the changes.
- `comprehensive`: Create a detailed description that thoroughly explains all aspects of the changes.

## Sections Options

- `summary`: Include only a summary section that briefly describes the changes.
- `changes`: Include sections for summary and detailed changes made.
- `testing`: Include sections for summary, changes, and testing information.
- `screenshots`: Include sections for summary, changes, testing, and visual references/screenshots.
- `dependencies`: Include sections for summary, changes, testing, and dependency information.
- `all`: Include all standard PR sections: summary, changes made, testing information, visual references/screenshots if applicable, and dependency changes.

## Reviewers Options

- `none`: Do not include specific guidance for reviewers.
- `focused`: Include targeted guidance for reviewers, highlighting specific areas that need attention.
- `detailed`: Include comprehensive guidance for reviewers with specific questions and areas to focus on.

## Examples

### Comprehensive PR description for a new feature

```
+++PullRequest(detail=comprehensive, sections=all, reviewers=detailed)
Create a pull request description for a feature that adds social login options to our authentication system.
```

Generates a detailed PR description with all sections and comprehensive reviewer guidance for a social login feature.

### Minimal PR description focusing on changes only

```
+++PullRequest(detail=minimal, sections=changes, reviewers=none)
Create a pull request description for a bug fix in the payment processing system.
```

Generates a concise PR description focusing only on the changes made to fix the payment processing bug.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a pull request description with the following sections and level of detail:

**Notes:** Simplified instruction for models with less context capacity.


## Implementation Guidance

### Web development project

**Original Prompt:**
```
Create a pull request description for a feature that adds social login options to our authentication system.
```

**Transformed Prompt:**
```
Generate a pull request description with the following structure and content: Provide a balanced level of detail that covers the main aspects of the changes. Include all standard PR sections: summary, changes made, testing information, visual references/screenshots if applicable, and dependency changes. Include targeted guidance for reviewers, highlighting specific areas that need attention.

Create a pull request description for a feature that adds social login options to our authentication system.
```

**Notes:** The decorator prepends instructions for generating a structured PR description with standard detail, all sections, and focused reviewer guidance.

## Transformation Details

**Base Instruction:** Generate a pull request description with the following structure and content:

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `detail`:
  - When set to `minimal`: Keep the description concise and focus only on essential information.
  - When set to `standard`: Provide a balanced level of detail that covers the main aspects of the changes.
  - When set to `comprehensive`: Create a detailed description that thoroughly explains all aspects of the changes.

- `sections`:
  - When set to `summary`: Include only a summary section that briefly describes the changes.
  - When set to `changes`: Include sections for summary and detailed changes made.
  - When set to `testing`: Include sections for summary, changes, and testing information.
  - When set to `screenshots`: Include sections for summary, changes, testing, and visual references/screenshots.
  - When set to `dependencies`: Include sections for summary, changes, testing, and dependency information.
  - When set to `all`: Include all standard PR sections: summary, changes made, testing information, visual references/screenshots if applicable, and dependency changes.

- `reviewers`:
  - When set to `none`: Do not include specific guidance for reviewers.
  - When set to `focused`: Include targeted guidance for reviewers, highlighting specific areas that need attention.
  - When set to `detailed`: Include comprehensive guidance for reviewers with specific questions and areas to focus on.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **CodeReview**: Enhances PullRequest PullRequest works well with CodeReview, as they address different aspects of the development workflow.
- **TechnicalDocumentation**: Enhances PullRequest Can be combined to generate both PR descriptions and related documentation.
