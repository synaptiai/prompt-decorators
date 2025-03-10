# server

MCP Server for Prompt Decorators.

This module provides integration between Prompt Decorators and the Model Context Protocol (MCP),
exposing prompt decorators as MCP tools that can be used by any MCP client.

Implementation follows the official MCP SDK patterns and best practices.

## Module Variables

### `F`

Type: `TypeVar`

Value: `~F`

### `MCP_AVAILABLE`

Type: `bool`

Value: `True`

### `logger`

Type: `Logger`

Value: `<Logger prompt-decorators-mcp (INFO)>`

### `mcp`

Type: `FastMCP`

Value: `<mcp.server.fastmcp.server.FastMCP object at 0x10716a710>`

## Functions

### `apply_decorators`

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

### `create_decorated_prompt`

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

### `get_decorator_details`

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

Lists all available prompt decorators.

Returns:
    A dictionary containing information about all available decorators.

**Signature:** `list_decorators() -> Dict[str, Any]`

**Returns:** `Dict`

### `run_server`

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

### `transform_prompt`

Transform a prompt using a list of decorator strings.

This tool directly transforms a prompt using the raw decorator syntax strings
(e.g., "+++StepByStep(numbered=true)"), which can be useful for clients
that already have decorator strings rather than structured decorator objects.

Args:
    prompt: The prompt text to transform.
    decorator_strings: List of decorator syntax strings to apply.

Returns:
    The transformed prompt, following MCP tool response format.

**Signature:** `transform_prompt(prompt: str, decorator_strings: List[str]) -> Dict[str, Any]`

**Parameters:**

- `prompt`: `str`
- `decorator_strings`: `List`

**Returns:** `Dict`
