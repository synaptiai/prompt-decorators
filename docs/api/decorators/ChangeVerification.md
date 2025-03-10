# ChangeVerification Decorator

Focuses on verifying that changes have the intended effect and don't introduce regressions.

**Category**: Systematic Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `type` | `enum` | Verification type | `functionality` |
| `method` | `enum` | Verification method | `manual-testing` |
| `coverage` | `enum` | Verification coverage | `dependent-areas` |

## Type Options

- `functionality`: Focus on verifying the functional behavior of the changes.
- `visual`: Focus on verifying the visual appearance and UI elements affected by the changes.
- `performance`: Focus on verifying the performance impact of the changes.
- `security`: Focus on verifying the security implications of the changes.

## Method Options

- `manual-testing`: Use manual testing procedures to verify the changes.
- `automated-tests`: Use automated tests to verify the changes.
- `dom-inspection`: Inspect the DOM structure to verify the changes.
- `logging`: Use logging and debug output to verify the changes.

## Coverage Options

- `changed-only`: Verify only the specific components that were changed.
- `dependent-areas`: Verify the changed components and any dependent areas that might be affected.
- `comprehensive`: Perform a comprehensive verification across the entire system.

## Examples

### Verifying UI updates after implementing sorting functionality

```
+++ChangeVerification(type=functionality, method=dom-inspection, coverage=dependent-areas)
Verify that the UI updates properly after implementing the sorting functionality. Check all elements that should respond to the sort action.
```

The model will provide guidance on how to verify the UI updates after implementing sorting functionality, focusing on functional aspects using DOM inspection and checking both the changed components and dependent areas.

### Verifying performance impact of database query optimization

```
+++ChangeVerification(type=performance, method=automated-tests, coverage=comprehensive)
Verify the performance impact of the new database query optimization.
```

The model will provide guidance on how to verify the performance impact of database query optimization using automated tests across the entire system.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Please verify that the changes work as expected and don't cause any problems. Check for {type} issues using {method} and focus on {coverage} areas.

**Notes:** Simplified instruction for models with more limited context windows.


## Implementation Guidance

### Web development

**Original Prompt:**
```
How should I test the new sorting feature?
```

**Transformed Prompt:**
```
Verify the changes to ensure they have the intended effect and don't introduce regressions. Focus on verifying the functional behavior of the changes. Use manual testing procedures to verify the changes. Verify the changed components and any dependent areas that might be affected.

How should I test the new sorting feature?
```

**Notes:** The decorator adds specific verification instructions based on the parameters.

## Transformation Details

**Base Instruction:** Verify the changes to ensure they have the intended effect and don't introduce regressions.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `type`:
  - When set to `functionality`: Focus on verifying the functional behavior of the changes.
  - When set to `visual`: Focus on verifying the visual appearance and UI elements affected by the changes.
  - When set to `performance`: Focus on verifying the performance impact of the changes.
  - When set to `security`: Focus on verifying the security implications of the changes.

- `method`:
  - When set to `manual-testing`: Use manual testing procedures to verify the changes.
  - When set to `automated-tests`: Use automated tests to verify the changes.
  - When set to `dom-inspection`: Inspect the DOM structure to verify the changes.
  - When set to `logging`: Use logging and debug output to verify the changes.

- `coverage`:
  - When set to `changed-only`: Verify only the specific components that were changed.
  - When set to `dependent-areas`: Verify the changed components and any dependent areas that might be affected.
  - When set to `comprehensive`: Perform a comprehensive verification across the entire system.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **TestingStrategy**: Enhances ChangeVerification ChangeVerification works well with TestingStrategy by focusing on verification aspects while TestingStrategy provides the overall testing approach.
- **BugReport**: Enhances ChangeVerification ChangeVerification can help identify issues that might need to be reported using BugReport.
