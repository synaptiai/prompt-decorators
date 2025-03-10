# TypeDefinition Decorator

Generates type definitions for improved code safety and documentation.

**Category**: Code Generation

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `system` | enum | Type system or annotation format | language-appropriate |
| `strictness` | enum | Level of type enforcement | moderate |
| `style` | enum | Type definition pattern | language-convention |

## System Options

- `typescript`: Use TypeScript's static type system with interfaces, type aliases, and generics as appropriate.
- `flow`: Apply Flow type annotations with appropriate syntax and features.
- `jsdoc`: Create JSDoc comments with type annotations for JavaScript code.
- `python-typing`: Implement Python's typing module annotations for type hints.
- `java-generics`: Use Java's generic type system with appropriate class and interface definitions.

## Strictness Options

- `loose`: Allow some type flexibility and implicit conversions where reasonable.
- `moderate`: Balance type safety with pragmatic flexibility, using union types where appropriate.
- `strict`: Enforce rigorous type checking with no implicit conversions and exhaustive type coverage.

## Style Options

- `inline`: Define types directly within the code as inline annotations.
- `declaration-file`: Create separate declaration files for type definitions.
- `interface-based`: Prefer interfaces over other type constructs when possible.
- `type-alias`: Use type aliases as the primary means of type definition.
- `generics`: Leverage generic types extensively for maximum reusability.

## Examples

### TypeScript interface-based type definitions for an e-commerce application

```
+++TypeDefinition(system=typescript, strictness=strict, style=interface-based)
Define types for an e-commerce application's product catalog and shopping cart.
```

The model will generate TypeScript interfaces with strict type checking for product catalog and shopping cart functionality.

### Python type annotations for a data processing pipeline

```
+++TypeDefinition(system=python-typing, strictness=moderate)
Create a data processing pipeline that handles CSV files and outputs JSON.
```

The model will generate Python code with appropriate type annotations from the typing module, with a moderate level of strictness.

## Model-Specific Implementations

### gpt-4o

**Instruction:** Generate comprehensive type definitions for the code according to the specified parameters. Focus on creating clear, well-structured types that enhance code safety and documentation. Consider edge cases and ensure type definitions are complete and accurate.

**Notes:** gpt-4o has stronger capabilities for understanding complex type systems and can handle more nuanced type definitions.


## Implementation Guidance

### TypeScript e-commerce application

**Original Prompt:**
```
Define types for an e-commerce application's product catalog and shopping cart.
```

**Transformed Prompt:**
```
Generate type definitions for the code according to the specified parameters. Focus on creating clear, well-structured types that enhance code safety and documentation. Use TypeScript's static type system with interfaces, type aliases, and generics as appropriate. Enforce rigorous type checking with no implicit conversions and exhaustive type coverage. Prefer interfaces over other type constructs when possible.

Define types for an e-commerce application's product catalog and shopping cart.
```

**Notes:** The decorator adds specific instructions for TypeScript with strict type checking and interface-based style.

## Transformation Details

**Base Instruction:** Generate type definitions for the code according to the specified parameters. Focus on creating clear, well-structured types that enhance code safety and documentation.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `system`:
  - When set to `typescript`: Use TypeScript's static type system with interfaces, type aliases, and generics as appropriate.
  - When set to `flow`: Apply Flow type annotations with appropriate syntax and features.
  - When set to `jsdoc`: Create JSDoc comments with type annotations for JavaScript code.
  - When set to `python-typing`: Implement Python's typing module annotations for type hints.
  - When set to `java-generics`: Use Java's generic type system with appropriate class and interface definitions.

- `strictness`:
  - When set to `loose`: Allow some type flexibility and implicit conversions where reasonable.
  - When set to `moderate`: Balance type safety with pragmatic flexibility, using union types where appropriate.
  - When set to `strict`: Enforce rigorous type checking with no implicit conversions and exhaustive type coverage.

- `style`:
  - When set to `inline`: Define types directly within the code as inline annotations.
  - When set to `declaration-file`: Create separate declaration files for type definitions.
  - When set to `interface-based`: Prefer interfaces over other type constructs when possible.
  - When set to `type-alias`: Use type aliases as the primary means of type definition.
  - When set to `generics`: Leverage generic types extensively for maximum reusability.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, gemini-pro
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeGeneration**: Enhances TypeDefinition TypeDefinition enhances CodeGeneration by adding strong typing to generated code.
- **Documentation**: Enhances TypeDefinition Type definitions serve as implicit documentation for code structure.
