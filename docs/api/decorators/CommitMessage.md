# CommitMessage Decorator

Generates structured, informative commit messages.

**Category**: Developer Workflow

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `style` | enum | Commit message format | conventional |
| `scope` | enum | Change scope information | include |
| `issue` | enum | Include issue references | reference |

## Style Options

- `conventional`: Follow the Conventional Commits format (type(scope): description) with types like feat, fix, docs, style, refactor, test, chore.
- `detailed`: Create a detailed commit message with a summary line followed by a blank line and a more detailed explanatory text.
- `minimal`: Create a brief, to-the-point commit message focusing only on the essential change.
- `semantic`: Use semantic versioning principles to indicate the nature and impact of changes.
- `custom`: Format the commit message according to the specific requirements provided in the prompt.

## Scope Options

- `include`: Include the scope of the change in parentheses after the type (e.g., feat(auth): add login functionality).
- `exclude`: Omit the scope information from the commit message.

## Issue Options

- `none`: Do not include any issue references in the commit message.
- `reference`: Reference related issues at the end of the commit message (e.g., 'Related to #123').
- `close`: Include closing keywords for issues (e.g., 'Closes #123', 'Fixes #123').

## Examples

### Conventional commit message for a bug fix

```
+++CommitMessage(style=conventional, scope=include, issue=reference)
Generate a commit message for changes that improve error handling in the authentication module, related to issue #143.
```

fix(auth): improve error handling in authentication module

Enhance error handling for failed login attempts with better user feedback and logging. Related to #143

### Detailed commit message without scope

```
+++CommitMessage(style=detailed, scope=exclude, issue=close)
Generate a commit message for adding a new feature that allows users to reset their password.
```

Add password reset functionality

Implements a secure password reset flow with email verification and temporary token generation. Users can now request password resets via the login page and receive email instructions.

Closes #156

### Minimal commit message

```
+++CommitMessage(style=minimal, issue=none)
Generate a commit message for updating the README with installation instructions.
```

Update README with installation instructions

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Write a clear git commit message for the following changes. The message should follow standard commit message conventions and clearly explain what was changed and why.

**Notes:** Simplified instruction for models with less context capacity.


## Implementation Guidance

### Git commit for a bug fix

**Original Prompt:**
```
Generate a commit message for changes that fix a login error in the authentication module.
```

**Transformed Prompt:**
```
Generate a commit message that is clear, concise, and follows best practices for version control. The message should effectively communicate the changes made in the commit. Follow the Conventional Commits format (type(scope): description) with types like feat, fix, docs, style, refactor, test, chore. Include the scope of the change in parentheses after the type (e.g., feat(auth): add login functionality). Reference related issues at the end of the commit message (e.g., 'Related to #123'). Generate a commit message for changes that fix a login error in the authentication module.
```

**Notes:** The decorator adds specific instructions for formatting the commit message according to conventional commits style.

## Transformation Details

**Base Instruction:** Generate a commit message that is clear, concise, and follows best practices for version control. The message should effectively communicate the changes made in the commit.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `style`:
  - When set to `conventional`: Follow the Conventional Commits format (type(scope): description) with types like feat, fix, docs, style, refactor, test, chore.
  - When set to `detailed`: Create a detailed commit message with a summary line followed by a blank line and a more detailed explanatory text.
  - When set to `minimal`: Create a brief, to-the-point commit message focusing only on the essential change.
  - When set to `semantic`: Use semantic versioning principles to indicate the nature and impact of changes.
  - When set to `custom`: Format the commit message according to the specific requirements provided in the prompt.

- `scope`:
  - When set to `include`: Include the scope of the change in parentheses after the type (e.g., feat(auth): add login functionality).
  - When set to `exclude`: Omit the scope information from the commit message.

- `issue`:
  - When set to `none`: Do not include any issue references in the commit message.
  - When set to `reference`: Reference related issues at the end of the commit message (e.g., 'Related to #123').
  - When set to `close`: Include closing keywords for issues (e.g., 'Closes #123', 'Fixes #123').

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances CommitMessage CommitMessage works well after CodeReview to generate appropriate commit messages based on code changes identified in the review.
- **PullRequest**: Enhances CommitMessage CommitMessage can be used to generate commit messages that will be included in a pull request description.
