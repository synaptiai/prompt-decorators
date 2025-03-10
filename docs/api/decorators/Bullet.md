# Bullet Decorator

Formats the response as a bulleted list, making information easier to scan and digest. This decorator is ideal for presenting sequential steps, key points, or collections of related items in a clean, concise format.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `style` | enum | The visual marker used for bullet points | dash |
| `indented` | boolean | Whether to allow nested, indented bullet points | True |
| `compact` | boolean | Whether to keep bullet points short and concise (true) or allow longer, more detailed points (false) | False |

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

## Compatibility

- **Requires**: None
- **Conflicts**: OutputFormat
- **Compatible Models**: gpt-4, gpt-3.5-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **OutputFormat**: Conflicts with Bullet OutputFormat may specify a structure incompatible with bullet points
- **Outline**: Conflicts with Bullet Outline has its own structured format that conflicts with bullet points
