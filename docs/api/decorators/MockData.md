# MockData Decorator

Generates test fixtures and mock data for testing.

**Category**: Testing And Debugging

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `complexity` | enum | Sophistication of generated data | moderate |
| `format` | enum | Output format of the mock data | json |
| `size` | enum | Amount of mock data to generate | medium |

## Complexity Options

- `simple`: Create basic mock data with minimal fields and simple relationships.
- `moderate`: Generate mock data with reasonable complexity including relationships and varied field values.
- `complex`: Produce sophisticated mock data with complex relationships, edge cases, and realistic variations.

## Format Options

- `json`: Output the mock data in JSON format.
- `csv`: Output the mock data in CSV format.
- `sql`: Output the mock data as SQL insert statements.
- `code`: Output the mock data as code objects in a programming language appropriate to the context.
- `graphql`: Output the mock data in GraphQL format.

## Size Options

- `small`: Generate a small sample of 3-5 records per entity.
- `medium`: Generate a medium-sized dataset of 10-20 records per entity.
- `large`: Generate a large dataset of 50-100 records per entity.

## Examples

### Generating complex JSON mock data for an e-commerce system

```
+++MockData(complexity=complex, format=json, size=medium)
Generate mock data for an e-commerce system with users, products, orders, and reviews.
```

Returns a medium-sized set of complex, interconnected mock data in JSON format for an e-commerce system, including users, products, orders, and reviews with realistic relationships.

### Creating simple SQL test data

```
+++MockData(complexity=simple, format=sql, size=small)
Generate test data for a blog database with authors, posts, and comments.
```

Returns SQL insert statements for a small set of simple blog data including authors, posts, and comments tables.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create realistic mock data for testing purposes. The data should be fictional but plausible.

**Notes:** Simpler instruction for models with less context capacity.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeGeneration**: Enhances MockData MockData works well with CodeGeneration to create test fixtures within generated code.
- **DataAnalysis**: Enhances MockData MockData can provide test data for DataAnalysis examples.
