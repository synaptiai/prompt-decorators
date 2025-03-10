# DebugStrategy Decorator

Specifies the overall approach to debugging and problem analysis.

**Category**: Systematic Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `approach` | enum | Debugging methodology | systematic |
| `verbosity` | enum | Debug output verbosity | standard |
| `priority` | enum | Issue resolution priority | functionality |

## Approach Options

- `systematic`: Use a systematic step-by-step debugging approach to identify and resolve issues.
- `incremental`: Debug incrementally by making small changes and testing after each modification.
- `root-cause`: Focus on identifying the underlying root cause rather than addressing symptoms.
- `isolation`: Isolate components to determine which specific part is causing the issue.
- `comparison`: Compare working and non-working states to identify differences causing the problem.

## Verbosity Options

- `minimal`: Provide only essential information about the debugging process and findings.
- `standard`: Include a balanced amount of detail about the debugging process and findings.
- `verbose`: Provide detailed explanations of each debugging step and observation.
- `comprehensive`: Document exhaustively all aspects of the debugging process, including all tests performed and results observed.

## Priority Options

- `functionality`: Prioritize restoring basic functionality over other concerns.
- `performance`: Focus on optimizing performance aspects of the solution.
- `ux`: Emphasize user experience considerations in the debugging process.
- `security`: Prioritize security implications and vulnerabilities in the debugging process.

## Examples

### Root cause analysis of an authentication issue

```
+++DebugStrategy(approach=root-cause, verbosity=verbose, priority=functionality)
Debug the authentication failure that occurs when users attempt to log in with social credentials. Identify the exact point of failure.
```

A detailed analysis focusing on finding the root cause of the authentication failure, with verbose explanations of each debugging step, prioritizing the restoration of functionality.

### Minimal debugging of a performance issue

```
+++DebugStrategy(approach=isolation, verbosity=minimal, priority=performance)
The application becomes slow after processing large datasets. Debug the performance bottleneck.
```

A concise analysis that isolates components to identify performance bottlenecks, with minimal explanatory text, focusing on performance optimization.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Use a structured debugging approach to solve this problem. {approach_instruction} {verbosity_instruction} {priority_instruction}

**Notes:** Simplified instruction format for models with more limited context windows.


## Implementation Guidance

### Software development debugging

**Original Prompt:**
```
Debug the authentication failure that occurs when users attempt to log in with social credentials. Identify the exact point of failure.
```

**Transformed Prompt:**
```
Apply a structured debugging approach to analyze and solve the problem. Focus on identifying the underlying root cause rather than addressing symptoms. Provide detailed explanations of each debugging step and observation. Prioritize restoring basic functionality over other concerns.

Debug the authentication failure that occurs when users attempt to log in with social credentials. Identify the exact point of failure.
```

**Notes:** The decorator adds specific debugging instructions based on the selected approach, verbosity, and priority parameters.

## Transformation Details

**Base Instruction:** Apply a structured debugging approach to analyze and solve the problem.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `approach`:
  - When set to `systematic`: Use a systematic step-by-step debugging approach to identify and resolve issues.
  - When set to `incremental`: Debug incrementally by making small changes and testing after each modification.
  - When set to `root-cause`: Focus on identifying the underlying root cause rather than addressing symptoms.
  - When set to `isolation`: Isolate components to determine which specific part is causing the issue.
  - When set to `comparison`: Compare working and non-working states to identify differences causing the problem.

- `verbosity`:
  - When set to `minimal`: Provide only essential information about the debugging process and findings.
  - When set to `standard`: Include a balanced amount of detail about the debugging process and findings.
  - When set to `verbose`: Provide detailed explanations of each debugging step and observation.
  - When set to `comprehensive`: Document exhaustively all aspects of the debugging process, including all tests performed and results observed.

- `priority`:
  - When set to `functionality`: Prioritize restoring basic functionality over other concerns.
  - When set to `performance`: Focus on optimizing performance aspects of the solution.
  - When set to `ux`: Emphasize user experience considerations in the debugging process.
  - When set to `security`: Prioritize security implications and vulnerabilities in the debugging process.

## Compatibility

- **Requires**: None
- **Conflicts**: QuickFix
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeAnalysis**: Enhances DebugStrategy DebugStrategy works well with CodeAnalysis to provide a comprehensive debugging framework.
- **QuickFix**: Conflicts with DebugStrategy DebugStrategy focuses on thorough analysis which may conflict with QuickFix's emphasis on rapid solutions.
