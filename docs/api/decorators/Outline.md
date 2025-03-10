# Outline Decorator

Structures the response as a hierarchical outline with headings and subheadings. This decorator organizes information in a clear, logical structure that highlights relationships between main topics and subtopics.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `depth` | number | Maximum nesting level of the outline | 3 |
| `style` | enum | Numbering or bullet style for the outline | numeric |
| `detailed` | boolean | Whether to include brief explanations under each outline point | False |

## Style Options

- `numeric`: Use numeric notation (1, 1.1, 1.1.1, etc.) for all outline levels.
- `bullet`: Use bullet point notation (•, ○, ▪, etc.) for all outline levels.
- `roman`: Use Roman numeral notation (I, II, III, etc. for top level, then A, B, C, etc. for second level).
- `alpha`: Use alphabetical notation (A, B, C, etc. for top level, then 1, 2, 3, etc. for second level).
- `mixed`: Use a mix of notation styles: numbers for level 1, letters for level 2, Roman numerals for level 3, etc.

## Examples

### Simple numeric outline of a complex topic

```
+++Outline
Explain the structure of the United States government.
```

Presents the US government structure as a numbered outline with up to 3 levels of hierarchy

### Detailed outline with mixed notation and deep hierarchy

```
+++Outline(style=mixed, depth=5, detailed=true)
Provide a comprehensive overview of machine learning techniques.
```

Creates a 5-level deep outline using mixed notation (numbers, letters, roman numerals) with brief explanations under each point, covering machine learning techniques

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Format your response as an outline with clear hierarchical structure. Use headings and subheadings with consistent formatting for each level.

**Notes:** This model may need more explicit instructions about maintaining consistent outline formatting


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Bullet**: Conflicts with Outline Bullet and Outline both specify different formatting structures that may conflict
- **StepByStep**: Enhances Outline Outline can complement StepByStep by providing a structured overview of the steps
