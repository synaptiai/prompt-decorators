# Refactor Decorator

Improves existing code structure while preserving functionality.

**Category**: Code Generation

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `goal` | `enum` | Primary objective of the refactoring | `maintainability` |
| `level` | `enum` | Extent of changes to make | `moderate` |
| `preserve` | `enum` | Aspects that must be preserved | `both` |

## Goal Options

- `performance`: Refactor the code to optimize for performance. Look for inefficient algorithms, unnecessary computations, and opportunities for caching or parallelization.
- `readability`: Refactor the code to improve readability. Focus on clear naming, consistent formatting, and logical organization of code elements.
- `maintainability`: Refactor the code to enhance maintainability. Reduce complexity, improve modularity, and ensure the code follows best practices and design patterns.
- `security`: Refactor the code to address security concerns. Identify and fix potential vulnerabilities, implement proper input validation, and follow security best practices.
- `testability`: Refactor the code to improve testability. Make functions more modular, reduce dependencies, and ensure components can be tested in isolation.

## Level Options

- `minor`: Make minimal changes to the code structure while addressing the main issues.
- `moderate`: Perform a balanced refactoring that addresses key issues without completely rewriting the code.
- `major`: Conduct a comprehensive refactoring that may involve significant restructuring of the code.

## Preserve Options

- `api`: Ensure the public API (function signatures, return values, etc.) remains unchanged during refactoring.
- `behavior`: Maintain the exact same behavior and output for all inputs, even if the API changes.
- `both`: Preserve both the API and behavior of the code during refactoring.

## Examples

### Refactoring for performance with moderate changes

```
+++Refactor(goal=performance, level=moderate)
Refactor this database query function that's causing performance issues.
```

The model will refactor the code focusing on performance optimizations while making moderate changes to the structure.

### Improving code readability while preserving API

```
+++Refactor(goal=readability, preserve=api)
Can you refactor this legacy code to make it more readable?
```

The model will focus on improving naming, formatting, and organization while ensuring the function signatures remain unchanged.

### Major security refactoring

```
+++Refactor(goal=security, level=major)
This authentication code has security issues. Please refactor it.
```

The model will perform extensive refactoring to address security vulnerabilities while maintaining the code's core functionality.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Refactor this code to improve its {goal} while making {level} changes and preserving {preserve}. Don't rewrite it completely - focus on structural improvements.

**Notes:** More explicit instructions help gpt-4 maintain the refactoring constraints.


## Implementation Guidance

### Python function refactoring

**Original Prompt:**
```
Can you help me improve this function?

def get_user_data(id):
  data = db.query("SELECT * FROM users WHERE id = " + id)
  return data
```

**Transformed Prompt:**
```
Refactor the provided code to improve its structure while preserving its functionality. Focus on making the code more maintainable. Perform a balanced refactoring that addresses key issues without completely rewriting the code. Preserve both the API and behavior of the code during refactoring.

Can you help me improve this function?

def get_user_data(id):
  data = db.query("SELECT * FROM users WHERE id = " + id)
  return data
```

**Notes:** The refactoring should address the SQL injection vulnerability while maintaining the function signature and behavior.

## Transformation Details

**Base Instruction:** Refactor the provided code to improve its structure while preserving its functionality. Focus on making the code more maintainable.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `goal`:
  - When set to `performance`: Refactor the code to optimize for performance. Look for inefficient algorithms, unnecessary computations, and opportunities for caching or parallelization.
  - When set to `readability`: Refactor the code to improve readability. Focus on clear naming, consistent formatting, and logical organization of code elements.
  - When set to `maintainability`: Refactor the code to enhance maintainability. Reduce complexity, improve modularity, and ensure the code follows best practices and design patterns.
  - When set to `security`: Refactor the code to address security concerns. Identify and fix potential vulnerabilities, implement proper input validation, and follow security best practices.
  - When set to `testability`: Refactor the code to improve testability. Make functions more modular, reduce dependencies, and ensure components can be tested in isolation.

- `level`:
  - When set to `minor`: Make minimal changes to the code structure while addressing the main issues.
  - When set to `moderate`: Perform a balanced refactoring that addresses key issues without completely rewriting the code.
  - When set to `major`: Conduct a comprehensive refactoring that may involve significant restructuring of the code.

- `preserve`:
  - When set to `api`: Ensure the public API (function signatures, return values, etc.) remains unchanged during refactoring.
  - When set to `behavior`: Maintain the exact same behavior and output for all inputs, even if the API changes.
  - When set to `both`: Preserve both the API and behavior of the code during refactoring.

## Compatibility

- **Requires**: None
- **Conflicts**: Rewrite, GenerateFromScratch
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Minimum Standard Version**: 1.0.0

## Related Decorators

- **CodeReview**: Enhances Refactor CodeReview can be used before Refactor to identify issues that need to be addressed.
- **Rewrite**: Conflicts with Refactor Rewrite typically creates new code from scratch, while Refactor preserves existing structure and functionality.
