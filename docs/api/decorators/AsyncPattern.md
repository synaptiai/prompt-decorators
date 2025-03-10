# AsyncPattern Decorator

Handles asynchronous operations with appropriate patterns for the language and environment.

**Category**: Code Generation

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `approach` | `enum` | Asynchronous programming model to use | `language-appropriate` |
| `error-handling` | `enum` | Error handling strategy | `approach-appropriate` |
| `cancellation` | `enum` | Support for operation cancellation | `none` |

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

### gpt-4-turbo

**Instruction:** Generate code that handles asynchronous operations using the specified pattern. For approach={approach}, use error handling with {error-handling} and implement {cancellation} cancellation support.

**Notes:** This model may need more explicit instructions about the specific patterns to use.

### gpt-4o

**Instruction:** When implementing asynchronous operations in the code, use the specified asynchronous pattern and error handling approach. Use {approach} as the primary asynchronous pattern. Implement {error-handling} for error handling. Support {cancellation} cancellation for asynchronous operations.

**Notes:** gpt-4o has better understanding of advanced asynchronous patterns and can implement them more reliably.


## Implementation Guidance

### JavaScript/TypeScript

**Original Prompt:**
```
Create a function that fetches user data from multiple APIs in parallel and combines the results.
```

**Transformed Prompt:**
```
When implementing asynchronous operations in the code, use the specified asynchronous pattern and error handling approach. Use async/await as the primary asynchronous pattern. Implement try/catch for error handling. Support signal cancellation for asynchronous operations.

Create a function that fetches user data from multiple APIs in parallel and combines the results.
```

**Notes:** The implementation uses async/await with Promise.all for parallel fetching, try/catch blocks for error handling, and accepts an AbortSignal parameter for cancellation.

### Python

**Original Prompt:**
```
Create a function that fetches user data from multiple APIs in parallel and combines the results.
```

**Transformed Prompt:**
```
When implementing asynchronous operations in the code, use the specified asynchronous pattern and error handling approach. Use async/await as the primary asynchronous pattern. Implement try/catch for error handling. Support signal cancellation for asynchronous operations.

Create a function that fetches user data from multiple APIs in parallel and combines the results.
```

**Notes:** The implementation uses Python's asyncio with async/await, try/except blocks, and cancellation tokens from asyncio.

## Transformation Details

**Base Instruction:** When implementing asynchronous operations in the code, use the specified asynchronous pattern and error handling approach.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `approach`:
  - When set to `promises`: Implement using Promise-based patterns for asynchronous operations.
  - When set to `async-await`: Use async/await syntax for cleaner asynchronous code.
  - When set to `observables`: Implement using Observable patterns for reactive asynchronous streams.
  - When set to `callbacks`: Use callback functions to handle asynchronous operations.
  - When set to `streams`: Implement using stream-based asynchronous processing.
  - When set to `events`: Use event-based asynchronous programming model.
  - Format: Use {value} as the primary asynchronous pattern.

- `error-handling`:
  - When set to `try-catch`: Handle errors using try/catch blocks around asynchronous operations.
  - When set to `error-first-callbacks`: Follow the error-first callback pattern where the first parameter is an error object.
  - When set to `promise-rejection`: Use promise rejection handling with .catch() or try/catch with async/await.
  - When set to `error-streams`: Handle errors through dedicated error streams or channels.
  - Format: Implement {value} for error handling.

- `cancellation`:
  - When set to `none`: No cancellation mechanism is required.
  - When set to `manual`: Implement manual cancellation through boolean flags or state tracking.
  - When set to `timeout`: Include timeout-based cancellation for asynchronous operations.
  - When set to `signal`: Use AbortController or similar signal-based cancellation mechanisms.
  - Format: Support {value} cancellation for asynchronous operations.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, claude-instant
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **LanguageSpecific**: Enhances AsyncPattern LanguageSpecific can provide context for language-appropriate async patterns.
- **ErrorHandling**: Enhances AsyncPattern ErrorHandling can provide more detailed error handling strategies that complement the async error handling approach.
