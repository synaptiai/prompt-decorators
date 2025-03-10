# Interface Decorator

Generates interface definitions for APIs, libraries, or components.

**Category**: Code Generation

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `style` | enum | Interface paradigm or API style | context-dependent |
| `verbosity` | enum | Level of documentation detail | documented |
| `format` | enum | Output format of the interface | context-dependent |

## Style Options

- `rest`: Use REST API design principles with appropriate HTTP methods and resource-based URLs.
- `graphql`: Design a GraphQL schema with types, queries, and mutations.
- `rpc`: Create an RPC-style interface with clearly defined methods and parameters.
- `soap`: Define a SOAP web service interface with XML schema definitions.
- `class`: Design an object-oriented class interface with methods and properties.
- `function`: Create a functional programming interface with pure functions.
- `event-driven`: Design an event-driven interface with events, subscribers, and handlers.

## Verbosity Options

- `minimal`: Include only essential documentation with brief descriptions.
- `documented`: Provide standard documentation with descriptions for all elements and parameters.
- `extensive`: Include comprehensive documentation with examples, edge cases, and implementation notes.

## Format Options

- `code`: Output as implementation code in the most appropriate language.
- `openapi`: Output as an OpenAPI/Swagger specification.
- `schema`: Output as a schema definition (JSON Schema, XML Schema, etc.).
- `typescript`: Output as TypeScript interface definitions.

## Examples

### REST API for user management

```
+++Interface(style=rest, verbosity=extensive, format=openapi)
Create an API interface for a user management service with authentication, user profiles, and role management.
```

Generates a comprehensive OpenAPI specification for a RESTful user management API with detailed documentation.

### GraphQL API with minimal documentation

```
+++Interface(style=graphql, verbosity=minimal)
Design an e-commerce product catalog API.
```

Produces a GraphQL schema for an e-commerce product catalog with essential documentation.

### TypeScript class interface

```
+++Interface(style=class, format=typescript)
Create a data structure for a task management system.
```

Generates TypeScript interfaces and classes for a task management system with standard documentation.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a well-structured interface definition following these specifications:

**Notes:** For gpt-4, more explicit instructions about structure may be needed.

### claude-3-7-sonnet-latest

**Instruction:** Design a clear and comprehensive interface with these parameters:

**Notes:** Claude models may benefit from more emphasis on comprehensive documentation.


## Implementation Guidance

### REST API design

**Original Prompt:**
```
Create an API interface for a user management service with authentication, user profiles, and role management.
```

**Transformed Prompt:**
```
Generate an interface definition with the following characteristics:
Interface style: rest
Documentation level: extensive
Output format: openapi

Create an API interface for a user management service with authentication, user profiles, and role management.
```

**Notes:** The decorator transforms the prompt to specify REST API design with extensive documentation in OpenAPI format.

### Class interface design

**Original Prompt:**
```
Design a data structure for managing a shopping cart.
```

**Transformed Prompt:**
```
Generate an interface definition with the following characteristics:
Interface style: class
Documentation level: documented
Output format: typescript

Design a data structure for managing a shopping cart.
```

**Notes:** The decorator transforms the prompt to specify a class-based interface with standard documentation in TypeScript.

## Transformation Details

**Base Instruction:** Generate an interface definition with the following characteristics:

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `style`:
  - When set to `rest`: Use REST API design principles with appropriate HTTP methods and resource-based URLs.
  - When set to `graphql`: Design a GraphQL schema with types, queries, and mutations.
  - When set to `rpc`: Create an RPC-style interface with clearly defined methods and parameters.
  - When set to `soap`: Define a SOAP web service interface with XML schema definitions.
  - When set to `class`: Design an object-oriented class interface with methods and properties.
  - When set to `function`: Create a functional programming interface with pure functions.
  - When set to `event-driven`: Design an event-driven interface with events, subscribers, and handlers.
  - Format: Interface style: {value}

- `verbosity`:
  - When set to `minimal`: Include only essential documentation with brief descriptions.
  - When set to `documented`: Provide standard documentation with descriptions for all elements and parameters.
  - When set to `extensive`: Include comprehensive documentation with examples, edge cases, and implementation notes.
  - Format: Documentation level: {value}

- `format`:
  - When set to `code`: Output as implementation code in the most appropriate language.
  - When set to `openapi`: Output as an OpenAPI/Swagger specification.
  - When set to `schema`: Output as a schema definition (JSON Schema, XML Schema, etc.).
  - When set to `typescript`: Output as TypeScript interface definitions.
  - Format: Output format: {value}

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeReview**: Enhances Interface CodeReview can be applied after Interface to evaluate the generated interface design.
- **LanguageSpecific**: Enhances Interface LanguageSpecific can refine the output to target a specific programming language.
