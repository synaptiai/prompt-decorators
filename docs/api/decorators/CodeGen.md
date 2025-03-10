# CodeGen Decorator

Generates code snippets or complete solutions with configurable style and documentation level.

**Category**: Code Generation

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `language` | enum | Programming language to generate code in | inferred |
| `style` | enum | Programming paradigm or coding style to use | oop |
| `comments` | enum | Level of code documentation to include | moderate |
| `error_handling` | enum | Level of error handling to include | basic |

## Language Options

- `python`: Option: python
- `javascript`: Option: javascript
- `typescript`: Option: typescript
- `java`: Option: java
- `csharp`: Option: csharp
- `go`: Option: go
- `rust`: Option: rust

## Style Options

- `functional`: Write the code using functional programming principles, emphasizing immutability and pure functions.
- `oop`: Structure the code using object-oriented programming principles with appropriate classes and inheritance.
- `procedural`: Write procedural code with a focus on sequential operations and procedures.
- `reactive`: Implement using reactive programming patterns with event streams and observers.
- `declarative`: Use a declarative approach focusing on what the program should accomplish rather than how.

## Comments Options

- `minimal`: Include only essential comments for complex logic.
- `moderate`: Add comments for functions, classes, and non-obvious logic.
- `extensive`: Provide comprehensive documentation including function descriptions, parameter explanations, and implementation details.

## Error_Handling Options

- `none`: Focus on the happy path without explicit error handling.
- `basic`: Include basic error handling for common edge cases.
- `comprehensive`: Implement thorough error handling, input validation, and appropriate error messages.

## Examples

### Generate TypeScript code with functional programming style

```
+++CodeGen(language=typescript, style=functional, comments=moderate)
```

Produces TypeScript code using functional programming paradigms with moderate documentation.

### Generate Python code with comprehensive error handling

```
+++CodeGen(language=python, error_handling=comprehensive)
```

Produces Python code with thorough error handling, input validation, and appropriate error messages.

### Generate Java code with minimal comments

```
+++CodeGen(language=java, comments=minimal)
```

Produces Java code with only essential comments for complex logic.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Write code to solve this problem. Use {language} and follow {style} programming style with {comments} comments and {error_handling} error handling.

**Notes:** Simplified instruction format works better with gpt-4 Turbo's context window limitations.


## Implementation Guidance

### TypeScript function implementation

**Original Prompt:**
```
Create a utility function that calculates the total price of items in a shopping cart with discounts applied.
```

**Transformed Prompt:**
```
Generate code that solves the following problem. Make sure the solution is correct, efficient, and follows best practices. Use typescript as the programming language. Write the code using functional programming principles, emphasizing immutability and pure functions. Add comments for functions, classes, and non-obvious logic. Include basic error handling for common edge cases.

Create a utility function that calculates the total price of items in a shopping cart with discounts applied.
```

**Notes:** The decorator adds specific instructions about language, style, comments, and error handling before the original prompt.

## Transformation Details

**Base Instruction:** Generate code that solves the following problem. Make sure the solution is correct, efficient, and follows best practices.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `language`:
  - Format: Use {value} as the programming language.

- `style`:
  - When set to `functional`: Write the code using functional programming principles, emphasizing immutability and pure functions.
  - When set to `oop`: Structure the code using object-oriented programming principles with appropriate classes and inheritance.
  - When set to `procedural`: Write procedural code with a focus on sequential operations and procedures.
  - When set to `reactive`: Implement using reactive programming patterns with event streams and observers.
  - When set to `declarative`: Use a declarative approach focusing on what the program should accomplish rather than how.

- `comments`:
  - When set to `minimal`: Include only essential comments for complex logic.
  - When set to `moderate`: Add comments for functions, classes, and non-obvious logic.
  - When set to `extensive`: Provide comprehensive documentation including function descriptions, parameter explanations, and implementation details.

- `error_handling`:
  - When set to `none`: Focus on the happy path without explicit error handling.
  - When set to `basic`: Include basic error handling for common edge cases.
  - When set to `comprehensive`: Implement thorough error handling, input validation, and appropriate error messages.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **Reasoning**: Enhances CodeGen Using Reasoning before CodeGen can help break down complex problems before code implementation.
- **Concise**: Conflicts with CodeGen Concise may reduce the level of comments and documentation that CodeGen is instructed to produce.
