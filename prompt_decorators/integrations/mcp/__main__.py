#!/usr/bin/env python
"""
Command-line entry point for running the Prompt Decorators MCP server.

Usage:
    python -m prompt_decorators.integrations.mcp [--verbose]
"""

import argparse
import logging
import sys


def main() -> None:
    """Run the Prompt Decorators MCP server."""
    parser = argparse.ArgumentParser(description="Run the Prompt Decorators MCP server")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument(
        "--name", type=str, default="Prompt Decorators", help="Server name to display"
    )
    args = parser.parse_args()

    # Configure logging level based on verbose flag
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stderr,
    )

    logger = logging.getLogger("prompt-decorators-main")
    logger.info(f"Starting Prompt Decorators MCP server: {args.name}")

    try:
        # Import and run the server
        from prompt_decorators.integrations.mcp.server import run_server

        run_server(verbose=args.verbose)
    except ImportError as e:
        logger.error(f"Failed to import server: {e}")
        logger.error("Please ensure the MCP SDK is installed: pip install mcp")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error running MCP server: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
