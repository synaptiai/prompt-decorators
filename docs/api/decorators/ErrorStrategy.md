# ErrorStrategy Decorator

Guides how errors and exceptions should be handled in the implementation.

**Category**: Implementation-Focused

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `approach` | enum | Error handling philosophy | language-standard |
| `detail` | enum | Error detail level | standard |
| `recovery` | enum | Error recovery approach | none |

## Approach Options

- `defensive`: Use defensive programming techniques to prevent errors from occurring.
- `fail-fast`: Fail immediately when errors are detected to prevent cascading failures.
- `return-result`: Use a Result/Either pattern to explicitly handle success and error cases.
- `exceptions`: Use exception handling mechanisms for error management.
- `monadic`: Apply monadic error handling patterns for functional composition.

## Detail Options

- `minimal`: Provide minimal error information, focusing on essential details only.
- `standard`: Include standard error information with type, message, and basic context.
- `detailed`: Provide detailed error information including context, cause, and potential solutions.
- `debug`: Include comprehensive debug information with stack traces and internal state.

## Recovery Options

- `none`: Do not implement automatic recovery mechanisms.
- `retry`: Implement retry logic for transient failures.
- `fallback`: Provide fallback mechanisms when primary operations fail.
- `circuit-breaker`: Implement circuit breaker pattern to prevent cascading failures.

## Examples

### File processing service with result pattern and retry logic

```
+++ErrorStrategy(approach=return-result, detail=detailed, recovery=retry)
Implement a file processing service that uses the Result pattern for error handling and includes retry logic for transient errors.
```

A file processing service implementation that uses a Result/Either pattern to handle errors, provides detailed error information, and implements retry logic for transient failures like network issues.

### Web API with fail-fast approach

```
+++ErrorStrategy(approach=fail-fast, detail=standard)
Create a REST API endpoint for user registration.
```

A REST API implementation that validates inputs early and fails immediately with standard error messages when invalid data is detected.

### Database service with circuit breaker pattern

```
+++ErrorStrategy(approach=exceptions, recovery=circuit-breaker)
Implement a database access service.
```

A database service that uses exceptions for error handling and implements a circuit breaker pattern to prevent cascading failures during database outages.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Implement error handling using the following approach:

**Notes:** May need more explicit guidance on specific error handling patterns.

### gpt-4

**Instruction:** Implement error handling with the following strategy:

**Notes:** Can handle more nuanced error handling approaches like monadic patterns.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Performance**: Enhances ErrorStrategy ErrorStrategy can enhance Performance by specifying efficient error handling approaches.
- **Logging**: Enhances ErrorStrategy ErrorStrategy works well with Logging to ensure errors are properly recorded.
