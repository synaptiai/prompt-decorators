# mcp

Model Context Protocol (MCP) integration for Prompt Decorators.

This module provides integration between Prompt Decorators and the Model Context Protocol (MCP),
allowing users to apply decorators through MCP tools.

## Public API

This module exports the following components:

- `mcp`: FastMCP - No description available
- `run_server`: Function - Run the MCP server
- `list_decorators`: Function - Lists all available prompt decorators
- `get_decorator_details`: Function - Get detailed information about a specific decorator
- `apply_decorators`: Function - Apply decorators to a prompt using the +++ syntax
- `create_decorated_prompt`: Function - Create a decorated prompt using a predefined template
- `get_available_decorators`: Function - Get a list of all available decorators
- `apply_dynamic_decorators`: Function - Apply decorators to a prompt using the +++ syntax

## Module Variables

### `logger`

Type: `Logger`

Value: `<Logger prompt-decorators-mcp (INFO)>`

### `mcp`

Type: `FastMCP`

Value: `<mcp.server.fastmcp.server.FastMCP object at 0x10716a710>`

## Functions

### `apply_decorators`

*Imported from `prompt_decorators.integrations.mcp.server`*

Apply decorators to a prompt using the +++ syntax.

Args:
    prompt: The prompt text to decorate.
    decorators: List of decorators to apply, each with name and parameters.

Returns:
    The decorated prompt with decorators applied, following MCP tool response format.

**Signature:** `apply_decorators(prompt: str, decorators: List[Dict[str, Any]]) -> Dict[str, Any]`

**Parameters:**

- `prompt`: `str`
- `decorators`: `List`

**Returns:** `Dict`

### `apply_dynamic_decorators`

*Imported from `prompt_decorators.dynamic_decorators_module`*

Apply decorators to a prompt using the +++ syntax.

Args:
    prompt: The prompt text with decorator syntax

Returns:
    The transformed prompt

**Signature:** `apply_dynamic_decorators(prompt: str) -> str`

**Parameters:**

- `prompt`: `str`

**Returns:** `str`

### `create_decorated_prompt`

*Imported from `prompt_decorators.integrations.mcp.server`*

Create a decorated prompt using a predefined template.

Args:
    template_name: The name of the template to use.
    content: The content to include in the prompt.
    parameters: Optional parameters for customizing the template.

Returns:
    The decorated prompt created from the template, following MCP tool response format.

**Signature:** `create_decorated_prompt(template_name: str, content: str, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]`

**Parameters:**

- `template_name`: `str`
- `content`: `str`
- `parameters`: `Optional` (default: `None`)

**Returns:** `Dict`

### `get_available_decorators`

*Imported from `prompt_decorators.dynamic_decorators_module`*

Get a list of all available decorators.

Returns:
    List of decorator definitions

**Signature:** `get_available_decorators() -> List[prompt_decorators.dynamic_decorators_module.DecoratorDefinition]`

**Returns:** `List`

### `get_decorator_details`

*Imported from `prompt_decorators.integrations.mcp.server`*

Get detailed information about a specific decorator.

Args:
    name: The name of the decorator to get details for.

Returns:
    A dictionary containing detailed information about the decorator.

**Signature:** `get_decorator_details(name: str) -> Dict[str, Any]`

**Parameters:**

- `name`: `str`

**Returns:** `Dict`

### `list_decorators`

*Imported from `prompt_decorators.integrations.mcp.server`*

Lists all available prompt decorators.

Returns:
    A dictionary containing information about all available decorators.

**Signature:** `list_decorators() -> Dict[str, Any]`

**Returns:** `Dict`

### `run_server`

*Imported from `prompt_decorators.integrations.mcp.server`*

Run the MCP server.

Args:
    host: The host to listen on.
    port: The port to listen on.

Returns:
    None

**Signature:** `run_server(host: str = '0.0.0.0', port: int = 5000) -> None`

**Parameters:**

- `host`: `str` (default: `0.0.0.0`)
- `port`: `int` (default: `5000`)
