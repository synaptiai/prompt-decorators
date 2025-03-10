# Architecture Decorator

Generates architectural designs based on requirements and constraints.

**Category**: Architecture And Design

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `style` | enum | Architectural pattern | requirements-dependent |
| `detail` | enum | Level of design detail | component |
| `focus` | enum | Design emphasis | balanced |

## Style Options

- `microservices`: Design using a microservices architecture with loosely coupled, independently deployable services.
- `monolith`: Design using a monolithic architecture with a unified codebase and deployment unit.
- `serverless`: Design using a serverless architecture with function-as-a-service components.
- `event-driven`: Design using an event-driven architecture with asynchronous communication patterns.
- `layered`: Design using a layered architecture with clear separation of concerns between layers.
- `hexagonal`: Design using a hexagonal (ports and adapters) architecture to separate business logic from external concerns.
- `ddd`: Design using Domain-Driven Design principles with bounded contexts and a ubiquitous language.

## Detail Options

- `overview`: Provide a high-level architectural overview with major components and their relationships.
- `component`: Detail the component-level design including interfaces, responsibilities, and interactions.
- `detailed`: Create a detailed design including data structures, APIs, deployment considerations, and implementation guidance.

## Focus Options

- `scalability`: Optimize the architecture for scalability, ensuring it can handle increasing loads and users.
- `maintainability`: Optimize the architecture for maintainability, ensuring it can be easily understood and modified.
- `performance`: Optimize the architecture for performance, minimizing latency and maximizing throughput.
- `security`: Optimize the architecture for security, protecting against threats and vulnerabilities.
- `cost`: Optimize the architecture for cost-efficiency, minimizing resource usage and operational expenses.
- `balanced`: Balance all quality attributes including scalability, maintainability, performance, security, and cost.

## Examples

### Microservices architecture for a video streaming platform

```
+++Architecture(style=microservices, detail=component, focus=scalability)
Design an architecture for a video streaming platform that needs to support millions of concurrent users.
```

A component-level microservices architecture optimized for scalability, with separate services for user management, content delivery, recommendation engine, and analytics.

### Serverless architecture for an e-commerce application

```
+++Architecture(style=serverless, detail=detailed, focus=cost)
Design an architecture for an e-commerce platform that processes orders and manages inventory.
```

A detailed serverless architecture optimized for cost efficiency, using functions for order processing, inventory updates, and payment handling with appropriate data stores and API gateways.

### Event-driven architecture for a financial system

```
+++Architecture(style=event-driven, detail=overview, focus=security)
Design an architecture for a banking system that handles transactions and account management.
```

A high-level overview of an event-driven architecture optimized for security, showing event flows between account management, transaction processing, and notification components with security controls.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create an architectural design diagram and explanation for the following requirements. Consider the architectural style, level of detail, and focus areas specified.

**Notes:** For models with more limited context, simplify the architectural descriptions and focus on key components.

### gpt-4

**Instruction:** Generate a comprehensive architectural design that addresses the requirements and constraints. Include diagrams, component descriptions, interaction patterns, and justifications for your design decisions.

**Notes:** GPT-4 can handle more complex architectural descriptions and provide more detailed diagrams and rationales.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, claude-instant
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **SystemDesign**: Enhances Architecture Architecture decorator provides more specific architectural guidance that complements the broader system design approach.
- **TechnicalSpecification**: Enhances Architecture Architecture decorator can be used before TechnicalSpecification to establish the high-level design before detailing specifications.
