# Nested Decorator

Organizes information in a deeply hierarchical structure with multiple levels of nesting. This decorator is ideal for complex topics with many subcategories, helping to maintain clarity through consistent organization patterns.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `depth` | number | Maximum nesting level of the hierarchy | 3 |
| `style` | enum | Visual style for hierarchical levels | mixed |
| `collapsible` | boolean | Whether to suggest the hierarchy could be rendered as collapsible sections (for UI implementations) | False |

## Style Options

- `bullet`: Use bullet points (•, ○, ■, □, etc.) consistently throughout all hierarchical levels.
- `numbered`: Use numbered lists (1., 1.1., 1.1.1., etc.) consistently throughout all hierarchical levels.
- `mixed`: Use a mix of formatting styles: numbers for top level (1., 2., etc.), letters for second level (a., b., etc.), and bullets for deeper levels.

## Examples

### Deep hierarchical organization of a complex domain

```
+++Nested
Explain the classification of living organisms.
```

Presents taxonomy in a nested hierarchy with domains, kingdoms, phyla, etc., using mixed notation styles for different levels

### Maximum depth collapsible structure for reference material

```
+++Nested(depth=5, style=bullet, collapsible=true)
Provide a comprehensive overview of programming paradigms.
```

Creates a 5-level deep bullet-point hierarchy of programming paradigms, designed to be rendered as collapsible sections

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a {depth}-level deep hierarchical structure for this topic. Use {style} formatting for the levels. Each level should contain more specific details than its parent level. Make sure the categories are logical and properly nested. {collapsible}

**Notes:** This model may need additional guidance to maintain consistent depth across all branches of the hierarchy


## Implementation Guidance

### Nested taxonomy explanation

**Original Prompt:**
```
Explain the classification of living organisms.
```

**Transformed Prompt:**
```
Please organize your response in a deeply hierarchical structure with clearly defined levels of nesting. Create a logical progression from major categories down to granular subcategories, maintaining consistent organization patterns throughout. Structure your response with 3 levels of nesting, where the information hierarchy reveals increasingly specific details at each level. Use a mix of formatting styles: numbers for top level (1., 2., etc.), letters for second level (a., b., etc.), and bullets for deeper levels. Present the full hierarchy with all levels visible simultaneously.

Explain the classification of living organisms.
```

### Collapsible programming paradigms overview

**Original Prompt:**
```
Provide a comprehensive overview of programming paradigms.
```

**Transformed Prompt:**
```
Please organize your response in a deeply hierarchical structure with clearly defined levels of nesting. Create a logical progression from major categories down to granular subcategories, maintaining consistent organization patterns throughout. Structure your response with 5 levels of nesting, where the information hierarchy reveals increasingly specific details at each level. Use bullet points (•, ○, ■, □, etc.) consistently throughout all hierarchical levels. Design the hierarchy to work as collapsible sections, where each parent category could expand to show child categories.

Provide a comprehensive overview of programming paradigms.
```

## Transformation Details

**Base Instruction:** Please organize your response in a deeply hierarchical structure with clearly defined levels of nesting. Create a logical progression from major categories down to granular subcategories, maintaining consistent organization patterns throughout.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `depth`:
  - Format: Structure your response with {value} levels of nesting, where the information hierarchy reveals increasingly specific details at each level.

- `style`:
  - When set to `bullet`: Use bullet points (•, ○, ■, □, etc.) consistently throughout all hierarchical levels.
  - When set to `numbered`: Use numbered lists (1., 1.1., 1.1.1., etc.) consistently throughout all hierarchical levels.
  - When set to `mixed`: Use a mix of formatting styles: numbers for top level (1., 2., etc.), letters for second level (a., b., etc.), and bullets for deeper levels.

- `collapsible`:
  - When set to `true`: Design the hierarchy to work as collapsible sections, where each parent category could expand to show child categories.
  - When set to `false`: Present the full hierarchy with all levels visible simultaneously.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Outline**: Enhances Nested Nested provides deeper hierarchical structure to Outline's organizational framework
- **MECE**: Enhances Nested MECE ensures categories in the Nested hierarchy are mutually exclusive and collectively exhaustive
- **Schema**: Enhances Nested Schema can provide a consistent data structure for each level of the Nested hierarchy
