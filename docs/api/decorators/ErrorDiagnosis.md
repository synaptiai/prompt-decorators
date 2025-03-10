# ErrorDiagnosis Decorator

Focuses on diagnosing and resolving specific errors or bugs.

**Category**: Systematic Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `severity` | `enum` | Error severity level | `significant` |
| `persistence` | `enum` | Error persistence pattern | `consistent` |
| `analysis` | `enum` | Analysis depth | `root-cause` |

## Severity Options

- `minor`: Treat this as a minor issue that may have limited impact.
- `significant`: Approach this as a significant issue that requires careful attention.
- `major`: Consider this a major issue with substantial impact on system functionality.
- `critical`: Treat this as a critical issue requiring immediate resolution.

## Persistence Options

- `intermittent`: Focus on diagnosing this intermittent issue, considering timing patterns and triggering conditions.
- `consistent`: Analyze this consistent issue that occurs reliably under specific conditions.
- `progressive`: Examine this progressive issue that worsens over time or with increased usage.
- `environment-specific`: Investigate this environment-specific issue that only manifests in particular contexts.

## Analysis Options

- `surface`: Provide a surface-level analysis identifying the most obvious potential causes.
- `detailed`: Conduct a detailed analysis examining multiple factors and their interactions.
- `root-cause`: Perform a root-cause analysis to identify the fundamental source of the issue.
- `comprehensive`: Deliver a comprehensive analysis covering all aspects including root causes, contributing factors, and systemic implications.

## Examples

### Diagnosing a critical database error

```
+++ErrorDiagnosis(severity=critical, persistence=consistent, analysis=root-cause)
Our database is consistently returning timeout errors when querying large datasets.
```

A systematic diagnosis of the database timeout issue, focusing on identifying the root cause of this critical and consistent problem.

### Investigating an intermittent UI glitch

```
+++ErrorDiagnosis(severity=minor, persistence=intermittent, analysis=surface)
Users occasionally report that the dropdown menu disappears when hovering over it.
```

A surface-level analysis of potential causes for the intermittent UI glitch, treating it as a minor issue.

### Comprehensive analysis of a progressive memory leak

```
+++ErrorDiagnosis(severity=major, persistence=progressive, analysis=comprehensive)
Our application's memory usage gradually increases until it crashes, usually after several hours of operation.
```

A comprehensive analysis of the progressive memory leak, including root causes, contributing factors, and systemic implications, treating it as a major issue.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Analyze and diagnose the described error or bug. Identify likely causes and recommend solutions based on the error characteristics.

**Notes:** Simplified instruction for models with less diagnostic capability.


## Implementation Guidance

### Software debugging scenario

**Original Prompt:**
```
The payment processing occasionally fails during high traffic periods. Diagnose the root cause of this intermittent error.
```

**Transformed Prompt:**
```
Diagnose the described error or bug with a systematic debugging approach. Identify potential causes and suggest solutions. Focus on diagnosing this intermittent issue, considering timing patterns and triggering conditions. Consider this a major issue with substantial impact on system functionality. Deliver a comprehensive analysis covering all aspects including root causes, contributing factors, and systemic implications.

The payment processing occasionally fails during high traffic periods. Diagnose the root cause of this intermittent error.
```

**Notes:** The decorator adds specific guidance for approaching the error diagnosis based on the parameters provided.

## Transformation Details

**Base Instruction:** Diagnose the described error or bug with a systematic debugging approach. Identify potential causes and suggest solutions.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `severity`:
  - When set to `minor`: Treat this as a minor issue that may have limited impact.
  - When set to `significant`: Approach this as a significant issue that requires careful attention.
  - When set to `major`: Consider this a major issue with substantial impact on system functionality.
  - When set to `critical`: Treat this as a critical issue requiring immediate resolution.

- `persistence`:
  - When set to `intermittent`: Focus on diagnosing this intermittent issue, considering timing patterns and triggering conditions.
  - When set to `consistent`: Analyze this consistent issue that occurs reliably under specific conditions.
  - When set to `progressive`: Examine this progressive issue that worsens over time or with increased usage.
  - When set to `environment-specific`: Investigate this environment-specific issue that only manifests in particular contexts.

- `analysis`:
  - When set to `surface`: Provide a surface-level analysis identifying the most obvious potential causes.
  - When set to `detailed`: Conduct a detailed analysis examining multiple factors and their interactions.
  - When set to `root-cause`: Perform a root-cause analysis to identify the fundamental source of the issue.
  - When set to `comprehensive`: Deliver a comprehensive analysis covering all aspects including root causes, contributing factors, and systemic implications.

## Compatibility

- **Requires**: None
- **Conflicts**: Simplify, CreativeWriting
- **Compatible Models**: gpt-4o, gpt-4-turbo, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **SystematicThinking**: Enhances ErrorDiagnosis ErrorDiagnosis works well with SystematicThinking to provide a structured approach to debugging.
- **Simplify**: Conflicts with ErrorDiagnosis ErrorDiagnosis typically requires detailed analysis which may conflict with simplification approaches.
