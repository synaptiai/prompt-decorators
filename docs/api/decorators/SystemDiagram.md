# SystemDiagram Decorator

Creates architectural diagrams and visual representations.

**Category**: Architecture And Design

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `notation` | `enum` | Diagram notation system | `c4` |
| `level` | `enum` | Detail level of the diagram | `container` |
| `focus` | `enum` | Diagram emphasis | `structure` |

## Notation Options

- `uml`: Use UML (Unified Modeling Language) notation for the diagram.
- `c4`: Follow the C4 model notation for the diagram.
- `archimate`: Apply ArchiMate notation standards to the diagram.
- `informal`: Create an informal, easy-to-understand diagram without strict notation rules.
- `flowchart`: Use standard flowchart notation for the diagram.

## Level Options

- `context`: Focus on the context level showing the system and its relationships with users and other systems.
- `container`: Show containers (applications, data stores, microservices) within the system.
- `component`: Break down into components showing the major structural building blocks and their interactions.
- `code`: Provide code-level details showing classes, interfaces, and relationships.

## Focus Options

- `structure`: Emphasize the structural elements and their relationships.
- `behavior`: Highlight the behavioral aspects and processes within the system.
- `interaction`: Focus on interactions and communications between system elements.
- `deployment`: Show the deployment architecture and infrastructure components.

## Examples

### Creating a C4 container diagram showing interactions

```
+++SystemDiagram(notation=c4, level=container, focus=interaction)
Create a system diagram showing how a user authentication service interacts with other system components.
```

Produces a C4 notation diagram at container level focusing on the interactions between the authentication service and other system components.

### UML class diagram for a software system

```
+++SystemDiagram(notation=uml, level=code, focus=structure)
Create a diagram for a blog system with User, Post, and Comment classes.
```

Generates a UML class diagram showing the structure of the blog system classes and their relationships.

### High-level system context diagram

```
+++SystemDiagram(notation=informal, level=context)
Show how our e-commerce platform connects to external systems.
```

Creates an informal context diagram showing the e-commerce platform and its connections to external systems like payment processors, shipping services, etc.

## Model-Specific Implementations

### gpt-4o

**Instruction:** Create a system diagram that visually represents the architecture or design described. Use clear notation and appropriate level of detail. The diagram should be described in text format that can be easily converted to a visual representation using tools like PlantUML, Mermaid, or similar diagramming tools.

**Notes:** gpt-4o has enhanced capabilities for structured outputs that can be converted to diagrams.


## Implementation Guidance

### Software Architecture Design

**Original Prompt:**
```
Create a system diagram showing how a user authentication service interacts with other system components.
```

**Transformed Prompt:**
```
Create a system diagram that visually represents the architecture or design described. Use clear notation and appropriate level of detail. Follow the C4 model notation for the diagram. Show containers (applications, data stores, microservices) within the system. Focus on interactions and communications between system elements.

Create a system diagram showing how a user authentication service interacts with other system components.
```

**Notes:** The decorator adds specific instructions about the diagram notation, level, and focus before the original prompt.

## Transformation Details

**Base Instruction:** Create a system diagram that visually represents the architecture or design described. Use clear notation and appropriate level of detail.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `notation`:
  - When set to `uml`: Use UML (Unified Modeling Language) notation for the diagram.
  - When set to `c4`: Follow the C4 model notation for the diagram.
  - When set to `archimate`: Apply ArchiMate notation standards to the diagram.
  - When set to `informal`: Create an informal, easy-to-understand diagram without strict notation rules.
  - When set to `flowchart`: Use standard flowchart notation for the diagram.

- `level`:
  - When set to `context`: Focus on the context level showing the system and its relationships with users and other systems.
  - When set to `container`: Show containers (applications, data stores, microservices) within the system.
  - When set to `component`: Break down into components showing the major structural building blocks and their interactions.
  - When set to `code`: Provide code-level details showing classes, interfaces, and relationships.

- `focus`:
  - When set to `structure`: Emphasize the structural elements and their relationships.
  - When set to `behavior`: Highlight the behavioral aspects and processes within the system.
  - When set to `interaction`: Focus on interactions and communications between system elements.
  - When set to `deployment`: Show the deployment architecture and infrastructure components.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo, claude-3-7-sonnet-latest, gemini-pro
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeGeneration**: Enhances SystemDiagram Can be used to generate diagrams that complement code generation tasks.
- **ArchitecturalPatterns**: Enhances SystemDiagram Works well with architectural pattern recommendations to visualize the suggested patterns.
