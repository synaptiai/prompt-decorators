# APIDesign Decorator

Designs API interfaces focusing on specific qualities.

**Category**: Architecture And Design

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `style` | enum | API architectural style | rest |
| `focus` | enum | Design priority | developer-experience |
| `documentation` | enum | Documentation approach | style-appropriate |

## Style Options

- `rest`: Design a RESTful API with appropriate resource-oriented endpoints, HTTP methods, and status codes.
- `graphql`: Design a GraphQL API with a well-structured schema, queries, mutations, and resolvers.
- `grpc`: Design a gRPC API with efficient protocol buffers and service definitions.
- `soap`: Design a SOAP API with appropriate XML schemas and WSDL definitions.
- `websocket`: Design a WebSocket API for real-time bidirectional communication.
- `webhook`: Design a webhook-based API for event-driven architectures.

## Focus Options

- `consistency`: Prioritize consistency in naming conventions, response formats, and error handling across all endpoints.
- `performance`: Optimize for performance with efficient data transfer, pagination, and caching strategies.
- `developer-experience`: Prioritize developer experience with intuitive endpoints, comprehensive documentation, and helpful error messages.
- `backward-compatibility`: Ensure backward compatibility through careful versioning and deprecation strategies.

## Documentation Options

- `openapi`: Document the API using OpenAPI/Swagger specifications.
- `graphql-schema`: Document the API using GraphQL schema language and introspection.
- `protobuf`: Document the API using Protocol Buffer definitions.
- `custom`: Create custom documentation that clearly explains all endpoints, parameters, and responses.
- `style-appropriate`: Use the documentation format most appropriate for the chosen API style.

## Examples

### Designing a GraphQL API for a content management system

```
+++APIDesign(style=graphql, focus=developer-experience, documentation=graphql-schema)
Design a GraphQL API for a content management system that prioritizes a great developer experience.
```

A comprehensive GraphQL API design for a CMS with a focus on developer experience, including schema definitions, query/mutation examples, and GraphQL-specific documentation.

### Designing a REST API focused on performance

```
+++APIDesign(style=rest, focus=performance)
Design an API for a high-traffic e-commerce platform.
```

A RESTful API design optimized for performance, with caching strategies, pagination, and efficient data transfer patterns.

### Designing a gRPC API with backward compatibility

```
+++APIDesign(style=grpc, focus=backward-compatibility, documentation=protobuf)
Design an API for a microservice architecture that needs to maintain compatibility with existing clients.
```

A gRPC API design with Protocol Buffer definitions that emphasizes versioning strategies and backward compatibility approaches.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Design an API following these specific requirements: {style} architecture, focusing on {focus}, with {documentation} documentation approach. Consider endpoints, data formats, error handling, and authentication.

**Notes:** Simplified instruction for models with more limited context windows.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, claude-instant
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **SystemDesign**: Enhances APIDesign APIDesign works well with SystemDesign by focusing on the API layer of a larger system architecture.
- **DatabaseDesign**: Enhances APIDesign APIDesign can be combined with DatabaseDesign to create a complete data access solution.
