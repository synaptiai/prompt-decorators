# DesignPattern Decorator

Applies a specific design pattern to generated code, ensuring architectural best practices.

**Category**: Code Generation

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `pattern` | enum | The design pattern to implement | inferred |
| `language` | enum | Programming language to use | inferred |
| `variation` | string | Specific variation of the pattern | standard |

## Pattern Options

- `singleton`: Implement a Singleton pattern to ensure only one instance of the class exists throughout the application.
- `factory`: Use a Factory pattern to create objects without specifying the exact class of object that will be created.
- `adapter`: Implement an Adapter pattern to allow incompatible interfaces to work together.
- `observer`: Use the Observer pattern to define a one-to-many dependency between objects.
- `strategy`: Implement the Strategy pattern to define a family of algorithms and make them interchangeable.
- `command`: Use the Command pattern to encapsulate a request as an object.
- `facade`: Implement a Facade pattern to provide a simplified interface to a complex subsystem.

## Language Options

- `python`: Option: python
- `javascript`: Option: javascript
- `typescript`: Option: typescript
- `java`: Option: java
- `csharp`: Option: csharp
- `go`: Option: go
- `rust`: Option: rust

## Examples

### Observer pattern in JavaScript

```
+++DesignPattern(pattern=observer, language=javascript)
Create a notification system for an e-commerce application that alerts different parts of the UI when the cart changes.
```

JavaScript implementation of the Observer pattern for a notification system, with Subject (Cart) and multiple Observer (UI components) classes.

### Factory pattern in Java

```
+++DesignPattern(pattern=factory, language=java)
Create a payment processing system that can handle different payment methods.
```

Java implementation of a Factory pattern that creates different payment processor objects based on the payment method requested.

### Singleton pattern with thread safety in C#

```
+++DesignPattern(pattern=singleton, language=csharp, variation=thread-safe)
Implement a logging service for a multi-threaded application.
```

C# implementation of a thread-safe Singleton pattern for a logging service using double-check locking.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Use the {pattern} design pattern in {language} for this code. Implement the {variation} version of the pattern.

**Notes:** Simpler instruction format works better with this model.

### claude-2

**Instruction:** Please implement the {pattern} design pattern in {language}, following the {variation} implementation approach. Ensure the code follows best practices for this architectural pattern.

**Notes:** More detailed instructions work better with Claude models.


## Implementation Guidance

### Observer pattern in JavaScript

**Original Prompt:**
```
Create a notification system for an e-commerce application that alerts different parts of the UI when the cart changes.
```

**Transformed Prompt:**
```
Apply the observer design pattern in javascript to the following code generation task. Use the standard variation of this pattern where appropriate.

Implement the Observer pattern to define a one-to-many dependency between objects using javascript syntax and conventions. Consider implementing the standard variation of this pattern if appropriate for the use case.

Create a notification system for an e-commerce application that alerts different parts of the UI when the cart changes.
```

**Notes:** The Observer pattern is ideal for this scenario as it allows multiple UI components to subscribe to cart change events.

### Singleton pattern in Python

**Original Prompt:**
```
Create a database connection manager for a web application.
```

**Transformed Prompt:**
```
Apply the singleton design pattern in python to the following code generation task. Use the standard variation of this pattern where appropriate.

Implement a Singleton pattern to ensure only one instance of the class exists throughout the application using python syntax and conventions. Consider implementing the standard variation of this pattern if appropriate for the use case.

Create a database connection manager for a web application.
```

**Notes:** The Singleton pattern ensures only one database connection pool is created, preventing resource exhaustion.

## Transformation Details

**Base Instruction:** Apply the {pattern} design pattern in {language} to the following code generation task. Use the {variation} variation of this pattern where appropriate.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `pattern`:
  - When set to `singleton`: Implement a Singleton pattern to ensure only one instance of the class exists throughout the application.
  - When set to `factory`: Use a Factory pattern to create objects without specifying the exact class of object that will be created.
  - When set to `adapter`: Implement an Adapter pattern to allow incompatible interfaces to work together.
  - When set to `observer`: Use the Observer pattern to define a one-to-many dependency between objects.
  - When set to `strategy`: Implement the Strategy pattern to define a family of algorithms and make them interchangeable.
  - When set to `command`: Use the Command pattern to encapsulate a request as an object.
  - When set to `facade`: Implement a Facade pattern to provide a simplified interface to a complex subsystem.

- `language`:
  - Format: using {value} syntax and conventions

- `variation`:
  - Format: Consider implementing the {value} variation of this pattern if appropriate for the use case.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo, claude-2, llama-2-70b
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances DesignPattern CodeReview can be used after DesignPattern to evaluate the implementation quality.
- **CodeOptimization**: Enhances DesignPattern CodeOptimization can be applied after DesignPattern to improve performance while maintaining the pattern structure.
