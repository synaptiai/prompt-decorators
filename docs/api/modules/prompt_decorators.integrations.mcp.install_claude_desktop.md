# install_claude_desktop

Installation helper for Claude Desktop integration.

This script generates a configuration file for Claude Desktop that sets up
the Prompt Decorators MCP integration.

## Functions

### `check_mcp_sdk`

Check if the MCP SDK is installed.

**Signature:** `check_mcp_sdk() -> bool`

**Returns:** `bool`

### `create_config_file`

Create a Claude Desktop configuration file.

**Signature:** `create_config_file(output_path: Optional[str] = None, server_name: Optional[str] = None) -> None`

**Parameters:**

- `output_path`: `Optional` (default: `None`)
- `server_name`: `Optional` (default: `None`)

### `find_package_path`

Find the path to the prompt-decorators package.

**Signature:** `find_package_path() -> str`

**Returns:** `str`

### `find_python_executable`

Find the path to the current Python executable.

**Signature:** `find_python_executable() -> str`

**Returns:** `str`

### `main`

Main function to parse arguments and create the configuration file.

**Signature:** `main() -> None`
