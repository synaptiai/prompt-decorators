#!/usr/bin/env python
"""
Plugin System Demonstration

This script demonstrates how to use the plugin system for decorator extensions.
"""

import os
import sys
import json
from pathlib import Path
import argparse
import time

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from prompt_decorators.utils.plugins import get_plugin_manager
from prompt_decorators.utils.discovery import get_registry


def demonstrate_plugin_discovery():
    """Demonstrate plugin discovery and loading."""
    print("\n=== Plugin Discovery ===")
    
    # Get the plugin manager
    plugin_manager = get_plugin_manager()
    
    # Add the example plugin directory
    plugin_dir = project_root / "examples" / "plugins"
    print(f"Adding plugin directory: {plugin_dir}")
    plugin_manager.add_plugin_directory(str(plugin_dir))
    
    # Discover plugins
    print("\nDiscovering plugins...")
    plugins = plugin_manager.discover_plugins()
    
    if plugins:
        print(f"Found {len(plugins)} plugins:")
        for plugin in plugins:
            print(f"  - {plugin.name} v{plugin.version}: {plugin.description}")
            print(f"    Decorators: {[d.__name__ for d in plugin.decorators]}")
    else:
        print("No plugins found.")


def demonstrate_plugin_loading():
    """Demonstrate loading plugins."""
    print("\n=== Plugin Loading ===")
    
    # Get the plugin manager
    plugin_manager = get_plugin_manager()
    
    # Load all discovered plugins
    print("Loading plugins...")
    count = plugin_manager.load_discovered_plugins()
    print(f"Loaded {count} plugins.")
    
    # Show loaded plugins
    loaded_plugins = plugin_manager.get_all_plugins()
    if loaded_plugins:
        print("\nLoaded plugins:")
        for name, plugin in loaded_plugins.items():
            print(f"  - {name} v{plugin.version}")
            for decorator in plugin.decorators:
                print(f"    - {decorator.name} (v{decorator.version}, category: {decorator.category})")
    else:
        print("No plugins loaded.")


def demonstrate_using_plugin_decorators():
    """Demonstrate using decorators from plugins."""
    print("\n=== Using Plugin Decorators ===")
    
    # Get the registry to find decorators
    registry = get_registry()
    
    # Get all decorators
    all_decorators = registry.get_all_decorators()
    
    # Try to find our example plugin decorators
    funny_decorator_class = registry.get_decorator("Funny")
    summary_points_decorator_class = registry.get_decorator("SummaryPoints")
    
    if funny_decorator_class and summary_points_decorator_class:
        print("Found plugin decorators!")
        
        # Create instances
        funny = funny_decorator_class(style="puns", pun_density=5)
        summary = summary_points_decorator_class(count=4, position="end")
        
        # Create a prompt
        prompt = "Explain the concept of recursion in programming."
        
        # Apply decorators
        print("\nApplying Funny decorator:")
        funny_prompt = funny.apply(prompt)
        print(f"Original: {prompt}")
        print(f"Decorated: {funny_prompt}")
        
        print("\nApplying SummaryPoints decorator:")
        summary_prompt = summary.apply(prompt)
        print(f"Original: {prompt}")
        print(f"Decorated: {summary_prompt}")
        
        print("\nCombining decorators:")
        combined_prompt = summary.apply(funny.apply(prompt))
        print(f"Combined: {combined_prompt}")
    else:
        print("Plugin decorators not found. Make sure plugins are loaded correctly.")


def demonstrate_hot_loading():
    """Demonstrate hot-loading of plugins."""
    print("\n=== Hot-Loading of Plugins ===")
    
    # Get the plugin manager
    plugin_manager = get_plugin_manager()
    
    # Start watching directories
    plugin_manager.start_watching_directories(interval=2)
    print("Started watching plugin directories (interval: 2s)")
    print("Changes to plugin files will be automatically detected.")
    
    print("\nYou can now modify plugin files and they will be automatically reloaded.")
    print("For demonstration purposes, we'll wait for 10 seconds...")
    
    # Wait for 10 seconds to simulate time for changes
    for i in range(10, 0, -1):
        print(f"Waiting... {i}s", end="\r")
        time.sleep(1)
    print("\nFinished waiting.")
    
    # Stop watching directories
    plugin_manager.stop_watching_directories()
    print("Stopped watching plugin directories.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demonstrate the plugin system")
    parser.add_argument(
        "--discovery", "-d",
        action="store_true",
        help="Run plugin discovery demonstration"
    )
    parser.add_argument(
        "--loading", "-l",
        action="store_true",
        help="Run plugin loading demonstration"
    )
    parser.add_argument(
        "--usage", "-u",
        action="store_true",
        help="Run plugin usage demonstration"
    )
    parser.add_argument(
        "--hot-loading", "-h",
        action="store_true",
        dest="hot_loading",
        help="Run hot-loading demonstration"
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Run all demonstrations"
    )
    
    args = parser.parse_args()
    
    # If no specific demonstrations were requested, run everything
    if not (args.discovery or args.loading or args.usage or args.hot_loading) or args.all:
        demonstrate_plugin_discovery()
        demonstrate_plugin_loading()
        demonstrate_using_plugin_decorators()
        demonstrate_hot_loading()
    else:
        if args.discovery:
            demonstrate_plugin_discovery()
        if args.loading:
            demonstrate_plugin_loading()
        if args.usage:
            demonstrate_using_plugin_decorators()
        if args.hot_loading:
            demonstrate_hot_loading() 