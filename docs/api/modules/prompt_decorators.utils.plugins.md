# plugins

Plugin System Module.

This module provides a plugin architecture for decorator extensions.

## Module Variables

### `logger`

Type: `Logger`

Value: `<Logger prompt_decorators.utils.plugins (INFO)>`

### `plugin_manager`

Type: `PluginManager`

Value: `<prompt_decorators.utils.plugins.PluginManager object at 0x10744f610>`

## Classes

### `Plugin`

Class representing a plugin containing decorator extensions.

A plugin is a collection of decorators that can be loaded dynamically.

#### Methods

##### `__init__`

Initialize a plugin.

Args:
    name: Name of the plugin
    version: Version of the plugin
    description: Description of the plugin
    author: Dictionary with author information
    path: Path to the plugin directory or file
    decorators: List of decorator classes in the plugin
    metadata: Additional metadata for the plugin

**Signature:** `__init__(self, name: str, version: str, description: str = '', author: Optional[Dict[str, str]] = None, path: Optional[str] = None, decorators: Optional[List[Type[prompt_decorators.core.base.DecoratorBase]]] = None, metadata: Optional[Dict[str, Any]] = None)`

**Parameters:**

- `name`: `str`
- `version`: `str`
- `description`: `str` (default: ``)
- `author`: `Optional` (default: `None`)
- `path`: `Optional` (default: `None`)
- `decorators`: `Optional` (default: `None`)
- `metadata`: `Optional` (default: `None`)

##### `disable`

Disable the plugin.

**Signature:** `disable(self) -> None`

**Parameters:**


##### `enable`

Enable the plugin.

**Signature:** `enable(self) -> None`

**Parameters:**


##### `to_dict`

Convert the plugin to a dictionary.

Args:
    self: The plugin instance

Returns:
    Dictionary representation of the plugin

**Signature:** `to_dict(self) -> Dict[str, Any]`

**Parameters:**


**Returns:** `Dict`

### `PluginManager`

Manager for decorator plugins.

This class provides functionality for loading, managing, and monitoring plugins.

#### Methods

##### `add_plugin_directory`

Add a directory to search for plugins.

Args:
    directory: Path to the directory containing plugins

Returns:
    None

**Signature:** `add_plugin_directory(self, directory: str) -> None`

**Parameters:**

- `directory`: `str`

##### `discover_plugins`

Discover plugins in the registered directories.

Args:
    self: The plugin manager instance

Returns:
    List of discovered plugins

**Signature:** `discover_plugins(self) -> List[prompt_decorators.utils.plugins.Plugin]`

**Parameters:**


**Returns:** `List`

##### `get_all_plugins`

Get all loaded plugins.

Args:
    self: The plugin manager instance

Returns:
    Dictionary mapping plugin names to Plugin objects

**Signature:** `get_all_plugins(self) -> Dict[str, prompt_decorators.utils.plugins.Plugin]`

**Parameters:**


**Returns:** `Dict`

##### `get_plugin`

Get a loaded plugin by name.

Args:
    plugin_name: Name of the plugin to get

Returns:
    The plugin, or None if not found

**Signature:** `get_plugin(self, plugin_name: str) -> Optional[prompt_decorators.utils.plugins.Plugin]`

**Parameters:**

- `plugin_name`: `str`

**Returns:** `Optional`

##### `load_discovered_plugins`

Load all discovered plugins.

Args:
    self: The plugin manager instance

Returns:
    Number of plugins loaded

**Signature:** `load_discovered_plugins(self) -> int`

**Parameters:**


**Returns:** `int`

##### `load_plugin`

Load a plugin.

Args:
    plugin: The plugin to load

Returns:
    True if loaded successfully, False otherwise

**Signature:** `load_plugin(self, plugin: prompt_decorators.utils.plugins.Plugin) -> bool`

**Parameters:**

- `plugin`: `Plugin`

**Returns:** `bool`

##### `register_hook`

Register a hook callback.

Args:
    hook_name: Name of the hook
    callback: Function to call when the hook is triggered

Returns:
    None

**Signature:** `register_hook(self, hook_name: str, callback: Callable) -> None`

**Parameters:**

- `hook_name`: `str`
- `callback`: `Callable`

##### `start_watching_directories`

Start watching plugin directories for changes.

Args:
    interval: How often to check for changes (in seconds)

Returns:
    None

**Signature:** `start_watching_directories(self, interval: int = 10) -> None`

**Parameters:**

- `interval`: `int` (default: `10`)

##### `stop_watching_directories`

Stop watching plugin directories for changes.

**Signature:** `stop_watching_directories(self) -> None`

**Parameters:**


##### `unload_plugin`

Unload a plugin.

Args:
    plugin_name: Name of the plugin to unload

Returns:
    True if unloaded successfully, False otherwise

**Signature:** `unload_plugin(self, plugin_name: str) -> bool`

**Parameters:**

- `plugin_name`: `str`

**Returns:** `bool`

## Functions

### `get_plugin_manager`

Get the global plugin manager.

Returns:
    The global plugin manager instance

**Signature:** `get_plugin_manager() -> prompt_decorators.utils.plugins.PluginManager`

**Returns:** `PluginManager`
