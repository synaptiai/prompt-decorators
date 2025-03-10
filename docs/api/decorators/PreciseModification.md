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

### gpt-3.5-turbo

**Instruction:** Be extremely careful when modifying this code. Make precise, targeted changes based on the sensitivity level, scope requirements, and validation needs specified below:

**Notes:** More explicit instruction for models with less context understanding.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances PreciseModification PreciseModification works well with CodeReview to ensure changes are properly scrutinized.
- **TestDrivenDevelopment**: Enhances PreciseModification Combining with TestDrivenDevelopment ensures proper test coverage for sensitive modifications.
