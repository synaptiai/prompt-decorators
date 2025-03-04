#!/usr/bin/env python
"""Check MkDocs Plugins.

This script checks if all required MkDocs plugins are installed.
It reads the mkdocs.yml file and checks if all plugins listed there are installed.

Usage:
    python scripts/check_mkdocs_plugins.py
"""

import importlib
import subprocess
import sys
from pathlib import Path

import yaml


def check_plugin(plugin_name):
    """Check if a plugin is installed.

    Args:
        plugin_name: Name of the plugin to check

    Returns:
        True if the plugin is installed, False otherwise
    """
    try:
        if plugin_name == "search":
            # Search is built-in
            return True

        # Try to check if the package is installed using pip
        package_name = f"mkdocs-{plugin_name}-plugin"
        if plugin_name == "mkdocstrings":
            package_name = "mkdocstrings"

        result = subprocess.run(
            ["pip", "show", package_name], capture_output=True, text=True
        )

        if result.returncode == 0:
            return True

        # Try alternative package name formats
        alt_package_name = f"mkdocs_{plugin_name.replace('-', '_')}"
        result = subprocess.run(
            ["pip", "show", alt_package_name], capture_output=True, text=True
        )

        return result.returncode == 0
    except Exception as e:
        print(f"Error checking plugin {plugin_name}: {e}")
        return False


def main():
    """Run the script."""
    # Read the mkdocs.yml file
    mkdocs_file = Path("mkdocs.yml")
    if not mkdocs_file.exists():
        print(f"Error: {mkdocs_file} not found")
        return 1

    with open(mkdocs_file, "r") as f:
        config = yaml.safe_load(f)

    # Check if plugins are defined
    if "plugins" not in config:
        print("No plugins defined in mkdocs.yml")
        return 0

    # Get the list of plugins
    plugins = config["plugins"]
    missing_plugins = []

    # Check each plugin
    for plugin in plugins:
        if isinstance(plugin, dict):
            # Plugin with configuration
            plugin_name = list(plugin.keys())[0]
        else:
            # Plugin without configuration
            plugin_name = plugin

        if not check_plugin(plugin_name):
            missing_plugins.append(plugin_name)
            print(f"Plugin '{plugin_name}' is not installed")
        else:
            print(f"Plugin '{plugin_name}' is installed")

    # Print summary
    if missing_plugins:
        print(f"\nMissing plugins: {', '.join(missing_plugins)}")
        return 1
    else:
        print("\nAll plugins are installed")
        return 0


if __name__ == "__main__":
    sys.exit(main())
