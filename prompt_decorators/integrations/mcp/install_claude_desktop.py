#!/usr/bin/env python
"""Installation helper for Claude Desktop integration.

This script generates a configuration file for Claude Desktop that sets up
the Prompt Decorators MCP integration.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional


def find_python_executable() -> str:
    """Find the path to the current Python executable."""
    return sys.executable


def find_package_path() -> str:
    """Find the path to the prompt-decorators package."""
    try:
        import prompt_decorators

        return os.path.dirname(
            os.path.dirname(os.path.dirname(prompt_decorators.__file__))
        )
    except ImportError:
        print("Error: prompt-decorators package not found.")
        print("Please install it with: pip install prompt-decorators")
        sys.exit(1)


def create_config_file(
    output_path: Optional[str] = None, server_name: Optional[str] = None
) -> None:
    """Create a Claude Desktop configuration file."""
    python_exec = find_python_executable()
    package_path = find_package_path()

    if not server_name:
        server_name = "Prompt Decorators"

    config = {
        "name": server_name,
        "command": python_exec,
        "args": ["-m", "prompt_decorators.integrations.mcp.claude_desktop"],
        "cwd": package_path,
        "env": {
            "PYTHONPATH": package_path,
            "PYTHONUNBUFFERED": "1",
            "PYTHONDONTWRITEBYTECODE": "1",
        },
    }

    if not output_path:
        output_path = "claude_desktop_config.json"

    with open(output_path, "w") as f:
        json.dump(config, f, indent=2)

    print(f"Claude Desktop configuration file created at: {output_path}")
    print("\nTo use this configuration with Claude Desktop:")
    print("1. Open Claude Desktop")
    print("2. Go to Settings (gear icon) > Advanced > Context Sources")
    print("3. Click 'Add Context Source'")
    print("4. Click 'Import from File' and select the generated configuration file")
    print("5. Click 'Save'")


def check_mcp_sdk() -> bool:
    """Check if the MCP SDK is installed."""
    try:
        import mcp

        return True
    except ImportError:
        return False


def main() -> None:
    """Main function to parse arguments and create the configuration file."""
    parser = argparse.ArgumentParser(
        description="Generate a Claude Desktop configuration file for Prompt Decorators."
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Path to save the configuration file (default: claude_desktop_config.json)",
    )
    parser.add_argument(
        "-n", "--name", help="Custom name for the server (default: Prompt Decorators)"
    )
    args = parser.parse_args()

    # Check if MCP SDK is installed
    if not check_mcp_sdk():
        print(
            "Warning: MCP SDK not found. This is required for Claude Desktop integration."
        )
        print("Install it with: pip install mcp")
        install = input("Would you like to install it now? (y/n): ")
        if install.lower() == "y":
            subprocess.check_call([sys.executable, "-m", "pip", "install", "mcp"])
            print("MCP SDK installed successfully.")
        else:
            print(
                "Please install MCP SDK manually before using the Claude Desktop integration."
            )

    create_config_file(args.output, args.name)


if __name__ == "__main__":
    main()
