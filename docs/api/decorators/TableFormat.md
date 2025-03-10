# TableFormat Decorator

Structures the AI's response in a tabular format with defined columns. This decorator is ideal for presenting comparative data, lists of items with attributes, or any information that benefits from clear columnar organization.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `columns` | `array` | List of column names for the table | `Required` |
| `format` | `enum` | Format style for the table representation | `markdown` |
| `alignment` | `enum` | Text alignment within table cells | `left` |

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

### gpt-4-turbo

**Instruction:** Create a table with these columns: {columns}. Use {format} formatting and make sure all columns are properly aligned and formatted consistently.

**Notes:** This model sometimes needs more explicit instructions to maintain consistent table formatting throughout the response


## Implementation Guidance

### Markdown table for comparison

**Original Prompt:**
```
Compare TypeScript and JavaScript features.
```

**Transformed Prompt:**
```
Please present your response in a tabular format with clearly defined columns to organize the information effectively. The table should include the following columns: Feature, TypeScript, JavaScript. Format the table using markdown syntax with headers and cell separators (e.g., | Column1 | Column2 |). Align all text within cells to the left.

Compare TypeScript and JavaScript features.
```

### CSV table for planets data

**Original Prompt:**
```
List the planets in our solar system with their key characteristics.
```

**Transformed Prompt:**
```
Please present your response in a tabular format with clearly defined columns to organize the information effectively. The table should include the following columns: Planet, Diameter, Distance from Sun, Orbital Period, Number of Moons. Format the table as comma-separated values (CSV) with each row on a new line and values separated by commas. Align all text within cells to the left.

List the planets in our solar system with their key characteristics.
```

## Transformation Details

**Base Instruction:** Please present your response in a tabular format with clearly defined columns to organize the information effectively.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `columns`:
  - Format: The table should include the following columns: {value}.

- `format`:
  - When set to `markdown`: Format the table using markdown syntax with headers and cell separators (e.g., | Column1 | Column2 |).
  - When set to `ascii`: Format the table using ASCII characters for borders and separators to create a plain text table.
  - When set to `csv`: Format the table as comma-separated values (CSV) with each row on a new line and values separated by commas.

- `alignment`:
  - When set to `left`: Align all text within cells to the left.
  - When set to `center`: Center all text within cells.
  - When set to `right`: Align all text within cells to the right.

## Compatibility

- **Requires**: None
- **Conflicts**: OutputFormat
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **OutputFormat**: Conflicts with TableFormat OutputFormat may specify a different structure that conflicts with TableFormat's tabular presentation
- **Bullet**: Conflicts with TableFormat Bullet's list structure conflicts with TableFormat's tabular organization
