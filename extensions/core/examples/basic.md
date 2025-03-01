# Basic Decorator Examples

This document demonstrates basic usage of individual core decorators.

## Reasoning Decorator

The Reasoning decorator encourages the AI to show its thought process before reaching conclusions.

### Example:

```
+++Reasoning(depth=comprehensive)
What are the ethical implications of autonomous vehicles?
```

### Expected Result:

The AI will provide a detailed reasoning process, exploring various ethical considerations of autonomous vehicles, such as:

1. Safety implications and the trolley problem
2. Liability and responsibility in accidents
3. Privacy concerns with data collection
4. Impact on employment for professional drivers
5. Accessibility and equity issues

The response will show the reasoning path before presenting conclusions.

## StepByStep Decorator

The StepByStep decorator structures the response as a sequence of steps.

### Example:

```
+++StepByStep(numbered=true)
How do I build a simple React component?
```

### Expected Result:

The AI will break down the process into numbered steps:

1. Set up your React environment
2. Create a new component file
3. Import React
4. Define your component function
5. Add JSX for the component's UI
6. Export the component
7. Import and use the component in your app

## OutputFormat Decorator

The OutputFormat decorator controls the format of the response.

### Example:

```
+++OutputFormat(format=json)
List the top 5 programming languages and their key features
```

### Expected Result:

The AI will respond with a JSON structure:

```json
{
  "languages": [
    {
      "name": "Python",
      "features": ["Easy syntax", "Versatile", "Large ecosystem"]
    },
    {
      "name": "JavaScript",
      "features": ["Web native", "Asynchronous", "Ubiquitous"]
    },
    {
      "name": "Java",
      "features": ["Platform independent", "Strong typing", "Enterprise-ready"]
    },
    {
      "name": "C++",
      "features": ["High performance", "Memory control", "Object-oriented"]
    },
    {
      "name": "Go",
      "features": ["Concurrent", "Simple", "Fast compilation"]
    }
  ]
}
```

## Tone Decorator

The Tone decorator adjusts the writing style of the response.

### Example:

```
+++Tone(style=technical)
Explain how garbage collection works in programming languages
```

### Expected Result:

The AI will respond with a technically precise explanation using appropriate terminology, focusing on memory management algorithms, reference counting, mark-and-sweep, generational collection, and other technical aspects of garbage collection.

## Version Decorator

The Version decorator specifies the standard version to use.

### Example:

```
+++Version(standard=1.0.0)
+++Reasoning(depth=comprehensive)
Explain quantum entanglement
```

### Expected Result:

The AI will interpret the decorators according to version 1.0.0 of the standard, ensuring consistent behavior across implementations. 