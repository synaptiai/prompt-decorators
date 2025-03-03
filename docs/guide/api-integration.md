# API Integration

This guide covers how to integrate the Prompt Decorators framework with various LLM APIs.

## OpenAI Integration

### Basic Integration

```python
import openai
from prompt_decorators.decorators import Reasoning, OutputFormat

# Set up OpenAI API key
openai.api_key = "your-api-key"

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators to a prompt
prompt = "Explain quantum entanglement."
decorated_prompt = output_format.apply(reasoning.apply(prompt))

# Call OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": decorated_prompt}
    ],
    temperature=0.7,
    max_tokens=1000
)

# Print the response
print(response.choices[0].message.content)
```

### Using the DecoratedRequest Class

```python
import openai
from prompt_decorators.core.request import DecoratedRequest
from prompt_decorators.decorators import Reasoning, OutputFormat

# Set up OpenAI API key
openai.api_key = "your-api-key"

# Create a decorated request
request = DecoratedRequest(
    prompt="Explain quantum mechanics.",
    decorators=[
        Reasoning(style="detailed", show_working=True),
        OutputFormat(format_type="markdown", pretty_print=True)
    ],
    model="gpt-4",
    api_params={
        "temperature": 0.7,
        "max_tokens": 1000
    }
)

# Apply all decorators
decorated_prompt = request.apply_decorators()

# Call OpenAI API
response = openai.ChatCompletion.create(
    model=request.model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": decorated_prompt}
    ],
    **request.api_params
)

# Print the response
print(response.choices[0].message.content)
```

## Anthropic Integration

### Basic Integration

```python
import anthropic
from prompt_decorators.decorators import Reasoning, OutputFormat

# Set up Anthropic API key
client = anthropic.Anthropic(api_key="your-api-key")

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators to a prompt
prompt = "Explain quantum entanglement."
decorated_prompt = output_format.apply(reasoning.apply(prompt))

# Call Anthropic API
response = client.completions.create(
    model="claude-2",
    prompt=f"{anthropic.HUMAN_PROMPT} {decorated_prompt} {anthropic.AI_PROMPT}",
    max_tokens_to_sample=1000,
    temperature=0.7
)

# Print the response
print(response.completion)
```

### Using the DecoratedRequest Class

```python
import anthropic
from prompt_decorators.core.request import DecoratedRequest
from prompt_decorators.decorators import Reasoning, OutputFormat

# Set up Anthropic API key
client = anthropic.Anthropic(api_key="your-api-key")

# Create a decorated request
request = DecoratedRequest(
    prompt="Explain quantum mechanics.",
    decorators=[
        Reasoning(style="detailed", show_working=True),
        OutputFormat(format_type="markdown", pretty_print=True)
    ],
    model="claude-2",
    api_params={
        "temperature": 0.7,
        "max_tokens_to_sample": 1000
    }
)

# Apply all decorators
decorated_prompt = request.apply_decorators()

# Call Anthropic API
response = client.completions.create(
    model=request.model,
    prompt=f"{anthropic.HUMAN_PROMPT} {decorated_prompt} {anthropic.AI_PROMPT}",
    **request.api_params
)

# Print the response
print(response.completion)
```

## LangChain Integration

### Basic Integration

```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from prompt_decorators.decorators import Reasoning, OutputFormat

# Create an LLM
llm = OpenAI(temperature=0.7)

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Create a base prompt template
base_template = "Explain {topic}."
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template=base_template
)

# Format the prompt
topic = "quantum entanglement"
prompt = prompt_template.format(topic=topic)

# Apply decorators
decorated_prompt = output_format.apply(reasoning.apply(prompt))

# Run the LLM
response = llm(decorated_prompt)

# Print the response
print(response)
```

### Creating a Custom LangChain Prompt Decorator

```python
from langchain.prompts import BasePromptTemplate
from langchain.llms import OpenAI
from typing import List, Dict, Any
from prompt_decorators.decorators import Reasoning, OutputFormat

class DecoratedPromptTemplate(BasePromptTemplate):
    """A LangChain prompt template that applies prompt decorators."""

    prompt_template: BasePromptTemplate
    decorators: List

    def format(self, **kwargs) -> str:
        """Format the prompt template and apply decorators.

        Args:
            **kwargs: The variables to format the template with.

        Returns:
            The formatted and decorated prompt.
        """
        # Format the base prompt
        base_prompt = self.prompt_template.format(**kwargs)

        # Apply decorators in sequence
        decorated_prompt = base_prompt
        for decorator in self.decorators:
            decorated_prompt = decorator.apply(decorated_prompt)

        return decorated_prompt

    @property
    def input_variables(self) -> List[str]:
        """Get the input variables for the prompt template.

        Returns:
            The list of input variables.
        """
        return self.prompt_template.input_variables

# Example usage
from langchain.prompts import PromptTemplate

# Create an LLM
llm = OpenAI(temperature=0.7)

# Create a base prompt template
base_template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic}."
)

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Create a decorated prompt template
decorated_template = DecoratedPromptTemplate(
    prompt_template=base_template,
    decorators=[reasoning, output_format]
)

# Format the prompt
topic = "quantum entanglement"
decorated_prompt = decorated_template.format(topic=topic)

# Run the LLM
response = llm(decorated_prompt)

# Print the response
print(response)
```

## Custom API Integration

You can integrate with any LLM API by applying decorators to your prompts before sending them to the API:

```python
import requests
from prompt_decorators.decorators import Reasoning, OutputFormat

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators to a prompt
prompt = "Explain quantum entanglement."
decorated_prompt = output_format.apply(reasoning.apply(prompt))

# Call a custom API
response = requests.post(
    "https://api.example.com/generate",
    json={
        "prompt": decorated_prompt,
        "temperature": 0.7,
        "max_tokens": 1000
    },
    headers={
        "Authorization": "Bearer your-api-key"
    }
)

# Print the response
print(response.json()["text"])
```

## Next Steps

- Explore the [API Reference](../api/index.md)
- Check out [Provider Examples](../examples/providers.md)
- Learn about [Model-Specific Adaptations](../api/core.md#model-specific)
