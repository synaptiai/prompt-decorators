# ReleaseNotes Decorator

Creates structured release notes for product updates.

**Category**: Developer Workflow

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `audience` | enum | Target reader | users |
| `detail` | enum | Information depth | detailed |
| `format` | enum | Release note structure | categorized |

## Audience Options

- `users`: Target the release notes for end users, focusing on benefits and user-facing changes.
- `developers`: Target the release notes for developers, including technical details and API changes.
- `stakeholders`: Target the release notes for business stakeholders, emphasizing business impact and strategic value.
- `public`: Target the release notes for public consumption, balancing technical details with accessible language.

## Detail Options

- `high-level`: Provide a concise overview of major changes without extensive details.
- `detailed`: Include comprehensive details about all changes, including minor improvements and fixes.

## Format Options

- `changelog`: Structure as a traditional changelog with version numbers and dated entries.
- `narrative`: Present as a narrative story highlighting the evolution and improvements.
- `categorized`: Organize changes into categories (Features, Improvements, Fixes, etc.).
- `markdown`: Format using Markdown syntax for easy integration with documentation systems.
- `html`: Format using HTML for web publication with appropriate tags and structure.

## Examples

### Creating detailed release notes for users in markdown format

```
+++ReleaseNotes(audience=users, detail=detailed, format=markdown)
Create release notes for version 2.3.0 which includes new payment methods, performance improvements, and bug fixes.
```

Produces comprehensive, user-focused release notes in markdown format, categorizing the new payment methods, performance improvements, and bug fixes.

### High-level release notes for stakeholders

```
+++ReleaseNotes(audience=stakeholders, detail=high-level, format=narrative)
Create release notes for our quarterly update with revenue impact features.
```

Generates concise, business-focused release notes in a narrative style, emphasizing strategic value and business impact.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Generate structured release notes for this product update. Organize information clearly for the specified audience.

**Notes:** Simpler instruction for models with less context capacity.


## Implementation Guidance

### Software product update

**Original Prompt:**
```
Create release notes for version 2.3.0 which includes new payment methods, performance improvements, and bug fixes.
```

**Transformed Prompt:**
```
Create structured release notes for the product update. Focus on clarity and organization. Target the release notes for end users, focusing on benefits and user-facing changes. Include comprehensive details about all changes, including minor improvements and fixes. Organize changes into categories (Features, Improvements, Fixes, etc.).

Create release notes for version 2.3.0 which includes new payment methods, performance improvements, and bug fixes.
```

**Notes:** The decorator adds structure and guidance for creating professional release notes tailored to the specified audience and format.

## Transformation Details

**Base Instruction:** Create structured release notes for the product update. Focus on clarity and organization.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `audience`:
  - When set to `users`: Target the release notes for end users, focusing on benefits and user-facing changes.
  - When set to `developers`: Target the release notes for developers, including technical details and API changes.
  - When set to `stakeholders`: Target the release notes for business stakeholders, emphasizing business impact and strategic value.
  - When set to `public`: Target the release notes for public consumption, balancing technical details with accessible language.

- `detail`:
  - When set to `high-level`: Provide a concise overview of major changes without extensive details.
  - When set to `detailed`: Include comprehensive details about all changes, including minor improvements and fixes.

- `format`:
  - When set to `changelog`: Structure as a traditional changelog with version numbers and dated entries.
  - When set to `narrative`: Present as a narrative story highlighting the evolution and improvements.
  - When set to `categorized`: Organize changes into categories (Features, Improvements, Fixes, etc.).
  - When set to `markdown`: Format using Markdown syntax for easy integration with documentation systems.
  - When set to `html`: Format using HTML for web publication with appropriate tags and structure.

## Compatibility

- **Requires**: None
- **Conflicts**: Summarize
- **Compatible Models**: gpt-4, gpt-3.5-turbo, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **TechnicalWriting**: Enhances ReleaseNotes TechnicalWriting can enhance the clarity and professionalism of the release notes.
- **Summarize**: Conflicts with ReleaseNotes Summarize may contradict the detailed nature of release notes, especially when detail=detailed.
