# TableFormat Decorator

Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `columns` | array | List of column names for the table | Required |
| `format` | enum | Format style for the table representation | markdown |
| `alignment` | enum | Text alignment within table cells | left |

## Format Options

- `markdown`: Format the table using markdown syntax with headers and cell separators (e.g., | Column1 | Column2 |).
- `ascii`: Format the table using ASCII characters for borders and separators to create a plain text table.
- `csv`: Format the table as comma-separated values (CSV) with each row on a new line and values separated by commas.

## Alignment Options

- `left`: Align all text within cells to the left.
- `center`: Center all text within cells.
- `right`: Align all text within cells to the right.

## Examples

### Simple comparison table in markdown format

```
+++TableFormat(columns=[Feature, TypeScript, JavaScript])
Compare TypeScript and JavaScript features.
```

Presents a markdown table comparing features of TypeScript and JavaScript with three columns

### Detailed CSV table with specific columns

```
+++TableFormat(columns=[Planet, Diameter, Distance from Sun, Orbital Period, Number of Moons], format=csv)
List the planets in our solar system with their key characteristics.
```

Generates a CSV-formatted table containing detailed information about each planet with the specified columns

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create a table with these columns: {columns}. Use {format} formatting and make sure all columns are properly aligned and formatted consistently.

**Notes:** This model sometimes needs more explicit instructions to maintain consistent table formatting throughout the response


## Compatibility

- **Requires**: None
- **Conflicts**: OutputFormat
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **OutputFormat**: Conflicts with TableFormat OutputFormat may specify a different structure that conflicts with TableFormat's tabular presentation
- **Bullet**: Conflicts with TableFormat Bullet's list structure conflicts with TableFormat's tabular organization
