# ConceptModel Decorator

Visualizes relationships between technical concepts.

**Category**: Developer Education

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `notation` | enum | Diagram type | concept-map |
| `complexity` | enum | Diagram sophistication | intermediate |
| `focus` | string | Central concept | main-topic |

## Notation Options

- `mind-map`: Organize the information as a mind map with a central concept and branching ideas.
- `concept-map`: Create a concept map with labeled relationships between concepts.
- `knowledge-graph`: Develop a knowledge graph with nodes representing concepts and edges showing relationships.
- `informal`: Use an informal diagram style that best represents the relationships between concepts.

## Complexity Options

- `basic`: Keep the diagram simple with only key concepts and primary relationships.
- `intermediate`: Include important secondary concepts and relationships in addition to primary ones.
- `comprehensive`: Create a detailed diagram capturing all relevant concepts, sub-concepts, and their interconnections.

## Examples

### Creating a concept map for React concepts

```
+++ConceptModel(notation=concept-map, complexity=intermediate)
Create a concept map showing the relationships between key React concepts including components, hooks, state, and context.
```

A concept map showing React concepts with components, hooks, state, and context as main nodes, with labeled relationships between them and relevant secondary concepts.

### Basic mind map for programming paradigms

```
+++ConceptModel(notation=mind-map, complexity=basic, focus=programming-paradigms)
Show the main programming paradigms and their key characteristics.
```

A simple mind map with programming paradigms as the central node, branching out to imperative, declarative, object-oriented, functional, and other paradigms.

## Model-Specific Implementations

### gpt-4

**Instruction:** Create a visual representation of the relationships between concepts using ASCII or Unicode characters. Structure the diagram to clearly show connections and hierarchies between ideas.

**Notes:** GPT-4 can create effective ASCII/Unicode diagrams for concept visualization.

### claude-2

**Instruction:** Create a visual representation of the relationships between concepts using ASCII art or structured text. Organize the information to clearly show connections and hierarchies between ideas.

**Notes:** Claude models can create effective text-based visualizations.


## Implementation Guidance

### Technical education

**Original Prompt:**
```
Explain the relationships between key React concepts including components, hooks, state, and context.
```

**Transformed Prompt:**
```
Create a concept map with labeled relationships between concepts. Include important secondary concepts and relationships in addition to primary ones. Center the diagram around the concept of main-topic.

Explain the relationships between key React concepts including components, hooks, state, and context.
```

**Notes:** The decorator transforms a simple explanation request into a request for a visual concept map.

## Transformation Details

**Base Instruction:** Create a visual representation of the relationships between concepts. Use a structured approach to show connections and hierarchies between ideas.

**Placement:** prepend

**Composition Behavior:** override

**Parameter Effects:**

- `notation`:
  - When set to `mind-map`: Organize the information as a mind map with a central concept and branching ideas.
  - When set to `concept-map`: Create a concept map with labeled relationships between concepts.
  - When set to `knowledge-graph`: Develop a knowledge graph with nodes representing concepts and edges showing relationships.
  - When set to `informal`: Use an informal diagram style that best represents the relationships between concepts.

- `complexity`:
  - When set to `basic`: Keep the diagram simple with only key concepts and primary relationships.
  - When set to `intermediate`: Include important secondary concepts and relationships in addition to primary ones.
  - When set to `comprehensive`: Create a detailed diagram capturing all relevant concepts, sub-concepts, and their interconnections.

- `focus`:
  - Format: Center the diagram around the concept of {value}.

## Compatibility

- **Requires**: None
- **Conflicts**: OutputFormat
- **Compatible Models**: gpt-4, gpt-3.5-turbo, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **DetailLevel**: Enhances ConceptModel DetailLevel can be used to further refine the depth of information in the concept model.
- **OutputFormat**: Conflicts with ConceptModel This decorator already specifies an output format, so it may conflict with other format specifications.
