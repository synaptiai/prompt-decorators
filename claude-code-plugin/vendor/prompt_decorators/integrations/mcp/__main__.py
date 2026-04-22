#!/usr/bin/env python
"""Command-line entry point for running the Prompt Decorators MCP server.

Usage:
    python -m prompt_decorators.integrations.mcp [`--host HOST`] [`--port PORT`] [`--verbose`]
"""

import argparse
import logging
import sys


def main() -> None:
    """Run the Prompt Decorators MCP server."""
    parser = argparse.ArgumentParser(description="Run the Prompt Decorators MCP server")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=5000, help="Port to listen on")
    args = parser.parse_args()

    # Configure logging level based on verbose flag
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stderr,
    )

    logger = logging.getLogger("prompt-decorators-main")
    logger.info(f"Starting Prompt Decorators MCP server on {args.host}:{args.port}")

    try:
        # Import and run the server
        from prompt_decorators.integrations.mcp.server import MCP_AVAILABLE, run_server

        if not MCP_AVAILABLE:
            logger.error("MCP SDK not installed. Please install with: pip install mcp")
            sys.exit(1)

        run_server(host=args.host, port=args.port)
    except ImportError as e:
        logger.error(f"Failed to import server: {e}")
        logger.error("Please ensure the MCP SDK is installed: pip install mcp")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error running MCP server: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
