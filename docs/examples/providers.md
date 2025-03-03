# Provider Examples

This page provides specific examples of using Prompt Decorators with different LLM providers.

## OpenAI Examples

### Using GPT-4 with Chain-of-Thought and JSON Output

```python
import openai
from prompt_decorators.decorators import ChainOfThought, OutputFormat

# Set up OpenAI API key
openai.api_key = "your-api-key"

# Create decorators
cot = ChainOfThought(steps=["understand", "analyze", "solve", "verify"])
json_format = OutputFormat(format_type="json", schema={
    "type": "object",
    "properties": {
        "answer": {"type": "string"},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "reasoning": {"type": "string"}
    },
    "required": ["answer", "confidence", "reasoning"]
})

# Apply decorators to a prompt
prompt = "What is the capital of France and what is its population?"
decorated_prompt = json_format.apply(cot.apply(prompt))

# Call OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": decorated_prompt}
    ],
    temperature=0.3,
    max_tokens=1000
)

# Print the response
print(response.choices[0].message.content)
```

### Using GPT-3.5 with Persona and Reasoning

```python
import openai
from prompt_decorators.decorators import Persona, Reasoning

# Set up OpenAI API key
openai.api_key = "your-api-key"

# Create decorators
persona = Persona(
    role="expert physicist",
    background="PhD in Theoretical Physics with 15 years of research experience",
    tone="educational but accessible"
)
reasoning = Reasoning(style="step_by_step", show_working=True)

# Apply decorators to a prompt
prompt = "Explain the concept of quantum tunneling."
decorated_prompt = reasoning.apply(persona.apply(prompt))

# Call OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
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

## Anthropic Examples

### Using Claude with Persona and Markdown Output

```python
import anthropic
from prompt_decorators.decorators import Persona, OutputFormat

# Set up Anthropic API key
client = anthropic.Anthropic(api_key="your-api-key")

# Create decorators
persona = Persona(
    role="expert historian",
    background="Professor of Ancient History with focus on Roman civilization",
    tone="scholarly but engaging"
)
markdown = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators to a prompt
prompt = "Describe the fall of the Roman Empire."
decorated_prompt = markdown.apply(persona.apply(prompt))

# Call Anthropic API
response = client.completions.create(
    model="claude-2",
    prompt=f"{anthropic.HUMAN_PROMPT} {decorated_prompt} {anthropic.AI_PROMPT}",
    max_tokens_to_sample=2000,
    temperature=0.7
)

# Print the response
print(response.completion)
```

### Using Claude with Chain-of-Thought and Structured Output

```python
import anthropic
import json
from prompt_decorators.decorators import ChainOfThought, OutputFormat

# Set up Anthropic API key
client = anthropic.Anthropic(api_key="your-api-key")

# Create decorators
cot = ChainOfThought(steps=["understand", "research", "analyze", "conclude"])
structured_output = OutputFormat(format_type="json", schema={
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "summary": {"type": "string"},
        "key_points": {"type": "array", "items": {"type": "string"}},
        "conclusion": {"type": "string"}
    },
    "required": ["title", "summary", "key_points", "conclusion"]
})

# Apply decorators to a prompt
prompt = "Analyze the impact of the Industrial Revolution on modern society."
decorated_prompt = structured_output.apply(cot.apply(prompt))

# Call Anthropic API
response = client.completions.create(
    model="claude-2",
    prompt=f"{anthropic.HUMAN_PROMPT} {decorated_prompt} {anthropic.AI_PROMPT}",
    max_tokens_to_sample=2000,
    temperature=0.5
)

# Parse the JSON response
try:
    result = json.loads(response.completion)
    print(json.dumps(result, indent=2))
except json.JSONDecodeError:
    print("Could not parse JSON response:")
    print(response.completion)
```

## Hugging Face Examples

### Using a Local Model with Reasoning

```python
from transformers import pipeline
from prompt_decorators.decorators import Reasoning

# Load a local model
generator = pipeline('text-generation', model='mistralai/Mistral-7B-Instruct-v0.1')

# Create decorator
reasoning = Reasoning(style="detailed", show_working=True)

# Apply decorator to a prompt
prompt = "Explain how photosynthesis works."
decorated_prompt = reasoning.apply(prompt)

# Format for instruction-tuned model
formatted_prompt = f"""<s>[INST] {decorated_prompt} [/INST]"""

# Generate response
response = generator(
    formatted_prompt,
    max_length=2000,
    num_return_sequences=1,
    temperature=0.7
)

# Print the response
print(response[0]['generated_text'])
```

### Using Hugging Face Inference API

```python
import requests
from prompt_decorators.decorators import OutputFormat, ChainOfThought

# Set up Hugging Face API key
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-70b-chat-hf"
headers = {"Authorization": f"Bearer your-api-key"}

# Create decorators
cot = ChainOfThought(steps=["understand", "analyze", "solve", "verify"])
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators to a prompt
prompt = "What are the ethical implications of artificial intelligence?"
decorated_prompt = output_format.apply(cot.apply(prompt))

# Format for Llama 2
formatted_prompt = f"""<s>[INST] {decorated_prompt} [/INST]"""

# Call Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": formatted_prompt,
    "parameters": {
        "max_new_tokens": 2000,
        "temperature": 0.7,
        "top_p": 0.9
    }
})

# Print the response
print(output[0]["generated_text"])
```

## LangChain Examples

### Using LangChain with Multiple Decorators

```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from prompt_decorators.decorators import Reasoning, OutputFormat, Persona

# Create an LLM
llm = OpenAI(temperature=0.7)

# Create decorators
persona = Persona(
    role="expert data scientist",
    background="10 years of experience in machine learning and data analysis",
    tone="technical but clear"
)
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Create a base prompt template
base_template = "Explain {topic} and provide a simple example."
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template=base_template
)

# Format the prompt
topic = "principal component analysis"
prompt = prompt_template.format(topic=topic)

# Apply decorators in sequence
decorated_prompt = prompt
for decorator in [persona, reasoning, output_format]:
    decorated_prompt = decorator.apply(decorated_prompt)

# Run the LLM
response = llm(decorated_prompt)

# Print the response
print(response)
```

### Using LangChain Agents with Decorators

```python
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.utilities import SerpAPIWrapper
from prompt_decorators.decorators import Reasoning, OutputFormat

# Set up tools
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for when you need to answer questions about current events or the current state of the world"
    )
]

# Create an LLM
llm = OpenAI(temperature=0)

# Initialize the agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Create decorators
reasoning = Reasoning(style="detailed", show_working=True)
output_format = OutputFormat(format_type="markdown", pretty_print=True)

# Apply decorators to a prompt
prompt = "What is the current population of Paris, France?"
decorated_prompt = output_format.apply(reasoning.apply(prompt))

# Run the agent
response = agent.run(decorated_prompt)

# Print the response
print(response)
```

## Next Steps

- Learn about [API Integration](../guide/api-integration.md)
- Explore [Advanced Usage](../guide/advanced-usage.md)
- Check out the [API Reference](../api/index.md)
