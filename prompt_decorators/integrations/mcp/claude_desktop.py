#!/usr/bin/env python
"""
Entry point for running the Prompt Decorators MCP server for Claude Desktop.

Usage:
    python -m prompt_decorators.integrations.mcp.claude_desktop [--verbose]
"""

import argparse
import logging
import os
import sys


def main() -> None:
    """Run the Prompt Decorators MCP server for Claude Desktop."""
    parser = argparse.ArgumentParser(
        description="Run the Prompt Decorators MCP server for Claude Desktop"
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    # Configure logging level based on verbose flag
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stderr,
    )

    logger = logging.getLogger("claude-desktop-launcher")
    logger.info("Initializing Prompt Decorators MCP server for Claude Desktop")

    # Check if MCP SDK is installed
    try:
        import mcp

        logger.info(f"MCP SDK version: {getattr(mcp, '__version__', 'unknown')}")
    except ImportError:
        logger.error("MCP SDK not installed")
        logger.error("Please install manually: pip install mcp")
        sys.exit(1)

    # Add the project directory to PYTHONPATH to ensure imports work correctly
    project_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )
    if project_dir not in sys.path:
        logger.debug(f"Adding project directory to PYTHONPATH: {project_dir}")
        sys.path.insert(0, project_dir)

    try:
        # Import and run the server
        from prompt_decorators.integrations.mcp.server import run_server

        logger.info("Starting Claude Desktop MCP server")
        run_server(verbose=args.verbose)
    except ImportError as e:
        logger.error(f"Failed to import server implementation: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error running Claude Desktop MCP server: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
