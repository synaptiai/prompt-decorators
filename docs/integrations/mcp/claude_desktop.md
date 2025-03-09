# Claude Desktop Integration

Prompt Decorators can be easily integrated with [Claude Desktop](https://claude.ai/desktop) using the MCP (Model Context Protocol) integration. This document explains how to set up and use the Prompt Decorators MCP server with Claude Desktop.

## Overview

Claude Desktop supports external tools through the MCP protocol, allowing you to extend Claude's capabilities with custom functionality. The Prompt Decorators MCP integration enables Claude to apply prompt decorators to your prompts, enhancing Claude's responses with structured reasoning, specific output formats, and more.

## Prerequisites

- Claude Desktop installed on your system
- Python 3.11 or higher
- Prompt Decorators package installed
- MCP SDK installed (`pip install mcp`)

## Installation

### 1. Install Required Packages

```bash
pip install prompt-decorators mcp
```

### 2. Create a Configuration File

Claude Desktop requires a configuration file that specifies how to run the MCP server. You can use our provided script to generate this configuration file:

```bash
python install_claude_desktop.py
```

This will create a `claude_desktop_config.json` file in your current directory with the appropriate configuration.

Alternatively, you can manually create a configuration file with the following structure:

```json
{
  "name": "Prompt Decorators",
  "command": "/absolute/path/to/python",
  "args": [
    "-m",
    "prompt_decorators.integrations.mcp.claude_desktop"
  ],
  "cwd": "/absolute/path/to/prompt-decorators",
  "env": {
    "PYTHONPATH": "/absolute/path/to/prompt-decorators",
    "PYTHONUNBUFFERED": "1",
    "PYTHONDONTWRITEBYTECODE": "1"
  }
}
```

Replace the paths with the appropriate paths on your system:
- `/absolute/path/to/python`: The path to your Python executable
- `/absolute/path/to/prompt-decorators`: The path to the directory containing the prompt-decorators package

### 3. Configure Claude Desktop

1. Open Claude Desktop
2. Go to Settings (gear icon) > Advanced > Context Sources
3. Click "Add Context Source"
4. Either:
   - Click "Import from File" and select your `claude_desktop_config.json` file
   - Or manually enter the configuration details

5. Click "Save"

## Using Prompt Decorators in Claude Desktop

Once the integration is set up, you can use Prompt Decorators in Claude Desktop through the `/tool` command.

### Available Tools

The integration provides four tools:

1. `list_decorators`: Lists all available prompt decorators
2. `get_decorator_details`: Gets detailed information about a specific decorator
3. `apply_decorators`: Applies decorators to a prompt
4. `create_decorated_prompt`: Creates a decorated prompt using a predefined template

### Example Usage

#### Listing Decorators

To see all available decorators:

```
/tool list_decorators
```

This will return a list of all available decorators with their descriptions, categories, and parameters.

#### Getting Decorator Details

To get detailed information about a specific decorator:

```
/tool get_decorator_details name=StepByStep
```

This will return detailed information about the StepByStep decorator, including its parameters and usage.

#### Applying Decorators

To apply decorators to a prompt:

```
/tool apply_decorators prompt="Explain quantum computing" decorators=[{"name": "StepByStep"}, {"name": "Academic", "parameters": {"level": "advanced"}}]
```

This will return a decorated prompt that includes the StepByStep and Academic decorators.

#### Using Templates

To create a decorated prompt using a predefined template:

```
/tool create_decorated_prompt template_name="detailed-reasoning" content="Why is the sky blue?"
```

This will return a decorated prompt using the detailed-reasoning template.

### Predefined Templates

The integration includes these predefined templates:

- **detailed-reasoning**: Enhanced critical thinking template with structured reasoning
- **academic-analysis**: Academic style analysis with citations and formal tone
- **explain-simply**: Simplify complex topics for broader understanding
- **creative-storytelling**: Creative writing with storytelling elements
- **problem-solving**: Structured approach to solving problems

## Troubleshooting

### Connection Issues

If Claude Desktop cannot connect to the MCP server:

1. Check that the paths in your configuration file are correct
2. Ensure that the MCP SDK is installed (`pip install mcp`)
3. Try running the server manually to check for errors:
   ```bash
   python -m prompt_decorators.integrations.mcp.claude_desktop --verbose
   ```
4. Check that the PYTHONPATH environment variable is set correctly in the configuration

### Debugging

You can run the Claude Desktop handler with the `--verbose`
