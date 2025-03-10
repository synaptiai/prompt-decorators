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

### gpt-3.5-turbo

**Instruction:** Write code to solve this problem. Use {language} and follow {style} programming style with {comments} comments and {error_handling} error handling.

**Notes:** Simplified instruction format works better with GPT-3.5 Turbo's context window limitations.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **Reasoning**: Enhances CodeGen Using Reasoning before CodeGen can help break down complex problems before code implementation.
- **Concise**: Conflicts with CodeGen Concise may reduce the level of comments and documentation that CodeGen is instructed to produce.
