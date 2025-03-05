# Model Context Protocol (MCP) Integration

The Prompt Decorators library provides integration with the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol), allowing you to use prompt decorators through MCP tools and predefined templates.

## Installation

The MCP integration is an optional feature that requires the MCP package. You can install it in one of two ways:

1. Install prompt-decorators with the MCP extras:

```bash
pip install "prompt-decorators[mcp]"
```

2. Or install the MCP package separately:

```bash
pip install "mcp[cli]"
```

If you try to use the MCP integration without the MCP package installed, you'll get an informative error message that guides you to install the required package.

## Usage

### Running as a Standalone Server

You can run the MCP integration as a standalone server:

```bash
python -m prompt_decorators.integrations.mcp
```

This will start an MCP server with the default configuration, exposing tools for applying decorators and using predefined templates.

### Integrating with Your Own MCP Server

You can also integrate the Prompt Decorators with your own MCP server:

```python
from prompt_decorators.integrations.mcp import create_mcp_server

# Create an MCP server with prompt decorator integration
mcp_server = create_mcp_server("my-decorator-server")

# Run the server
mcp_server.run()
```

## Available Tools

The MCP integration provides the following tools:

### `apply_decorators`

Apply prompt decorators to transform a prompt using the `+++` syntax.

**Parameters:**
- `prompt` (string): The prompt text containing decorator annotations (+++Decorator syntax)

**Example:**
```python
result = await mcp_client.tools.apply_decorators(
    prompt="+++Reasoning(depth='comprehensive')\n+++StepByStep()\nExplain quantum computing."
)
```

**Response:**
```json
{
  "transformed_prompt": "Please provide detailed reasoning...\nPlease break down your response...\nExplain quantum computing.",
  "decorators_applied": ["Reasoning", "StepByStep"],
  "original_prompt": "+++Reasoning(depth='comprehensive')\n+++StepByStep()\nExplain quantum computing."
}
```

### `list_decorators`

Get a list of all available prompt decorators with their descriptions.

**Example:**
```python
decorators = await mcp_client.tools.list_decorators()
```

### `get_decorator_details`

Get detailed information about a specific decorator.

**Parameters:**
- `decorator_name` (string): The name of the decorator to retrieve details for

**Example:**
```python
details = await mcp_client.tools.get_decorator_details(decorator_name="Reasoning")
```

### `create_decorated_prompt`

Apply a predefined decorator template to a prompt.

**Parameters:**
- `template_name` (string): The name of the template to apply
- `prompt` (string): The prompt text to decorate
- `additional_params` (object, optional): Optional additional parameters for the template

**Example:**
```python
result = await mcp_client.tools.create_decorated_prompt(
    template_name="detailed-reasoning",
    prompt="Explain how quantum computing works."
)
```

## Predefined Templates

The MCP integration comes with several predefined templates:

| Template Name | Description | Decorators |
|---------------|-------------|------------|
| `detailed-reasoning` | Transform prompt for detailed reasoning and step-by-step analysis | `Reasoning(depth="comprehensive")`, `StepByStep(numbered=True)` |
| `academic-analysis` | Transform prompt for scholarly academic analysis with citations | `Reasoning(depth="comprehensive")`, `CiteSources(style="APA")`, `OutputFormat(format_type="markdown")` |
| `explain-simply` | Explain a complex topic in simple, accessible terms | `ELI5()`, `StepByStep(numbered=True)` |
| `creative-storytelling` | Generate creative narrative content | `Creative(level="high")`, `OutputFormat(format_type="markdown")` |
| `problem-solving` | Structured approach to solving complex problems | `StepByStep(numbered=True)`, `TreeOfThought(branches=3)`, `Limitations(position="end")` |
| `balanced-viewpoint` | Present multiple perspectives on a contentious topic | `Balanced()`, `PeerReview(criteria="all")`, `Steelman()` |
| `technical-documentation` | Generate clear technical documentation with code examples | `OutputFormat(format_type="markdown")`, `Audience(level="technical")`, `StepByStep(numbered=True)` |
| `data-analysis` | Analyze data with structured insights and visualizations | `TableFormat()`, `Reasoning(depth="comprehensive")`, `Prioritize(criteria="impact")` |

## Using Templates with MCP Prompts API

The MCP integration also supports the MCP Prompts API, allowing you to use predefined templates through the `prompts/get` and `prompts/list` methods.

**Example:**
```python
# List available prompt templates
templates = await mcp_client.prompts.list()

# Use a template
response = await mcp_client.prompts.get(
    name="detailed-reasoning",
    arguments={"prompt": "Explain how quantum computing works."}
)
```

## Creating Custom Templates

You can create custom templates by passing them to the `create_mcp_server` function:

```python
from prompt_decorators.integrations.mcp import create_mcp_server, DecoratorTemplate
import prompt_decorators.decorators as pd

custom_templates = {
    "my-custom-template": DecoratorTemplate(
        description="My custom template",
        decorators=[
            pd.Reasoning(depth="comprehensive"),
            pd.StepByStep(numbered=True)
        ],
        example="Example prompt for my custom template."
    )
}

mcp_server = create_mcp_server(templates=custom_templates)
mcp_server.run()
```

## Decorator Syntax

The MCP integration supports the `+++` syntax for applying decorators to prompts. For example:

```
+++StepByStep
+++Concise
Explain how to make a sandwich
```

This will apply both the `StepByStep` and `Concise` decorators to the prompt "Explain how to make a sandwich".

You can also include parameters:

```
+++Reasoning(depth='comprehensive')
+++OutputFormat(format_type='markdown')
Explain quantum computing
```

## Error Handling

All MCP tools include robust error handling. If an error occurs during decorator application, the original prompt is returned along with an error message.

## Logging

The MCP integration includes detailed logging to help diagnose issues. By default, logs are written to the console with the INFO level. You can adjust the logging level by configuring the Python logging system:

```python
import logging
logging.getLogger("prompt-decorators-mcp").setLevel(logging.DEBUG)
```
