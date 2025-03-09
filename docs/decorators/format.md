# Output Format Decorators

This section documents decorators that control the structure and formatting of responses in the Prompt Decorators framework.

## OutputFormat

The `OutputFormat` decorator specifies the overall format for the output.

**Category**: Format

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `format` | enum | The output format (e.g., "text", "markdown", "json", "yaml", "html", "csv") | "markdown" |
| `schema` | string | Optional schema for structured formats like JSON | "" |
| `pretty` | boolean | Whether to format the output with proper indentation and spacing | true |

**Example**:

```
+++OutputFormat(format="json", pretty=true)
List the top 5 programming languages and their key features.
```

**Compatible with**: Most other decorators

## Bullet

The `Bullet` decorator formats output as a bulleted list.

**Category**: Format

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `style` | enum | The bullet style to use (e.g., "dash", "asterisk", "dot", "number", "letter") | "dash" |
| `max_items` | integer | Maximum number of bullet points | 10 |
| `hierarchical` | boolean | Whether to allow nested bullet points | true |
| `intro` | boolean | Whether to include an introductory sentence before the list | true |

**Example**:

```
+++Bullet(style="asterisk", max_items=7)
What are the main benefits of exercise?
```

**Compatible with**: Most other decorators, may conflict with `OutputFormat(format="json")`

## TableFormat

The `TableFormat` decorator formats output as a table.

**Category**: Format

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `columns` | string | Comma-separated list of column names | "" |
| `alignment` | string | Alignment for columns (e.g., "left", "center", "right") | "left" |
| `max_rows` | integer | Maximum number of rows | 10 |
| `include_header` | boolean | Whether to include a header row | true |
| `format` | enum | Table format style (e.g., "markdown", "ascii", "html") | "markdown" |

**Example**:

```
+++TableFormat(columns="Country,Capital,Population", max_rows=5)
List the largest countries by population.
```

**Compatible with**: Most other decorators, may conflict with other format decorators

## Outline

The `Outline` decorator structures output as a hierarchical outline.

**Category**: Format

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `depth` | integer | Maximum depth of the outline | 3 |
| `numbering` | boolean | Whether to use numbering (true) or bullets (false) | true |
| `expand_level` | integer | Default level to expand with details | 2 |
| `intro` | boolean | Whether to include an introduction before the outline | true |

**Example**:

```
+++Outline(depth=3, numbering=true)
Explain the structure of a typical novel.
```

**Compatible with**: Most reasoning decorators, may conflict with other format decorators

## Summary

The `Summary` decorator provides a concise summary of a longer response.

**Category**: Format

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `length` | enum | The length of the summary (e.g., "brief", "moderate", "comprehensive") | "moderate" |
| `position` | enum | Where to place the summary (e.g., "start", "end", "both") | "start" |
| `bullet_points` | boolean | Whether to format the summary as bullet points | false |
| `include_details` | boolean | Whether to include the detailed response after the summary | true |

**Example**:

```
+++Summary(length="brief", position="start", bullet_points=true)
Explain quantum computing.
```

**Compatible with**: Most other decorators

## Schema

The `Schema` decorator formats output according to a specific schema or data structure.

**Category**: Format

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `format` | enum | The schema format (e.g., "json", "yaml", "xml") | "json" |
| `schema` | string | The schema definition as a string | "" |
| `example` | string | Optional example of the expected output format | "" |
| `strict` | boolean | Whether to enforce strict schema compliance | true |

**Example**:

```
+++Schema(format="json", schema='{"name": "string", "age": "number", "skills": "string[]"}')
Describe a fictional programmer named Alice.
```

**Compatible with**: May conflict with other format decorators

## Nested

The `Nested` decorator allows for hierarchical structuring of content.

**Category**: Format

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `levels` | integer | Number of hierarchical levels | 3 |
| `format` | enum | Format for each level (e.g., "headings", "bullets", "numbers") | "headings" |
| `collapse` | boolean | Whether to suggest collapsible sections in supported formats | false |
| `details_depth` | integer | Maximum depth for detailed content | 2 |

**Example**:

```
+++Nested(levels=3, format="headings")
Explain the organization of a modern operating system.
```

**Compatible with**: Many reasoning decorators, may conflict with other format decorators

## Priority

The `Priority` decorator organizes information by priority or importance.

**Category**: Format

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `levels` | integer | Number of priority levels | 3 |
| `display` | enum | How to display priorities (e.g., "numbers", "labels", "symbols") | "labels" |
| `descending` | boolean | Whether to list in descending priority (highest first) | true |
| `criteria` | string | Criteria for determining priority | "importance" |

**Example**:

```
+++Priority(levels=3, display="labels")
What should I consider when buying a laptop?
```

**Compatible with**: Most other decorators

## MECE

The `MECE` (Mutually Exclusive, Collectively Exhaustive) decorator organizes information into comprehensive, non-overlapping categories.

**Category**: Format

**Parameters**:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `categories` | integer | Target number of categories | 5 |
| `format` | enum | Format for categories (e.g., "headings", "sections", "cards") | "headings" |
| `justify` | boolean | Whether to justify the MECE classification | true |
| `hierarchical` | boolean | Whether to allow hierarchical categorization | false |

**Example**:

```
+++MECE(categories=4, justify=true)
What are the different approaches to artificial intelligence?
```

**Compatible with**: Most reasoning decorators

## Using Format Decorators

Format decorators can be combined with other types of decorators to control both content and presentation:

```
+++Reasoning(approach="comprehensive")
+++OutputFormat(format="markdown")
+++Bullet(style="number")
Explain the advantages and disadvantages of microservices architecture.
```

This combines comprehensive reasoning with markdown formatting and numbered bullets.

## Choosing the Right Format

When selecting a format decorator, consider:

1. **Audience needs**: What format will be most useful to your audience?
2. **Content type**: What format best suits the type of information you're presenting?
3. **Compatibility**: Which format works best with your other decorators?
4. **Technical requirements**: Do you need machine-readable output (like JSON) or human-readable presentation?

## See Also

- [Reasoning Decorators](reasoning.md)
- [Style Decorators](style.md)
- [Creating Custom Format Decorators](../tutorials/creating_custom_decorator.md)
