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

### gpt-4-turbo

**Instruction:** Create a detailed postmortem document for the incident. Include what happened, why it happened, and how to prevent it in the future.

**Notes:** Simplified instruction for models with more limited context windows.


## Implementation Guidance

### Software development team

**Original Prompt:**
```
Create a postmortem for the database outage we experienced yesterday that caused 45 minutes of downtime.
```

**Transformed Prompt:**
```
Create a detailed postmortem document that analyzes the incident, identifies root causes, and proposes preventive measures. Create a comprehensive postmortem covering timeline, root cause analysis, impact assessment, and future prevention. Provide balanced coverage of what happened, why it happened, and how to prevent recurrence. Write for the technical team with appropriate technical details.

Create a postmortem for the database outage we experienced yesterday that caused 45 minutes of downtime.
```

**Notes:** The decorator adds structure and guidance for creating a comprehensive postmortem document tailored to the technical team.

## Transformation Details

**Base Instruction:** Create a detailed postmortem document that analyzes the incident, identifies root causes, and proposes preventive measures.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `format`:
  - When set to `timeline`: Structure the postmortem as a chronological timeline of events.
  - When set to `5-whys`: Use the 5 Whys technique to identify the root cause by repeatedly asking why the problem occurred.
  - When set to `fishbone`: Organize the analysis using a fishbone (Ishikawa) diagram approach to categorize potential causes.
  - When set to `comprehensive`: Create a comprehensive postmortem covering timeline, root cause analysis, impact assessment, and future prevention.

- `focus`:
  - When set to `what-happened`: Focus primarily on documenting what happened during the incident in detail.
  - When set to `why`: Emphasize root cause analysis and why the incident occurred.
  - When set to `prevention`: Concentrate on preventive measures and future safeguards.
  - When set to `balanced`: Provide balanced coverage of what happened, why it happened, and how to prevent recurrence.

- `audience`:
  - When set to `team`: Write for the technical team with appropriate technical details.
  - When set to `leadership`: Format for leadership with executive summary and business impact.
  - When set to `stakeholders`: Address concerns of all stakeholders with both technical and business perspectives.
  - When set to `public`: Create a public-facing document that explains the incident without revealing sensitive details.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4-turbo, gpt-4o, claude-3-7-sonnet-latest, llama-3.2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **RootCauseAnalysis**: Enhances PostMortem RootCauseAnalysis can enhance the 'why' aspect of PostMortem analysis.
- **TechnicalDocumentation**: Enhances PostMortem TechnicalDocumentation can improve the structure and clarity of the postmortem document.
