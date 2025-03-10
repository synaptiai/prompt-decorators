# DataModel Decorator

Designs data models, schemas, and database structures.

**Category**: Architecture And Design

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `type` | `enum` | Database or persistence paradigm | `context-dependent` |
| `optimization` | `enum` | Performance optimization focus | `balanced` |
| `format` | `enum` | Output format | `schema` |

## Type Options

- `relational`: Use relational database design principles with normalized tables, primary keys, and foreign keys.
- `document`: Design a document-oriented schema with embedded documents and references where appropriate.
- `graph`: Create a graph data model with nodes, relationships, and properties to represent the domain.
- `key-value`: Design a key-value storage structure with efficient access patterns.
- `time-series`: Develop a time-series data model optimized for temporal data and time-based queries.
- `hybrid`: Combine multiple database paradigms in a polyglot persistence architecture.

## Optimization Options

- `reads`: Optimize the data model for read-heavy operations, considering denormalization where appropriate.
- `writes`: Optimize the data model for write-heavy operations, focusing on insertion and update efficiency.
- `storage`: Optimize the data model for storage efficiency, minimizing redundancy and space requirements.
- `balanced`: Balance the data model for general-purpose use with reasonable performance across reads, writes, and storage.

## Format Options

- `erd`: Present the result as an Entity-Relationship Diagram with entities, relationships, and cardinality.
- `schema`: Present the result as a formal schema definition.
- `code`: Present the result as implementation code (ORM, schema definition, etc.).
- `diagram`: Present the result as a visual diagram with appropriate notation.
- `ddl`: Present the result as Data Definition Language (DDL) statements.

## Examples

### Designing a relational database schema for a social media platform

```
+++DataModel(type=relational, optimization=reads, format=erd)
Design a data model for a social media platform with users, posts, comments, and likes.
```

An Entity-Relationship Diagram showing the structure of a relational database optimized for read operations, with entities for users, posts, comments, and likes, including their relationships and attributes.

### Creating a document database schema for a content management system

```
+++DataModel(type=document, format=schema)
Design a data model for a content management system with articles, categories, tags, and users.
```

A document schema definition showing collections for articles, categories, tags, and users, with embedded documents and references appropriate for a document database.

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a detailed data model with the following specifications. Include all necessary entities, relationships, attributes, and constraints for the domain.

**Notes:** More explicit instruction for models with less context understanding.


## Implementation Guidance

### Designing a relational database for an e-commerce platform

**Original Prompt:**
```
Design a data model for an e-commerce platform with products, customers, orders, and reviews.
```

**Transformed Prompt:**
```
Design a data model based on the following requirements. Consider appropriate entities, relationships, attributes, and constraints. Use relational database design principles with normalized tables, primary keys, and foreign keys. Optimize the data model for read-heavy operations, considering denormalization where appropriate. Present the result as an Entity-Relationship Diagram with entities, relationships, and cardinality.

Design a data model for an e-commerce platform with products, customers, orders, and reviews.
```

**Notes:** The decorator adds specific guidance for a relational database optimized for reads and presented as an ERD.

## Transformation Details

**Base Instruction:** Design a data model based on the following requirements. Consider appropriate entities, relationships, attributes, and constraints.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `type`:
  - When set to `relational`: Use relational database design principles with normalized tables, primary keys, and foreign keys.
  - When set to `document`: Design a document-oriented schema with embedded documents and references where appropriate.
  - When set to `graph`: Create a graph data model with nodes, relationships, and properties to represent the domain.
  - When set to `key-value`: Design a key-value storage structure with efficient access patterns.
  - When set to `time-series`: Develop a time-series data model optimized for temporal data and time-based queries.
  - When set to `hybrid`: Combine multiple database paradigms in a polyglot persistence architecture.

- `optimization`:
  - When set to `reads`: Optimize the data model for read-heavy operations, considering denormalization where appropriate.
  - When set to `writes`: Optimize the data model for write-heavy operations, focusing on insertion and update efficiency.
  - When set to `storage`: Optimize the data model for storage efficiency, minimizing redundancy and space requirements.
  - When set to `balanced`: Balance the data model for general-purpose use with reasonable performance across reads, writes, and storage.

- `format`:
  - When set to `erd`: Present the result as an Entity-Relationship Diagram with entities, relationships, and cardinality.
  - When set to `schema`: Present the result as a formal schema definition.
  - When set to `code`: Present the result as implementation code (ORM, schema definition, etc.).
  - When set to `diagram`: Present the result as a visual diagram with appropriate notation.
  - When set to `ddl`: Present the result as Data Definition Language (DDL) statements.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **SystemDesign**: Enhances DataModel DataModel works well with SystemDesign to create comprehensive technical specifications.
- **CodeImplementation**: Enhances DataModel DataModel can provide the schema design that CodeImplementation can then implement.
