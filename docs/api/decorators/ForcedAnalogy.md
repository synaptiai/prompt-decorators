# ForcedAnalogy Decorator

Explains concepts by specifically comparing them to a particular domain or field. This decorator forces analogies from a specified source domain to make complex or unfamiliar topics more relatable and understandable.

**Category**: Reasoning

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `source` | `string` | The specific domain, field, or context to draw analogies from | `Required` |
| `comprehensiveness` | `enum` | How comprehensively to map concepts between domains | `comprehensive` |
| `mappings` | `number` | Number of distinct concept mappings to create between domains | `3` |

## Comprehensiveness Options

- `basic`: Create simple, straightforward analogies with clear one-to-one mappings between the most fundamental concepts.
- `comprehensive`: Develop well-rounded analogies that cover the major components and processes, with moderately detailed mappings between domains.
- `detailed`: Construct elaborate, nuanced analogies with detailed mappings that capture subtle aspects, edge cases, and complexities of the topic.

## Examples

### Explaining a technical concept using sports analogies

```
+++ForcedAnalogy(source=sports)
Explain how blockchain technology works.
```

Explains blockchain technology by mapping concepts to sports analogies (e.g., ledger as scoreboard, miners as referees, consensus as rulebook)

### Detailed cooking analogy for complex scientific process

```
+++ForcedAnalogy(source=cooking, comprehensiveness=detailed, mappings=5)
Describe how CRISPR gene editing works.
```

Provides a detailed explanation of CRISPR through cooking analogies, with 5 distinct concept mappings (e.g., DNA as recipe, Cas9 as kitchen knife, guide RNA as cooking instructions)

## Model-Specific Implementations

### gpt-4-turbo

**Instruction:** Create an explanation that uses only {source}-based analogies. Identify {mappings} key concepts from the topic and map each one to something from {source}. For each mapping, explain: 1) The original concept, 2) The {source} analogy, and 3) How they are similar and different. Be {comprehensiveness} in your mapping depth. Stick to this domain exclusively - don't use analogies from any other fields.

**Notes:** This model may need explicit reminders to stay within the specified source domain and to clearly label which concept maps to which analogy


## Implementation Guidance

### Using sports analogies to explain blockchain

**Original Prompt:**
```
Explain how blockchain technology works.
```

**Transformed Prompt:**
```
Please explain this topic using analogies drawn specifically from a particular domain. Create explicit comparisons that map concepts from the topic to elements, processes, or ideas from the specified source domain. Use analogies specifically from the domain of sports. Draw all your comparisons and metaphors from this domain to explain the target concepts. Develop well-rounded analogies that cover the major components and processes, with moderately detailed mappings between domains. Create exactly 3 distinct concept mappings between the target domain and the source domain. Each mapping should connect a specific element from the topic to a corresponding element in the sports domain.

Explain how blockchain technology works.
```

### Detailed cooking analogies for CRISPR gene editing

**Original Prompt:**
```
Describe how CRISPR gene editing works.
```

**Transformed Prompt:**
```
Please explain this topic using analogies drawn specifically from a particular domain. Create explicit comparisons that map concepts from the topic to elements, processes, or ideas from the specified source domain. Use analogies specifically from the domain of cooking. Draw all your comparisons and metaphors from this domain to explain the target concepts. Construct elaborate, nuanced analogies with detailed mappings that capture subtle aspects, edge cases, and complexities of the topic. Create exactly 5 distinct concept mappings between the target domain and the source domain. Each mapping should connect a specific element from the topic to a corresponding element in the cooking domain.

Describe how CRISPR gene editing works.
```

## Transformation Details

**Base Instruction:** Please explain this topic using analogies drawn specifically from a particular domain. Create explicit comparisons that map concepts from the topic to elements, processes, or ideas from the specified source domain.

**Placement:** prepend

**Composition Behavior:** accumulate

**Parameter Effects:**

- `source`:
  - Format: Use analogies specifically from the domain of {value}. Draw all your comparisons and metaphors from this domain to explain the target concepts.

- `comprehensiveness`:
  - When set to `basic`: Create simple, straightforward analogies with clear one-to-one mappings between the most fundamental concepts.
  - When set to `comprehensive`: Develop well-rounded analogies that cover the major components and processes, with moderately detailed mappings between domains.
  - When set to `detailed`: Construct elaborate, nuanced analogies with detailed mappings that capture subtle aspects, edge cases, and complexities of the topic.

- `mappings`:
  - Format: Create exactly {value} distinct concept mappings between the target domain and the source domain. Each mapping should connect a specific element from the topic to a corresponding element in the {source} domain.

## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-4o, gpt-4-turbo
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **Analogical**: Enhances ForcedAnalogy ForcedAnalogy constrains the source domain for analogies, while Analogical provides more general analogy-based reasoning
- **ELI5**: Enhances ForcedAnalogy ForcedAnalogy can be combined with ELI5 to create simple, accessible analogies from a specific domain
- **Technical**: Enhances ForcedAnalogy ForcedAnalogy helps make technical topics more accessible by mapping them to familiar domains
