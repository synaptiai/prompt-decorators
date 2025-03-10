# PreciseModification Decorator

Guides careful, targeted modifications to sensitive parts of the codebase.

**Category**: Systematic Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `sensitivity` | enum | Code sensitivity level | sensitive |
| `scope` | enum | Modification scope | minimal |
| `validation` | enum | Required validation approach | both |

## Sensitivity Options

- `normal`: This code has standard sensitivity. Apply normal caution when modifying.
- `sensitive`: This code has elevated sensitivity. Be careful with modifications and consider potential side effects.
- `critical`: This code is critical to system operation. Exercise extreme caution with any modifications.
- `fragile`: This code is fragile and prone to breaking. Make minimal, precise changes with thorough testing.

## Scope Options

- `isolated`: Make changes that are completely isolated from other components.
- `contained`: Ensure changes are contained to a specific module or subsystem.
- `minimal`: Make the smallest possible changes to achieve the objective.
- `precise`: Make surgical, precise modifications targeting only the specific issue.

## Validation Options

- `review`: All changes must be carefully reviewed before implementation.
- `tests`: All changes must be validated with appropriate test coverage.
- `both`: All changes require both code review and test validation.
- `comprehensive`: All changes require comprehensive validation including code review, testing, and integration verification.

## Examples

### Modifying fragile payment processing code

```
+++PreciseModification(sensitivity=fragile, scope=precise, validation=comprehensive)
Update the payment processing calculation without affecting any other components. This is a critical system that requires extensive validation.
```

The model will provide a solution that makes extremely careful, surgical changes to the payment processing calculation, with comprehensive validation steps and awareness of the code's fragility.

### Normal sensitivity code modification with minimal scope

```
+++PreciseModification(sensitivity=normal, scope=minimal)
Refactor this utility function to improve performance.
```

The model will provide a solution that makes minimal changes to the utility function while maintaining normal caution appropriate for non-critical code.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Be extremely careful when modifying this code. Make precise, targeted changes based on the sensitivity level, scope requirements, and validation needs specified below:

**Notes:** More explicit instruction for models with less context understanding.


## Implementation Guidance

### Payment processing system modification

**Original Prompt:**
```
Update the payment processing calculation without affecting any other components.
```

**Transformed Prompt:**
```
When modifying code, ensure changes are carefully targeted and appropriate for the sensitivity level of the codebase. Consider the scope of changes and implement proper validation procedures. This code is fragile and prone to breaking. Make minimal, precise changes with thorough testing. Make surgical, precise modifications targeting only the specific issue. All changes require comprehensive validation including code review, testing, and integration verification. Update the payment processing calculation without affecting any other components.
```

**Notes:** The decorator adds specific guidance on how to approach modifying fragile payment processing code with precise scope and comprehensive validation.

## Transformation Details

**Base Instruction:** When modifying code, ensure changes are carefully targeted and appropriate for the sensitivity level of the codebase. Consider the scope of changes and implement proper validation procedures.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `sensitivity`:
  - When set to `normal`: This code has standard sensitivity. Apply normal caution when modifying.
  - When set to `sensitive`: This code has elevated sensitivity. Be careful with modifications and consider potential side effects.
  - When set to `critical`: This code is critical to system operation. Exercise extreme caution with any modifications.
  - When set to `fragile`: This code is fragile and prone to breaking. Make minimal, precise changes with thorough testing.

- `scope`:
  - When set to `isolated`: Make changes that are completely isolated from other components.
  - When set to `contained`: Ensure changes are contained to a specific module or subsystem.
  - When set to `minimal`: Make the smallest possible changes to achieve the objective.
  - When set to `precise`: Make surgical, precise modifications targeting only the specific issue.

- `validation`:
  - When set to `review`: All changes must be carefully reviewed before implementation.
  - When set to `tests`: All changes must be validated with appropriate test coverage.
  - When set to `both`: All changes require both code review and test validation.
  - When set to `comprehensive`: All changes require comprehensive validation including code review, testing, and integration verification.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances PreciseModification PreciseModification works well with CodeReview to ensure changes are properly scrutinized.
- **TestDrivenDevelopment**: Enhances PreciseModification Combining with TestDrivenDevelopment ensures proper test coverage for sensitive modifications.
