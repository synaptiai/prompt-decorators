# Timeline Decorator

Organizes information in chronological order, highlighting key events or developments over time. This decorator is ideal for historical accounts, project planning, process evolution, or any topic with a temporal dimension.

**Category**: Structure

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `granularity` | `enum` | The level of time detail to include in the timeline | `year` |
| `format` | `enum` | The presentation format for the timeline | `list` |
| `details` | `enum` | The level of detail to include for each timeline event | `moderate` |

## Granularity Options

- `day`: Structure the timeline with day-level precision, including specific dates for events where relevant.
- `month`: Structure the timeline with month-level precision, grouping events by month and year.
- `year`: Structure the timeline with year-level precision, organizing events by year.
- `decade`: Structure the timeline by decades, grouping events into 10-year periods.
- `century`: Structure the timeline by centuries, organizing events into 100-year periods.
- `era`: Structure the timeline by broad historical eras or epochs, labeling each period appropriately.

## Format Options

- `list`: Present the timeline as a chronological list with clear dates/periods and descriptions for each entry.
- `narrative`: Present the timeline as a flowing narrative that moves chronologically through time while maintaining clear temporal markers.
- `table`: Present the timeline as a table with columns for date/period and description/events.

## Details Options

- `minimal`: For each timeline entry, include only the most essential information - key events, dates, and primary actors.
- `moderate`: For each timeline entry, include balanced information with important details, context, and significance.
- `comprehensive`: For each timeline entry, provide extensive details including background context, significance, consequences, and connections to other events.

## Examples

### Basic chronological timeline of major events

```
+++Timeline
Describe the key developments in artificial intelligence.
```

Presents a year-by-year list of important AI milestones and breakthroughs from earliest developments to present day

### Detailed narrative timeline with specific date granularity

```
+++Timeline(granularity=month, format=narrative, details=comprehensive)
What were the major events of the Apollo 11 mission?
```

Provides a flowing narrative account of the Apollo 11 mission with month/day dates and comprehensive details of each significant event

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create a chronological timeline that shows the sequence of events or developments. Include clear time markers ({granularity} level) and organize the information in {format} format. For each entry, provide {details} level of detail.

**Notes:** This model sometimes needs more explicit instructions to maintain consistent chronological ordering throughout a response


## Implementation Guidance

### Year-level timeline of AI developments

**Original Prompt:**
```
Describe the key developments in artificial intelligence.
```

**Transformed Prompt:**
```
Please organize your response as a timeline that presents information chronologically, highlighting key events or developments over time. Structure the timeline with year-level precision, organizing events by year. Present the timeline as a chronological list with clear dates/periods and descriptions for each entry. For each timeline entry, include balanced information with important details, context, and significance.

Describe the key developments in artificial intelligence.
```

### Detailed narrative of space mission by month

**Original Prompt:**
```
What were the major events of the Apollo 11 mission?
```

**Transformed Prompt:**
```
Please organize your response as a timeline that presents information chronologically, highlighting key events or developments over time. Structure the timeline with month-level precision, grouping events by month and year. Present the timeline as a flowing narrative that moves chronologically through time while maintaining clear temporal markers. For each timeline entry, provide extensive details including background context, significance, consequences, and connections to other events.

What were the major events of the Apollo 11 mission?
```

## Transformation Details

**Base Instruction:** Please organize your response as a timeline that presents information chronologically, highlighting key events or developments over time.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `granularity`:
  - When set to `day`: Structure the timeline with day-level precision, including specific dates for events where relevant.
  - When set to `month`: Structure the timeline with month-level precision, grouping events by month and year.
  - When set to `year`: Structure the timeline with year-level precision, organizing events by year.
  - When set to `decade`: Structure the timeline by decades, grouping events into 10-year periods.
  - When set to `century`: Structure the timeline by centuries, organizing events into 100-year periods.
  - When set to `era`: Structure the timeline by broad historical eras or epochs, labeling each period appropriately.

- `format`:
  - When set to `list`: Present the timeline as a chronological list with clear dates/periods and descriptions for each entry.
  - When set to `narrative`: Present the timeline as a flowing narrative that moves chronologically through time while maintaining clear temporal markers.
  - When set to `table`: Present the timeline as a table with columns for date/period and description/events.

- `details`:
  - When set to `minimal`: For each timeline entry, include only the most essential information - key events, dates, and primary actors.
  - When set to `moderate`: For each timeline entry, include balanced information with important details, context, and significance.
  - When set to `comprehensive`: For each timeline entry, provide extensive details including background context, significance, consequences, and connections to other events.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **StepByStep**: Enhances Timeline StepByStep can complement Timeline by clarifying the sequential nature of chronological events
- **TableFormat**: Enhances Timeline When Timeline uses table format, TableFormat can further refine the presentation with additional formatting options
