# AsyncPattern Decorator

Handles asynchronous operations with appropriate patterns for the language and environment.

**Category**: Code Generation

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `approach` | enum | Asynchronous programming model to use | language-appropriate |
| `error-handling` | enum | Error handling strategy | approach-appropriate |
| `cancellation` | enum | Support for operation cancellation | none |

## Approach Options

- `promises`: Implement using Promise-based patterns for asynchronous operations.
- `async-await`: Use async/await syntax for cleaner asynchronous code.
- `observables`: Implement using Observable patterns for reactive asynchronous streams.
- `callbacks`: Use callback functions to handle asynchronous operations.
- `streams`: Implement using stream-based asynchronous processing.
- `events`: Use event-based asynchronous programming model.

## Error-Handling Options

- `try-catch`: Handle errors using try/catch blocks around asynchronous operations.
- `error-first-callbacks`: Follow the error-first callback pattern where the first parameter is an error object.
- `promise-rejection`: Use promise rejection handling with .catch() or try/catch with async/await.
- `error-streams`: Handle errors through dedicated error streams or channels.

## Cancellation Options

- `none`: No cancellation mechanism is required.
- `manual`: Implement manual cancellation through boolean flags or state tracking.
- `timeout`: Include timeout-based cancellation for asynchronous operations.
- `signal`: Use AbortController or similar signal-based cancellation mechanisms.

## Examples

### JavaScript async/await with try/catch and AbortController

```
+++AsyncPattern(approach=async-await, error-handling=try-catch, cancellation=signal)
Create a function that fetches user data from multiple APIs in parallel and combines the results.
```

The model will generate JavaScript code using async/await syntax, with try/catch blocks for error handling, and accepting an AbortSignal parameter to support cancellation.

### Node.js callback-based approach

```
+++AsyncPattern(approach=callbacks, error-handling=error-first-callbacks)
Create a function that reads multiple files and processes their contents.
```

The model will generate Node.js code using callback functions with the error-first pattern for handling asynchronous file operations.

### Reactive programming with observables

```
+++AsyncPattern(approach=observables, error-handling=error-streams, cancellation=manual)
Create a service that monitors real-time data from multiple sources.
```

The model will generate code using Observable patterns (like RxJS) with error streams for error handling and manual subscription management for cancellation.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Generate code that handles asynchronous operations using the specified pattern. For approach={approach}, use error handling with {error-handling} and implement {cancellation} cancellation support.

**Notes:** This model may need more explicit instructions about the specific patterns to use.

### gpt-4

**Instruction:** When implementing asynchronous operations in the code, use the specified asynchronous pattern and error handling approach. Use {approach} as the primary asynchronous pattern. Implement {error-handling} for error handling. Support {cancellation} cancellation for asynchronous operations.

**Notes:** GPT-4 has better understanding of advanced asynchronous patterns and can implement them more reliably.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, claude-instant
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **LanguageSpecific**: Enhances AsyncPattern LanguageSpecific can provide context for language-appropriate async patterns.
- **ErrorHandling**: Enhances AsyncPattern ErrorHandling can provide more detailed error handling strategies that complement the async error handling approach.
