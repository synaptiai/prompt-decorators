# LearningPath Decorator

Creates step-by-step learning roadmaps.

**Category**: Developer Education

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `for` | string | Learning subject | context-dependent |
| `experience` | enum | Learner starting point | beginner |
| `timeframe` | enum | Available learning time | self-paced |

## Experience Options

- `beginner`: complete beginner with no prior knowledge
- `intermediate`: learner with basic understanding seeking to deepen knowledge
- `advanced`: experienced practitioner looking to master advanced concepts
- `career-change`: professional transitioning from another field

## Timeframe Options

- `week`: one week (intensive crash course)
- `month`: one month (focused daily learning)
- `quarter`: three months (steady consistent progress)
- `year`: one year (comprehensive mastery program)
- `self-paced`: flexible self-paced schedule

## Examples

### Creating a React learning path for beginners over three months

```
+++LearningPath(for=react, experience=beginner, timeframe=quarter)
Create a learning roadmap for a junior developer to become proficient in React and its ecosystem.
```

A structured, progressive learning path for React that spans three months, starting with fundamentals and building to advanced concepts, with appropriate resources and milestones for beginners.

### Creating an advanced machine learning path for experienced practitioners

```
+++LearningPath(for="machine learning", experience=advanced, timeframe=year)
```

A comprehensive year-long advanced learning path for machine learning that covers cutting-edge techniques, research papers, and practical implementations for someone already familiar with the basics.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Create a detailed, step-by-step learning path for {for}. The path should be for {experience} level learners and designed to be completed in a {timeframe}. Include specific resources, practice projects, and clear milestones.

**Notes:** Simplified instruction with more direct language for models with smaller context windows.


## Compatibility

- **Requires**: None
- **Conflicts**: Curriculum
- **Compatible Models**: gpt-4, gpt-3.5-turbo, claude-2, llama-2
- **Standard Version**: 1.0.0 - 1.5.0

## Related Decorators

- **ExpertLevel**: Enhances LearningPath ExpertLevel can be used to specify the expertise level of the content creator, while LearningPath focuses on the learner's experience level.
- **Curriculum**: Conflicts with LearningPath Both decorators aim to structure educational content and may provide conflicting instructions.
