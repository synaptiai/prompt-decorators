# Bullet Decorator

Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `style` | `enum` | The visual marker used for bullet points | `dash` |
| `indented` | `boolean` | Whether to allow nested, indented bullet points | `True` |
| `compact` | `boolean` | Whether to keep bullet points short and concise (true) or allow longer, more detailed points (false) | `False` |

## Style Options

- `dash`: Use dash markers (- ) for all bullet points.
- `dot`: Use dot markers (• ) for all bullet points.
- `arrow`: Use arrow markers (→ ) for all bullet points.
- `star`: Use star markers (★ ) for all bullet points.
- `plus`: Use plus markers (+ ) for all bullet points.

## Examples

### Basic bulleted list of key points

```
+++Bullet
What are the main factors to consider when buying a laptop?
```

Presents key laptop purchasing factors as a bulleted list with dash markers

### Compact star bullets with nesting disabled

```
+++Bullet(style=star, indented=false, compact=true)
List the benefits of regular exercise.
```

Provides a flat list of concise, star-bulleted points about exercise benefits, with no nested sub-points

## Implementation Guidance

### Standard dash bullets with indentation

**Original Prompt:**
```
What are the main factors to consider when buying a laptop?
```

**Transformed Prompt:**
```
Please format your response as a bulleted list to make the information easy to scan and digest. Use dash markers (- ) for all bullet points. Use hierarchical, indented sub-points where appropriate to show relationships between ideas. Allow detailed explanations in each bullet point when necessary.

What are the main factors to consider when buying a laptop?
```

### Compact star bullets with no indentation

**Original Prompt:**
```
List the benefits of regular exercise.
```

**Transformed Prompt:**
```
Please format your response as a bulleted list to make the information easy to scan and digest. Use star markers (★ ) for all bullet points. Use a flat list structure with no indentation or sub-points. Keep each bullet point concise - ideally one line per point.

List the benefits of regular exercise.
```

## Transformation Details

**Base Instruction:** Please format your response as a bulleted list to make the information easy to scan and digest.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `style`:
  - When set to `dash`: Use dash markers (- ) for all bullet points.
  - When set to `dot`: Use dot markers (• ) for all bullet points.
  - When set to `arrow`: Use arrow markers (→ ) for all bullet points.
  - When set to `star`: Use star markers (★ ) for all bullet points.
  - When set to `plus`: Use plus markers (+ ) for all bullet points.

- `indented`:
  - When set to `true`: Use hierarchical, indented sub-points where appropriate to show relationships between ideas.
  - When set to `false`: Use a flat list structure with no indentation or sub-points.

- `compact`:
  - When set to `true`: Keep each bullet point concise - ideally one line per point.
  - When set to `false`: Allow detailed explanations in each bullet point when necessary.

## Compatibility

- **Requires**: None
- **Conflicts**: OutputFormat
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **OutputFormat**: Conflicts with Bullet OutputFormat may specify a structure incompatible with bullet points
- **Outline**: Conflicts with Bullet Outline has its own structured format that conflicts with bullet points
