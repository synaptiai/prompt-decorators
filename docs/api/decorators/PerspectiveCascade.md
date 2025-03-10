# PerspectiveCascade Decorator

Systematically explores a topic through a sequence of diverse, interconnected viewpoints, with each perspective building upon previous ones to reveal multidimensional insights

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `perspectives` | number | Number of distinct perspectives to explore in the cascade | 4 |
| `domain` | enum | Domain-specific perspective set to use | custom |
| `integrationLevel` | enum | How tightly to integrate perspectives in the cascade | moderate |
| `interactionStyle` | enum | How to manage the interaction through perspectives | guided |
| `customPerspectives` | string | Custom list of perspectives to explore (comma-separated) |  |

## Domain Options

- `business`: Use a business-oriented cascade that explores: 1) Operational considerations, 2) Human/stakeholder impacts, 3) Organizational culture implications, 4) Market/competitive positioning.
- `product`: Use a product development cascade that explores: 1) User needs and pain points, 2) Technical feasibility and constraints, 3) Market viability and positioning, 4) Future adaptability and scaling.
- `research`: Use a research-oriented cascade that explores: 1) Methodological approaches, 2) Theoretical frameworks, 3) Practical implementation considerations, 4) Implications and applications.
- `problem-solving`: Use a problem-solving cascade that explores: 1) Problem definition and framing, 2) Causal factors and systems analysis, 3) Solution approaches and evaluation, 4) Implementation and adaptation.
- `decision-making`: Use a decision-making cascade that explores: 1) Practical considerations, 2) Ethical dimensions, 3) Strategic alignment, 4) Emotional and intuitive aspects.
- `content-creation`: Use a content-creation cascade that explores: 1) Core message and purpose, 2) Audience needs and perspectives, 3) Format and delivery considerations, 4) Engagement and impact potential.
- `negotiation`: Use a negotiation-focused cascade that explores: 1) Your interests and priorities, 2) Counterparty perspectives and needs, 3) Contextual factors and constraints, 4) Creative options and integrative solutions.
- `custom`: Develop a custom perspective cascade appropriate to the specific topic and context.

## Integrationlevel Options

- `basic`: Ensure basic connections between perspectives, highlighting key relationship points.
- `moderate`: Create moderate integration with explicit connections and reflections on how each perspective transforms understanding of previous viewpoints.
- `comprehensive`: Implement comprehensive integration where perspectives deeply inform each other, with explicit synthesis of insights across the full cascade.

## Interactionstyle Options

- `guided`: Guide the user through each perspective with explicit questions to elicit their input before moving to the next perspective.
- `autonomous`: Present the full cascade of perspectives with minimal interruption, providing a comprehensive analysis.
- `hybrid`: Balance guidance and autonomy by presenting initial perspectives, then pausing for input at key integration points.

## Examples

### Business strategy exploration

```
+++PerspectiveCascade(domain=business, perspectives=4, integrationLevel=comprehensive)
```

Analyzes business strategy through four perspectives (operational, human, cultural, and market) with comprehensive integration between viewpoints

### Product development with custom perspectives

```
+++PerspectiveCascade(customPerspectives=technical,financial,ethical,user-experience, integrationLevel=moderate)
```

Explores product development through a cascade of technical, financial, ethical, and user experience perspectives with moderate integration

## Implementation Guidance

### Corporate policy development

**Original Prompt:**
```
Help me develop a sustainability policy for my manufacturing company.
```

**Transformed Prompt:**
```
Approach this topic using Perspective Cascading, a method that systematically explores the subject through a sequence of diverse, interconnected viewpoints. Each new perspective should build upon previous ones while introducing novel elements, creating a flowing exploration that reveals insights at the boundaries between different perspectives. Use a business-oriented cascade that explores: 1) Operational considerations, 2) Human/stakeholder impacts, 3) Organizational culture implications, 4) Market/competitive positioning. Create moderate integration with explicit connections and reflections on how each perspective transforms understanding of previous viewpoints. Guide the user through each perspective with explicit questions to elicit their input before moving to the next perspective.

Help me develop a sustainability policy for my manufacturing company.
```

## Transformation Details

**Base Instruction:** Approach this topic using Perspective Cascading, a method that systematically explores the subject through a sequence of diverse, interconnected viewpoints. Each new perspective should build upon previous ones while introducing novel elements, creating a flowing exploration that reveals insights at the boundaries between different perspectives.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `perspectives`:
  - When set to `3`: Explore three key perspectives in sequence, ensuring each builds upon previous insights.
  - When set to `4`: Develop a four-perspective cascade that provides a comprehensive exploration of the topic.
  - When set to `5`: Create a rich five-perspective cascade that thoroughly examines the topic from multiple angles.
  - When set to `6`: Implement an extensive six-perspective cascade for maximum insight generation.

- `domain`:
  - When set to `business`: Use a business-oriented cascade that explores: 1) Operational considerations, 2) Human/stakeholder impacts, 3) Organizational culture implications, 4) Market/competitive positioning.
  - When set to `product`: Use a product development cascade that explores: 1) User needs and pain points, 2) Technical feasibility and constraints, 3) Market viability and positioning, 4) Future adaptability and scaling.
  - When set to `research`: Use a research-oriented cascade that explores: 1) Methodological approaches, 2) Theoretical frameworks, 3) Practical implementation considerations, 4) Implications and applications.
  - When set to `problem-solving`: Use a problem-solving cascade that explores: 1) Problem definition and framing, 2) Causal factors and systems analysis, 3) Solution approaches and evaluation, 4) Implementation and adaptation.
  - When set to `decision-making`: Use a decision-making cascade that explores: 1) Practical considerations, 2) Ethical dimensions, 3) Strategic alignment, 4) Emotional and intuitive aspects.
  - When set to `content-creation`: Use a content-creation cascade that explores: 1) Core message and purpose, 2) Audience needs and perspectives, 3) Format and delivery considerations, 4) Engagement and impact potential.
  - When set to `negotiation`: Use a negotiation-focused cascade that explores: 1) Your interests and priorities, 2) Counterparty perspectives and needs, 3) Contextual factors and constraints, 4) Creative options and integrative solutions.
  - When set to `custom`: Develop a custom perspective cascade appropriate to the specific topic and context.

- `integrationLevel`:
  - When set to `basic`: Ensure basic connections between perspectives, highlighting key relationship points.
  - When set to `moderate`: Create moderate integration with explicit connections and reflections on how each perspective transforms understanding of previous viewpoints.
  - When set to `comprehensive`: Implement comprehensive integration where perspectives deeply inform each other, with explicit synthesis of insights across the full cascade.

- `interactionStyle`:
  - When set to `guided`: Guide the user through each perspective with explicit questions to elicit their input before moving to the next perspective.
  - When set to `autonomous`: Present the full cascade of perspectives with minimal interruption, providing a comprehensive analysis.
  - When set to `hybrid`: Balance guidance and autonomy by presenting initial perspectives, then pausing for input at key integration points.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: claude-3-opus-20240229, claude-3-sonnet-20240229, gpt-4, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **DeepDive**: Enhances PerspectiveCascade DeepDive can be used to explore individual perspectives more thoroughly when needed
- **Socratic**: Enhances PerspectiveCascade Socratic questioning works well with the guided interaction style to facilitate perspective exploration
- **Debate**: Conflicts with PerspectiveCascade Debate focuses on oppositional perspectives rather than the flowing cascade approach
