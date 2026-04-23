"""Plugin System Module.

This module provides a plugin architecture for decorator extensions.
"""
import importlib
import importlib.util
import inspect
import json
import logging
import pkgutil
import sys
import threading
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Type

from prompt_decorators.core.base import BaseDecorator
from prompt_decorators.utils.discovery import get_registry
from prompt_decorators.utils.factory import DecoratorFactory

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Plugin:
    """Class representing a plugin containing decorator extensions.

    A plugin is a collection of decorators that can be loaded dynamically.
    """

    def __init__(
        self,
        name: str,
        version: str,
        description: str = "",
        author: Optional[Dict[str, str]] = None,
        path: Optional[str] = None,
        decorators: Optional[List[Type[BaseDecorator]]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ):
        """Initialize a plugin.

        Args:
            name: Name of the plugin
            version: Version of the plugin
            description: Description of the plugin
            author: Dictionary with author information
            path: Path to the plugin directory or file
            decorators: List of decorator classes in the plugin
            metadata: Additional metadata for the plugin
        """
        self.name = name
        self.version = version
        self.description = description
        self.author = author or {}
        self.path = path
        self.decorators = decorators or []
        self.metadata = metadata or {}
        self.enabled = True

    def disable(self) -> None:
        """Disable the plugin."""
        self.enabled = False

    def enable(self) -> None:
        """Enable the plugin."""
        self.enabled = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert the plugin to a dictionary.

        Args:
            self: The plugin instance

        Returns:
            Dictionary representation of the plugin
        """
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "author": self.author,
            "path": self.path,
            "metadata": self.metadata,
            "enabled": self.enabled,
            "decorators": [d.__name__ for d in self.decorators],
        }


class PluginManager:
    """Manager for decorator plugins.

    This class provides functionality for loading, managing, and monitoring plugins.
    """

    _instance = None

    def __new__(cls):
        """Create a singleton instance of the plugin manager.

        Returns:
            The singleton instance of the plugin manager.
        """
        if cls._instance is None:
            cls._instance = super(PluginManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self) -> None:
        """Initialize the plugin manager."""
        self._plugins: Dict[str, Plugin] = {}
        self._plugin_directories: List[str] = []
        self._watch_directories: bool = False
        self._watch_interval: int = 10  # seconds
        self._watch_thread: Optional[threading.Thread] = None
        self._stop_watching: threading.Event = threading.Event()
        self._registry = get_registry()
        self._factory = DecoratorFactory(self._registry)
        self._initialized_plugins: Set[str] = set()
        self._plugin_hooks: Dict[str, List[Callable]] = {}

    def add_plugin_directory(self, directory: str) -> None:
        """Add a directory to search for plugins.

        Args:
            directory: Path to the directory containing plugins

        Returns:
            None
        """
        directory_path = Path(directory)
        if not directory_path.exists() or not directory_path.is_dir():
            logger.warning(f"Plugin directory not found: {directory}")
            return

        if str(directory_path) not in self._plugin_directories:
            self._plugin_directories.append(str(directory_path))
            logger.info(f"Added plugin directory: {directory}")

    def discover_plugins(self) -> List[Plugin]:
        """Discover plugins in the registered directories.

        Args:
            self: The plugin manager instance

        Returns:
            List of discovered plugins
        """
        discovered_plugins = []

        for directory in self._plugin_directories:
            directory_path = Path(directory)

            if not directory_path.exists() or not directory_path.is_dir():
                continue

            logger.info(f"Scanning for plugins in: {directory}")

            # Find Python packages (directories with __init__.py)
            for item in directory_path.iterdir():
                if item.is_dir() and (item / "__init__.py").exists():
                    plugin = self._load_plugin_from_package(item)
                    if plugin:
                        discovered_plugins.append(plugin)

                # Find Python modules (*.py files)
                elif (
                    item.is_file()
                    and item.suffix == ".py"
                    and not item.name.startswith("_")
                ):
                    plugin = self._load_plugin_from_module(item)
                    if plugin:
                        discovered_plugins.append(plugin)

                # Find JSON plugin definitions
                elif item.is_file() and item.suffix == ".json":
                    plugin = self._load_plugin_from_json(item)
                    if plugin:
                        discovered_plugins.append(plugin)

        return discovered_plugins

    def load_discovered_plugins(self) -> int:
        """Load all discovered plugins.

        Args:
            self: The plugin manager instance

        Returns:
            Number of plugins loaded
        """
        plugins = self.discover_plugins()
        count = 0

        for plugin in plugins:
            if self.load_plugin(plugin):
                count += 1

        return count

    def load_plugin(self, plugin: Plugin) -> bool:
        """Load a plugin.

        Args:
            plugin: The plugin to load

        Returns:
            True if loaded successfully, False otherwise
        """
        if plugin.name in self._plugins:
            logger.warning(
                f"Plugin {plugin.name} already loaded. Unload first to replace."
            )
            return False

        # Register the plugin's decorators
        for decorator_class in plugin.decorators:
            self._registry.register_decorator(decorator_class)

        # Add to loaded plugins
        self._plugins[plugin.name] = plugin
        logger.info(f"Loaded plugin: {plugin.name} v{plugin.version}")

        # Call initialization hook if defined
        self._call_hook("plugin_loaded", plugin)

        return True

    def unload_plugin(self, plugin_name: str) -> bool:
        """Unload a plugin.

        Args:
            plugin_name: Name of the plugin to unload

        Returns:
            True if unloaded successfully, False otherwise
        """
        if plugin_name not in self._plugins:
            logger.warning(f"Plugin {plugin_name} not found.")
            return False

        plugin = self._plugins[plugin_name]

        # Call unload hook if defined
        self._call_hook("plugin_unloaded", plugin)

        # Remove from loaded plugins
        del self._plugins[plugin_name]
        logger.info(f"Unloaded plugin: {plugin_name}")

        return True

    def get_plugin(self, plugin_name: str) -> Optional[Plugin]:
        """Get a loaded plugin by name.

        Args:
            plugin_name: Name of the plugin to get

        Returns:
            The plugin, or None if not found
        """
        return self._plugins.get(plugin_name)

    def get_all_plugins(self) -> Dict[str, Plugin]:
        """Get all loaded plugins.

        Args:
            self: The plugin manager instance

        Returns:
            Dictionary mapping plugin names to Plugin objects
        """
        return self._plugins.copy()

    def register_hook(self, hook_name: str, callback: Callable) -> None:
        """Register a hook callback.

        Args:
            hook_name: Name of the hook
            callback: Function to call when the hook is triggered

        Returns:
            None
        """
        if hook_name not in self._plugin_hooks:
            self._plugin_hooks[hook_name] = []

        self._plugin_hooks[hook_name].append(callback)

    def _call_hook(self, hook_name: str, *args, **kwargs) -> None:
        """Call all registered callbacks for a hook.

        Args:
            hook_name: Name of the hook to call
            args: Positional arguments to pass to the callbacks. These are forwarded to each registered callback.
            kwargs: Keyword arguments to pass to the callbacks. These are forwarded to each registered callback.

        Returns:
            None
        """
        if hook_name not in self._plugin_hooks:
            return

        for callback in self._plugin_hooks[hook_name]:
            try:
                callback(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error calling hook {hook_name}: {e}")

    def _load_plugin_from_package(self, package_path: Path) -> Optional[Plugin]:
        """Load a plugin from a Python package.

        Args:
            package_path: Path to the package directory

        Returns:
            Loaded plugin, or None if loading failed
        """
        try:
            # Get the package name
            package_name = package_path.name

            # Add the parent directory to sys.path
            sys.path.insert(0, str(package_path.parent))

            try:
                # Try to import the module
                module = importlib.import_module(package_name)

                # Look for a plugin definition
                if hasattr(module, "plugin_info"):
                    plugin_info = module.plugin_info

                    # Validate plugin info
                    if not isinstance(plugin_info, dict):
                        logger.warning(f"Invalid plugin_info in {package_name}")
                        return None

                    if "name" not in plugin_info or "version" not in plugin_info:
                        logger.warning(
                            f"Missing required fields in plugin_info for {package_name}"
                        )
                        return None

                    # Create plugin object
                    plugin = Plugin(
                        name=plugin_info["name"],
                        version=plugin_info["version"],
                        description=plugin_info.get("description", ""),
                        author=plugin_info.get("author", {}),
                        path=str(package_path),
                        metadata=plugin_info.get("metadata", {}),
                    )

                    # Find decorator classes
                    decorators = []
                    for _name, obj in inspect.getmembers(module):
                        if (
                            inspect.isclass(obj)
                            and obj.__module__ == module.__name__
                            and issubclass(obj, BaseDecorator)
                            and obj != BaseDecorator
                        ):
                            decorators.append(obj)

                    # Find decorators in submodules
                    for _, submodule_name, _is_pkg in pkgutil.iter_modules(
                        [str(package_path)]
                    ):
                        try:
                            submodule = importlib.import_module(
                                f"{package_name}.{submodule_name}"
                            )
                            for _name, obj in inspect.getmembers(submodule):
                                if (
                                    inspect.isclass(obj)
                                    and obj.__module__ == submodule.__name__
                                    and issubclass(obj, BaseDecorator)
                                    and obj != BaseDecorator
                                ):
                                    decorators.append(obj)
                        except ImportError as e:
                            logger.warning(
                                f"Error importing submodule {submodule_name}: {e}"
                            )

                    plugin.decorators = decorators
                    logger.info(
                        f"Found plugin {plugin.name} with {len(decorators)} decorators"
                    )

                    return plugin
                else:
                    logger.warning(f"No plugin_info found in {package_name}")
                    return None
            finally:
                # Remove the added path
                if sys.path[0] == str(package_path.parent):
                    sys.path.pop(0)

        except Exception as e:
            logger.error(f"Error loading plugin from package {package_path}: {e}")
            return None

    def _load_plugin_from_module(self, module_path: Path) -> Optional[Plugin]:
        """Load a plugin from a Python module.

        Args:
            module_path: Path to the module file

        Returns:
            Loaded plugin, or None if loading failed
        """
        try:
            # Get the module name
            module_name = module_path.stem

            # Add the parent directory to sys.path
            sys.path.insert(0, str(module_path.parent))

            try:
                # Try to import the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                if not spec or not spec.loader:
                    logger.warning(f"Could not create spec for {module_path}")
                    return None

                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Look for a plugin definition
                if hasattr(module, "plugin_info"):
                    plugin_info = module.plugin_info

                    # Validate plugin info
                    if not isinstance(plugin_info, dict):
                        logger.warning(f"Invalid plugin_info in {module_name}")
                        return None

                    if "name" not in plugin_info or "version" not in plugin_info:
                        logger.warning(
                            f"Missing required fields in plugin_info for {module_name}"
                        )
                        return None

                    # Create plugin object
                    plugin = Plugin(
                        name=plugin_info["name"],
                        version=plugin_info["version"],
                        description=plugin_info.get("description", ""),
                        author=plugin_info.get("author", {}),
                        path=str(module_path),
                        metadata=plugin_info.get("metadata", {}),
                    )

                    # Find decorator classes
                    decorators = []
                    for _name, obj in inspect.getmembers(module):
                        if (
                            inspect.isclass(obj)
                            and obj.__module__ == module.__name__
                            and issubclass(obj, BaseDecorator)
                            and obj != BaseDecorator
                        ):
                            decorators.append(obj)

                    plugin.decorators = decorators
                    logger.info(
                        f"Found plugin {plugin.name} with {len(decorators)} decorators"
                    )

                    return plugin
                else:
                    logger.warning(f"No plugin_info found in {module_name}")
                    return None
            finally:
                # Remove the added path
                if sys.path[0] == str(module_path.parent):
                    sys.path.pop(0)

        except Exception as e:
            logger.error(f"Error loading plugin from module {module_path}: {e}")
            return None

    def _load_plugin_from_json(self, json_path: Path) -> Optional[Plugin]:
        """Load a plugin from a JSON file.

        Args:
            json_path: Path to the JSON file

        Returns:
            Loaded plugin, or None if loading failed
        """
        try:
            # Load the JSON file
            with open(json_path, "r") as f:
                plugin_info = json.load(f)

            # Validate plugin info
            if not isinstance(plugin_info, dict):
                logger.warning(f"Invalid JSON format in {json_path}")
                return None

            if (
                "name" not in plugin_info
                or "version" not in plugin_info
                or "decorators" not in plugin_info
            ):
                logger.warning(f"Missing required fields in {json_path}")
                return None

            # Create plugin object
            plugin = Plugin(
                name=plugin_info["name"],
                version=plugin_info["version"],
                description=plugin_info.get("description", ""),
                author=plugin_info.get("author", {}),
                path=str(json_path),
                metadata=plugin_info.get("metadata", {}),
            )

            # Load decorators
            decorators = []
            for decorator_info in plugin_info.get("decorators", []):
                # Create a decorator class from the JSON definition
                decorator_class = self._factory.create_dynamic_class(decorator_info)
                if decorator_class:
                    decorators.append(decorator_class)

            plugin.decorators = decorators
            logger.info(f"Found plugin {plugin.name} with {len(decorators)} decorators")

            return plugin

        except Exception as e:
            logger.error(f"Error loading plugin from JSON {json_path}: {e}")
            return None

    def start_watching_directories(self, interval: int = 10) -> None:
        """Start watching plugin directories for changes.

        Args:
            interval: How often to check for changes (in seconds)

        Returns:
            None
        """
        if self._watch_thread and self._watch_thread.is_alive():
            logger.warning("Already watching directories.")
            return

        self._watch_interval = interval
        self._watch_directories = True
        self._stop_watching.clear()

        self._watch_thread = threading.Thread(
            target=self._watch_directories_thread, daemon=True
        )
        self._watch_thread.start()

        logger.info(f"Started watching plugin directories (interval: {interval}s)")

    def stop_watching_directories(self) -> None:
        """Stop watching plugin directories for changes."""
        if not self._watch_thread or not self._watch_thread.is_alive():
            logger.warning("Not currently watching directories.")
            return

        self._watch_directories = False
        self._stop_watching.set()
        self._watch_thread.join(timeout=2.0)
        self._watch_thread = None

        logger.info("Stopped watching plugin directories")

    def _watch_directories_thread(self) -> None:
        """Thread function to watch plugin directories for changes."""
        # Remember the last modification times
        last_modified_times: Dict[str, float] = {}

        # First scan
        for directory in self._plugin_directories:
            directory_path = Path(directory)
            if directory_path.exists() and directory_path.is_dir():
                for item in directory_path.glob("**/*"):
                    if item.is_file():
                        last_modified_times[str(item)] = item.stat().st_mtime

        # Main loop
        while self._watch_directories and not self._stop_watching.is_set():
            try:
                # Check for changes
                for directory in self._plugin_directories:
                    directory_path = Path(directory)
                    if not directory_path.exists() or not directory_path.is_dir():
                        continue

                    # Check all files in the directory
                    for item in directory_path.glob("**/*"):
                        if not item.is_file():
                            continue

                        item_path = str(item)
                        current_mtime = item.stat().st_mtime

                        # If this is a new file or modified file
                        if (
                            item_path not in last_modified_times
                            or current_mtime > last_modified_times[item_path]
                        ):
                            logger.info(f"Detected change in {item_path}")

                            # Reload plugin
                            if (
                                item.suffix == ".py"
                                or item.suffix == ".json"
                                or item.name == "__init__.py"
                            ):
                                # For simplicity, just reload all plugins
                                self._reload_all_plugins()

                                # Update all modification times
                                for update_item in directory_path.glob("**/*"):
                                    if update_item.is_file():
                                        last_modified_times[
                                            str(update_item)
                                        ] = update_item.stat().st_mtime

                                # We've reloaded everything, so break out of the loop
                                break

                            # Update modification time
                            last_modified_times[item_path] = current_mtime

                # Sleep for the interval
                time.sleep(self._watch_interval)

            except Exception as e:
                logger.error(f"Error while watching directories: {e}")
                time.sleep(self._watch_interval)

    def _reload_all_plugins(self) -> None:
        """Reload all plugins."""
        logger.info("Reloading all plugins...")

        # Remember currently loaded plugins
        current_plugins = list(self._plugins.keys())

        # Unload all plugins
        for plugin_name in current_plugins:
            self.unload_plugin(plugin_name)

        # Reload all plugins
        self.load_discovered_plugins()

        logger.info("Finished reloading plugins.")


# Create a global plugin manager instance
plugin_manager = PluginManager()


# Function to get the global plugin manager
def get_plugin_manager() -> PluginManager:
    """Get the global plugin manager.

    Returns:
        The global plugin manager instance
    """
    return plugin_manager
