# LoggingStrategy Decorator

Defines a strategy for implementing logging to aid debugging and monitoring.

**Category**: Systematic Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `level` | `enum` | Logging detail level | `standard` |
| `targets` | `enum` | Logging targets | `console` |
| `lifecycle` | `enum` | Log lifecycle management | `temporary` |

## Level Options

- `minimal`: Implement minimal logging that captures only critical events and errors.
- `standard`: Implement standard logging that captures important application events, errors, and basic flow information.
- `verbose`: Implement verbose logging that captures detailed information about application flow, state changes, and all significant events.
- `diagnostic`: Implement diagnostic logging that captures comprehensive details about internal operations, variable states, and system interactions for troubleshooting purposes.

## Targets Options

- `console`: Direct logs to the console or standard output.
- `file`: Write logs to persistent files with appropriate rotation and management.
- `service`: Send logs to a dedicated logging service or aggregator.
- `all`: Implement multiple logging targets including console, file, and service integration.

## Lifecycle Options

- `temporary`: Implement logging as a temporary measure that can be easily removed when no longer needed.
- `permanent`: Implement logging as a permanent part of the system architecture.
- `conditional`: Implement conditional logging that activates based on environment variables or configuration.
- `togglable`: Implement logging that can be dynamically enabled or disabled at runtime.

## Examples

### Implementing diagnostic logging for authentication flow

```
+++LoggingStrategy(level=diagnostic, targets=console, lifecycle=togglable)
Implement comprehensive logging for the authentication flow that can be enabled/disabled with a debug flag.
```

The model will generate code for an authentication flow with detailed diagnostic logging that outputs to the console and can be toggled on/off via a debug flag.

### Standard file logging for production environment

```
+++LoggingStrategy(level=standard, targets=file, lifecycle=permanent)
Create a user registration system with appropriate logging.
```

The model will implement a user registration system with standard-level logging written to files as a permanent part of the system.

### Minimal conditional logging for performance-sensitive operations

```
+++LoggingStrategy(level=minimal, targets=service, lifecycle=conditional)
Write a high-performance data processing function.
```

The model will create a high-performance function with minimal logging sent to a service, activated only under specific conditions to minimize performance impact.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Add logging to the code with the following characteristics: {level} detail level, output to {targets}, and {lifecycle} persistence.

**Notes:** Simplified instruction format works better with gpt-4 Turbo.


## Implementation Guidance

### Node.js application

**Original Prompt:**
```
Write a user authentication function for my Express app.
```

**Transformed Prompt:**
```
Implement a logging strategy for the code or system being discussed. Implement diagnostic logging that captures comprehensive details about internal operations, variable states, and system interactions for troubleshooting purposes. Direct logs to the console or standard output. Implement logging that can be dynamically enabled or disabled at runtime.

Write a user authentication function for my Express app.
```

**Notes:** The transformed prompt instructs the model to include diagnostic-level logging in the authentication function with console output that can be toggled on/off.

### Python backend service

**Original Prompt:**
```
Create a data processing pipeline that handles CSV imports.
```

**Transformed Prompt:**
```
Implement a logging strategy for the code or system being discussed. Implement verbose logging that captures detailed information about application flow, state changes, and all significant events. Write logs to persistent files with appropriate rotation and management. Implement conditional logging that activates based on environment variables or configuration.

Create a data processing pipeline that handles CSV imports.
```

**Notes:** The transformed prompt adds instructions for verbose file-based logging with conditional activation based on environment settings.

## Transformation Details

**Base Instruction:** Implement a logging strategy for the code or system being discussed.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `level`:
  - When set to `minimal`: Implement minimal logging that captures only critical events and errors.
  - When set to `standard`: Implement standard logging that captures important application events, errors, and basic flow information.
  - When set to `verbose`: Implement verbose logging that captures detailed information about application flow, state changes, and all significant events.
  - When set to `diagnostic`: Implement diagnostic logging that captures comprehensive details about internal operations, variable states, and system interactions for troubleshooting purposes.

- `targets`:
  - When set to `console`: Direct logs to the console or standard output.
  - When set to `file`: Write logs to persistent files with appropriate rotation and management.
  - When set to `service`: Send logs to a dedicated logging service or aggregator.
  - When set to `all`: Implement multiple logging targets including console, file, and service integration.

- `lifecycle`:
  - When set to `temporary`: Implement logging as a temporary measure that can be easily removed when no longer needed.
  - When set to `permanent`: Implement logging as a permanent part of the system architecture.
  - When set to `conditional`: Implement conditional logging that activates based on environment variables or configuration.
  - When set to `togglable`: Implement logging that can be dynamically enabled or disabled at runtime.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **ErrorHandling**: Enhances LoggingStrategy LoggingStrategy works well with ErrorHandling to create robust error tracking and debugging capabilities.
- **PerformanceOptimization**: Conflicts with LoggingStrategy Verbose or diagnostic logging may impact performance, so be cautious when combining with PerformanceOptimization.
