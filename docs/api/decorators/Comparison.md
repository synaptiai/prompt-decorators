# Comparison Decorator

Structures the response as a direct comparison between multiple items, concepts, or approaches. This decorator is ideal for highlighting similarities and differences across specific dimensions or criteria.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `aspects` | array | Specific aspects or dimensions to compare |  |
| `format` | enum | The presentation format for the comparison | table |
| `highlight` | boolean | Whether to explicitly emphasize key differences | True |

## Format Options

- `table`: Present the comparison in a tabular format with items as columns (or rows) and comparison aspects as rows (or columns).
- `prose`: Present the comparison as flowing paragraphs that discuss each aspect across all items in a narrative style.
- `bullets`: Present the comparison as bulleted lists grouped by aspect or by item.

## Examples

### Basic tabular comparison of specific aspects

```
+++Comparison(aspects=[performance,cost,ease of use,ecosystem])
Compare React, Angular, and Vue for front-end development.
```

Creates a table comparing React, Angular, and Vue across the specified aspects, with key differences highlighted

### Prose-based comparison without specific aspects

```
+++Comparison(format=prose, highlight=false)
Compare democracy and authoritarianism as political systems.
```

Delivers a flowing prose comparison between democracy and authoritarianism, covering key differences and similarities in paragraph form

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create a direct comparison between the items/concepts mentioned in the question. Use {format} format and compare them along {aspects} dimensions. {highlight}

**Notes:** This model sometimes needs more explicit structure for complex multi-dimensional comparisons


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **TableFormat**: Enhances Comparison When using table format, TableFormat can provide additional formatting options for the comparison table
- **Balanced**: Enhances Comparison Balanced works well with Comparison to ensure fair treatment of each item being compared
