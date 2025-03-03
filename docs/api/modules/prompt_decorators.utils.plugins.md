# Module `prompt_decorators.utils.plugins`

Plugin System Module

This module provides a plugin architecture for decorator extensions.

## Classes

- [`Plugin`](#class-plugin): Class representing a plugin containing decorator extensions.
- [`PluginManager`](#class-pluginmanager): Manager for decorator plugins.

### Class `Plugin`

Class representing a plugin containing decorator extensions.

A plugin is a collection of decorators that can be loaded dynamically.

#### Methods

- `__init__(name, version, description, author, path, decorators, metadata)`
- `disable() -> <class 'NoneType'>`
- `enable() -> <class 'NoneType'>`
- `to_dict() -> typing.Dict[str, typing.Any]`

### Class `PluginManager`

Manager for decorator plugins.

This class provides functionality for loading, managing, and monitoring plugins.

#### Methods

- `add_plugin_directory(directory) -> <class 'NoneType'>`
- `discover_plugins() -> typing.List[prompt_decorators.utils.plugins.Plugin]`
- `get_all_plugins() -> typing.Dict[str, prompt_decorators.utils.plugins.Plugin]`
- `get_plugin(plugin_name) -> typing.Optional[prompt_decorators.utils.plugins.Plugin]`
- `load_discovered_plugins() -> <class 'int'>`
- `load_plugin(plugin) -> <class 'bool'>`
- `register_hook(hook_name, callback) -> <class 'NoneType'>`
- `start_watching_directories(interval=10) -> <class 'NoneType'>`
- `stop_watching_directories() -> <class 'NoneType'>`
- `unload_plugin(plugin_name) -> <class 'bool'>`

## Functions

- [`get_plugin_manager`](#function-get_plugin_manager): Get the global plugin manager.

### Function `get_plugin_manager`

**Signature:** `get_plugin_manager() -> <class 'prompt_decorators.utils.plugins.PluginManager'>`

Get the global plugin manager.

Returns:
    The global plugin manager instance
