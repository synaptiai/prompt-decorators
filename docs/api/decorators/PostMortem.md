# PostMortem Decorator

Creates incident reviews and postmortem documents.

**Category**: Developer Workflow

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `format` | enum | Document structure | comprehensive |
| `focus` | enum | Analysis emphasis | balanced |
| `audience` | enum | Target readers | team |

## Format Options

- `timeline`: Structure the postmortem as a chronological timeline of events.
- `5-whys`: Use the 5 Whys technique to identify the root cause by repeatedly asking why the problem occurred.
- `fishbone`: Organize the analysis using a fishbone (Ishikawa) diagram approach to categorize potential causes.
- `comprehensive`: Create a comprehensive postmortem covering timeline, root cause analysis, impact assessment, and future prevention.

## Focus Options

- `what-happened`: Focus primarily on documenting what happened during the incident in detail.
- `why`: Emphasize root cause analysis and why the incident occurred.
- `prevention`: Concentrate on preventive measures and future safeguards.
- `balanced`: Provide balanced coverage of what happened, why it happened, and how to prevent recurrence.

## Audience Options

- `team`: Write for the technical team with appropriate technical details.
- `leadership`: Format for leadership with executive summary and business impact.
- `stakeholders`: Address concerns of all stakeholders with both technical and business perspectives.
- `public`: Create a public-facing document that explains the incident without revealing sensitive details.

## Examples

### Basic postmortem for a database outage

```
+++PostMortem(format=comprehensive, focus=balanced, audience=team)
Create a postmortem for the database outage we experienced yesterday that caused 45 minutes of downtime.
```

A comprehensive postmortem document analyzing the database outage, including timeline, root cause analysis, impact assessment, and preventive measures, written for a technical team audience.

### Executive-focused incident review

```
+++PostMortem(format=timeline, focus=prevention, audience=leadership)
Analyze the recent security breach that affected our customer data.
```

A timeline-based postmortem focused on prevention strategies, formatted for leadership with executive summary and business impact assessment.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create a detailed postmortem document for the incident. Include what happened, why it happened, and how to prevent it in the future.

**Notes:** Simplified instruction for models with more limited context windows.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **RootCauseAnalysis**: Enhances PostMortem RootCauseAnalysis can enhance the 'why' aspect of PostMortem analysis.
- **TechnicalDocumentation**: Enhances PostMortem TechnicalDocumentation can improve the structure and clarity of the postmortem document.
